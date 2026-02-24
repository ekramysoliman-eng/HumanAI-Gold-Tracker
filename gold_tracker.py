import streamlit as st
from scrapling import fetchers

# System Configuration
st.set_page_config(page_title="Human AI - Universal Scraper", page_icon="🌐")

# UI Headers
st.title("🌐 Universal Data Scraper - Human AI")
st.write("Professional grade stealth extraction engine.")

# Input Section
url_input = st.text_input("Target URL:", placeholder="https://example.com")
selector_input = st.text_input("Target CSS Selector:", placeholder=".price, #id, or h1")

# Execution Logic
if st.button('Execute Extraction'):
    if url_input and selector_input:
        with st.spinner('Scrapling Stealth Engine is fetching data...'):
            try:
                # Initialize StealthyFetcher with Adaptive learning enabled
                fetcher = fetchers.StealthyFetcher()
                fetcher.adaptive = True 
                
                # Dynamic request with network idle waiting
                page = fetcher.fetch(url_input, network_idle=True)
                
                # Targeted data extraction
                result = page.css(selector_input).text()
                
                if result:
                    st.success("✅ Extraction Completed:")
                    st.code(result, language='text')
                else:
                    st.warning("⚠️ Element not found. Please verify the CSS Selector.")
                    
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.info("Required: Please enter both URL and CSS Selector to proceed.")

# Footer
st.divider()
st.caption("Human AI Engine | Strategic Intelligence Division | Abu Dhabi - Egypt")
