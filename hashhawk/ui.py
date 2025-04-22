

import os
import sys
import hashlib

# Ensure project root is on Python path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
from hashhawk.utils import detect_hash_type
from hashhawk.cracker import crack_md5_list

st.set_page_config(page_title="HashHawk", page_icon="bird", layout="centered")

st.title("🔐 HashHawk Password Audit & Cracker")
st.write("Welcome to HashHawk, your go-to tool for password auditing and cracking!")

# 1. Input hash
hash_input = st.text_input("Enter a hash to crack:")

# 2. Upload wordlist
wordlist_file = st.file_uploader("Upload a wordlist (.txt)", type="txt")

if st.button("Crack Hash"):
    # … validation omitted for brevity …
    h = hash_input.strip()
    htype = detect_hash_type(h)
    st.info(f"Detected hash type: **{htype}**")

    content = wordlist_file.read().decode("utf-8", errors="ignore").splitlines()
    if htype == "md5":
        total = len(content)
        progress_bar = st.progress(0.0)   # start at 0%

        cracked = None
        for idx, pw in enumerate(content):
            #  update the progress bar
            progress_bar.progress((idx + 1) / total)

            #  attempt to crack
            if hashlib.md5(pw.encode()).hexdigest() == h:
                cracked = pw
                progress_bar.progress(1.0)
                break

        # Final result
        if cracked:
            st.success(f"✅ Cracked: **{cracked}**")
        else:
            st.warning("❌ Password not found in wordlist.")
    else:
        st.warning(f"Cracking for **{htype}** not yet supported.")