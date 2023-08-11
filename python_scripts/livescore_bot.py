import requests
from bs4 import BeautifulSoup
import time
import logging
import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_db_connection():
    """Create a new database connection."""
    try:
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="your_db_host",
            port="your_db_port"
        )
        return conn
    except Exception as e:
        logger.error(f"Error creating database connection: {e}")
        raise

def close_db_connection(conn):
    """Close the database connection."""
    try:
        if conn:
            conn.close()
    except Exception as e:
        logger.error(f"Error closing database connection: {e}")

def scrape_live_scores():
    url = "https://www.example.com/live-scores"  # Replace with the actual URL

    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')

        matches = soup.find_all('div', class_='match')
        
        for match in matches:
            league = match.find('div', class_='league').text
            team1 = match.find('div', class_='team1').text
            team2 = match.find('div', class_='team2').text
            score = match.find('div', class_='score').text

            # Print and save to the database
            print(f"{league}: {team1} {score} {team2}")
            cursor.execute(sql.SQL('INSERT INTO scores (league, team1, team2, score) VALUES (%s, %s, %s, %s)'),
                           (league, team1, team2, score))
            conn.commit()

    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred during the request: {e}")
    except OperationalError as e:
        logger.error(f"Operational error: {e}")
    except Exception as e:
        logger.error(f"An error occurred while scraping: {e}")
    finally:
        close_db_connection(conn)

# Scrape live scores every 30 seconds
while True:
    scrape_live_scores()
    time.sleep(30)

