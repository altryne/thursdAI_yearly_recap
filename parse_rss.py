#!/usr/bin/env python3
"""
Parse ThursdAI RSS feed and organize 2025 episodes into folders by quarter and month.

Creates folder structure:
- Q1 2025/
  - January 2025/
    - episode_name.md
    - ...
  - January_2025_combined.md
  - February 2025/
  - ...
  - Q1_2025_combined.md
- Q2 2025/
  - ...
etc.
"""

import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from html import unescape
import re
from collections import defaultdict


def parse_rss(file_path: str) -> list[dict]:
    """Parse the RSS file and return a list of episode dictionaries."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Define namespaces used in the RSS
    namespaces = {
        'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
    }
    
    episodes = []
    
    # Find all items in the channel
    channel = root.find('channel')
    if channel is None:
        print("No channel found in RSS")
        return episodes
    
    for item in channel.findall('item'):
        episode = {}
        
        # Extract title
        title_elem = item.find('title')
        if title_elem is not None and title_elem.text:
            episode['title'] = clean_cdata(title_elem.text)
        else:
            episode['title'] = 'Untitled Episode'
        
        # Extract publication date
        pub_date_elem = item.find('pubDate')
        if pub_date_elem is not None and pub_date_elem.text:
            episode['pub_date_raw'] = pub_date_elem.text
            episode['pub_date'] = parse_date(pub_date_elem.text)
        else:
            continue  # Skip items without dates
        
        # Extract description
        desc_elem = item.find('description')
        if desc_elem is not None and desc_elem.text:
            episode['description'] = clean_cdata(desc_elem.text)
        else:
            episode['description'] = ''
        
        # Extract link
        link_elem = item.find('link')
        if link_elem is not None and link_elem.text:
            episode['link'] = link_elem.text
        else:
            episode['link'] = ''
        
        # Extract creator
        creator_elem = item.find('dc:creator', namespaces)
        if creator_elem is not None and creator_elem.text:
            episode['creator'] = clean_cdata(creator_elem.text)
        else:
            episode['creator'] = ''
        
        # Extract duration
        duration_elem = item.find('itunes:duration', namespaces)
        if duration_elem is not None and duration_elem.text:
            episode['duration'] = format_duration(duration_elem.text)
        else:
            episode['duration'] = ''
        
        # Extract audio URL
        enclosure_elem = item.find('enclosure')
        if enclosure_elem is not None:
            episode['audio_url'] = enclosure_elem.get('url', '')
        else:
            episode['audio_url'] = ''
        
        # Extract image URL
        image_elem = item.find('itunes:image', namespaces)
        if image_elem is not None:
            episode['image_url'] = image_elem.get('href', '')
        else:
            episode['image_url'] = ''
        
        episodes.append(episode)
    
    return episodes


def clean_cdata(text: str) -> str:
    """Clean CDATA wrapper and unescape HTML entities."""
    if text is None:
        return ''
    # Remove CDATA wrapper if present
    text = text.strip()
    if text.startswith('<![CDATA['):
        text = text[9:]
    if text.endswith(']]>'):
        text = text[:-3]
    return unescape(text).strip()


def parse_date(date_str: str) -> datetime:
    """Parse RFC 2822 date format used in RSS feeds."""
    # Example: 'Fri, 05 Dec 2025 01:03:51 GMT'
    try:
        return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    except ValueError:
        # Try without timezone
        try:
            return datetime.strptime(date_str[:25], '%a, %d %b %Y %H:%M:%S')
        except ValueError:
            return datetime.now()


def format_duration(duration_str: str) -> str:
    """Format duration from seconds to HH:MM:SS."""
    try:
        seconds = int(duration_str)
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"
    except ValueError:
        return duration_str


def get_quarter(month: int) -> int:
    """Get quarter number from month number."""
    return (month - 1) // 3 + 1


def sanitize_filename(title: str) -> str:
    """Create a safe filename from a title."""
    # Remove emojis and special characters
    title = re.sub(r'[^\w\s\-]', '', title)
    # Replace spaces with underscores
    title = re.sub(r'\s+', '_', title)
    # Limit length
    return title[:100]


def html_to_markdown(html_content: str) -> str:
    """Convert HTML content to markdown (basic conversion)."""
    text = html_content
    
    # Replace common HTML tags
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<p>', '\n\n', text)
    text = re.sub(r'</p>', '', text)
    text = re.sub(r'<strong>', '**', text)
    text = re.sub(r'</strong>', '**', text)
    text = re.sub(r'<em>', '*', text)
    text = re.sub(r'</em>', '*', text)
    text = re.sub(r'<a\s+[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', text)
    text = re.sub(r'</?ul>', '\n', text)
    text = re.sub(r'<li>', '\n* ', text)
    text = re.sub(r'</li>', '', text)
    text = re.sub(r'<h\d>', '\n## ', text)
    text = re.sub(r'</h\d>', '\n', text)
    
    # Remove any remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Clean up multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


def create_episode_markdown(episode: dict) -> str:
    """Create markdown content for a single episode."""
    date_str = episode['pub_date'].strftime('%B %d, %Y')
    
    content = f"""# {episode['title']}

**Date:** {date_str}  
**Duration:** {episode['duration']}  
**Link:** [{episode['link']}]({episode['link']})

---

## Description

{html_to_markdown(episode['description'])}
"""
    return content


def create_combined_markdown(episodes: list[dict], period_name: str) -> str:
    """Create combined markdown for multiple episodes."""
    content = f"""# ThursdAI Episodes - {period_name}

Total Episodes: {len(episodes)}

---

"""
    # Sort episodes by date (newest first)
    sorted_episodes = sorted(episodes, key=lambda x: x['pub_date'], reverse=True)
    
    for episode in sorted_episodes:
        date_str = episode['pub_date'].strftime('%B %d, %Y')
        content += f"""## {episode['title']}

**Date:** {date_str}  
**Duration:** {episode['duration']}  
**Link:** [{episode['link']}]({episode['link']})

{html_to_markdown(episode['description'])}

---

"""
    return content


def main():
    """Main function to parse RSS and create folder structure."""
    script_dir = Path(__file__).parent
    rss_file = script_dir / 'all_thursdai.rss'
    
    if not rss_file.exists():
        print(f"RSS file not found: {rss_file}")
        return
    
    print(f"Parsing RSS file: {rss_file}")
    episodes = parse_rss(str(rss_file))
    print(f"Found {len(episodes)} total episodes")
    
    # Filter for 2025 episodes only
    episodes_2025 = [ep for ep in episodes if ep['pub_date'].year == 2025]
    print(f"Found {len(episodes_2025)} episodes from 2025")
    
    if not episodes_2025:
        print("No episodes found for 2025!")
        return
    
    # Organize by quarter and month
    quarters = defaultdict(lambda: defaultdict(list))
    
    for episode in episodes_2025:
        month = episode['pub_date'].month
        quarter = get_quarter(month)
        month_name = episode['pub_date'].strftime('%B')
        
        quarters[quarter][month_name].append(episode)
    
    # Create folder structure and files
    output_dir = script_dir / '2025_episodes'
    output_dir.mkdir(exist_ok=True)
    
    for quarter_num in sorted(quarters.keys()):
        quarter_name = f"Q{quarter_num} 2025"
        quarter_dir = output_dir / quarter_name
        quarter_dir.mkdir(exist_ok=True)
        
        quarter_episodes = []
        
        for month_name in sorted(quarters[quarter_num].keys(), 
                                  key=lambda x: datetime.strptime(x, '%B').month):
            month_full_name = f"{month_name} 2025"
            month_dir = quarter_dir / month_full_name
            month_dir.mkdir(exist_ok=True)
            
            month_episodes = quarters[quarter_num][month_name]
            quarter_episodes.extend(month_episodes)
            
            # Create individual episode files
            for episode in month_episodes:
                filename = sanitize_filename(episode['title']) + '.md'
                filepath = month_dir / filename
                
                content = create_episode_markdown(episode)
                filepath.write_text(content, encoding='utf-8')
                print(f"  Created: {filepath.relative_to(script_dir)}")
            
            # Create combined file for the month
            combined_filename = f"{month_name}_2025_combined.md"
            combined_path = quarter_dir / combined_filename
            combined_content = create_combined_markdown(month_episodes, month_full_name)
            combined_path.write_text(combined_content, encoding='utf-8')
            print(f"Created monthly combined: {combined_path.relative_to(script_dir)}")
        
        # Create combined file for the quarter
        quarter_combined_filename = f"Q{quarter_num}_2025_combined.md"
        quarter_combined_path = quarter_dir / quarter_combined_filename
        quarter_combined_content = create_combined_markdown(quarter_episodes, quarter_name)
        quarter_combined_path.write_text(quarter_combined_content, encoding='utf-8')
        print(f"Created quarterly combined: {quarter_combined_path.relative_to(script_dir)}")
    
    print(f"\nDone! Output written to: {output_dir}")
    print("\nFolder structure:")
    print_tree(output_dir, script_dir)


def print_tree(path: Path, base: Path, prefix: str = ""):
    """Print a tree structure of the directory."""
    entries = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
    
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{entry.name}")
        
        if entry.is_dir():
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(entry, base, next_prefix)


if __name__ == '__main__':
    main()
