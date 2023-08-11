import requests
from bs4 import BeautifulSoup
import logging
import psycopg2
import hashlib
import schedule
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    cursor = conn.cursor()

    # Create the news table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id SERIAL PRIMARY KEY,
            title TEXT,
            source TEXT,
            link TEXT,
            hash TEXT
        )
    ''')
    conn.commit()
except Exception as e:
    logger.error(f"Error connecting to the database: {e}")
    exit(1)

# Define the base URL for AWS news
base_url = 'https://aws.amazon.com/about-aws/whats-new/'

# Function to calculate MD5 hash of a string
def calculate_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Function to scrape and store AWS news
def scrape_aws_news():
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        news_articles = soup.find_all('div', class_='lb-container')
        
        for article in news_articles:
            title = article.find('h4').text
            source = article.find('span', class_='lb-source').text
            link = article.find('a')['href']
            article_data = f"{title}{source}{link}"
            article_hash = calculate_hash(article_data)
            
            # Check if the article is already in the database
            cursor.execute('SELECT id FROM news WHERE hash = %s', (article_hash,))
            existing_article = cursor.fetchone()
            
            if not existing_article:
                # Insert data into the database
                cursor.execute('INSERT INTO news (title, source, link, hash) VALUES (%s, %s, %s, %s)',
                               (title, source, link, article_hash))
                conn.commit()
    except Exception as e:
        logger.error(f"An error occurred while scraping: {e}")

# Schedule the scraping function to run every day
schedule.every(1).day.do(scrape_aws_news)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

# Close the database connection
conn.close()

