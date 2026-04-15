import streamlit as st
import requests

st.title("Company Info Fetcher")

domain = st.text_input("Enter company domain (e.g. google.com)")

# function to validate domain input
def is_valid_domain(domain):
    return domain and "." in domain

def check_image(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200 and response.content
    except:
        return False

if st.button("Fetch Info"):
    if domain:
        if not is_valid_domain(domain):
            domain = domain + ".com"

        st.subheader(domain)

        clearbit_url = f"https://logo.clearbit.com/{domain}"
        google_favicon = f"https://www.google.com/s2/favicons?sz=128&domain={domain}"

        # try clearbit first
        if check_image(clearbit_url):
            st.image(clearbit_url, caption="Company Logo", width=150)
            st.success("Loaded from Clearbit API")
        else:
            st.image(google_favicon, caption="Company Logo (Fallback)", width=150)
            st.info("Company logo loaded")

        st.write("Domain:", domain)
        st.write("Clearbit URL:", clearbit_url)

    else:
        st.error("Please enter a domain")
