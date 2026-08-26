
# 🔍 IFTUBE - YouTube Metadata & OSINT Scanner

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Rg100152/iftube)](https://github.com/Rg100152/iftube/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/Rg100152/iftube)](https://github.com/Rg100152/iftube/issues)
[![GitHub Forks](https://img.shields.io/github/forks/Rg100152/iftube)](https://github.com/Rg100152/iftube/network)
[![GitHub Downloads](https://img.shields.io/github/downloads/Rg100152/iftube/total)](https://github.com/Rg100152/iftube/releases)
[![Code Size](https://img.shields.io/github/languages/code-size/Rg100152/iftube)](https://github.com/Rg100152/iftube)
[![Last Commit](https://img.shields.io/github/last-commit/Rg100152/iftube)](https://github.com/Rg100152/iftube/commits)

> **Deep Public Metadata & OSINT Scanner for YouTube Videos**
> *Extract comprehensive public information from any YouTube video*

---

## 👤 Owner & Creator

**Raj Gautam**
- GitHub: [@Rg100152](https://github.com/Rg100152)
- Project: [IFTUBE](https://github.com/Rg100152/iftube)

---

## ✨ Features

### 📊 **Metadata Extraction**
- ✅ **Video ID** & **URL Type** (Watch/Shorts/Live/Embed)
- ✅ **Title**, **Channel Name** & **Channel ID**
- ✅ **Upload Date** & **Duration**
- ✅ **View Count**, **Like Count**, **Comment Count**
- ✅ **Category**, **Language**, **Age Limit**
- ✅ **Availability Status**
- ✅ **Thumbnail URLs** (all resolutions)
- ✅ **Hashtags** & **Keywords** with frequency analysis
- ✅ **Open Graph** (og:) metadata
- ✅ **JSON-LD** structured data
- ✅ **External Links** found in description

### 🔍 **OSINT Analysis**
- ✅ **Detected Country/Region** (based on language)
- ✅ **Estimated Revenue** (based on views and CPM)
- ✅ **Keyword Density Analysis**
- ✅ **Metadata Completeness Score**
- ✅ **Channel Verification Status**
- ✅ **Content Categorization**

### 🎨 **Visual Features**
- ✅ Animated ASCII Logo
- ✅ Color-coded terminal output
- ✅ Emoji-enhanced interface
- ✅ Tabulated results for easy reading
- ✅ Progress indicators for long operations

### 📁 **Output Options**
- ✅ **JSON Report** (structured data)
- ✅ **Text Report** (human-readable)
- ✅ **CSV Export** (for spreadsheets)
- ✅ **HTML Report** (for web viewing)
- ✅ **PDF Report** (for documentation)

### ⚡ **Performance**
- ✅ Auto-install missing dependencies
- ✅ Caching for faster repeated scans
- ✅ Parallel processing for batch scans
- ✅ Configurable timeout and retry settings

---

## 🚀 Quick Start

### Installation

#### Option 1: Direct Install (Recommended)
```bash
# Clone the repository
git clone https://github.com/Rg100152/iftube.git
cd iftube

# Install dependencies
pip install -r requirements.txt

# Run the tool
python iftube.py
```

Option 2: Install as Package

```bash
# Install globally
pip install -e .

# Run from anywhere
iftube
```

Option 3: One-Line Install (Auto-install)

```bash
# Download and run (auto-installs dependencies)
curl -sSL https://raw.githubusercontent.com/Rg100152/iftube/main/iftube.py | python3
```

Basic Usage

```bash
# Run the tool
python iftube.py

# Then paste a YouTube URL when prompted
> https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Command Line Options

```bash
# Scan a video directly
python iftube.py --url "https://youtu.be/dQw4w9WgXcQ"

# Save report to JSON
python iftube.py --url "https://youtu.be/dQw4w9WgXcQ" --save

# Batch scan multiple URLs
python iftube.py --file urls.txt --batch

# Quiet mode (no output)
python iftube.py --url "https://youtu.be/dQw4w9WgXcQ" --quiet

# Enable debug mode
python iftube.py --url "https://youtu.be/dQw4w9WgXcQ" --debug
```

---

📊 Example Output

```
╔══════════════════════════════════════════════════════════════╗
║  🔍 DEEP PUBLIC METADATA & OSINT SCANNER v1.0.0           ║
║  👤 Owner: Raj Gautam                                     ║
║  📦 Open Source: https://github.com/Rg100152/iftube       ║
╚══════════════════════════════════════════════════════════════╝

🔎 Scanning URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
📹 Video ID: dQw4w9WgXcQ

⏳ Fetching page data...
⏳ Parsing metadata...
⏳ Extracting deep info with yt-dlp...
⏳ Performing OSINT analysis...

╔══════════════════════════════════════════════════════════════╗
║                    SCAN RESULTS                             ║
╚══════════════════════════════════════════════════════════════╝

📋 BASIC INFORMATION
┌────────────────────┬──────────────────────────────────────────────┐
│ Video ID           │ dQw4w9WgXcQ                                │
│ URL Type           │ Standard Watch Page                        │
│ Video ID Valid     │ ✅ Yes                                     │
│ Scan Timestamp     │ 2024-01-15T14:30:25                       │
│ Page Status        │ 200                                       │
│ Page Size          │ 245,678 bytes                             │
└────────────────────┴──────────────────────────────────────────────┘

🎬 VIDEO METADATA
┌────────────────────┬──────────────────────────────────────────────┐
│ Title              │ Never Gonna Give You Up                    │
│ Channel            │ Rick Astley                                │
│ Channel ID         │ UC8l9n5yqZQoXJXoXJXoXJXx                  │
│ Upload Date        │ October 25, 2009                          │
│ Duration           │ 213 seconds                               │
│ Views              │ 1,234,567,890                            │
│ Likes              │ 15,678,901                               │
│ Comments           │ 234,567                                  │
│ Category           │ Music                                    │
│ Language           │ en                                       │
│ Age Limit          │ None                                     │
│ Availability       │ Public                                   │
└────────────────────┴──────────────────────────────────────────────┘

🔍 OSINT ANALYSIS
┌────────────────────┬──────────────────────────────────────────────┐
│ Detected Region    │ United States/United Kingdom               │
│ Hashtag Count      │ 5                                          │
│ Word Count         │ 127                                       │
│ Metadata Completeness│ 92%                                     │
│ Estimated Revenue  │ ~$2,469,135.78                           │
└────────────────────┴──────────────────────────────────────────────┘

🏷️ HASHTAGS
#NeverGonnaGiveYouUp #RickAstley #80sMusic #Classic #Memes

📊 TOP KEYWORDS
  • never: 5 times
  • gonna: 4 times
  • give: 4 times
  • up: 3 times
  • rick: 3 times
  • astley: 3 times
  • music: 2 times
  • video: 2 times

🔗 EXTERNAL LINKS
  • https://www.rickastley.com
  • https://spotify.com/rickastley
  • https://itunes.apple.com/rickastley

🖼️ THUMBNAILS
  • https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg
  • https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg
  • https://i.ytimg.com/vi/dQw4w9WgXcQ/default.jpg
```

---

📁 Project Structure

```
iftube/
├── 📄 README.md              # Documentation
├── 📄 LICENSE                # MIT License
├── 📄 requirements.txt       # Dependencies
├── 📄 setup.py              # Installation script
├── 📄 config.json           # Configuration file
├── 📄 iftube.py             # Main script
├── 📁 reports/              # Scan reports (created automatically)
├── 📁 cache/                # Cache directory
├── 📁 temp/                 # Temporary files
├── 📁 examples/             # Example usage
│   └── sample_output.txt
└── 📁 docs/                 # Additional documentation
    ├── API.md
    ├── CONTRIBUTING.md
    └── CHANGELOG.md
```

---

🛠️ Dependencies

Package Version Purpose
requests =2.28.0 HTTP requests to fetch YouTube pages
beautifulsoup4 =4.11.0 HTML parsing for metadata extraction
yt-dlp =2023.12.30 YouTube metadata extraction
tabulate =0.9.0 Formatted table output
lxml =4.9.0 Faster HTML parsing engine

Optional Dependencies

Package Purpose
rich Enhanced terminal output with colors/formatting
pandas Data analysis and export to CSV/Excel
flask Web interface for the tool
PyQt5 Desktop GUI application
nltk Natural language processing
scikit-learn Machine learning for content analysis

Install All Dependencies

```bash
# Minimal (required)
pip install requests beautifulsoup4 yt-dlp tabulate lxml

# Full (all features)
pip install -r requirements.txt

# With extras
pip install -e .[gui,web,analytics]
```

---

⚙️ Configuration

config.json Options

```json
{
  "scan": {
    "timeout": 30,           // Request timeout in seconds
    "max_retries": 3,        // Number of retry attempts
    "cache_enabled": true,   // Enable caching
    "parallel_requests": 5   // Concurrent requests
  },
  "osint": {
    "revenue": {
      "cpm_rate": 2.5,       // Cost per 1000 views ($)
      "currency": "USD"      // Currency for revenue
    }
  },
  "output": {
    "directory": "reports",  // Output directory
    "color_output": true,    // Enable colored output
    "emoji_enabled": true    // Enable emojis
  }
}
```

Environment Variables

```bash
# Override config settings
export IFTUBE_CPM=3.0
export IFTUBE_TIMEOUT=45
export IFTUBE_OUTPUT_DIR=./my_reports
export IFTUBE_DEBUG=true
export IFTUBE_QUIET=true
export IFTUBE_CACHE=false
```

---

📝 Command Line Arguments

Argument Description
--url YouTube URL to scan
--file Text file with URLs (one per line)
--batch Enable batch scanning mode
--save Save report to file
--config Custom config file path
--output Output directory
--quiet Suppress all output
--debug Enable debug mode
--verbose Enable verbose output
--version Show version information
--help Show help message

---

🎯 Use Cases

1. Content Analysis

· Analyze video metadata for research
· Study trending topics and hashtags
· Track channel growth and engagement

2. OSINT Investigations

· Gather public information about videos
· Verify video authenticity
· Identify content patterns and trends

3. Marketing Research

· Analyze competitor videos
· Study engagement metrics
· Estimate revenue potential

4. Data Collection

· Extract metadata for databases
· Build datasets for analysis
· Monitor video changes over time

5. Educational Purposes

· Learn about metadata extraction
· Understand web scraping techniques
· Practice OSINT methodologies

---

🔧 Troubleshooting

Common Issues

1. Missing Dependencies

```bash
# Auto-install (handled by script)
python iftube.py

# Manual install
pip install -r requirements.txt
```

2. Connection Timeout

```bash
# Increase timeout in config
"timeout": 60
```

3. Rate Limiting

```bash
# Use caching
"cache_enabled": true

# Increase delay between requests
"retry_delay": 5
```

4. SSL Certificate Errors

```bash
# Disable SSL verification (not recommended)
"verify_ssl": false
```

Debug Mode

```bash
# Enable debug mode
python iftube.py --debug

# Check logs
tail -f iftube.log
```

---

🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

Development Setup

```bash
# Clone the repository
git clone https://github.com/Rg100152/iftube.git
cd iftube

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest tests/

# Check code style
flake8 iftube.py
black iftube.py
```

Code Style Guidelines

· Follow PEP 8 standards
· Use descriptive variable names
· Add docstrings for all functions
· Write unit tests for new features
· Update documentation accordingly

---

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 Raj Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

🛡️ Disclaimer

IMPORTANT: This tool extracts ONLY PUBLIC metadata available through YouTube's official pages and APIs.

· ✅ Legal: All data is legally obtainable through standard web scraping
· ✅ Safe: No private data (IP, email, tokens) is accessed
· ✅ Ethical: Respects YouTube's robots.txt
· ❌ No Hacking: Does not bypass security measures
· ❌ No Piracy: Does not download videos
· ❌ No Automation: Manual scanning only

Use Responsibly: This tool is for educational and research purposes only. 
Please respect YouTube's terms of service and use responsibly.

---

📚 Documentation

· API Documentation
· Contributing Guide
· Changelog
· FAQ

---

📞 Support & Contact

Issues & Bugs

· GitHub Issues
· Bug Report Template

Questions & Discussions

· GitHub Discussions
· Discord Community

Follow & Connect

· Owner: Raj Gautam
· Twitter: @RG100152
· LinkedIn: Raj Gautam

---

🌟 Star History

https://api.star-history.com/svg?repos=Rg100152/iftube&type=Date

---

🙏 Acknowledgments

· yt-dlp - YouTube metadata extraction
· BeautifulSoup - HTML parsing
· Requests - HTTP requests
· All contributors and users of IFTUBE

---

📊 Statistics

https://github-readme-stats.vercel.app/api/pin/?username=Rg100152&repo=iftube&show_owner=true&theme=dark

---

🏆 Changelog

v1.0.0 (Current)

· ✅ Initial release
· ✅ Full metadata extraction
· ✅ OSINT analysis
· ✅ JSON and text reports
· ✅ Auto-install dependencies
· ✅ Colorful terminal output
· ✅ Configuration system

Coming Soon (v1.1.0)

· 🚀 Web interface
· 🚀 Batch scanning
· 🚀 CSV/Excel export
· 🚀 Database integration
· 🚀 API mode
· 🚀 GUI application

---

💖 Support the Project

If you find IFTUBE useful, consider:

· ⭐ Starring the repository
· 🍴 Forking the project
· 🐛 Reporting issues
· 📝 Contributing code
· 📢 Spreading the word
· 💰 Buy me a coffee

---

📈 Roadmap

☐ Web Interface (Flask/Django)
☐ Desktop GUI (PyQt/Tkinter)
☐ Database Integration
☐ Batch Processing
☐ Multiple Export Formats
☐ Real-time Monitoring
☐ API Mode
☐ Docker Support
☐ CI/CD Pipeline
☐ Automated Testing

---

🔗 Links

· GitHub: https://github.com/Rg100152/iftube
· Issues: https://github.com/Rg100152/iftube/issues
· Discussions: https://github.com/Rg100152/iftube/discussions
· Releases: https://github.com/Rg100152/iftube/releases

---

<div align="center">

Made with ❤️ by Raj Gautam

If you like this project, don't forget to ⭐ star it on GitHub!

</div>
```

---

📄 Alternative: Quick README (Minimal Version)

For those who prefer a shorter README:

```markdown
# IFTUBE - YouTube Metadata Scanner 🔍

**Owner: Raj Gautam** | [GitHub](https://github.com/Rg100152/iftube)

## 🚀 Quick Start

```bash
git clone https://github.com/Rg100152/iftube.git
cd iftube
pip install -r requirements.txt
python iftube.py
```

✨ Features

· Extract video metadata (title, views, likes, etc.)
· OSINT analysis (region, revenue estimate)
· Hashtag and keyword extraction
· JSON and text reports
· Colorful terminal output

📊 Example

```
🎬 VIDEO METADATA
┌────────────────┬──────────────────────────┐
│ Title          │ Never Gonna Give You Up  │
│ Views          │ 1,234,567,890           │
│ Estimated Revenue│ ~$2,469,135.78        │
└────────────────┴──────────────────────────┘
```

📜 License

MIT License - see LICENSE

Made with ❤️ by Raj Gautam

```

---

## 🎯 **README Sections Summary**

| Section | Content |
|---------|---------|
| **Header** | Badges, title, description |
| **Owner** | Creator information |
| **Features** | All tool capabilities |
| **Quick Start** | Installation and usage |
| **Example Output** | Sample scan results |
| **Project Structure** | File organization |
| **Dependencies** | Required packages |
| **Configuration** | Config file options |
| **CLI Arguments** | Command line options |
| **Use Cases** | Practical applications |
| **Troubleshooting** | Common issues |
| **Contributing** | Development guidelines |
| **License** | MIT License |
| **Disclaimer** | Legal/ethical notice |
| **Support** | Contact information |
| **Changelog** | Version history |
| **Roadmap** | Future plans |

---

This complete README is fully professional, informative, and ready for your GitHub repository! 🚀
