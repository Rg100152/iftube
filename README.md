🔍 IFTUBE

YouTube Metadata & Public OSINT Scanner

IFTUBE is a free and open-source Python CLI tool for collecting and analyzing publicly available YouTube metadata from a video URL.

It combines direct webpage metadata parsing with "yt-dlp" extraction and performs lightweight OSINT-style analysis to produce a structured overview of the target video.

«Built for the community. Free for everyone. Open by design.»

---

✨ Features

- 🔗 YouTube URL analysis
- 🆔 Automatic Video ID extraction
- 🎬 Video title and channel information
- 📅 Upload date
- 👁️ View count
- 👍 Like count when available
- 💬 Comment count when available
- ⏱️ Video duration
- 🏷️ Categories and tags
- 🌐 Language information
- 🖼️ Thumbnail URLs
- 🔗 External links found in public page metadata
- #️⃣ Hashtag extraction
- 📊 Keyword-frequency analysis
- 🧠 Metadata completeness score
- 🌍 Language-based region indication
- 📡 HTTP response information
- 📄 JSON report generation
- 🎨 Cyber-style terminal interface
- 📦 Automatic dependency installation
- 🐍 Python-based and cross-platform

---

⚡ Quick Start

1. Clone the repository

git clone https://github.com/Rg100152/iftube.git
cd iftube

2. Run IFTUBE

python3 iftube.py

IFTUBE will automatically check for the required Python packages and attempt to install missing dependencies.

---

📦 Manual Installation

If you prefer installing dependencies manually:

pip install -r requirements.txt

Required packages:

requests
beautifulsoup4
yt-dlp
tabulate

Then run:

python3 iftube.py

---

🖥️ Usage

Start the scanner:

python3 iftube.py

You will see:

📌 Enter YouTube URL (or 'exit' to quit):
>

Paste a YouTube URL:

https://www.youtube.com/watch?v=VIDEO_ID

IFTUBE will perform several stages:

[1] URL validation
[2] Video ID extraction
[3] Webpage retrieval
[4] Public metadata parsing
[5] yt-dlp metadata extraction
[6] OSINT-style analysis
[7] Result presentation
[8] Optional JSON report generation

---

🔍 Supported URL Types

IFTUBE can recognize common YouTube URL formats such as:

https://www.youtube.com/watch?v=XXXXXXXXXXX
https://youtu.be/XXXXXXXXXXX
https://www.youtube.com/shorts/XXXXXXXXXXX
https://www.youtube.com/live/XXXXXXXXXXX
https://www.youtube.com/embed/XXXXXXXXXXX

---

📊 What IFTUBE Collects

🎬 Video Metadata

Depending on what YouTube exposes publicly and what "yt-dlp" can retrieve:

Title
Channel Name
Channel ID
Channel URL
Upload Date
Duration
View Count
Like Count
Comment Count
Category
Tags
Language
Age Limit
Availability
Thumbnail URLs

🌐 Web Metadata

IFTUBE also examines publicly exposed webpage metadata such as:

Open Graph title
Open Graph description
Open Graph image
Open Graph URL
HTML title
Meta description
Meta keywords
JSON-LD metadata
Public hashtags
Public external links

🧠 OSINT Analysis

The tool performs lightweight analysis including:

URL Type
Video ID validation
Hashtag count
Description word count
Keyword frequency
Metadata completeness
Language-based region indication

---

🖥️ Example Output

╔══════════════════════════════════════════════════════════════╗
║                    SCAN RESULTS                             ║
╚══════════════════════════════════════════════════════════════╝

📋 BASIC INFORMATION

+------------------+----------------------+
| Video ID         | XXXXXXXXXXX          |
| URL Type         | Standard Watch Page  |
| Video ID Valid   | ✅ Yes               |
| Page Status      | 200                  |
| Page Size        | 250,000 bytes        |
+------------------+----------------------+

🎬 VIDEO METADATA

+------------------+----------------------+
| Title            | Example Video        |
| Channel          | Example Channel      |
| Upload Date      | August 27, 2026      |
| Duration         | 420 seconds          |
| Views            | 125,000              |
| Likes            | 8,500                |
| Comments         | 620                  |
| Language         | en                   |
+------------------+----------------------+

🔍 OSINT ANALYSIS

+------------------------+----------------------+
| Detected Region        | United States/UK     |
| Hashtag Count          | 8                    |
| Word Count             | 320                  |
| Metadata Completeness  | 82%                  |
+------------------------+----------------------+

---

💾 JSON Reports

IFTUBE can save scan results as a JSON file.

Example:

iftube_scan_VIDEO_ID_20260827_010000.json

The report contains structured information such as:

{
  "scan_timestamp": "...",
  "url": "...",
  "video_id": "...",
  "metadata": {},
  "technical": {},
  "osint": {},
  "analysis": {}
}

This makes the output useful for:

- Automation
- Research
- Data analysis
- OSINT workflows
- Educational projects
- Integration with other scripts

---

🧩 Project Structure

iftube/
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── iftube.py
├── config.json
└── examples/
    └── sample_output.txt

File Description

File| Description
"iftube.py"| Main scanner
"config.json"| Configuration
"requirements.txt"| Python dependencies
"setup.py"| Package configuration
"README.md"| Project documentation
"LICENSE"| Open-source license
"examples/"| Example output

---

🛠️ Technology Stack

IFTUBE is built with:

- Python 3
- "requests"
- "BeautifulSoup4"
- "yt-dlp"
- "tabulate"
- Python standard library

---

📱 Compatible Environments

IFTUBE is designed to work on common Python environments, including:

- 🐧 Linux
- 🪟 Windows
- 🍎 macOS
- 📱 Termux
- 📱 Pydroid 3

Some environments may require additional permissions or package-management configuration.

---

⚠️ Important Limitations

IFTUBE only reports information that can be obtained through publicly accessible pages, metadata, or supported extraction mechanisms.

It does not provide access to private YouTube account information.

IFTUBE cannot legitimately reveal things such as:

Private email addresses
Private IP addresses
Private account data
Private analytics
Private revenue information
Authentication credentials
Cookies or session secrets
Private uploader location
Hidden device information

If a field is unavailable, the scanner may return:

N/A

This is expected behavior.

---

💰 Revenue Estimate

Any revenue-related value shown by the tool is only a rough theoretical estimate.

Actual YouTube revenue can vary significantly depending on:

- Audience location
- RPM
- CPM
- Advertiser demand
- Content category
- Monetization status
- YouTube Premium views
- Ad availability

Therefore, revenue estimates should not be treated as actual creator earnings.

---

🔐 Responsible Use

IFTUBE is intended for:

- Educational research
- Public-data analysis
- OSINT learning
- Metadata research
- Python development
- Cybersecurity education
- Open-source experimentation

Use the tool responsibly and respect YouTube's terms, applicable laws, privacy expectations, and rate limits.

Do not use it to attempt to access private information or bypass authentication and access controls.

---

🚀 Roadmap

Future versions may introduce:

[ ] Better URL parser
[ ] Improved metadata extraction
[ ] Rich terminal UI
[ ] Progress animations
[ ] JSON/CSV export
[ ] Report directory support
[ ] Configuration system
[ ] Metadata comparison
[ ] Multiple URL scanning
[ ] Channel-level public analysis
[ ] Improved error handling
[ ] Plugin architecture
[ ] Unit tests
[ ] PyPI packaging
[ ] GitHub Actions CI

---

🤝 Contributing

IFTUBE is open source and contributions are welcome.

Contribution workflow

git clone https://github.com/Rg100152/iftube.git
cd iftube

Create a branch:

git checkout -b feature/my-feature

Make your changes and test them.

Then:

git add .
git commit -m "Add: my feature"
git push origin feature/my-feature

Open a Pull Request on GitHub.

Good contribution ideas

- Bug fixes
- Better metadata extraction
- Improved error handling
- Documentation
- Tests
- CLI improvements
- Performance improvements
- Cross-platform compatibility

---

🐛 Issues

Found a bug or have an idea?

Open an issue in the GitHub repository and include:

Python version
Operating system
IFTUBE version
Command used
Error message
Expected behavior
Actual behavior

Avoid posting private credentials, cookies, API keys, or other sensitive information.

---

📜 License

IFTUBE is released under the license included in this repository.

See:

LICENSE

before redistributing or modifying the project.

---

👨‍💻 Author

Raj Gautam

IFTUBE is an independent open-source project created for learning, experimentation, public metadata analysis, and the open-source community.

---

❤️ Open Source

IFTUBE is free to use and developed with an open-source philosophy.

«No paywall. No unnecessary API barrier. Just open source.»

If you find IFTUBE useful, consider:

⭐ Starring the repository
🐛 Reporting bugs
💡 Suggesting features
🔧 Contributing code
📖 Improving documentation

---

🔗 Repository

GitHub:

https://github.com/Rg100152/iftube

---

IFTUBE

Public Data
     ↓
YouTube URL
     ↓
Metadata Extraction
     ↓
yt-dlp + HTML Parser
     ↓
OSINT Analysis
     ↓
Structured Results
     ↓
JSON Report

IFTUBE — Explore public metadata. Learn. Build. Share.
