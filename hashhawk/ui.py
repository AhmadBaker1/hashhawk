# hashhawk/ui.py

import os
import sys

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
            # Read the uploaded wordlist into a Python list
            content = wordlist_file.read().decode("utf-8", errors="ignore").splitlines()
            
            if htype == "md5":
                with st.spinner("Cracking…"):
                    result = crack_md5_list(h, content)
                if result:
                    st.success(f"✅ Cracked: **{result}**")
                else:
                    st.warning("❌ Password not found in wordlist.")
            else:
                st.warning(f"Cracking for **{htype}** not yet supported.")
