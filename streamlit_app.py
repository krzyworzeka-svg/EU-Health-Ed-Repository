import streamlit as st
import pandas as pd
import json
import glob
import os

# App Configuration
st.set_page_config(page_title="OneHealth EU Analysis", layout="wide")
st.title("🇪🇺 OneHealth & Planetary Health: EU Analysis Dashboard")
st.markdown("---")

# Data Loader
@st.cache_data
def load_data():
    import re
    def normalize(text):
        return re.sub(r'\s+', '', text.lower())

    files = glob.glob("data/*/analysis.jsonl")
    all_data = []
    for f in files:
        country_code = os.path.basename(os.path.dirname(f))
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                record = json.loads(line)
                record['country'] = country_code
                
                # Construct base GitHub URL
                doc_name = record.get('source_document', '')
                if doc_name:
                    base_url = f"https://github.com/krzyworzeka-svg/EU-Health-Ed-Repository/blob/main/data/{country_code}/transcripts/{doc_name}"
                    local_path = f"data/{country_code}/transcripts/{doc_name}"
                    
                    # Discover line number for deep link robustly
                    line_num = None
                    raw_text = record.get('raw_text', '')
                    
                    if raw_text and os.path.exists(local_path):
                        target = normalize(raw_text)[:40] # first 40 non-whitespace chars
                        try:
                            with open(local_path, 'r', encoding='utf-8') as transcript:
                                lines = transcript.readlines()
                                for i in range(len(lines)):
                                    combined = lines[i]
                                    if i + 1 < len(lines):
                                        combined += lines[i+1]
                                    
                                    if target in normalize(combined):
                                        line_num = i + 1
                                        break
                        except Exception:
                            pass
                    
                    if line_num:
                        record['source_link'] = f"{base_url}?plain=1#L{line_num}"
                    else:
                        record['source_link'] = base_url
                else:
                    record['source_link'] = None
                
                all_data.append(record)
    return pd.DataFrame(all_data)

# Load context
df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
selected_country = st.sidebar.multiselect("Select Country", options=df['country'].unique(), default=df['country'].unique())
selected_concept = st.sidebar.multiselect("Select Concept", options=df['concept'].unique(), default=df['concept'].unique())
selected_topic = st.sidebar.multiselect("Select Topic", options=df['topic'].unique(), default=df['topic'].unique())

# Filter data
mask = (df['country'].isin(selected_country)) & (df['concept'].isin(selected_concept)) & (df['topic'].isin(selected_topic))
filtered_df = df[mask]

# Dashboard Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Count", len(filtered_df))
with col2:
    st.metric("Unique Topics", filtered_df['topic'].nunique())
with col3:
    st.metric("OH vs PH", f"{len(filtered_df[filtered_df['concept']=='OH'])} / {len(filtered_df[filtered_df['concept']=='PH'])}")

# Data Table
st.subheader("Extracted Snippets (OH/PH)")

# Configure columns to display the GitHub link clearly
if not filtered_df.empty and 'source_link' in filtered_df.columns:
    display_cols = ['country', 'topic', 'raw_text', 'translation_en', 'concept', 'type', 'source_link']
    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True,
        column_config={
            "source_link": st.column_config.LinkColumn(
                "Source Document",
                help="Click to view the raw transcript on GitHub",
                display_text="View Transcript 🔗"
            )
        }
    )
else:
    st.dataframe(filtered_df[['country', 'topic', 'raw_text', 'translation_en', 'concept', 'type']], use_container_width=True)

# Concept Chart
st.subheader("Distribution by Concept")
concept_count = filtered_df['concept'].value_counts()
st.bar_chart(concept_count)

# Topic Chart
st.subheader("Themes Explorer")
topic_count = filtered_df['topic'].value_counts()
st.bar_chart(topic_count)

st.markdown("---")
st.info("Data source: Official EU Member State Health Education Curricula.")
