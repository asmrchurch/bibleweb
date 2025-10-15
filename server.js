const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, 'build')));
app.use('/static', express.static(path.join(__dirname, 'public', 'static')));

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

// Function to extract verse text from Bible HTML
function extractVerseFromBible(htmlPath, chapter, verse) {
    try {
        const html = fs.readFileSync(htmlPath, 'utf-8');
        const verseId = `${chapter}-${verse}`;

        // Find the verse element by ID
        const verseRegex = new RegExp(`<em id="${verseId}"[^>]*>.*?</em><span id='verse'><span id='verse'>([^<]+)</span></span>`, 's');
        const match = html.match(verseRegex);

        if (match && match[1]) {
            return match[1].trim();
        }

        return '';
    } catch (error) {
        console.error('Error extracting verse:', error);
        return '';
    }
}

// Book name mapping (English to Japanese)
const bookNamesJa = {
    genesis: '創世記',
    exodus: '出エジプト記',
    leviticus: 'レビ記',
    numbers: '民数記',
    deuteronomy: '申命記',
    joshua: 'ヨシュア記',
    judges: '士師記',
    ruth: 'ルツ記',
    '1samuel': 'サムエル記上',
    '2samuel': 'サムエル記下',
    '1kings': '列王記上',
    '2kings': '列王記下',
    '1chronicles': '歴代志上',
    '2chronicles': '歴代志下',
    ezra: 'エズラ記',
    nehemiah: 'ネヘミヤ記',
    esther: 'エステル記',
    job: 'ヨブ記',
    psalms: '詩篇',
    proverbs: '箴言',
    ecclesiastes: '伝道の書',
    songofsongs: '雅歌',
    isaiah: 'イザヤ書',
    jeremiah: 'エレミヤ書',
    lamentations: '哀歌',
    ezekiel: 'エゼキエル書',
    daniel: 'ダニエル書',
    hosea: 'ホセア書',
    joel: 'ヨエル書',
    amos: 'アモス書',
    obadiah: 'オバデヤ書',
    jonah: 'ヨナ書',
    micah: 'ミカ書',
    nahum: 'ナホム書',
    habakkuk: 'ハバクク書',
    zephaniah: 'ゼパニヤ書',
    haggai: 'ハガイ書',
    zechariah: 'ゼカリヤ書',
    malachi: 'マラキ書',
    matthew: 'マタイによる福音書',
    mark: 'マルコによる福音書',
    luke: 'ルカによる福音書',
    john: 'ヨハネによる福音書',
    acts: '使徒行伝',
    romans: 'ローマ人への手紙',
    '1corinthians': 'コリント人への第一の手紙',
    '2corinthians': 'コリント人への第二の手紙',
    galatians: 'ガラテヤ人への手紙',
    ephesians: 'エペソ人への手紙',
    philippians: 'ピリピ人への手紙',
    colossians: 'コロサイ人への手紙',
    '1thessalonians': 'テサロニケ人への第一の手紙',
    '2thessalonians': 'テサロニケ人への第二の手紙',
    '1timothy': 'テモテへの第一の手紙',
    '2timothy': 'テモテへの第二の手紙',
    titus: 'テトスへの手紙',
    philemon: 'ピレモンへの手紙',
    hebrews: 'ヘブル人への手紙',
    james: 'ヤコブの手紙',
    '1peter': 'ペテロの第一の手紙',
    '2peter': 'ペテロの第二の手紙',
    '1john': 'ヨハネの第一の手紙',
    '2john': 'ヨハネの第二の手紙',
    '3john': 'ヨハネの第三の手紙',
    jude: 'ユダの手紙',
    revelation: 'ヨハネの黙示録',
    tobit: 'トビト記',
    judith: 'ユディト記',
    wisdom: '知恵の書',
    sirach: 'シラ書',
    baruch: 'バルク書',
    '1maccabees': 'マカバイ記一',
    '2maccabees': 'マカバイ記二',
    susanna: 'スザンナ'
};

// Special handling for Bible verse pages to inject meta tags
app.get('/bible/:section/:chapter/:verse', (req, res) => {
    const { section, chapter, verse } = req.params;
    const htmlPath = path.join(__dirname, 'public', 'static', 'html', 'norm', `${section}.htm`);
    const url = `https://www.asmrchurch.com/bible/${section}/${chapter}/${verse}`;

    // Extract verse text from HTML
    const verseText = extractVerseFromBible(htmlPath, chapter, verse);
    const bookNameJa = bookNamesJa[section] || section;
    const title = `${bookNameJa} ${chapter}:${verse}`;
    const description = verseText || '口語訳聖書 旧約：1955年版・新約：1954年版';
    const image = 'https://www.asmrchurch.com/static/images/c4.jpg';

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

