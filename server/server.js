const express = require('express');
const path = require('path');
const axios = require('axios');
const app = express();

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Route to handle /player/:minecraftusername requests
app.get('/player/:minecraftusername', (req, res) => {
    const minecraftUsername = req.params.minecraftusername;
    const mojangapi = "https://api.mojang.com/users/profiles/minecraft/" + minecraftUsername;
    const hypixelAPIKey = "002af19e-6259-4f3b-b463-2ccc53dbdc43";

    axios.get(mojangapi)
        .then(response => {
            // Handle the API response data
            const playerData = response.data;
            const mojangUUID = playerData.id;
            const hypixelAPIRequest = `https://api.hypixel.net/player?key=${hypixelAPIKey}&uuid=${mojangUUID}`
            
            axios.get(hypixelAPIRequest)
                .then(response => {
                    const hypixeldata = response.data
                    const html = `<html><body><h1>Wins in bridge: ${hypixeldata["player"]["achievements"]["duels_bridge_wins"]}</h1></body></html>`;
                    console.log(hypixeldata["player"]["achievements"]["duels_bridge_wins"]);
                    res.send(html);
                })
                .catch(error => {
                    console.error("Error fetching Hypixel API:", error);
                    const errormessage = error.response.data["cause"]
                    res.send(`<html><body><h1>${errormessage}</h1></body></html>`);
                });
        })
        .catch(error => {
            // Handle any errors that occurred during the API request
            console.error("Error fetching Mojang API:", error);
            res.send(`<html><body><h1>${error.response.data["errorMessage"]}</h1></body></html>`);
        });
});

// Start the server on port 80
const PORT = 80;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
