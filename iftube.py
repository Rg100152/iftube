#!/usr/bin/env python3
"""
IFTUBE - YouTube Metadata & OSINT Scanner
Owner: Raj Gautam
Auto-installs required packages if missing
"""

import sys
import subprocess
import os

# ==================== AUTO INSTALLER ====================
def install_packages():
    """Auto-install required packages"""
    required = ['requests', 'beautifulsoup4', 'yt-dlp', 'tabulate']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"📦 Installing missing packages: {', '.join(missing)}")
        for package in missing:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--quiet'])
                print(f"✅ Installed: {package}")
            except:
                print(f"❌ Failed to install: {package}")
                print(f"Please manually install: pip install {package}")
                return False
        print("✅ All packages installed!\n")
        return True
    return True

# Install packages before importing
if not install_packages():
    sys.exit(1)

# Now import
import re
import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple

try:
    import requests
    from bs4 import BeautifulSoup
    import yt_dlp
    from tabulate import tabulate
except ImportError as e:
    print(f"❌ Still missing: {e}")
    print("Please manually install: pip install requests beautifulsoup4 yt-dlp tabulate")
    sys.exit(1)

# ==================== CONFIGURATION ====================
VERSION = "1.0.0"
OWNER = "Raj Gautam"
TOOL_NAME = "IFTUBE"
COLORS = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "END": "\033[0m"
}

# ==================== ASCII ART LOGO ====================
LOGO = r"""
    ██▓▓███████ ████████ ██    ██ ██████  ███████ 
    ▓██▒▓█   ▀ ██   ▀  ██    ██ ██   ██ ██      
    ▒██▒▒███   ██      ██    ██ ██████  █████   
    ░██░▒▓█  ▄ ▓█▄    ██    ██ ██   ██ ██      
    ░██░░█████ ░██████  ██████  ██████  ███████ 
    ░▓  ░░ ░░ ░ ░ ░░ ░ ░░ ░░ ░ ░ ░░ ░ ░ ░░ ░ ░
"""

def print_banner():
    """Display animated banner with tool info"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Animated typing effect for logo
    for line in LOGO.split('\n'):
        if line.strip():
            print(f"{COLORS['CYAN']}{line}{COLORS['END']}")
            time.sleep(0.05)
    
    print(f"\n{COLORS['BOLD']}{COLORS['GREEN']}╔══════════════════════════════════════════════════════════════╗{COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['GREEN']}║  {COLORS['YELLOW']}🔍 DEEP PUBLIC METADATA & OSINT SCANNER v{VERSION}{COLORS['GREEN']}           ║{COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['GREEN']}║  {COLORS['CYAN']}👤 Owner: {OWNER}{COLORS['GREEN']}                                             ║{COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['GREEN']}╚══════════════════════════════════════════════════════════════╝{COLORS['END']}")
    print()

# ==================== CORE SCANNER ====================
class YouTubeScanner:
    def __init__(self, url: str):
        self.url = url.strip()
        self.video_id = self.extract_video_id()
        self.data = {
            "scan_timestamp": datetime.now().isoformat(),
            "url": self.url,
            "video_id": self.video_id,
            "metadata": {},
            "technical": {},
            "osint": {},
            "analysis": {}
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def extract_video_id(self) -> Optional[str]:
        """Extract YouTube video ID from various URL formats"""
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/live\/([a-zA-Z0-9_-]{11})'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.url)
            if match:
                return match.group(1)
        return None

    def get_url_type(self) -> str:
        """Determine URL type"""
        if 'youtu.be' in self.url:
            return 'youtu.be (Shortened)'
        elif '/shorts/' in self.url:
            return 'YouTube Shorts'
        elif '/live/' in self.url:
            return 'YouTube Live'
        elif '/embed/' in self.url:
            return 'Embedded Player'
        elif '/watch?v=' in self.url:
            return 'Standard Watch Page'
        else:
            return 'Unknown'

    def fetch_page(self) -> Optional[str]:
        """Fetch YouTube page HTML"""
        try:
            response = self.session.get(self.url, timeout=10)
            if response.status_code == 200:
                self.data['technical']['status_code'] = response.status_code
                self.data['technical']['page_size'] = len(response.text)
                self.data['technical']['redirect_url'] = response.url if response.url != self.url else None
                return response.text
            else:
                self.data['technical']['status_code'] = response.status_code
                return None
        except Exception as e:
            print(f"{COLORS['RED']}❌ Error fetching page: {e}{COLORS['END']}")
            return None

    def parse_metadata(self, html: str):
        """Parse metadata from HTML using BeautifulSoup"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract Open Graph metadata
        og_data = {}
        for tag in soup.find_all('meta', property=re.compile(r'^og:')):
            og_data[tag.get('property')] = tag.get('content', '')
        
        # Extract standard meta tags
        meta_data = {}
        for tag in soup.find_all('meta', attrs={'name': True}):
            meta_data[tag.get('name')] = tag.get('content', '')
        
        # Extract JSON-LD
        json_ld = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                json_ld.append(data)
            except:
                pass
        
        # Extract title
        title = soup.find('title')
        title = title.text.strip() if title else 'N/A'
        
        # Extract description from meta
        description = meta_data.get('description', og_data.get('og:description', 'N/A'))
        
        # Extract keywords/tags
        keywords = meta_data.get('keywords', '').split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        
        # Extract all links
        links = []
        for link in soup.find_all('a', href=True):
            links.append(link['href'])
        
        # Extract external links (non-youtube)
        external_links = [l for l in links if 'youtube.com' not in l and 'youtu.be' not in l and l.startswith('http')]
        
        # Extract hashtags
        hashtags = re.findall(r'#\w+', html)
        
        self.data['metadata'] = {
            'title': title,
            'description': description,
            'og_title': og_data.get('og:title', 'N/A'),
            'og_description': og_data.get('og:description', 'N/A'),
            'og_image': og_data.get('og:image', 'N/A'),
            'og_url': og_data.get('og:url', 'N/A'),
            'keywords': keywords[:10] if keywords else [],
            'json_ld': json_ld[:3] if json_ld else [],
            'hashtags': list(set(hashtags))[:20],
            'external_links': external_links[:20],
            'all_links': links[:50]
        }

    def extract_ytdlp_info(self):
        """Extract metadata using yt-dlp"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,
                'force_generic_extractor': False
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                if info:
                    self.data['metadata'].update({
                        'channel_name': info.get('channel', 'N/A'),
                        'channel_id': info.get('channel_id', 'N/A'),
                        'channel_url': info.get('channel_url', 'N/A'),
                        'upload_date': info.get('upload_date', 'N/A'),
                        'view_count': info.get('view_count', 0),
                        'like_count': info.get('like_count', 0),
                        'comment_count': info.get('comment_count', 0),
                        'duration': info.get('duration', 0),
                        'categories': info.get('categories', []),
                        'tags': info.get('tags', []),
                        'language': info.get('language', 'N/A'),
                        'age_limit': info.get('age_limit', 0),
                        'availability': info.get('availability', 'N/A'),
                        'thumbnails': info.get('thumbnails', [])
                    })
                    
                    # Parse upload date
                    if 'upload_date' in info and info['upload_date'] != 'N/A':
                        try:
                            date_obj = datetime.strptime(info['upload_date'], '%Y%m%d')
                            self.data['metadata']['upload_date_formatted'] = date_obj.strftime('%B %d, %Y')
                        except:
                            pass
        except Exception as e:
            print(f"{COLORS['YELLOW']}⚠️ yt-dlp partial extraction: {e}{COLORS['END']}")

    def analyze_content(self):
        """Perform OSINT-style analysis"""
        meta = self.data['metadata']
        
        # URL type
        self.data['osint']['url_type'] = self.get_url_type()
        self.data['osint']['video_id_valid'] = bool(self.video_id and len(self.video_id) == 11)
        
        # Channel info
        if meta.get('channel_name') != 'N/A':
            self.data['osint']['channel_name'] = meta['channel_name']
            self.data['osint']['channel_id'] = meta.get('channel_id', 'N/A')
            self.data['osint']['channel_url'] = meta.get('channel_url', 'N/A')
        
        # Content analysis
        description = meta.get('description', '')
        hashtags = meta.get('hashtags', [])
        self.data['osint']['hashtag_count'] = len(hashtags)
        self.data['osint']['word_count'] = len(description.split())
        self.data['osint']['keyword_density'] = self.calculate_keyword_density(description)
        
        # Metadata completeness score
        fields_present = sum(1 for k, v in meta.items() if v and v != 'N/A' and v != [] and v != 0)
        total_fields = len(meta)
        self.data['osint']['metadata_completeness'] = f"{int((fields_present/total_fields)*100)}%"
        
        # Region/Country detection (based on language and other clues)
        if meta.get('language') and meta['language'] != 'N/A':
            self.data['osint']['detected_region'] = self.language_to_country(meta['language'])
        
        # Revenue estimation (approximate based on views)
        views = meta.get('view_count', 0)
        if views and views > 0:
            # Extremely rough estimate (YouTube CPM varies widely)
            estimated_revenue = views * 0.001 * 2  # $2 RPM average
            self.data['osint']['estimated_revenue'] = f"~${estimated_revenue:,.2f}"
        else:
            self.data['osint']['estimated_revenue'] = "N/A"

    def calculate_keyword_density(self, text: str) -> List[Tuple[str, int]]:
        """Calculate keyword frequency in text"""
        words = re.findall(r'\w+', text.lower())
        freq = {}
        for word in words:
            if len(word) > 3:  # Ignore short words
                freq[word] = freq.get(word, 0) + 1
        # Return top 10
        return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

    def language_to_country(self, lang_code: str) -> str:
        """Map language code to country/region"""
        lang_map = {
            'en': 'United States/United Kingdom',
            'hi': 'India',
            'es': 'Spain/Latin America',
            'fr': 'France/Canada',
            'de': 'Germany',
            'ja': 'Japan',
            'ko': 'South Korea',
            'pt': 'Brazil/Portugal',
            'ru': 'Russia',
            'zh': 'China/Taiwan',
            'ar': 'Middle East/North Africa',
            'it': 'Italy',
            'nl': 'Netherlands',
            'pl': 'Poland',
            'tr': 'Turkey'
        }
        return lang_map.get(lang_code[:2], 'Unknown')

    def scan(self):
        """Main scanning method"""
        print(f"{COLORS['BLUE']}🔎 Scanning URL: {self.url}{COLORS['END']}")
        print(f"{COLORS['CYAN']}📹 Video ID: {self.video_id}{COLORS['END']}\n")
        
        # Step 1: Fetch page
        print(f"{COLORS['YELLOW']}⏳ Fetching page data...{COLORS['END']}")
        html = self.fetch_page()
        if not html:
            print(f"{COLORS['RED']}❌ Failed to fetch page{COLORS['END']}")
            return
        
        # Step 2: Parse metadata
        print(f"{COLORS['YELLOW']}⏳ Parsing metadata...{COLORS['END']}")
        self.parse_metadata(html)
        
        # Step 3: Extract with yt-dlp
        print(f"{COLORS['YELLOW']}⏳ Extracting deep info with yt-dlp...{COLORS['END']}")
        self.extract_ytdlp_info()
        
        # Step 4: OSINT analysis
        print(f"{COLORS['YELLOW']}⏳ Performing OSINT analysis...{COLORS['END']}\n")
        self.analyze_content()

    def display_results(self):
        """Display results in a formatted table"""
        meta = self.data['metadata']
        tech = self.data['technical']
        osint = self.data['osint']
        
        print(f"{COLORS['BOLD']}{COLORS['GREEN']}╔══════════════════════════════════════════════════════════════╗{COLORS['END']}")
        print(f"{COLORS['BOLD']}{COLORS['GREEN']}║                    SCAN RESULTS                             ║{COLORS['END']}")
        print(f"{COLORS['BOLD']}{COLORS['GREEN']}╚══════════════════════════════════════════════════════════════╝{COLORS['END']}\n")
        
        # Basic Info
        print(f"{COLORS['BOLD']}{COLORS['CYAN']}📋 BASIC INFORMATION{COLORS['END']}")
        basic_table = [
            ["Video ID", self.video_id or 'N/A'],
            ["URL Type", osint.get('url_type', 'N/A')],
            ["Video ID Valid", '✅ Yes' if osint.get('video_id_valid') else '❌ No'],
            ["Scan Timestamp", self.data['scan_timestamp']],
            ["Page Status", tech.get('status_code', 'N/A')],
            ["Page Size", f"{tech.get('page_size', 0):,} bytes" if tech.get('page_size') else 'N/A']
        ]
        print(tabulate(basic_table, tablefmt="grid"))
        print()

        # Video Metadata
        print(f"{COLORS['BOLD']}{COLORS['CYAN']}🎬 VIDEO METADATA{COLORS['END']}")
        video_table = [
            ["Title", meta.get('title', 'N/A')[:70] + '...' if len(meta.get('title', '')) > 70 else meta.get('title', 'N/A')],
            ["Channel", meta.get('channel_name', 'N/A')],
            ["Channel ID", meta.get('channel_id', 'N/A')],
            ["Upload Date", meta.get('upload_date_formatted', meta.get('upload_date', 'N/A'))],
            ["Duration", f"{meta.get('duration', 0)} seconds" if meta.get('duration') else 'N/A'],
            ["Views", f"{meta.get('view_count', 0):,}" if meta.get('view_count') else 'N/A'],
            ["Likes", f"{meta.get('like_count', 0):,}" if meta.get('like_count') else 'N/A'],
            ["Comments", f"{meta.get('comment_count', 0):,}" if meta.get('comment_count') else 'N/A'],
            ["Category", ', '.join(meta.get('categories', ['N/A']))[:50]],
            ["Language", meta.get('language', 'N/A')],
            ["Age Limit", meta.get('age_limit', 0) or 'None'],
            ["Availability", meta.get('availability', 'N/A')]
        ]
        print(tabulate(video_table, tablefmt="grid"))
        print()

        # OSINT Analysis
        print(f"{COLORS['BOLD']}{COLORS['CYAN']}🔍 OSINT ANALYSIS{COLORS['END']}")
        osint_table = [
            ["Detected Region", osint.get('detected_region', 'N/A')],
            ["Hashtag Count", osint.get('hashtag_count', 0)],
            ["Word Count", osint.get('word_count', 0)],
            ["Metadata Completeness", osint.get('metadata_completeness', 'N/A')],
            ["Estimated Revenue", osint.get('estimated_revenue', 'N/A')]
        ]
        print(tabulate(osint_table, tablefmt="grid"))
        print()

        # Hashtags
        if meta.get('hashtags'):
            print(f"{COLORS['BOLD']}{COLORS['CYAN']}🏷️ HASHTAGS{COLORS['END']}")
            hashtag_str = ' '.join(meta['hashtags'][:10])
            print(f"{COLORS['YELLOW']}{hashtag_str}{COLORS['END']}\n")

        # Top Keywords
        if osint.get('keyword_density'):
            print(f"{COLORS['BOLD']}{COLORS['CYAN']}📊 TOP KEYWORDS{COLORS['END']}")
            for word, count in osint['keyword_density'][:8]:
                print(f"{COLORS['GREEN']}  • {word}: {count} times{COLORS['END']}")
            print()

        # External Links
        if meta.get('external_links'):
            print(f"{COLORS['BOLD']}{COLORS['CYAN']}🔗 EXTERNAL LINKS{COLORS['END']}")
            for link in meta['external_links'][:5]:
                print(f"{COLORS['BLUE']}  • {link[:80]}{COLORS['END']}")
            if len(meta['external_links']) > 5:
                print(f"{COLORS['YELLOW']}  ... and {len(meta['external_links']) - 5} more{COLORS['END']}")
            print()

        # Thumbnail URLs
        if meta.get('thumbnails'):
            print(f"{COLORS['BOLD']}{COLORS['CYAN']}🖼️ THUMBNAILS{COLORS['END']}")
            for thumb in meta['thumbnails'][:3]:
                print(f"{COLORS['BLUE']}  • {thumb.get('url', 'N/A')[:60]}{COLORS['END']}")

    def save_report(self):
        """Save scan results to JSON file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"iftube_scan_{self.video_id}_{timestamp}.json"
        
        # Clean data for JSON
        clean_data = self.data.copy()
        # Remove large lists for cleaner JSON
        if 'metadata' in clean_data:
            clean_data['metadata'].pop('all_links', None)
            clean_data['metadata'].pop('json_ld', None)
            clean_data['metadata'].pop('external_links', None)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(clean_data, f, indent=2, ensure_ascii=False)
        
        print(f"{COLORS['GREEN']}✅ Report saved: {filename}{COLORS['END']}")

# ==================== MAIN ====================
def main():
    print_banner()
    
    while True:
        print(f"{COLORS['BOLD']}{COLORS['YELLOW']}📌 Enter YouTube URL (or 'exit' to quit):{COLORS['END']}")
        url = input("> ").strip()
        
        if url.lower() in ['exit', 'quit', 'q']:
            print(f"{COLORS['GREEN']}👋 Thank you for using IFTUBE!{COLORS['END']}")
            break
        
        if not url:
            continue
        
        # Validate URL
        if 'youtube.com' not in url and 'youtu.be' not in url:
            print(f"{COLORS['RED']}❌ Invalid YouTube URL. Please try again.{COLORS['END']}\n")
            continue
        
        scanner = YouTubeScanner(url)
        if not scanner.video_id:
            print(f"{COLORS['RED']}❌ Could not extract video ID. Invalid URL?{COLORS['END']}\n")
            continue
        
        # Perform scan
        scanner.scan()
        
        # Display results
        scanner.display_results()
        
        # Save report
        print(f"{COLORS['YELLOW']}\n💾 Save report to JSON? (y/n):{COLORS['END']}")
        if input("> ").lower() == 'y':
            scanner.save_report()
        
        print(f"\n{COLORS['GREEN']}{'='*60}{COLORS['END']}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{COLORS['YELLOW']}⚠️ Scan interrupted by user{COLORS['END']}")
        sys.exit(0)
    except Exception as e:
        print(f"{COLORS['RED']}❌ Unexpected error: {e}{COLORS['END']}")
        sys.exit(1)
