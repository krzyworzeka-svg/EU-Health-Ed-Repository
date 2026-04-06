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
def load_data():
    files = glob.glob("data/*/analysis.jsonl")
    all_data = []
    for f in files:
        country_code = os.path.basename(os.path.dirname(f))
        with open(f, 'r', encoding='utf-8') as file:
            for line in file:
                record = json.loads(line)
                record['country'] = country_code
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
