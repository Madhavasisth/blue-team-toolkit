![CI](https://github.com/Madhavasisth/blue-team-toolkit/actions/workflows/ci.yml/badge.svg)

# 🛡 Blue Team Toolkit

A modular, extensible security detection framework designed to simulate core blue team detection logic.  

Blue Team Toolkit analyzes log files, detects suspicious activity patterns, prioritizes alerts by severity, and provides structured output with automated testing and CI integration.

---

## 🚀 Features

- Modular detection architecture
- SSH brute-force detection
- Suspicious login correlation (fail → success pattern)
- Severity classification (LOW / MEDIUM / HIGH / CRITICAL)
- Alert prioritization
- Colored SOC-style CLI output
- JSON alert export
- Automated unit testing with pytest
- GitHub Actions CI integration

---

## 🧠 Detection Modules

### 1️⃣ Brute Force Detector
Detects multiple failed SSH login attempts within a configurable time window.

**Severity:** MEDIUM

---

### 2️⃣ Suspicious Login Correlation
Detects successful logins that occur after multiple failed attempts from the same IP within a time window.

**Severity:** HIGH

This simulates real-world attacker behavior:
Brute force → successful compromise.

---

## 🏗 Architecture


blue-team-toolkit/
│
├── toolkit/
│ ├── brute_force.py
│ ├── suspicious_login.py
│ ├── engine.py
│ └── constants.py
│
├── cli.py
├── tests/
│ ├── test_bruteforce.py
│ └── test_suspicious_login.py
│
└── .github/workflows/ci.yml


### 🔎 Detection Flow

1. CLI receives arguments
2. Engine executes all registered detection modules
3. Modules return standardized alert objects
4. Alerts are sorted by severity
5. Results are printed and optionally exported to JSON

---

## ▶️ Usage

Activate virtual environment:


source venv/bin/activate


Run detection:


python3 cli.py --log sample_logs.txt --threshold 5 --window 120


Optional arguments:


--output alerts.json


---

## 📦 Installation (Local Development)

Clone repository:


git clone https://github.com/Madhavasisth/blue-team-toolkit.git

cd blue-team-toolkit


Create virtual environment:


python3 -m venv venv
source venv/bin/activate


Install dependencies:


pip install -r requirements.txt


Run tests:


pytest


---

## 🧪 Testing & CI

- Unit tests written using `pytest`
- GitHub Actions automatically runs tests on:
  - Every push
  - Every pull request
- CI status visible via badge at top of README

---

## 🔮 Future Improvements

- Real-time log monitoring mode (`--follow`)
- Additional detection modules (port scan, privilege escalation, anomaly detection)
- MITRE ATT&CK technique mapping
- Plugin-based detection registration
- Severity scoring refinement
- Packaging as installable CLI tool

---

## 🎯 Project Goal

This project demonstrates:

- Security event detection logic
- Event correlation techniques
- Modular architecture design
- Testing discipline
- CI/CD workflow integration
- Defensive security engineering fundamentals

---

## 👨‍💻 Author

Madhav Vasisth  
Cybersecurity Enthusiast | Systems Developer
