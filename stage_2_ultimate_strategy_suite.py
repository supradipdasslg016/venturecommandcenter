import json
import logging
import requests
import pandas as pd
from sqlalchemy import create_engine

# Initialize elite executive diagnostic analytics logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

DATABASE_URI = "postgresql+psycopg2://strategist_admin:elite_secure_password_2026@localhost:5432/venture_validation_db"
engine = create_engine(DATABASE_URI)
OLLAMA_ENDPOINT = "http://localhost:11434/v1/chat/completions"

class UltimateStrategySuiteEngine:
    def __init__(self, topic: str):
        self.topic = topic

    def pull_aggregated_warehouse_intelligence(self):
        """Extracts multi-source text intelligence blocks from your PostgreSQL data core."""
        logging.info("Harvesting unstructured data layers from PostgreSQL production warehouse...")
        
        corp_data = pd.read_sql("SELECT raw_summary_text FROM corporate_intelligence_matrix;", con=engine)
        acad_data = pd.read_sql("SELECT raw_abstract, identified_research_gaps FROM academic_literature_matrix LIMIT 5;", con=engine)
        feed_data = pd.read_sql("SELECT raw_review_text FROM market_feedback LIMIT 5;", con=engine)
        
        context_block = "=== COMPETITOR & BOARDROOM RISK DISCLOSURES ===\n"
        context_block += "\n".join(corp_data['raw_summary_text'].tolist()) + "\n\n"
        
        context_block += "=== ACADEMIC METHODOLOGIES & RESEARCH GAPS ===\n"
        for _, row in acad_data.iterrows():
            context_block += f"Abstract: {row['raw_abstract']} | Research Gap: {row['identified_research_gaps']}\n"
            
        context_block += "\n=== LIVE CONSUMER CRITICISMS & FEEDBACK ===\n"
        context_block += "\n".join(feed_data['raw_review_text'].tolist())
        
        return context_block[:7000] # Optimized contextual window length for local model processing

    def execute_mbb_boardroom_synthesis(self, raw_intelligence: str):
        """Runs an end-to-end multi-framework corporate evaluation log."""
        logging.info("Routing data core to local Llama3 engine for 8-Framework Executive Synthesis...")
        
        system_prompt = (
            "You are a Senior Managing Director and Strategy Partner running an enterprise validation evaluation. "
            "You synthesize data into clear, actionable corporate strategy frameworks used by McKinsey, Bain, and BCG. "
            "Your output MUST be a single, valid JSON object matching the requested schema layout perfectly. "
            "Do not include any chat commentary or markdown formatting blocks outside the JSON."
        )
        
        user_prompt = f"""
        Analyze the following multi-source market data for the topic: '{self.topic}'.
        You must evaluate this data layer across 8 premium strategy frameworks.

        Market Data:
        {raw_intelligence}

        Format your final response exactly like this JSON structure:
        {{
            "pestel_macro_analysis": {{
                "political_regulatory": "Regulatory constraints or compliance hurdles",
                "economic_market": "Capital requirements or pricing trends",
                "technological_disruptions": "Core architectural or system technology vectors"
            }},
            "porter_five_forces_friction": {{
                "supplier_power": "Low/Medium/High details",
                "buyer_power": "Low/Medium/High details",
                "competitive_rivalry_intensity": "Low/Medium/High details"
            }},
            "blue_ocean_errc_action_grid": {{
                "eliminate_reduce": "What standard legacy industry parameters must we remove or minimize?",
                "raise_create": "What value innovations must we elevate or introduce to capture open white-space?"
            }},
            "vrio_defensibility_matrix": {{
                "value_rarity": "Core asset value and competitive rarity profile",
                "inimitability_organization": "Barriers to copying and team execution setup"
            }},
            "bcg_growth_share_matrix": {{
                "portfolio_classification": "Is this market entry a Star, Question Mark, Cash Cow, or Dog? Explain why.",
                "capital_allocation_strategy": "The exact corporate investment directive based on growth vs share metrics."
            }},
            "mckinsey_7s_alignment": {{
                "hard_elements_gaps": "Gaps identified across Strategy, Structure, and Systems infrastructure.",
                "soft_elements_gaps": "Gaps identified across Shared Values, Skills, Staff, and corporate Style."
            }},
            "ansoff_growth_vector": {{
                "quadrant_assignment": "Market Penetration / Product Development / Market Development / Diversification",
                "risk_profile_mitigation": "The calculated framework execution risk level and core structural mitigation play."
            }},
            "ohmae_3cs_strategic_triangle": {{
                "customer_axis_focus": "The primary unmet consumer need or friction point to target.",
                "competitor_axis_defensibility": "The specific vulnerability in the top-10 public players to exploit.",
                "corporation_axis_capability": "The core internal capability or asset required to win."
            }}
        }}
        """

        payload = {
            "model": "llama3",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"},
            "stream": False,
            "temperature": 0.15
        }

        try:
            res = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
            res_json = res.json()
            
            # Intercept server errors cleanly
            if 'error' in res_json:
                logging.error(f"⚠️ Ollama Server Error: {res_json['error']}")
                return
                
            if 'choices' not in res_json:
                logging.error(f"⚠️ Unexpected Ollama response layout: {res_json}")
                return

            dossier = json.loads(res_json['choices'][0]['message']['content'])
            
            print("\n" + "="*80)
            print("🏆 THE ULTIMATE UNIFIED STRATEGIC CONVERSION INTERFACE")
            print("="*80 + "\n")
            print(json.dumps(dossier, indent=4))
            print("\n" + "="*80)
            logging.info("=== SUCCESS: ALL 8 STRATEGIC ROADMAPS COMPILED LIVE ===")
            
        except Exception as e:
            logging.error(f"Strategy Suite framework compilation failure: {e}")

if __name__ == "__main__":
    master_suite = UltimateStrategySuiteEngine(
        topic="Electric vehicle battery recycling scale and logistics bottlenecks"
    )
    data_context = master_suite.pull_aggregated_warehouse_intelligence()
    master_suite.execute_mbb_boardroom_synthesis(data_context)
    