# Tata Sky/Play IPTV Playlist Generator

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python script to generate M3U playlist files for Tata Sky/Play channels with comprehensive channel information.

## 📋 Overview

This repository contains a Python script that generates M3U playlist files for Tata Sky/Play channels. The playlists are compatible with popular IPTV players and include comprehensive channel information with proper formatting.

## 🎯 Features

- **Complete Channel List**: Generates playlists with all major Tata Sky/Play channels
- **Multiple Formats**: Creates complete playlist, HD-only, SD-only, and category-organized playlists
- **Proper M3U Format**: Follows standard M3U format with EPG information, logos, and group titles
- **JSON Channel Data**: Includes comprehensive channel data in JSON format
- **Well-Documented**: Complete documentation and usage instructions

## 📦 Included Files

- `generate_tata_sky_m3u.py` - Main Python script to generate playlists
- `tata_sky_playlist.m3u` - Complete playlist with all channels
- `tata_sky_playlist_hd.m3u` - HD channels only
- `tata_sky_playlist_sd.m3u` - SD channels only
- `tata_sky_playlist_categories.m3u` - Channels organized by category
- `tata_sky_channels.json` - Channel data in JSON format
- `README.md` - This documentation file

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Basic knowledge of command line

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tata-sky-iptv.git
cd tata-sky-iptv
```

2. Run the script:

```bash
python3 generate_tata_sky_m3u.py
```

3. The script will generate all playlist files in the current directory.

## 📺 Generated Playlists

### 1. Complete Playlist (`tata_sky_playlist.m3u`)

Contains all channels including both HD and SD versions, organized by category.

### 2. HD Playlist (`tata_sky_playlist_hd.m3u`)

Contains only HD channels for high-definition viewing.

### 3. SD Playlist (`tata_sky_playlist_sd.m3u`)

Contains only SD channels for lower bandwidth requirements.

### 4. Categories Playlist (`tata_sky_playlist_categories.m3u`)

Channels organized by category with section headers for easy navigation.

## 📊 Channel Categories

The playlists include channels from the following categories:

- **Hindi Entertainment**: Star Plus, Sony Entertainment, Zee TV, Colors, &TV
- **Hindi Movies**: Star Gold, Sony Max, Zee Cinema
- **English Entertainment**: Star World, WB, Zee Cafe
- **News**: Aaj Tak, India Today, NDTV, Times Now, Republic TV
- **Sports**: Star Sports, Sony Sports Ten
- **Kids**: Cartoon Network, Pogo, Nickelodeon
- **Regional**:
  - Tamil: Sun TV, Sun Music, Sun News
  - Telugu: ETV Telugu, Gemini TV
  - Kannada: Udaya TV, Udaya Music
  - Malayalam: Asianet, Surya TV
  - Bengali: Zee Bangla
  - Marathi: Zee Marathi
  - Gujarati: Zee Gujarati
- **Music**: 9XM, MTV India, Bollywood HD
- **Lifestyle & Infotainment**: Discovery, National Geographic, Animal Planet
- **Religious**: Aastha TV, Sadhna TV, Sanskar TV
- **Shopping**: Jewellery TV, Fashion TV

## 🎨 M3U Format

The playlists follow the standard M3U format with extended information:

```m3u
#EXTINF:-1 tvg-id="starplus" tvg-name="Star Plus" tvg-logo="https://i.imgur.com/1.png" group-title="Hindi Entertainment", Star Plus
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
#EXTVLCOPT:http-referrer=https://www.tataplay.com/
```

### Tags Explained

- `#EXTINF`: Channel information line
  - `-1`: Duration (live stream)
  - `tvg-id`: Unique channel identifier
  - `tvg-name`: Channel name
  - `tvg-logo`: Channel logo URL
  - `group-title`: Category/group
  - Channel name: Display name
- `#EXTVLCOPT`: VLC options for user agent and referrer

## 📱 Compatible IPTV Players

The generated playlists work with the following popular IPTV players:

### Android
- **TiviMate** - Premium IPTV player with excellent features
- **IPTV Smarters Pro** - Free and feature-rich
- **Perfect Player** - Popular and reliable
- **VLC for Android** - Free and open-source

### iOS
- **IPTV Smarters Pro** - Available on App Store
- **VLC for iOS** - Free and open-source

### Windows
- **VLC Media Player** - Free and open-source
- **IPTVnator** - Modern IPTV player

### macOS
- **VLC Media Player** - Free and open-source
- **IPTVnator** - Modern IPTV player

### Linux
- **VLC Media Player** - Free and open-source
- **Kodi** - Powerful media center

### Smart TVs
- **VLC for Smart TVs**
- **IPTV apps** available on Samsung, LG, and Android TVs

## 🎬 How to Use

### Method 1: Import Playlist URL

1. Upload the `.m3u` file to a web server or cloud storage (Google Drive, Dropbox, etc.)
2. Get the direct download link
3. Open your IPTV player
4. Add the playlist using the URL
5. Enjoy watching!

### Method 2: Local File Import

1. Copy the `.m3u` file to your device
2. Open your IPTV player
3. Import the playlist from local storage
4. Enjoy watching!

## ⚠️ Important Notes

### Stream URLs Required

**This script generates a template playlist with channel information only.** You need to add actual stream URLs for each channel to make them playable.

To add stream URLs, you can:

1. **Use a Tata Sky account**: Extract stream URLs from your Tata Sky/Play account using authentication scripts (see [ForceGT/Tata-Sky-IPTV](https://github.com/ForceGT/Tata-Sky-IPTV))

2. **Use third-party services**: Some services provide M3U playlists with working stream URLs

3. **Manual addition**: Edit the `.m3u` file and add stream URLs manually

### Legal Disclaimer

This script is for educational purposes only. Ensure you have proper authorization to access and stream the channels. Unauthorized streaming may violate copyright laws and terms of service.

## 🔧 Customization

### Adding More Channels

Edit the `generate_tata_sky_m3u.py` file and add more channels to the `channels` list:

```python
{
    "name": "Channel Name",
    "id": "channel_id",
    "logo": "https://i.imgur.com/logo.png",
    "group": "Category Name",
    "hd": True/False,
    "epg": EPG_NUMBER
}
```

### Changing Channel Order

Modify the `channels` list order in the script to change the playlist order.

### Adding Custom Logos

Replace the logo URLs with your preferred logo images.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions or issues, please open an issue in the GitHub repository.

## 📚 Related Projects

- [ForceGT/Tata-Sky-IPTV](https://github.com/ForceGT/Tata-Sky-IPTV) - Authentication-based playlist generator
- [Rob2k9/Tata-Sky-IPTV](https://github.com/Rob2k9/Tata-Sky-IPTV) - Fork with additional features
- [dnyaneshpainjane/Tataplay-m3u-webplay](https://github.com/dnyaneshpainjane/Tataplay-m3u-webplay) - PHP web application
- [YoCodeCrafters/tataplay-generator](https://github.com/YoCodeCrafters/tataplay-generator) - PHP script with API integration

## 🙏 Acknowledgments

- Tata Sky/Play for providing the channel data
- Open-source community for M3U format and IPTV players
- ForceGT for the original research and implementation

## 📅 Version History

- **v1.0.0** (December 2025) - Initial release with comprehensive channel list

---

**Disclaimer**: This script is for educational purposes only. Always ensure you have proper authorization to access and stream content. Unauthorized streaming may violate copyright laws and terms of service.
