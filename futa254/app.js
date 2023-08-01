const API_BASE_URL = "https://your-api-url.com"; // Replace with the actual API base URL

async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching data:", error.message);
        return null;
    }
}

async function displayMatchList() {
    const matchListContainer = document.getElementById("matchList");
    const matches = await fetchData(`${API_BASE_URL}/matches`);
    
    if (!matches) {
        matchListContainer.innerHTML = "<p>Error fetching match data.</p>";
        return;
    }

    let matchListHTML = "<h2>Upcoming Matches</h2><ul>";
    matches.forEach(match => {
        matchListHTML += `<li data-match-id="${match.id}">${match.date}: ${match.homeTeam} vs. ${match.awayTeam}</li>`;
    });
    matchListHTML += "</ul>";

    matchListContainer.innerHTML = matchListHTML;
    addMatchClickListeners();
}

function displayMatchDetails(matchId) {
    const matchDetailsContainer = document.getElementById("matchDetails");

    // Display loading message while fetching details
    matchDetailsContainer.innerHTML = "<p>Loading match details...</p>";

    fetchData(`${API_BASE_URL}/matches/${matchId}`)
        .then(match => {
            if (!match) {
                matchDetailsContainer.innerHTML = "<p>Error fetching match details.</p>";
                return;
            }

            // Display match details
            const matchDetailsHTML = `
                <h2>Match Details</h2>
                <p>Date: ${match.date}</p>
                <p>Home Team: ${match.homeTeam}</p>
                <p>Away Team: ${match.awayTeam}</p>
                <!-- Add more details as needed -->
            `;

            matchDetailsContainer.innerHTML = matchDetailsHTML;
        });
}

function addMatchClickListeners() {
    const matchListItems = document.querySelectorAll("#matchList li");
    matchListItems.forEach(item => {
        item.addEventListener("click", () => {
            const matchId = item.getAttribute("data-match-id");
            displayMatchDetails(matchId);
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    displayMatchList();
});

