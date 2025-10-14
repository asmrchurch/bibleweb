const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, 'build')));

// Function to extract metadata from markdown
function extractMetadata(markdownPath) {
    try {
        const markdown = fs.readFileSync(markdownPath, 'utf-8');
        const lines = markdown.split('\n');

        // Extract title (first H1)
        const titleLine = lines.find(line => line.startsWith('#'));
        const title = titleLine ? titleLine.replace(/^#\s*/, '').trim() : '説教';

        // Extract description (first paragraph after title)
        const titleIndex = lines.findIndex(line => line.startsWith('#'));
        let description = '';
        for (let i = titleIndex + 1; i < lines.length; i++) {
            const line = lines[i].trim();
            if (line && !line.startsWith('!') && !line.startsWith('#')) {
                description = line;
                break;
            }
        }
        // Clean and limit description
        description = description.replace(/[*_`~[\]()]/g, '').substring(0, 150) || '説教の内容をお読みください。';

        // Extract first image
        const imageMatch = markdown.match(/!\[.*?\]\((.*?)\)/);
        const image = imageMatch && imageMatch[1]
            ? `https://www.asmrchurch.com${imageMatch[1]}`
            : 'https://www.asmrchurch.com/static/images/i4.jpg';

        return { title, description, image };
    } catch (error) {
        console.error('Error extracting metadata:', error);
        return {
            title: '説教 - ASMRキリスト教会',
            description: 'ASMRキリスト教会の説教',
            image: 'https://www.asmrchurch.com/static/images/i4.jpg'
        };
    }
}

// Special handling for sermon pages to inject meta tags
app.get('/sermon/:id', (req, res) => {
    const sermonId = req.params.id;
    const markdownPath = path.join(__dirname, 'public', 'static', 'markdown', 'sermon', `${sermonId}.md`);
    const url = `https://www.asmrchurch.com/sermon/${sermonId}`;

    // Extract metadata from the markdown file
    const { title, description, image } = extractMetadata(markdownPath);

    // Read the index.html file
    const indexPath = path.join(__dirname, 'build', 'index.html');
    let html = fs.readFileSync(indexPath, 'utf-8');

    // Inject meta tags into the head
    const metaTags = `
    <meta property="og:type" content="article" />
    <meta property="og:title" content="${title.replace(/"/g, '&quot;')}" />
    <meta property="og:description" content="${description.replace(/"/g, '&quot;')}" />
    <meta property="og:url" content="${url}" />
    <meta property="og:image" content="${image}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="${title.replace(/"/g, '&quot;')}" />
    <meta name="twitter:description" content="${description.replace(/"/g, '&quot;')}" />
    <meta name="twitter:url" content="${url}" />
    <meta name="twitter:image" content="${image}" />
    <title>${title.replace(/"/g, '&quot;')} - ASMRキリスト教会</title>
    <meta name="description" content="${description.replace(/"/g, '&quot;')}" />
    `;

    // Replace the existing title and description, and inject OG tags
    html = html.replace(/<title>.*?<\/title>/, `<title>${title.replace(/"/g, '&quot;')} - ASMRキリスト教会</title>`);
    html = html.replace(/<meta name="description".*?>/, `<meta name="description" content="${description.replace(/"/g, '&quot;')}" />`);
    html = html.replace('</head>', `${metaTags}</head>`);

    res.send(html);
});

// Route all other non-matching requests to React's index.html
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

const port = process.env.PORT || 80;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

