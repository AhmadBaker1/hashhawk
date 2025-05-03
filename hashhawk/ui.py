# === hashhawk/ui.py ===
import os
import sys
import hashlib
import streamlit as st
from hashhawk.utils import detect_hash_type
from hashhawk.cracker import crack_md5_list, crack_sha1_list, crack_sha256_list

# Ensure project root is on Python path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Page configuration
st.set_page_config(page_title="HashHawk", page_icon="🔐", layout="centered")

# Sidebar guide
with st.sidebar:
    st.header("Usage Guide")
    st.markdown(
        """
1. **Download** the `wordlist.txt` from the [GitHub repo](https://github.com/AhmadBaker1/hashhawk/blob/main/wordlist.txt).
2. **Enter** the hash you want to crack (e.g., `5f4dcc3b5aa765d61d8327deb882cf99`).
3. **Upload** your `wordlist.txt` file.
4. **Click** **Crack Hash** and watch the progress bar with hash type detection.
5. **This is in it's early stages, working my way to become cybersecurity expert**.
"""
    )

# Main interface
st.title("🔐 HashHawk Password Audit & Cracker")
st.write("Welcome to HashHawk, your go-to tool for password auditing and cracking!")

# Input: hash
hash_input = st.text_input("Enter a hash to crack:")

# Upload: wordlist
wordlist_file = st.file_uploader("Upload a wordlist (.txt)", type="txt")

if st.button("Crack Hash"):
    if not hash_input:
        st.error("Please enter a hash.")
    elif not wordlist_file:
        st.error("Please upload a wordlist.")
    else:
        h = hash_input.strip()
        try:
            htype = detect_hash_type(h)
        except ValueError as e:
            st.error(str(e))
        else:
            st.info(f"Detected hash type: **{htype}**")
            content = wordlist_file.read().decode("utf-8", errors="ignore").splitlines()
            
            # Choose the right cracker function
            if htype == "md5":
                cracker_fn = crack_md5_list
            elif htype == "sha1":
                cracker_fn = crack_sha1_list
            elif htype == "sha256":
                cracker_fn = crack_sha256_list
            else:
                st.warning(f"Cracking for **{htype}** not yet supported.")
                cracker_fn = None

            if cracker_fn:
                total = len(content)
                progress_bar = st.progress(0.0)
                cracked = None

                for idx, pw in enumerate(content):
                    # Update progress fraction
                    progress_bar.progress((idx + 1) / total)
                    # Attempt crack using dynamic hashlib
                    digest = getattr(hashlib, htype)(pw.encode()).hexdigest()
                    if digest == h:
                        cracked = pw
                        progress_bar.progress(1.0)
                        break

                if cracked:
                    st.success(f"✅ Cracked: **{cracked}**")
                else:
                    st.warning("❌ Password not found in wordlist.")

# === tests/test_cracker.py ===
import tempfile
from hashhawk.cracker import crack_md5_list


def test_crack_md5_success():
    sample_hash = '5f4dcc3b5aa765d61d8327deb882cf99'
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.write('password\nfoo')
        path = tmp.name
    with open(path) as f:
        wordlist = f.read().splitlines()
    assert crack_md5_list(sample_hash, wordlist) == 'password'