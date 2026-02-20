# 🔐 SSH Brute Force Detector

A lightweight Python-based SSH log analysis tool that detects brute-force attacks using threshold-based detection logic.

---

## 🚀 Features

- Parses SSH log files
- Extracts attacker IP addresses using regex
- Detects multiple failed login attempts
- Configurable threshold via CLI
- Structured JSON alert generation
- Clean modular design

---

## 🧠 Detection Logic

The tool scans log lines containing:

    Failed password

It extracts IP addresses and counts failed attempts.

If attempts exceed the defined threshold, an alert is triggered.

---

## 📦 Installation

No external dependencies required.

Clone the repository:

    git clone https://github.com/Madhavasisth/ssh-bruteforce-detector.git
    cd ssh-bruteforce-detector

---

## ▶️ Usage

Run:

    python3 detector.py --log sample_logs.txt --threshold 5

Optional arguments:

    --output alerts.json

---

## 📁 Project Structure
ssh-bruteforce-detector/
│
├── detector.py
├── sample_logs.txt
├── README.md
├── requirements.txt
└── .gitignore


---

## 🔮 Future Improvements

- Add time-window based detection
- Add real-time log monitoring
- Add unit tests
- Add Docker support
- MITRE ATT&CK mapping

---

## 👨‍💻 Author

Madhav Vasisth  
Cybersecurity Enthusiast | Systems Developer
