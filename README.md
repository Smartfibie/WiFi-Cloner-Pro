# WiFi-Cloner-Pro

Fully authorized WiFi scanner, cloner, and connector — now with full Linux support and GUI interface.

## Features
- Scans nearby WiFi networks using Aircrack-ng (airodump-ng)
- Fully functional PyQt5 GUI interface
- Works on Linux with aircrack-ng installed
- Future support for cloning, spoofing, and advanced network analysis

## Dependencies

- Python 3.x
- PyQt5
- Aircrack-ng

## Installation for Linux

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install aircrack-ng -y
python3 --version
sudo apt install python3 python3-pip -y
git clone https://github.com/Smartfibie/WiFi-Cloner-Pro.git
cd WiFi-Cloner-Pro
pip3 install -r requirements.txt
pip install pyqt5
iwconfig
sudo airmon-ng start wlan0
sudo airodump-ng --write /tmp/scan --write-interval 1 --output-format csv wlan0mon
python3 gui/main_window.py
