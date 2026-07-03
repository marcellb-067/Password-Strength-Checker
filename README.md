#  MARCELL'S Password Strength Checker

A modern Python desktop application that analyzes password strength against real-world security criteria and 10,000+ commonly leaked passwords from actual data breaches.

Built while studying for the **CompTIA Security+** certification to reinforce practical cybersecurity concepts through hands-on development.

---

##  Features

-  **Modern GUI** built with `customtkinter` (dark theme, rounded corners, hover states)
-  **Multi-criteria password analysis**:
  - Length verification (8+ and 12+ character tiers)
  - Character diversity (uppercase, lowercase, numbers, symbols)
  - Comparison against 10,000+ commonly leaked passwords
- **Real-time color coded feedback** (red → green scale)
- **Actionable recommendations** for improving weak passwords
- **Veto logic** automatically rejects any password found in breach databases

---

## 🛠 Tech Stack

- **Python 3.14+**
- **customtkinter** — modern GUI framework
- **Pillow (PIL)** — image processing for the logo
- **SecLists** — real leaked password data from public security research

---

## 📸 Screenshot

<img width="617" height="769" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/ccc9dd02-8d70-4c01-bd25-222a4700ee4c" />
<img width="624" height="785" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/7ce9bf72-1182-4b6d-a48c-da087a043c28" />



---

## 🚀 How to Run

### Prerequisites
- Python 3.10 or newer
- pip

### Installation

1. Clone the repository:
git clone https://github.com/marcellbrwn-067/password-checker.git
cd password-checker

2. Install the required libraries
pip install customtkinter Pillow

3. Run the app
python checker_ui.py

## 📁 Project Structure
password-checker/
├── checker.py              # Command-line version
├── checker_ui.py           # GUI version (main entry point)
├── common_passwords.txt    # 10,000 leaked passwords for blocklist
├── logo.png                # App icon
├── README.md               # This file
└── .gitignore              # Files Git should ignore

---

##  What I Learned

Building this project reinforced key concepts from Security+ and general software engineering:

- **Password security fundamentals** — length, character diversity, breach databases
- **Dictionary attacks and how to defend against them**
- **Python fundamentals** — functions, loops, dictionaries, error handling, file I/O
- **GUI development** — event-driven programming, widget layouts, styling
- **Software architecture** — separation of concerns between logic and presentation
- **Real-world security data** — using SecLists (industry-standard leaked password lists)

---

##  Security Note

This tool is for **educational purposes**. It uses a static list of common passwords. In production, you would want to integrate with services like the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) which provides real-time access to 850+ million breached passwords.

---

##  About the Author

**Marcell Brown**
Economics @ Georgia State University • Information Technology Minor
Building at the intersection of tech and business.

- LinkedIn: [linkedin.com/in/marcell-brown-767b12286](https://linkedin.com/in/marcell-brown-767b12286)
- GitHub: [github.com/marcellbrwn-067](https://github.com/marcellbrwn-067)
