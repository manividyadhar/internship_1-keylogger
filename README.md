# Educational Keylogger Project

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ⚠️ Legal & Ethical Disclaimer

**WARNING**: This project is for **educational purposes only**. 

- ✅ Use only on systems you own
- ✅ Get explicit written permission before monitoring any device
- ❌ Unauthorized keylogging is **ILLEGAL** in most jurisdictions
- ❌ Violates privacy laws and computer fraud statutes

**By using this software, you agree to use it responsibly and legally.**

## 📋 Project Overview

A cross-platform educational keylogger built with Python that demonstrates:
- Keyboard event monitoring
- File I/O operations
- Cross-platform compatibility
- Logging and data persistence
- Ethical security research principles

### Features

- ✨ Cross-platform support (Windows & Linux)
- 📝 Real-time keystroke logging
- 🔒 Buffered writing for efficiency
- 📊 System information logging
- ⌨️ Special key detection
- 🛑 Emergency stop (ESC key)
- 📁 Organized log file management
- ⏰ Timestamped log files

## 🚀 Installation Guide

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Administrator/sudo privileges (for some systems)

### Step-by-Step Installation

#### For Windows:

```bash
# 1. Clone the repository
git clone https://github.com/Bhaveshpooniwala1/PRODIGY_CS_04.git
cd educational-keylogger

# 2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the keylogger
python keylogger.py
```

#### For Linux:

```bash
# 1. Clone the repository
git clone https://github.com/Bhaveshpooniwala1/PRODIGY_CS_04.git
cd educational-keylogger

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the keylogger (may require sudo)
sudo python3 keylogger.py
```

## 📖 Usage

### Basic Usage

```bash
# Activate virtual environment first
python keylogger.py
```

### What Happens:

1. Program displays ethical warning
2. Asks for consent confirmation
3. Creates `keylogs/` directory if not exists
4. Starts logging keystrokes
5. Press **ESC** to stop and save logs

### Output Example

```
[+] Created log directory: keylogs
[+] Logging to: keylogs/keylog_20241207_143052.txt
============================================================
EDUCATIONAL KEYLOGGER - RUNNING
============================================================
[*] Keylogger is now active...
[*] Press ESC to stop logging
============================================================
```

## 📁 Project Structure

```
educational-keylogger/
│
├── keylogger.py          # Main keylogger script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── LICENSE              # License file
├── .gitignore          # Git ignore file
│
├── keylogs/            # Generated log files directory
│   ├── keylog_20241207_143052.txt
│   └── keylog_20241207_154823.txt
│
└── docs/               # Additional documentation
    ├── INSTALLATION.md
    └── ETHICS.md
```

## 🔧 Configuration

### Customization Options

In `keylogger.py`, you can modify:

```python
# Buffer size (keys before writing to file)
self.buffer_size = 10

# Log directory name
log_dir = "keylogs"

# Date format
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
```

## 📊 Log File Format

```
2024-12-07 14:30:52 - ==================================================
2024-12-07 14:30:52 - KEYLOGGER SESSION STARTED
2024-12-07 14:30:52 - ==================================================
2024-12-07 14:30:52 - System: Windows
2024-12-07 14:30:52 - Release: 10
2024-12-07 14:30:52 - hello world[ENTER]
2024-12-07 14:31:15 - testing[BACKSPACE][BACKSPACE]
```

## 🛠️ Technical Details

### Key Components

1. **KeyLogger Class**: Main class handling all logging operations
2. **Event Listeners**: Captures keyboard events using pynput
3. **Buffer System**: Efficient writing with configurable buffer size
4. **Log Management**: Timestamped files with system information

### Technologies Used

- **pynput**: Cross-platform keyboard monitoring
- **logging**: Python's built-in logging framework
- **datetime**: Timestamp generation
- **platform**: System information gathering

## 🐛 Troubleshooting

### Common Issues

**Issue 1: Permission Denied (Linux)**
```bash
# Solution: Run with sudo
sudo python3 keylogger.py
```

**Issue 2: Module Not Found**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Issue 3: Pynput Not Working**
```bash
# Linux: Install X11 development libraries
sudo apt-get install python3-xlib
```

**Issue 4: Virtual Environment Issues**
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

## 📈 Learning Outcomes

By completing this project, you will learn:

- ✅ Event-driven programming
- ✅ File I/O operations in Python
- ✅ Cross-platform development
- ✅ Security research ethics
- ✅ System-level programming
- ✅ Error handling and logging
- ✅ Buffer management
- ✅ Git version control

## 🚀 Deployment Guide

### GitHub Deployment

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

### Quick Deploy

```bash
git init
git add .
git commit -m "Initial commit: Educational keylogger project"
git branch -M main
git remote add origin https://github.com/Bhaveshpooniwala1/PRODIGY_CS_04.git
git push -u origin main
```

## 🎓 Advanced Features to Add

1. **Email Notifications**: Send logs via email
2. **Encryption**: Encrypt log files
3. **GUI Interface**: Build a Tkinter interface
4. **Remote Logging**: Send logs to remote server
5. **Screenshot Capture**: Capture screenshots on specific triggers
6. **Application Tracking**: Track active applications
7. **Statistical Analysis**: Analyze typing patterns
8. **Stealth Mode**: Hide console window

## 📚 Additional Resources

- [Python pynput Documentation](https://pynput.readthedocs.io/)
- [Ethical Hacking Guide](https://www.eccouncil.org/ethical-hacking/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## ⚖️ Legal Notice

This software is provided for **educational purposes only**. The author and contributors are not responsible for any misuse or damage caused by this program. Users are solely responsible for compliance with applicable laws.

## 👤 Author

**Your Name**
- GitHub: [BhaveshPooniwala1](https://github.com/Bhaveshpooniwala1)
- LinkedIn: [Bhavesh Pooniwala](https://www.linkedin.com/in/bhavesh-pooniwala/)

## 🙏 Acknowledgments

- Python Software Foundation
- pynput library developers
- Security research community

---

**Remember**: With great power comes great responsibility. Use this knowledge ethically! 🛡️
