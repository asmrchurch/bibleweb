const express = require('express');
const path = require('path');
const fs = require('fs');  // <-- Add this for logging
const app = express();

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, 'build')));

// Route all non-matching requests to React's index.html
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

const port = process.env.PORT || 80;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

