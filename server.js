const express = require('express');
const path = require('path');
const fs = require('fs');  // <-- Add this for logging
const app = express();

// Middleware for logging user IPs (Minimal change)
app.use((req, res, next) => {
    const userIP = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    const logMessage = `${new Date().toISOString()} - IP: ${userIP} - ${req.method} ${req.url}`;

    console.log(logMessage);  // Show log in terminal (pm2 logs)
    
    // Append log to file (non-blocking, to avoid performance issues)
    fs.appendFile(path.join(__dirname, 'access.log'), logMessage, (err) => {
        if (err) console.error('Failed to write log:', err);
    });

    next();  // Ensure the request proceeds to existing handlers
});

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

