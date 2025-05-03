# HashHawk

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-1.4%2B-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

---

🔐 **HashHawk** is a **password auditing & cracking toolkit** built in Python with a sleek Streamlit GUI. It auto-detects common hash types (MD5, SHA-1, SHA-256) and provides real-time progress feedback as it crawls your wordlists.

---

## 🚀 Features
- **Multi-Algorithm Support:** MD5, SHA-1 & SHA-256 cracking  
- **Real-Time Progress:** Visual progress bar shows completion percentage  
- **Auto-Detect Hash Type:** Instantly identifies the algorithm used  
- **Streamlit GUI:** Simple, interactive UI with sidebar usage guide  
- **Wordlist Upload:** Drag & drop or browse to upload any `.txt` wordlist  
- **Unit Tested:** Built-in pytest suite for core cracking functions  

---

## 📸 Screenshot

[![Screenshot-2025-05-02-213706.png](https://i.postimg.cc/rw9RZNSV/Screenshot-2025-05-02-213706.png)](https://postimg.cc/68yQyRjg)

---

### ▶️ Quick Usage (no install)
1. Paste or type your target hash (e.g. `5f4dcc3b5aa765d61d8327deb882cf99`).  
2. Upload your `wordlist.txt`.  
3. Click **Crack Hash** and watch the progress bar.  

> **Tip:** Try the sample MD5 hash of “password” above to see it in action!

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hashhawk.git
   cd hashhawk

2. **🤝 Contributing & Local Setup**
   ```bash
   cd hashhawk
   python -m venv .venv
3. **Allow activation of scripts in this session**
   ```bash
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
4. **Activate the venv**
   ```bash
   . .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   streamlit run hashhawk\ui.py
   ```
   
   ## ✨ Technologies
Python, `hashlib`, `passlib/bcrypt`, Streamlit, pytest, Git

---

Made with ❤️ by Ahmad Baker  
