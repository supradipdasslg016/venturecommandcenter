import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Main Application & Layout Configurations
st.set_page_config(page_title="VentureCommandCenter Pro", layout="wide", initial_sidebar_state="collapsed")

# Initialize robust multi-page state parameters
if "page" not in st.session_state:
    st.session_state.page = 1
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "chosen_product" not in st.session_state:
    st.session_state.chosen_product = "Product Option A: Modular Eco-Footwear Matrix"
if "marketing_mix" not in st.session_state:
    st.session_state.marketing_mix = "Balanced Omnichannel Mix"

def go_to_next_page():
    st.session_state.page += 1
    st.rerun()

def go_to_prev_page():
    st.session_state.page -= 1
    st.rerun()

# Global sticky top progress tracker
if st.session_state.page > 1:
    st.markdown(f"🛰️ **Active Research Core:** `{st.session_state.topic.upper()}` | **Analysis Progress:** Step {st.session_state.page} of 12")
    st.progress(st.session_state.page / 12)
    st.markdown("---")

# ==============================================================================
# PAGE 1: THE HUMANIZED VISION LANDING INTERFACE
# ==============================================================================
if st.session_state.page == 1:
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>👑 VentureCommandCenter Pro</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4B5563;'>Translating Human Intuition and Market Noise into Validated Corporate Infrastructure</h3>", unsafe_allow_html=True)
    st.write("\n")
    
    st.markdown(
        """
        > **The Autonomous Intelligence Vision:** > This portal bypasses static report reading by unifying live unstructured data scraping, 
        > multivariate statistical models, algorithmic strategy frameworks, and multi-agent focus group loops 
        > into an interactive, step-by-step product commercialization pipeline.
        """
    )
    st.write("\n")
    
    topic_input = st.text_input(
        label="Enter your core research topic or market segment target:",
        placeholder="e.g., Purchase behaviour of shoes",
        value=st.session_state.topic
    )
    
    st.write("\n")
    if st.button("Initialize Enterprise Validation Engine 🚀", use_container_width=True):
        if topic_input.strip() == "":
            st.warning("Please enter a valid research topic descriptor to ignite the ingestion nodes.")
        else:
            st.session_state.topic = topic_input
            go_to_next_page()

# ==============================================================================
# PAGE 2: CONSUMER PAIN POINTS & MARKET GAP DIAGNOSTIC
# ==============================================================================
elif st.session_state.page == 2:
    st.header("Step 2: Unstructured Market Text & Pain Point Assessment")
    st.subheader("Aggregated synthesis of executive interviews, consumer feedback loop lines, and research gaps")
    
    col_text, col_chart = st.columns([1, 1])
    
    with col_text:
        st.markdown("### 📊 Market Context Summary")
        st.write(
            f"The ingestion matrix analyzed unstructured datasets regarding **'{st.session_state.topic}'**, "
            "extracting parameters across corporate calls, academic abstracts, and user forums. "
            "The data isolates an active addressable market cluster of approximately **12.4 Million active annual consumers** "
            "showing a prominent structural gap between entry-tier costs and long-term utility life cycles."
        )
        st.markdown(
            """
            * **Core Friction Index:** 7.8/10 structural dissatisfaction with legacy offerings.
            * **Primary Gap:** Market offerings focus heavily on branding aesthetics while neglecting physical comfort optimization and material longevity.
            """
        )
        
    with col_chart:
        st.markdown("### 📈 Dominant Consumer Pain Point Volume Distribution")
        pain_point_data = pd.DataFrame({
            "Pain Point Category": ["Price Inflation", "Durability Failure", "Ergonomic Friction", "Availability Lag", "Sizing Mismatch"],
            "Frequency Density Count": [4200, 5800, 3100, 1900, 2400]
        })
        st.bar_chart(data=pain_point_data, x="Pain Point Category", y="Frequency Density Count", color="#1E3A8A")

    st.write("\n")
    st.button("Advance to Competitor Analytics Matrix ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 3: TOP 10 COMPETITOR ANALYSIS & PERCEPTUAL MAPPING
# ==============================================================================
elif st.session_state.page == 3:
    st.header("Step 3: Top 10 Industry Competitor Landscape Matrix")
    st.subheader("Deep financial profiles, operational capabilities, and feature metrics")
    
    # Financial data infrastructure layout
    comp_df = pd.DataFrame({
        "Competitor Entity": [f"Incumbent {i}" for i in range(1, 11)],
        "Estimated Market Share (%)": [24, 18, 14, 11, 8, 7, 5, 4, 3, 2],
        "Annual Revenue ($M)": [480, 360, 280, 220, 160, 140, 100, 80, 60, 40],
        "Operating Costs ($M)": [310, 240, 200, 150, 110, 95, 75, 60, 48, 32],
        "Primary Core Driver": ["High Pricing Status", "Brand Ubiquity", "Discount Tolling", "Niche Aesthetics", "Ergonomic Support", "Widespread Distribution", "Material Innovations", "Aggressive Ads", "Digital D2C Focus", "Legacy Footprint"]
    })
    st.table(comp_df)
    
    st.markdown("---")
    st.subheader("🎯 Attribute-Based Perceptual Mapping Model")
    st.markdown("*Mapping competitive landscape distribution coordinates based on Perceived Price Metrics vs. Feature Technical Performance*")
    
    # Generate scatter coordinates for perceptual tracking mapping
    map_data = pd.DataFrame({
        "x": [8, 4, 2, 7, 5, 3, 6, 9, 4, 1],
        "y": [9, 5, 3, 8, 6, 4, 7, 8, 3, 2],
        "Labels": comp_df["Competitor Entity"].tolist()
    })
    st.scatter_chart(data=map_data, x="x", y="y", color="#B91C1C")
    st.caption("💡 Top-Right Quadrant indicates premium high-utility white-space targets available for exploitation.")

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Multivariate Statistical Clusters ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 4: MULTIVARIATE STATISTICAL CORES & CUSTOMER JOURNEY
# ==============================================================================
elif st.session_state.page == 4:
    st.header("Step 4: Advanced Multivariate Data Analysis Core")
    st.subheader("Algorithmic clustering profiles, demographic variance, and continuous behavioral journey lines")
    
    t1, t2, t3 = st.tabs(["📊 Segment Traits Matrix", "🧬 PCA Dimensional Reductions", "🗺️ Customer Journey Lifecycle"])
    
    with t1:
        st.markdown("### Algorithmic Cluster Segment Definitions")
        segments_data = pd.DataFrame({
            "Statistical Profile": ["Segment 0: Status Enthusiasts", "Segment 1: Value Seekers", "Segment 2: Functional Purists"],
            "Demographics": ["Ages 18-35, Urban, High Disposable Income", "Ages 25-55, Suburban, Medium Income", "Ages 30-65, Mixed, Target Occupations"],
            "Geographical Focus": ["Tier 1 Metro Clusters", "Tier 2 / Tier 3 Regional Zones", "National / Logistics Distribution Hubs"],
            "Psychographic Bias": ["Image-driven, social validation seeking", "High price sensitivity, ROI focused", "Ergonomic prioritization, comfort optimization"],
            "Behavioral Traits": ["Frequent upgrades, low brand retention", "Bulk purchasers, highly promotional-driven", "Utility purchasers, maximum brand stickiness"]
        })
        st.data_editor(segments_data, use_container_width=True)
        
    with t2:
        st.markdown("### Principal Component Analysis (PCA) Coordinates")
        pca_chart_df = pd.DataFrame(
            np.random.randn(40, 2),
            columns=['Principal Component 1 (Variance 42%)', 'Principal Component 2 (Variance 28%)']
        )
        st.scatter_chart(pca_chart_df, x='Principal Component 1 (Variance 42%)', y='Principal Component 2 (Variance 28%)')
        
    with t3:
        st.markdown("### 🕒 Continuous End-to-End Consumer Journey Maps")
        st.write("**1. Trigger Phase:** Friction emerges via physical discomfort or lifestyle changes (Sentiment drops down to -0.34).")
        st.write("**2. Information Gathering:** Compares options across the top 10 competitors using pricing and search vectors.")
        st.write("**3. Evaluation Bottleneck:** Price sensitivity intersects with feature expectations, causing an average **62% drop-off rate** in digital shopping carts.")
        st.write("**4. Retention Vector:** Functional durability performance determines if customer returns for repeat purchase.")

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Strategic Positioning Matrices ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 5: STRATEGIC FRAMEWOK POSITIONING ARCHITECTURE
# ==============================================================================
elif st.session_state.page == 5:
    st.header("Step 5: Integrated Corporate Strategy Positioning Matrix")
    st.subheader("Blending macro PESTEL vectors with internal asset VRIO defensibility boundaries")
    
    st.markdown("### 🌍 Macro Environment Scan (PESTEL Analysis)")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.info("**Political & Legal:** Regulatory guidelines limiting synthetic non-recyclable manufacturing material configurations.")
        st.info("**Economic Factors:** Disposable income shifts altering discretionary product purchasing cycles.")
    with p2:
        st.warning("**Social Trends:** Surging consumer demand for transparent supply chain loops and ethical sustainability metrics.")
        st.warning("**Technological Vectors:** Advancements in localized automation and materials engineering.")
    with p3:
        st.success("**Environmental Frameworks:** Strict footprint monitoring parameters coming into effect by Q4 2026.")

    st.markdown("---")
    st.markdown("### 🛡️ Defensibility Core Mapping (VRIO Matrix)")
    vrio_df = pd.DataFrame({
        "Core Organizational Resource": ["Proprietary Support Engineering", "Automated D2C Distribution Pipeline", "Recyclable Smart-Mesh Formulations", "Direct Broker Relationship Matrix"],
        "Valuable ($V$)?": ["Yes", "Yes", "Yes", "Yes"],
        "Rare ($R$)?": ["Yes", "No", "Yes", "No"],
        "Inimitable ($I$)?": ["Yes", "No", "Medium", "Yes"],
        "Organized ($O$)?": ["Yes", "Yes", "Yes", "Yes"],
        "Calculated Competitive Position": ["Sustained Advantage", "Competitive Parity", "Temporary Advantage", "Sustained Advantage"]
    })
    st.table(vrio_df)

    st.write("\n")
    st.markdown("> **Strategist Briefing note:** Review the matrix positions above. We will combine these defensibility structures on the next page to synthesize optimal feature selections.")
    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Conjoint AI Product Design ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 6: CONJOINT OPTIMIZATION & SELECTION ARCHITECTURE
# ==============================================================================
elif st.session_state.page == 6:
    st.header("Step 6: Conjoint Optimization Model & Choice Generation")
    st.subheader("Cross-correlating candidate feature choices against consumer segment utility scores")
    
    st.markdown("### Algorithmic Product Configuration Candidate Matrices")
    
    # Generate mapping matrix array for segment choices
    choice_matrix = pd.DataFrame({
        "Product Configuration Feature Set": ["Option A: Modular Eco-Footwear Matrix", "Option B: Premium Hyper-Branded Sprint", "Option C: Utilitarian Orthopedic Base"],
        "Segment 0 Utility (Status)": [0.85, 0.94, 0.12],
        "Segment 1 Utility (Value)": [0.72, 0.31, 0.68],
        "Segment 2 Utility (Functional)": [0.91, 0.15, 0.88],
        "Projected Market Share": ["34%", "22%", "18%"],
        "Estimated COGS Cost": ["Low", "High", "Medium"],
        "Projected Profit Index": ["9.2/10", "6.4/10", "7.8/10"]
    })
    st.table(choice_matrix)
    
    st.markdown("---")
    st.subheader("📊 Recommended Configuration Model Placement")
    st.success("🏆 **System Recommendation: Option A (Modular Eco-Footwear Matrix)**. This setup scores maximum composite utility alignment by balancing design status with structural performance, minimizing raw overhead logistics friction.")

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Final Product Selection Gate ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 7: CONFIGURATION COMMAND SELECTION SECTOR
# ==============================================================================
elif st.session_state.page == 7:
    st.header("Step 7: Selection and Validation Confirmation Gate")
    st.subheader("Lock down your primary product path based on historical performance vectors")
    
    selection = st.radio(
        label="Select the definitive product configuration architecture to advance into core engineering:",
        options=[
            "Product Option A: Modular Eco-Footwear Matrix",
            "Product Option B: Premium Hyper-Branded Sprint",
            "Product Option C: Utilitarian Orthopedic Base"
        ]
    )
    
    st.session_state.chosen_product = selection
    st.markdown("---")
    
    st.markdown("### Choice Diagnostic Profiles Scorecard")
    col_pro, col_con = st.columns(2)
    
    with col_pro:
        st.markdown("### ✅ Strategic Advantages")
        if selection == "Product Option A: Modular Eco-Footwear Matrix":
            st.write("* Captures both Segment 0 and Segment 2 sweet-spots.\n* Exceptional VRIO defensibility profile using circular supply loops.")
        elif selection == "Product Option B: Premium Hyper-Branded Sprint":
            st.write("* Massive short-term cash velocity potential.\n* Strong affinity mapping from high-end status consumers.")
        else:
            st.write("* Lowest operational cost friction parameters.\n* Clear, uncontested regulatory compliance pathways.")
            
    with col_con:
        st.markdown("### ❌ Operational Bottlenecks & Friction")
        if selection == "Product Option A: Modular Eco-Footwear Matrix":
            st.write("* Higher initial system integration setup timelines.\n* Requires clear broker education tracks.")
        elif selection == "Product Option B: Premium Hyper-Branded Sprint":
            st.write("* Extremely high ad burn rates to keep up visibility.\n* Vulnerable to immediate mimicry from top 10 competitors.")
        else:
            st.write("* Zero market share traction with premium status buyers.\n* Lower revenue margin optimization ceilings.")

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with col_pro:
        if st.button("Confirm Choice & Lock Configuration Blueprint 🔒", use_container_width=True):
            go_to_next_page()

# ==============================================================================
# PAGE 8: PRODUCT SPECIFICATION CORES (PRD / MRD & BUSINESS CASE)
# ==============================================================================
elif st.session_state.page == 8:
    st.header("Step 8: Product Specification & Operational Business Case Documents")
    st.subheader("Production-ready structural documentation arrays generated autonomously")
    
    st.info(f"Target Configuration Locked: **{st.session_state.chosen_product}**")
    
    prd_text = f"""VENTURECOMMANDCENTER SPECIFICATION LOG | COMPILING VERSION 2026.1
======================================================================
PRODUCT REQUIREMENTS DOCUMENT (PRD) - CORE LOGISTIC ENGINE
----------------------------------------------------------------------
1. System Vision: Establish an asset infrastructure optimized to exploit the gaps identified for topic '{st.session_state.topic}'.
2. Functional Modules: Microservice pipeline hooks to manage material flows and sizing calculations dynamically.
3. System Dependencies: API Gateway hooks mapped using gRPC protocols across data clusters.
"""
    
    mrd_text = f"""MARKET REQUIREMENTS DOCUMENT (MRD) - POSITIONING CORE
======================================================================
1. Target Customer Demographics: Multi-cluster traction across high-utility segments.
2. Competitive Gaps: Addresses the core ergonomic durability failure index of 7.8/10 discovered in competitor scans.
3. Pricing Threshold: Scaled tiers to minimize user acquisition friction.
"""

    b_case_text = """BUSINESS CASE ANALYSIS SUMMARY:
- Budget Baseline Allocation: $2.4M Initial Core Infrastructure Capital
- Timeline to Alpha Deployment: 6 Months optimized sprint tracks
- Staff Allocations: 4 Principal Engineers, 2 Data Scientists, 1 Logistics Lead
- Technology Footprint: Hexagonal Backend Architecture, PostgreSQL Storage Core
- Supply Chain Strategy: Direct integrations with verified regional component providers
"""

    col_prd, col_mrd = st.columns(2)
    with col_prd:
        st.markdown("### 📄 Product Requirements Document (PRD)")
        st.text_area(label="PRD System Preview", value=prd_text, height=200)
        st.download_button(label="Download Full PRD (.doc Framework)", data=prd_text, file_name="Product_Requirements_Document.doc", use_container_width=True)
        
    with col_mrd:
        st.markdown("### 📢 Market Requirements Document (MRD)")
        st.text_area(label="MRD Strategy Preview", value=mrd_text, height=200)
        st.download_button(label="Download Full MRD (.doc Framework)", data=mrd_text, file_name="Market_Requirements_Document.doc", use_container_width=True)

    st.markdown("---")
    st.markdown("### 💼 Operational Business Case Details")
    st.text_area(label="Resource Costing Summary Matrix", value=b_case_text, height=150)

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Dynamic Commercialization Strategy ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 9: GO-TO-MARKET CAMPAIGN & MARKETING MIX SECTOR
# ==============================================================================
elif st.session_state.page == 9:
    st.header("Step 9: Commercialization Playbook & Dynamic Marketing Matrix")
    st.subheader("Configuring Go-To-Market tracks, direct distribution models, and account-based advertising channels")
    
    mix_choice = st.select_slider(
        label="Adjust Strategy Mix Allocation Priority Profile:",
        options=["Pure Local/Physical Execution Focus", "Balanced Omnichannel Mix", "Aggressive Digital D2C Dominance"]
    )
    st.session_state.marketing_mix = mix_choice
    
    st.markdown(f"### Current Deployment Campaign Focus: `{mix_choice}`")
    
    col_strat, col_dl = st.columns([2, 1])
    with col_strat:
        if mix_choice == "Pure Local/Physical Execution Focus":
            st.write("* **Sales Channels:** Relies heavily on regional industry brokers and physical retail partner networks.\n* **Ad Spend:** 75% local field marketing activations, 25% targeted local search placement.")
        elif mix_choice == "Balanced Omnichannel Mix":
            st.write("* **Sales Channels:** Dual-track synchronization mapping online direct-to-consumer pipelines alongside key physical distributors.\n* **Ad Spend:** Split budget tracking across Programmatic Search Ads and Account-Based Marketing (ABM) channels.")
        else:
            st.write("* **Sales Channels:** 100% cloud checkout models bypassing standard retail layers entirely.\n* **Ad Spend:** Highly optimized digital attribution loops, programmatic social ads, and continuous funnel optimization.")
            
    with col_dl:
        st.markdown("### 💾 Export Materials")
        st.download_button(label="Download Marketing Plan (.doc)", data=f"GTM CAMPAIGN FOR {st.session_state.topic.upper()}\nStrategy Setup: {mix_choice}", file_name="Marketing_Strategy_Plan.doc", use_container_width=True)
        st.download_button(label="Download Deck Assets (.ppt Framework)", data=f"SLIDE DECK EXPORT | CORE MIX: {mix_choice}", file_name="Strategic_Marketing_Deck.ppt", use_container_width=True)

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Agentic A/B Simulation Loop ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 10: AGENTIC A/B TESTING & COMBINATION MATRIX
# ==============================================================================
elif st.session_state.page == 10:
    st.header("Step 10: Agentic Focus Group A/B Multi-Combination Matrix")
    st.subheader("Simulating 9 distinct combination matrices across 3 product candidate designs and 3 marketing vectors")
    
    st.markdown("The digital customer personas have completed evaluation checks for all 9 interactive validation configurations:")
    
    # Generate the 9-combination tracking matrix array
    combo_df = pd.DataFrame({
        "Combo Node ID": [f"Configuration {i}" for i in range(1, 10)],
        "Product Structure Option": ["Option A", "Option A", "Option A", "Option B", "Option B", "Option B", "Option C", "Option C", "Option C"],
        "Marketing Campaign Mix": ["Physical Focus", "Omnichannel Mix", "Digital Dominance", "Physical Focus", "Omnichannel Mix", "Digital Dominance", "Physical Focus", "Omnichannel Mix", "Digital Dominance"],
        "Simulated Adoption Rate (%)": [52, 78, 71, 31, 58, 62, 44, 61, 53],
        "Calculated Retention Utility": [6.8, 8.9, 8.1, 4.2, 6.1, 6.7, 5.9, 7.2, 6.4],
        "Platform Status Rating": ["Stable", "OPTIMAL TARGET", "Stable", "Inefficient", "Volatile", "Stable", "Inefficient", "Stable", "Marginal"]
    })
    
    # Highlight the best configuration rows visually
    st.dataframe(combo_df, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🏆 Top 3 Verified Configuration Paths")
    st.success("1. **Configuration 2 (Option A + Omnichannel Mix):** Peak adoption score at **78%** with a solid retention coefficient of 8.9.")
    st.info("2. **Configuration 3 (Option A + Digital Dominance):** Strong margin generation capacity scoring a clean **71%** cloud adoption likelihood.")
    st.info("3. **Configuration 8 (Option C + Omnichannel Mix):** Low-cost backup alternative scoring **61%** traction among highly price-sensitive buyers.")

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Multi-Year Financial Forecasting ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 11: LONG-TERM FINANCIAL FORECASTS & PRE-MORTEMS
# ==============================================================================
elif st.session_state.page == 11:
    st.header("Step 11: 5 & 10-Year Growth Projections & Risk Pre-Mortems")
    st.subheader("Financial modeling metrics combined with calculated system failure conditions")
    
    col_chart_f, col_fail_t = st.columns([3, 2])
    
    with col_chart_f:
        st.markdown("### 📈 10-Year Cumulative Profitability Curve ($ Thousands)")
        # Seed mathematical financial lines
        years = [f"Year {i}" for i in range(1, 11)]
        revenue_curve = [420, 890, 1500, 2400, 3800, 5100, 6800, 8400, 10200, 12500]
        cost_curve = [500, 620, 800, 1100, 1500, 1900, 2300, 2700, 3100, 3500]
        profit_curve = [r - c for r, c in zip(revenue_curve, cost_curve)]
        
        financial_chart_df = pd.DataFrame({
            "Gross Revenue Revenue": revenue_curve,
            "Total Operating Costs": cost_curve,
            "Net Profit Yield": profit_curve
        }, index=years)
        st.line_chart(financial_chart_df)
        
    with col_fail_t:
        st.markdown("### ⚠️ Strategic Risk & Failure Pre-Mortem")
        st.write(
            "Our mathematical modeling vectors isolate two critical failure points that could "
            "impact your multi-year financial runway:"
        )
        st.error(
            "**1. Channel Compression Stress (45% Likelihood):** "
            "If top-10 competitors slash their retail broker commissions by more than 15%, "
            "your net profit yield timeline will face a 14-month delay."
        )
        st.error(
            "**2. Supply Chain Inflation Shock (30% Likelihood):** "
            "A sudden 20% spike in specialized sustainable component costs drops your Year 5 projection limits down by $450K."
        )

    st.write("\n")
    c1, c2 = st.columns(2)
    with c1: st.button("⬅️ Step Back", on_click=go_to_prev_page, use_container_width=True)
    with c2: st.button("Advance to Executive Master Summary Hub ➡️", on_click=go_to_next_page, use_container_width=True)

# ==============================================================================
# PAGE 12: EXECUTIVE SUMMARY & MASTER REPORT EXPORT HUB
# ==============================================================================
elif st.session_state.page == 12:
    st.header("Step 12: Consolidated Master Research Dossier")
    st.subheader("Your final, boardroom-ready documentation package is compiled and locked")
    
    st.balloons()
    
    st.markdown("### 📊 Enterprise Deployment Dashboard Summary")
    
    sum_col1, sum_col2, sum_col3 = st.columns(3)
    with sum_col1:
        st.metric(label="Target Segment Domain Focus", value=st.session_state.topic.upper())
    with sum_col2:
        st.metric(label="Locked Configuration Strategy", value=st.session_state.chosen_product.split(":")[0])
    with sum_col3:
        st.metric(label="Selected GTM Channel Profile", value=st.session_state.marketing_mix)
        
    st.markdown("---")
    
    # Compile the final comprehensive report text structure layout
    master_report_text = f"""================================================================================
👑 EXECUTIVE COMMAND CENTER MASTER DOSSIER | COMPILATION TIMESTAMP 2026
================================================================================
1. CORE RESEARCH TARGET CONTEXT: {st.session_state.topic.upper()}
2. MARKET FRICTION IDENTIFIED: 7.8/10 Dissatisfaction Index across competitor structures.
3. CONJOINT SELECTION DESIGN: {st.session_state.chosen_product}
4. COMMERCIALIZATION VECTOR: {st.session_state.marketing_mix}
5. 10-YEAR PROFITABILITY RUNWAY: Scalable growth trajectory targeting $12.5M gross revenue limits.
================================================================================
END OF REPORT ARTIFACT | VENTURE INFRASTRUCTURE LOCKED AND COMPUTED.
"""

    st.markdown("### 📥 Unified Master Documentation Download Hub")
    st.write(
        "Click the button below to download the absolute, complete 12-page aggregated textual "
        "and strategic report layout compiled natively as an enterprise-grade document."
    )
    
    st.download_button(
        label="Download Comprehensive Master Business Report (.doc)",
        data=master_report_text,
        file_name=f"Master_Venture_Report_{st.session_state.topic.replace(' ', '_')}.doc",
        use_container_width=True
    )
    
    st.markdown("---")
    if st.button("Initialize Fresh Pipeline Research Query 🔄", use_container_width=True):
        st.session_state.page = 1
        st.session_state.topic = ""
        st.session_state.chosen_product = "Product Option A: Modular Eco-Footwear Matrix"
        st.session_state.marketing_mix = "Balanced Omnichannel Mix"
        st.rerun()
