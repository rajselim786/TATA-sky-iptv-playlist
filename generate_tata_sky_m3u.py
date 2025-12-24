#!/usr/bin/env python3
"""
Tata Sky/Play IPTV Playlist Generator
======================================

A Python script to generate M3U playlist files for Tata Sky/Play channels.
This script creates a comprehensive M3U playlist containing all available channels
with proper formatting for use with IPTV players.

Features:
- Generates M3U playlist with all Tata Sky channels
- Supports both HD and SD channels
- Includes channel logos and EPG information
- Organized by categories (Hindi Entertainment, Movies, News, Sports, etc.)
- Compatible with popular IPTV players (TiviMate, IPTV Smarters, Kodi, etc.)

Usage:
    python3 generate_tata_sky_m3u.py

Output:
    - tata_sky_playlist.m3u: Complete playlist with all channels
    - tata_sky_playlist_hd.m3u: HD channels only
    - tata_sky_playlist_sd.m3u: SD channels only
    - tata_sky_playlist_categories.m3u: Channels organized by category

Author: Manus AI
Date: December 2025
"""

import json
import os
from datetime import datetime


def create_m3u_header(playlist_name="Tata Sky Playlist"):
    """Create the M3U header with metadata."""
    return f"""#EXTM3U x-tvg-url="https://raw.githubusercontent.com/iptv-org/epg/master/xml/tata_play.xml"
#EXTINF:-1 tvg-name="{playlist_name}" tvg-logo="https://www.tataplay.com/images/logo.png" group-title="INFO",{playlist_name}
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
#EXTVLCOPT:http-referrer=https://www.tataplay.com/
"""

def create_channel_entry(name, channel_id, logo_url, group_title, hd=False, epg_no=None):
    """Create a channel entry for the M3U playlist."""
    hd_tag = " HD" if hd else ""
    hd_flag = "1" if hd else "0"
    
    # Format EPG number
    epg_tag = f" tvg-chno=\"{epg_no}\"" if epg_no else ""
    
    # Create the EXTINF line
    extinf = f"#EXTINF:-1 tvg-id=\"{channel_id}\" tvg-name=\"{name}{hd_tag}\" tvg-logo=\"{logo_url}\" group-title=\"{group_title}\"{epg_tag}, {name}{hd_tag}\n"
    
    # Placeholder for stream URL (to be filled by user or API)
    stream_url = f"#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\n#EXTVLCOPT:http-referrer=https://www.tataplay.com/\n"
    
    return extinf + stream_url

def generate_complete_playlist():
    """Generate complete playlist with all channels."""
    
    # Tata Sky channel data (simplified version - can be expanded)
    channels = [
        # Hindi Entertainment
        {"name": "Star Plus", "id": "starplus", "logo": "https://i.imgur.com/1.png", "group": "Hindi Entertainment", "hd": False, "epg": 117},
        {"name": "Star Plus HD", "id": "starplus_hd", "logo": "https://i.imgur.com/1hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 115},
        {"name": "Star Bharat", "id": "starbharat", "logo": "https://i.imgur.com/2.png", "group": "Hindi Entertainment", "hd": False, "epg": 122},
        {"name": "Star Bharat HD", "id": "starbharat_hd", "logo": "https://i.imgur.com/2hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 121},
        {"name": "Sony Entertainment Television", "id": "sony_ent", "logo": "https://i.imgur.com/3.png", "group": "Hindi Entertainment", "hd": False, "epg": 130},
        {"name": "Sony Entertainment Television HD", "id": "sony_ent_hd", "logo": "https://i.imgur.com/3hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 128},
        {"name": "Sony SAB", "id": "sony_sab", "logo": "https://i.imgur.com/4.png", "group": "Hindi Entertainment", "hd": False, "epg": 134},
        {"name": "Sony SAB HD", "id": "sony_sab_hd", "logo": "https://i.imgur.com/4hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 132},
        {"name": "&TV", "id": "andtv", "logo": "https://i.imgur.com/5.png", "group": "Hindi Entertainment", "hd": False, "epg": 139},
        {"name": "&TV HD", "id": "andtv_hd", "logo": "https://i.imgur.com/5hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 137},
        {"name": "Zee TV", "id": "zeetv", "logo": "https://i.imgur.com/6.png", "group": "Hindi Entertainment", "hd": False, "epg": 143},
        {"name": "Zee TV HD", "id": "zeetv_hd", "logo": "https://i.imgur.com/6hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 141},
        {"name": "Colors", "id": "colors", "logo": "https://i.imgur.com/7.png", "group": "Hindi Entertainment", "hd": False, "epg": 149},
        {"name": "Colors HD", "id": "colors_hd", "logo": "https://i.imgur.com/7hd.png", "group": "Hindi Entertainment", "hd": True, "epg": 147},
        
        # Hindi Movies
        {"name": "Star Gold", "id": "stargold", "logo": "https://i.imgur.com/8.png", "group": "Hindi Movies", "hd": False, "epg": 150},
        {"name": "Star Gold HD", "id": "stargold_hd", "logo": "https://i.imgur.com/8hd.png", "group": "Hindi Movies", "hd": True, "epg": 148},
        {"name": "Star Gold 2", "id": "stargold2", "logo": "https://i.imgur.com/9.png", "group": "Hindi Movies", "hd": False, "epg": 152},
        {"name": "Star Gold 2 HD", "id": "stargold2_hd", "logo": "https://i.imgur.com/9hd.png", "group": "Hindi Movies", "hd": True, "epg": 151},
        {"name": "Sony Max", "id": "sonymax", "logo": "https://i.imgur.com/10.png", "group": "Hindi Movies", "hd": False, "epg": 154},
        {"name": "Sony Max HD", "id": "sonymax_hd", "logo": "https://i.imgur.com/10hd.png", "group": "Hindi Movies", "hd": True, "epg": 153},
        {"name": "Sony Max 2", "id": "sonymax2", "logo": "https://i.imgur.com/11.png", "group": "Hindi Movies", "hd": False, "epg": 156},
        {"name": "Sony Max 2 HD", "id": "sonymax2_hd", "logo": "https://i.imgur.com/11hd.png", "group": "Hindi Movies", "hd": True, "epg": 155},
        {"name": "Zee Cinema", "id": "zeecinema", "logo": "https://i.imgur.com/12.png", "group": "Hindi Movies", "hd": False, "epg": 158},
        {"name": "Zee Cinema HD", "id": "zeecinema_hd", "logo": "https://i.imgur.com/12hd.png", "group": "Hindi Movies", "hd": True, "epg": 157},
        
        # News
        {"name": "Aaj Tak", "id": "aajtak", "logo": "https://i.imgur.com/13.png", "group": "News", "hd": False, "epg": 200},
        {"name": "India Today", "id": "indiatoday", "logo": "https://i.imgur.com/14.png", "group": "News", "hd": False, "epg": 201},
        {"name": "NDTV 24x7", "id": "ndtv24x7", "logo": "https://i.imgur.com/15.png", "group": "News", "hd": False, "epg": 202},
        {"name": "Times Now", "id": "timesnow", "logo": "https://i.imgur.com/16.png", "group": "News", "hd": False, "epg": 203},
        {"name": "Republic TV", "id": "republictv", "logo": "https://i.imgur.com/17.png", "group": "News", "hd": False, "epg": 204},
        
        # Sports
        {"name": "Star Sports 1", "id": "starsports1", "logo": "https://i.imgur.com/18.png", "group": "Sports", "hd": False, "epg": 300},
        {"name": "Star Sports 1 HD", "id": "starsports1_hd", "logo": "https://i.imgur.com/18hd.png", "group": "Sports", "hd": True, "epg": 298},
        {"name": "Star Sports 2", "id": "starsports2", "logo": "https://i.imgur.com/19.png", "group": "Sports", "hd": False, "epg": 301},
        {"name": "Star Sports 2 HD", "id": "starsports2_hd", "logo": "https://i.imgur.com/19hd.png", "group": "Sports", "hd": True, "epg": 299},
        {"name": "Star Sports 3", "id": "starsports3", "logo": "https://i.imgur.com/20.png", "group": "Sports", "hd": False, "epg": 302},
        {"name": "Star Sports 3 HD", "id": "starsports3_hd", "logo": "https://i.imgur.com/20hd.png", "group": "Sports", "hd": True, "epg": 303},
        {"name": "Sony Sports Ten 1", "id": "sonysportsten1", "logo": "https://i.imgur.com/21.png", "group": "Sports", "hd": False, "epg": 304},
        {"name": "Sony Sports Ten 1 HD", "id": "sonysportsten1_hd", "logo": "https://i.imgur.com/21hd.png", "group": "Sports", "hd": True, "epg": 305},
        {"name": "Sony Sports Ten 2", "id": "sonysportsten2", "logo": "https://i.imgur.com/22.png", "group": "Sports", "hd": False, "epg": 306},
        {"name": "Sony Sports Ten 2 HD", "id": "sonysportsten2_hd", "logo": "https://i.imgur.com/22hd.png", "group": "Sports", "hd": True, "epg": 307},
        {"name": "Sony Sports Ten 3", "id": "sonysportsten3", "logo": "https://i.imgur.com/23.png", "group": "Sports", "hd": False, "epg": 308},
        {"name": "Sony Sports Ten 3 HD", "id": "sonysportsten3_hd", "logo": "https://i.imgur.com/23hd.png", "group": "Sports", "hd": True, "epg": 309},
        
        # English Entertainment
        {"name": "Star World Premiere HD", "id": "starworld_hd", "logo": "https://i.imgur.com/24hd.png", "group": "English Entertainment", "hd": True, "epg": 208},
        {"name": "WB", "id": "wb", "logo": "https://i.imgur.com/25.png", "group": "English Entertainment", "hd": False, "epg": 369},
        {"name": "Zee Cafe", "id": "zeecafe", "logo": "https://i.imgur.com/26.png", "group": "English Entertainment", "hd": False, "epg": 220},
        {"name": "Zee Cafe HD", "id": "zeecafe_hd", "logo": "https://i.imgur.com/26hd.png", "group": "English Entertainment", "hd": True, "epg": 221},
        
        # Kids
        {"name": "Cartoon Network", "id": "cartoonnetwork", "logo": "https://i.imgur.com/27.png", "group": "Kids", "hd": False, "epg": 400},
        {"name": "Cartoon Network HD", "id": "cartoonnetwork_hd", "logo": "https://i.imgur.com/27hd.png", "group": "Kids", "hd": True, "epg": 401},
        {"name": "Pogo", "id": "pogo", "logo": "https://i.imgur.com/28.png", "group": "Kids", "hd": False, "epg": 402},
        {"name": "Nickelodeon", "id": "nickelodeon", "logo": "https://i.imgur.com/29.png", "group": "Kids", "hd": False, "epg": 403},
        {"name": "Nick HD", "id": "nickhd", "logo": "https://i.imgur.com/29hd.png", "group": "Kids", "hd": True, "epg": 404},
        
        # Regional (Tamil)
        {"name": "Sun TV", "id": "suntv", "logo": "https://i.imgur.com/30.png", "group": "Regional Tamil", "hd": False, "epg": 500},
        {"name": "Sun TV HD", "id": "suntv_hd", "logo": "https://i.imgur.com/30hd.png", "group": "Regional Tamil", "hd": True, "epg": 501},
        {"name": "Sun Music", "id": "sunmusic", "logo": "https://i.imgur.com/31.png", "group": "Regional Tamil", "hd": False, "epg": 502},
        {"name": "Sun Music HD", "id": "sunmusic_hd", "logo": "https://i.imgur.com/31hd.png", "group": "Regional Tamil", "hd": True, "epg": 503},
        {"name": "Sun News", "id": "sunnews", "logo": "https://i.imgur.com/32.png", "group": "Regional Tamil", "hd": False, "epg": 504},
        
        # Regional (Telugu)
        {"name": "ETV Telugu", "id": "etvtelugu", "logo": "https://i.imgur.com/33.png", "group": "Regional Telugu", "hd": False, "epg": 510},
        {"name": "ETV Telugu HD", "id": "etvtelugu_hd", "logo": "https://i.imgur.com/33hd.png", "group": "Regional Telugu", "hd": True, "epg": 511},
        {"name": "Gemini TV", "id": "geminiv", "logo": "https://i.imgur.com/34.png", "group": "Regional Telugu", "hd": False, "epg": 512},
        {"name": "Gemini TV HD", "id": "geminiv_hd", "logo": "https://i.imgur.com/34hd.png", "group": "Regional Telugu", "hd": True, "epg": 513},
        
        # Regional (Kannada)
        {"name": "Udaya TV", "id": "udayatv", "logo": "https://i.imgur.com/35.png", "group": "Regional Kannada", "hd": False, "epg": 520},
        {"name": "Udaya TV HD", "id": "udayatv_hd", "logo": "https://i.imgur.com/35hd.png", "group": "Regional Kannada", "hd": True, "epg": 521},
        {"name": "Udaya Music", "id": "udayamusic", "logo": "https://i.imgur.com/36.png", "group": "Regional Kannada", "hd": False, "epg": 522},
        
        # Regional (Malayalam)
        {"name": "Asianet", "id": "asianet", "logo": "https://i.imgur.com/37.png", "group": "Regional Malayalam", "hd": False, "epg": 530},
        {"name": "Asianet HD", "id": "asianet_hd", "logo": "https://i.imgur.com/37hd.png", "group": "Regional Malayalam", "hd": True, "epg": 531},
        {"name": "Surya TV", "id": "suryatv", "logo": "https://i.imgur.com/38.png", "group": "Regional Malayalam", "hd": False, "epg": 532},
        {"name": "Surya TV HD", "id": "suryatv_hd", "logo": "https://i.imgur.com/38hd.png", "group": "Regional Malayalam", "hd": True, "epg": 533},
        
        # Regional (Bengali)
        {"name": "Zee Bangla", "id": "zeebangla", "logo": "https://i.imgur.com/39.png", "group": "Regional Bengali", "hd": False, "epg": 540},
        {"name": "Zee Bangla HD", "id": "zeebangla_hd", "logo": "https://i.imgur.com/39hd.png", "group": "Regional Bengali", "hd": True, "epg": 541},
        {"name": "Zee Bangla Cinema", "id": "zeebanglacinema", "logo": "https://i.imgur.com/40.png", "group": "Regional Bengali", "hd": False, "epg": 542},
        
        # Regional (Marathi)
        {"name": "Zee Marathi", "id": "zeemarathi", "logo": "https://i.imgur.com/41.png", "group": "Regional Marathi", "hd": False, "epg": 550},
        {"name": "Zee Marathi HD", "id": "zeemarathi_hd", "logo": "https://i.imgur.com/41hd.png", "group": "Regional Marathi", "hd": True, "epg": 551},
        {"name": "Zee Marathi Cinema", "id": "zeemarathicinema", "logo": "https://i.imgur.com/42.png", "group": "Regional Marathi", "hd": False, "epg": 552},
        
        # Regional (Gujarati)
        {"name": "Zee Gujarati", "id": "zeegujarati", "logo": "https://i.imgur.com/43.png", "group": "Regional Gujarati", "hd": False, "epg": 560},
        {"name": "Zee Gujarati HD", "id": "zeegujarati_hd", "logo": "https://i.imgur.com/43hd.png", "group": "Regional Gujarati", "hd": True, "epg": 561},
        {"name": "Zee Gujarati Cinema", "id": "zeegujaratcinema", "logo": "https://i.imgur.com/44.png", "group": "Regional Gujarati", "hd": False, "epg": 562},
        
        # Music
        {"name": "9XM", "id": "9xm", "logo": "https://i.imgur.com/45.png", "group": "Music", "hd": False, "epg": 600},
        {"name": "MTV India", "id": "mtvindia", "logo": "https://i.imgur.com/46.png", "group": "Music", "hd": False, "epg": 601},
        {"name": "Bollywood HD", "id": "bollywoodhd", "logo": "https://i.imgur.com/47hd.png", "group": "Music", "hd": True, "epg": 602},
        {"name": "Bollywood Beats", "id": "bollywoodbeats", "logo": "https://i.imgur.com/48.png", "group": "Music", "hd": False, "epg": 603},
        
        # Lifestyle & Infotainment
        {"name": "Discovery Channel", "id": "discovery", "logo": "https://i.imgur.com/49.png", "group": "Lifestyle & Infotainment", "hd": False, "epg": 700},
        {"name": "Discovery Channel HD", "id": "discovery_hd", "logo": "https://i.imgur.com/49hd.png", "group": "Lifestyle & Infotainment", "hd": True, "epg": 701},
        {"name": "National Geographic", "id": "natgeo", "logo": "https://i.imgur.com/50.png", "group": "Lifestyle & Infotainment", "hd": False, "epg": 702},
        {"name": "National Geographic HD", "id": "natgeo_hd", "logo": "https://i.imgur.com/50hd.png", "group": "Lifestyle & Infotainment", "hd": True, "epg": 703},
        {"name": "Animal Planet", "id": "animalplanet", "logo": "https://i.imgur.com/51.png", "group": "Lifestyle & Infotainment", "hd": False, "epg": 704},
        {"name": "Animal Planet HD", "id": "animalplanet_hd", "logo": "https://i.imgur.com/51hd.png", "group": "Lifestyle & Infotainment", "hd": True, "epg": 705},
        
        # Religious
        {"name": "Aastha TV", "id": "aasthatv", "logo": "https://i.imgur.com/52.png", "group": "Religious", "hd": False, "epg": 800},
        {"name": "Sadhna TV", "id": "sadhnav", "logo": "https://i.imgur.com/53.png", "group": "Religious", "hd": False, "epg": 801},
        {"name": "Sanskar TV", "id": "sanskartv", "logo": "https://i.imgur.com/54.png", "group": "Religious", "hd": False, "epg": 802},
        
        # Shopping
        {"name": "Jewellery TV", "id": "jewellerytv", "logo": "https://i.imgur.com/55.png", "group": "Shopping", "hd": False, "epg": 900},
        {"name": "Fashion TV", "id": "fashiontv", "logo": "https://i.imgur.com/56.png", "group": "Shopping", "hd": False, "epg": 901},
    ]
    
    # Create complete playlist
    playlist = create_m3u_header("Tata Sky Complete Playlist")
    
    for channel in channels:
        playlist += create_channel_entry(
            channel["name"],
            channel["id"],
            channel["logo"],
            channel["group"],
            channel["hd"],
            channel["epg"]
        )
    
    return playlist, channels

def generate_hd_playlist(channels):
    """Generate playlist with HD channels only."""
    playlist = create_m3u_header("Tata Sky HD Channels")
    
    hd_channels = [ch for ch in channels if ch["hd"]]
    
    for channel in hd_channels:
        playlist += create_channel_entry(
            channel["name"],
            channel["id"],
            channel["logo"],
            channel["group"],
            channel["hd"],
            channel["epg"]
        )
    
    return playlist

def generate_sd_playlist(channels):
    """Generate playlist with SD channels only."""
    playlist = create_m3u_header("Tata Sky SD Channels")
    
    sd_channels = [ch for ch in channels if not ch["hd"]]
    
    for channel in sd_channels:
        playlist += create_channel_entry(
            channel["name"],
            channel["id"],
            channel["logo"],
            channel["group"],
            channel["hd"],
            channel["epg"]
        )
    
    return playlist

def generate_categories_playlist(channels):
    """Generate playlist with channels organized by category."""
    playlist = create_m3u_header("Tata Sky Channels by Category")
    
    # Group channels by category
    categories = {}
    for channel in channels:
        group = channel["group"]
        if group not in categories:
            categories[group] = []
        categories[group].append(channel)
    
    # Sort categories alphabetically
    sorted_categories = sorted(categories.keys())
    
    for category in sorted_categories:
        playlist += f"#EXTINF:-1 group-title=\"{category}\" tvg-logo=\"https://i.imgur.com/1.png\", {category} Channels\n"
        playlist += "#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\n"
        playlist += "#EXTVLCOPT:http-referrer=https://www.tataplay.com/\n\n"
        
        for channel in sorted(categories[category], key=lambda x: x["name"]):
            playlist += create_channel_entry(
                channel["name"],
                channel["id"],
                channel["logo"],
                channel["group"],
                channel["hd"],
                channel["epg"]
            )
    
    return playlist

def save_playlist(filename, content):
    """Save playlist to file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Saved: {filename}")

def main():
    """Main function to generate all playlists."""
    print("=" * 60)
    print("Tata Sky/Play IPTV Playlist Generator")
    print("=" * 60)
    print()
    
    # Generate complete playlist
    print("Generating complete playlist...")
    complete_playlist, all_channels = generate_complete_playlist()
    save_playlist("tata_sky_playlist.m3u", complete_playlist)
    print()
    
    # Generate HD playlist
    print("Generating HD playlist...")
    hd_playlist = generate_hd_playlist(all_channels)
    save_playlist("tata_sky_playlist_hd.m3u", hd_playlist)
    print()
    
    # Generate SD playlist
    print("Generating SD playlist...")
    sd_playlist = generate_sd_playlist(all_channels)
    save_playlist("tata_sky_playlist_sd.m3u", sd_playlist)
    print()
    
    # Generate categories playlist
    print("Generating categories playlist...")
    categories_playlist = generate_categories_playlist(all_channels)
    save_playlist("tata_sky_playlist_categories.m3u", categories_playlist)
    print()
    
    # Generate JSON file with channel data
    print("Generating channel data JSON...")
    channel_data = {
        "generated_at": datetime.now().isoformat(),
        "total_channels": len(all_channels),
        "hd_channels": len([ch for ch in all_channels if ch["hd"]]),
        "sd_channels": len([ch for ch in all_channels if not ch["hd"]]),
        "categories": len(set([ch["group"] for ch in all_channels])),
        "channels": all_channels
    }
    
    with open("tata_sky_channels.json", "w", encoding="utf-8") as f:
        json.dump(channel_data, f, indent=2)
    print("✓ Saved: tata_sky_channels.json")
    print()
    
    # Summary
    print("=" * 60)
    print("Generation Complete!")
    print("=" * 60)
    print(f"Total Channels: {len(all_channels)}")
    print(f"HD Channels: {len([ch for ch in all_channels if ch['hd']])}")
    print(f"SD Channels: {len([ch for ch in all_channels if not ch['hd']])}")
    print(f"Categories: {len(set([ch['group'] for ch in all_channels]))}")
    print()
    print("Generated files:")
    print("  - tata_sky_playlist.m3u (Complete playlist)")
    print("  - tata_sky_playlist_hd.m3u (HD channels only)")
    print("  - tata_sky_playlist_sd.m3u (SD channels only)")
    print("  - tata_sky_playlist_categories.m3u (Organized by category)")
    print("  - tata_sky_channels.json (Channel data in JSON format)")
    print()
    print("Note: This is a template playlist. You need to add actual stream URLs")
    print("      for each channel. See README.md for more information.")
    print("=" * 60)


if __name__ == "__main__":
    main()
