import streamlit as st
from scrapling import fetchers
import pandas as pd

# System and UI Configuration
st.set_page_config(page_title="Human AI - Medical Intelligence", layout="wide")

# Target Global Medical Giants
medical_giants = {
    "Medtronic": "https://www.medtronic.com/us-en/healthcare-professionals/products.html",
    "J&J MedTech": "https://www.jnjmedtech.com/en-US/products",
    "Siemens Healthineers": "https://www.siemens-healthineers.com/products-services",
    "Abbott": "https://www.abbott.com/products.html",
    "Stryker": "https://www.stryker.com/us/en/portfolios.html",
    "Philips": "https://www.philips.com/healthcare/solutions",
    "Boston Scientific": "https://www.bostonscientific.com/en-US/products.html",
    "Fresenius": "https://www.fresenius.com/products",
    "Cardinal Health": "https://www.cardinalhealth.com/en/product-solutions.html"
}

# App Header
st.title("🩺 Medical Device Intelligence - Aura Abu Dhabi")
st.write("Professional Data Acquisition Engine for Global Healthcare Leaders.")

# Selection Interface
selected_company = st.selectbox("Select Target Corporation:", list(medical_giants.keys()))
target_url = medical_giants[selected_company]

st.info(f"Targeting Intelligence at: {target_url}")

# Dynamic Inputs
target_selector = st.text_input("CSS Selector (e.g., h2, .product-card, .title):", "h2")

# Processing Logic
if st.button("Launch Stealth Extraction"):
    if target_url and target_selector:
        with st.spinner(f"Agent infiltrating {selected_company} infrastructure..."):
            try:
                # Scrapling Stealth Engine Initialization
                fetcher = fetchers.StealthyFetcher()
                fetcher.adaptive = True  # Self-healing if site structure changes
                
                # Fetching with high-level browser emulation
                page = fetcher.fetch(target_url, network_idle=True)
                
                # Multi-element extraction
                extracted_data = page.css(target_selector).text_all()
                
                if extracted_data:
                    st.success(f"Successfully harvested {len(extracted_data)} data points!")
                    
                    # Formatting into a Professional Data Table
                    df = pd.DataFrame(extracted_data, columns=["Extracted Information"])
                    st.dataframe(df, use_container_width=True)
                    
                    # Export Options
                    csv_data = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Dataset as CSV",
                        data=csv_data,
                        file_name=f"{selected_company}_intel.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No data found. The site might be using protected headers or different selectors.")
            
            except Exception as e:
                st.error(f"Critical System Error: {str(e)}")
    else:
        st.error("Operation Aborted: URL and Selector are mandatory.")

# Strategic Footer
st.divider()
st.caption("Human AI Engine | Strategic Acquisition Unit | Abu Dhabi - Egypt")
