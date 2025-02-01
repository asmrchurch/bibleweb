const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();

app.use(express.static('build'));

app.use((req, res, next) => {
    const userIP = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    const logMessage = `${new Date().toISOString()} - IP: ${userIP} - ${req.method} ${req.url}\n`;

    console.log(logMessage);

    fs.appendFileSync(path.join(__dirname, 'access.log'), logMessage);

    next();
});

const PORT = process.env.PORT || 80;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
