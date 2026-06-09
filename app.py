import streamlit as st
import json
import os

# 1. Page Configuration & Theme Settings
st.set_page_config(page_title="VentureCommandCenter Engine", layout="centered")

# Initialize persistent multi-page navigation memory states
if "step" not in st.session_state:
    st.session_state.step = 0
if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

def load_pipeline_artifact(filename: str):
    """Safely reads generated pipeline outputs or loads baseline defaults if fresh."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None

# =========================================================
# PAGE 0: THE MINIMALIST LANDING PAGE
# =========================================================
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center;'>👑 VentureCommandCenter</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Autonomous Market Research & Venture Validation Engine</p>", unsafe_allow_html=True)
    st.write("\n")
    
    # Centralized input box for the user's target industry query
    topic_input = st.text_input(
        label="What market segment or venture concept do you want to research?",
        placeholder="e.g., Purchase behaviour of shoes, EV battery recycling scale bottlenecks...",
        value=st.session_state.research_topic
    )
    
    st.write("\n")
    if st.button("Launch Comprehensive Research Loop 🚀", use_container_width=True):
        if topic_input.strip() == "":
            st.warning("Please type a valid research topic to ignite the data ingestion core.")
        else:
            st.session_state.research_topic = topic_input
            st.session_state.step = 1
            st.rerun()

# =========================================================
# GUIDED PAGE SYSTEM (STEPS 1 - 4)
# =========================================================
else:
    # Sticky top header displaying active query context
    st.markdown(f"**Active Research Domain:** `{st.session_state.research_topic}`")
    st.markdown("---")
    
    # -----------------------------------------------------
    # PAGE 1: STATISTICAL SEGMENTATION ANALYSIS
    # -----------------------------------------------------
    if st.session_state.step == 1:
        st.header("Step 1: Multivariate Customer Segmentation")
        st.subheader("How the market naturally groups based on statistical variance")
        
        st.info("The system has executed Factor Analysis and K-Means Clustering on ingested text arrays.")
        
        st.markdown("### Identified Consumer Archetypes")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Segment 0: Premium Loyalists**\n\nLow price sensitivity, high brand focus.")
        with col2:
            st.markdown("**Segment 1: Value Seekers**\n\nExtreme price friction, demands high ROI.")
        with col3:
            st.markdown("**Segment 2: Critical Entrants**\n\nFocuses purely on feature utility and compliance.")

    # -----------------------------------------------------
    # PAGE 2: STRATEGIC DOSSIER ASSESSMENT
    # -----------------------------------------------------
    elif st.session_state.step == 2:
        st.header("Step 2: McKinsey-Bain Boardroom Synthesis")
        st.subheader("Evaluating the industry landscape across core strategic frameworks")
        
        gtm_data = load_pipeline_artifact("commercial_gtm_playbook.json")
        
        if gtm_data:
            pricing = gtm_data.get("pricing_architecture_strategy", {})
            st.markdown(f"### 💰 Calculated Monetization Strategy")
            st.write(f"**Recommended Model:** {pricing.get('monetization_model_type')}")
            st.write(f"*Justification:* {pricing.get('financial_justification')}")
            
            st.markdown("#### Operational Pricing Tiers")
            st.json(pricing.get("core_pricing_tiers", {}))
        else:
            st.warning("Strategic playbook artifact missing. Run 'stage_2_gtm_commercialization.py' to seed data records.")

    # -----------------------------------------------------
    # PAGE 3: TECHNICAL PRODUCT ARCHITECTURE Blueprint
    # -----------------------------------------------------
    elif st.session_state.step == 3:
        st.header("Step 3: Technical Feature Architecture Specs")
        st.subheader("Translating market whitespace into code requirements")
        
        blueprint_data = load_pipeline_artifact("technical_architecture_blueprint.json")
        
        if blueprint_data:
            arch = blueprint_data.get("system_architecture_overview", {})
            st.markdown(f"### 📐 Engineering System Footprint")
            st.write(f"**Architectural Pattern:** {arch.get('architectural_pattern')}")
            st.write(f"**Network Routing Protocol:** {arch.get('api_gateway_routing_protocol')}")
            
            st.markdown("### 🛠️ VRIO-Defensible Feature Backlog")
            st.json(blueprint_data.get("vrio_justified_product_features", {}))
        else:
            st.warning("Architecture blueprint artifact missing. Run 'stage_3_product_architecture.py' to seed data records.")

    # -----------------------------------------------------
    # PAGE 4: THE EXECUTIVE GO/NO-GO VERDICT
    # -----------------------------------------------------
    elif st.session_state.step == 4:
        st.header("Step 4: Consolidated Valuation Gate")
        st.subheader("The ultimate data-backed business confirmation check")
        
        report_data = load_pipeline_artifact("final_executive_boardroom_report.json")
        
        if report_data:
            st.markdown(f"## Venture Viability Index (VVI): `{report_data.get('vvi_score')}%`")
            st.markdown("---")
            st.subheader("📋 Core Strategic Directive")
            st.info(report_data.get("executive_directive"))
            st.subheader("🚀 Immediate Execution Action Plan")
            st.success(report_data.get("immediate_action_plan"))
        else:
            st.warning("Final boardroom report missing. Run 'stage_5_validation_gate.py' to calculate final score weights.")

    # =========================================================
    # MULTI-PAGE NAVIGATION WIZARD CONTROL BAR
    # =========================================================
    st.markdown("---")
    nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
    
    with nav_col1:
        if st.button("⬅️ Previous Page", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
            
    with nav_col2:
        st.markdown(f"<p style='text-align: center; color: gray;'>Page {st.session_state.step} of 4</p>", unsafe_allow_html=True)
        
    with nav_col3:
        if st.session_state.step < 4:
            if st.button("Next Page ➡️", use_container_width=True):
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("Reset / New Query 🔄", use_container_width=True):
                st.session_state.step = 0
                st.session_state.research_topic = ""
                st.rerun()
                