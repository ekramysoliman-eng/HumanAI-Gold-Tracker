import streamlit as st
from scrapling import fetchers
import pandas as pd

# Global System Configuration
st.set_page_config(page_title="Human AI - Unified Medical Intel", layout="wide")

# Consolidated Target List: Global Leaders & UAE Distributors
medical_targets = {
    "Medtronic": "https://www.medtronic.com/us-en/healthcare-professionals/products.html",
    "J&J MedTech": "https://www.jnjmedtech.com/en-US/products",
    "Siemens Healthineers": "https://www.siemens-healthineers.com/products-services",
    "Abbott": "https://www.abbott.com/products.html",
    "Stryker": "https://www.stryker.com/us/en/portfolios.html",
    "BD (Becton Dickinson)": "https://www.bd.com/en-us/offerings",
    "Philips": "https://www.philips.com/healthcare/solutions",
    "Boston Scientific": "https://www.bostonscientific.com/en-US/products.html",
    "Fresenius": "https://www.fresenius.com/products",
    "Cardinal Health": "https://www.cardinalhealth.com/en/product-solutions.html",
    "GE HealthCare": "https://www.gehealthcare.com/products",
    "Al Zahrawi Medical (Dubai)": "https://www.zahrawi.com/products/",
    "Gulf Medical": "https://gulfmedical.com/products/",
    "AKI Healthcare": "https://www.akigroup.com/healthcare",
    "Leader Healthcare": "https://leaderhealthcare.co/products/",
    "Amico Group": "https://www.amicogroup.com/specialties/"
}

# Application Header
st.title("🌐 Unified Medical Intelligence Engine")
st.write("Strategic Data Acquisition for Aura-AbuDhabi Bio-Digital Twin Project.")

# Target Selection Interface
selected_entity = st.selectbox("Select Target Corporation or Distributor:", list(medical_targets.keys()))
current_url = medical_targets[selected_entity]

st.info(f"Stealth Protocol Ready for: {current_url}")

# Custom Extraction Settings
target_selector = st.text_input("Enter Extraction Selector (Default is h2 for titles):", "h2")

# Main Execution Logic
if st.button("Initialize Stealth Harvest"):
    if current_url and target_selector:
        with st.spinner(f"Infiltrating {selected_entity} Infrastructure..."):
            try:
                # Initialize Scrapling with Stealth and Adaptive layers
                fetcher = fetchers.StealthyFetcher()
                fetcher.adaptive = True 
                
                # Fetching the live page with Network Idle detection
                page = fetcher.fetch(current_url, network_idle=True)
                
                # Dynamic data extraction using Scrapling CSS engine
                harvested_data = page.css(target_selector).text_all()
                
                if harvested_data:
                    st.success(f"Success! Captured {len(harvested_data)} high-value data points.")
                    
                    # Formatting data for analysis
                    df = pd.DataFrame(harvested_data, columns=["Extracted Technical Data"])
                    st.dataframe(df, use_container_width=True)
                    
                    # Intelligence Export
                    csv_output = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Intelligence Report (CSV)",
                        data=csv_output,
                        file_name=f"{selected_entity}_report.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("Warning: No data found. Verify the CSS selector for this specific domain.")
            
            except Exception as e:
                st.error(f"Critical System Failure: {str(e)}")
    else:
        st.error("System Error: URL and Selector parameters are mandatory.")

# Global Footer
st.divider()
st.caption("Human AI Project | Bio-Digital Twin Division | Abu Dhabi - UAE")
