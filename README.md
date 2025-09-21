# 🌊 Flood - Random Poetry Generator

A beautiful Python Flask web application that generates random poems using English language templates with cycling word options. Each poem is unique, created by selecting random words from curated pools to fill poetic templates.

## ✨ Features

- **Random Poem Generation**: Creates unique poems using templates and word pools
- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **API Endpoint**: RESTful API for programmatic access to poem generation
- **Copy to Clipboard**: Easy sharing of generated poems
- **Keyboard Shortcuts**: Press 'G' to generate, 'C' to copy
- **Mobile Responsive**: Works perfectly on all device sizes

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+ (for npm scripts)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fproulx-boostsecurity/flood.git
   cd flood
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser to [http://localhost:5000](http://localhost:5000)

### Using npm scripts

```bash
# Install dependencies and run tests
npm install
npm test

# Start the application
npm start

# Development mode
npm run dev
```

## 📖 Usage

### Web Interface

1. Visit the homepage to see a randomly generated poem
2. Click "✨ Generate New Poem" to create a new poem
3. Click "📋 Copy Poem" to copy the current poem to clipboard
4. Use keyboard shortcuts: 'G' to generate, 'C' to copy

### API Usage

Get a random poem as JSON:

```bash
curl http://localhost:5000/api/poem
```

Example response:
```json
{
  "title": "Nature's Song",
  "lines": [
    "The beautiful flower dances through the meadow,",
    "While butterflies play in the golden morning.",
    "A rose petal glows so bright,",
    "In this magical world of light."
  ]
}
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
npm test

# Run Python tests only
python -m pytest tests/ -v
```

## 🎨 Customization

### Adding New Poem Templates

Edit `app.py` and add new templates to the `POEM_TEMPLATES` list:

```python
{
    "title": "Your Template Title",
    "lines": [
        "Line with {placeholder} words",
        "Another line with {different_placeholder}"
    ]
}
```

### Adding New Word Categories

Add new word pools to the `WORD_POOLS` dictionary in `app.py`:

```python
WORD_POOLS = {
    "your_category": ["word1", "word2", "word3"],
    # ... existing categories
}
```

## 🚀 Deployment

### GitHub Actions

This repository includes a GitHub Actions workflow that automatically:

- Builds and tests the application when PRs are opened from forks
- Creates GitHub releases with packaged application
- Uses `pull_request_target` for secure fork handling

### Manual Deployment

1. Package the application:
   ```bash
   tar -czf flood-release.tar.gz app.py requirements.txt package.json templates static
   ```

2. Deploy to your server and extract
3. Install dependencies and run

## 🛠️ Development

### Project Structure

```
flood/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── package.json          # npm configuration and scripts
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── app.js        # Client-side JavaScript
├── tests/
│   ├── __init__.py
│   └── test_app.py       # Test suite
└── .github/
    └── workflows/
        └── release.yml    # GitHub Actions workflow
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `npm test`
5. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Built with Flask and Bootstrap
- Uses Crimson Text font from Google Fonts
- Gradient backgrounds inspired by modern web design trends