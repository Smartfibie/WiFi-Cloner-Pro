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
## 🛠️ System Requirements

- Ubuntu / Debian / Kali / ParrotOS / Arch-based Linux
- sudo/root access
- External or internal wireless adapter that supports monitor mode

---

## 🔧 Step-by-Step Installation

### 1️⃣ Update System

````bash
sudo apt update && sudo apt upgrade -y
2️⃣ Install Aircrack-ng
sudo apt install aircrack-ng -y

3️⃣ Install Python 3 and pip
sudo apt install python3 python3-pip -y

4️⃣ Clone Repository
git clone https://github.com/Smartfibie/WiFi-Cloner-Pro.git
cd WiFi-Cloner-Pro

5️⃣ Install Python Dependencies
pip3 install -r requirements.txt

Or manually install PyQt5:
pip3 install pyqt5

6️⃣ Identify Interface
iwconfig

7️⃣ Enable Monitor Mode
sudo airmon-ng start wlan0

8️⃣ Start Network Scan
sudo airodump-ng --write /tmp/scan --write-interval 1 --output-format csv wlan0mon

9️⃣ Launch WiFi-Cloner-Pro GUI
python3 gui/main_window.py

🔟 Disable Monitor Mode (Optional)
sudo airmon-ng stop wlan0mon
