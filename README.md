# EU-Health-Ed-Repository
Repository of official EU health education policy and institutional documents, compiled for research within COST Action CA24106 BEACON. Supports comparative analysis, mapping of strategies, and cross-country studies of health education systems and policies.

# 🌍 EU Health Education: One Health & Planetary Health Repository
### An Open Science Initiative within the **Beacon COST Action** framework

![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)
![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Framework: Critical Realism](https://img.shields.io/badge/Framework-Critical%20Realism-orange.svg)

## 📋 Project Overview
This repository hosts a harmonized, multi-country dataset mapping the integration of **One Health (OH)** and **Planetary Health (PH)** within EU-27 school curricula. 

By utilizing an AI-assisted pipeline for thematic extraction, validated by regional experts, we explore how different European bioregions (from Mediterranean heatwaves to Boreal forest management) translate global health threats into national educational mandates.

### 🎯 Research Goals
* **The "Great Divide":** Identifying the divergence between Northern "Resource-based" and Southern "Survival-based" health education models.
* **AMR & Zoonoses:** Mapping the explicit vs. implicit presence of antimicrobial resistance and zoonotic threats in primary and secondary schools.
* **Climate Adaptation:** Analyzing educational responses to urban heat islands and biodiversity loss.

---

## 🏛 Repository Structure
We follow a **Three-Level Data Architecture** inspired by the principles of **Critical Realism**:

* **Level I: Empirical Metadata (`master.yaml`)** – The "Source of Truth." Links official legislative PDFs to raw text transcripts.
* **Level II: Thematic Snippets (`analysis.jsonl`)** – AI-extracted raw text fragments, translated and categorized (Explicite/Implicite).
* **Level III: Expert Synthesis (`review_[ISO].md`)** – Human-in-the-loop validation and qualitative insights into national "Generative Mechanisms."

```text
/data
  └───ES
      ├───sources        <-- Original PDF documents
      ├───transcripts    <-- Raw text (Full-text MD)
      ├───master.yaml    <-- System Registry
      ├───analysis.jsonl <-- AI Thematic Mining
      └───review_ES.md   <-- Expert Validation
````

-----

## 🚀 Interactive Dashboard

Explore the data through our **Streamlit Live Portal**:
👉 `[https://eu-health-ed-repository.streamlit.app/]`

  * **Interactive Map:** Filter OH/PH themes across the EU.
  * **Snippet Explorer:** Search for specific terms (e.g., "zoonoses") across all countries.
  * **Bioregional Insights:** Compare Mediterranean and Boreal educational strategies side-by-side.

-----

## 🤝 Join the Consortium

This project is an official output of the **Beacon COST Action**. We are actively seeking Country Experts to validate datasets for their respective nations.

  * **Authorship:** Contributors are eligible for co-authorship in ***The Lancet Planetary Health***, ***WIREs Climate Change***, and ***Scientific Data***.
  * **Guidelines:** Please refer to [CONTRIBUTING.md](https://www.google.com/search?q=./CONTRIBUTING.md) for our collaboration manifesto and CRediT taxonomy details.

-----

-----

**Lead Architect:** [Paweł Krzyworzeka]  
**Institution:** [Kozminski University]  
**Contact:** [pkrzyworzeka@kozminski.edu.pl]

```

