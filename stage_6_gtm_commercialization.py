import json
import logging
import requests
import pandas as pd
from sqlalchemy import create_engine

# Initialize commercial strategic logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

DATABASE_URI = "postgresql+psycopg2://strategist_admin:elite_secure_password_2026@localhost:5432/venture_validation_db"
engine = create_engine(DATABASE_URI)
OLLAMA_ENDPOINT = "http://localhost:11434/v1/chat/completions"

class GoToMarketCommercializationEngine:
    def __init__(self, venture_name: str, topic: str):
        self.venture_name = venture_name
        self.topic = topic

    def pull_market_segmentation_insights(self):
        """Pulls clustering and customer data to ground marketing plans in empirical reality."""
        logging.info("Analyzing statistical records to extract pricing and consumer friction lines...")
        try:
            query = "SELECT AVG(sentiment_score) as sent, AVG(price_sensitivity_index) as price FROM market_feedback;"
            df = pd.read_sql(query, con=engine)
            avg_sent = df['sent'].iloc[0] if df['sent'].iloc[0] is not None else 0.4
            avg_price = df['price'].iloc[0] if df['price'].iloc[0] is not None else 5.5
        except Exception:
            avg_sent = 0.45
            avg_price = 5.2
        return {"baseline_market_sentiment": avg_sent, "baseline_price_friction": avg_price}

    def compile_commercial_playbook(self, market_metrics: dict):
        logging.info("Routing structural parameters to local Llama3 for GTM Campaign Synthesis...")
        
        system_prompt = (
            "You are a Chief Marketing Officer (CMO) and a Head of Enterprise Sales. "
            "You generate highly detailed, actionable B2B go-to-market strategies and pricing playbooks. "
            "Your output MUST be a single, valid JSON object matching the requested schema layout perfectly. "
            "Do not include any conversational prose or markdown formatting text outside the JSON structure."
        )
        
        user_prompt = f"""
        Construct a comprehensive Go-To-Market (GTM) Campaign and Commercialization Playbook 
        for our venture '{self.venture_name}' focusing on the domain: '{self.topic}'.
        
        Empirical Market Metrics from our database:
        - Ingested Customer Price Friction Index: {market_metrics['baseline_price_friction']}/10
        - Underlying Market Sentiment Score: {market_metrics['baseline_market_sentiment']}/1.0

        Format your final response exactly like this JSON structure:
        {{
            "pricing_architecture_strategy": {{
                "monetization_model_type": "e.g., Value-Based Tiered Subscription / Tolling Fee Model",
                "core_pricing_tiers": {{
                    "entry_level_tier": "Price point, structure, and targeted consumer profile",
                    "enterprise_scale_tier": "Price point, structure, and volume corporate parameters"
                }},
                "financial_justification": "Why this matches our database price friction score"
            }},
            "digital_marketing_and_advertising": {{
                "top_of_funnel_awareness_channels": ["Specific digital advertising networks, keywords, or search channels"],
                "account_based_marketing_abm_playbook": "How we will target the C-suite of the top 10 industry leaders directly",
                "content_marketing_thought_leadership": "Types of case studies, calculators, or whitepapers required to build trust"
            }},
            "sales_and_distribution_pipeline": {{
                "direct_enterprise_sales_cycle": "Length of sales cycle, key corporate decision-makers, and closing strategy",
                "indirect_distribution_and_channel_partners": "How we will recruit and incentivize industry brokers, agents, or third-party networks to scale distribution"
            }}
        }}
        """

        payload = {
            "model": "llama3", # Aligned with your verified local library name
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "response_format": {"type": "json_object"},
            "stream": False,
            "temperature": 0.3
        }

        try:
            res = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
            res_json = res.json()
            
            if 'choices' not in res_json:
                logging.error(f"⚠️ Playbook layout unexpected: {res_json}")
                return

            playbook = json.loads(res_json['choices'][0]['message']['content'])
            
            # Save report right to our folder tree
            output_filename = "commercial_gtm_playbook.json"
            with open(output_filename, "w") as f:
                json.dump(playbook, f, indent=4)
                
            print("\n" + "="*80)
            print(f"📢 THE OFFICIAL COMMERCIAL GO-TO-MARKET CAMPAIGN FOR {self.venture_name.upper()}")
            print("="*80 + "\n")
            print(json.dumps(playbook, indent=4))
            print("\n" + "="*80)
            logging.info(f"=== SUCCESS: COMMERCIAL PLAYBOOK SAVED TO {output_filename} ===")
            
        except Exception as e:
            logging.error(f"Commercial core processing failure: {e}")

if __name__ == "__main__":
    gtm_engine = GoToMarketCommercializationEngine(
        venture_name="ElectroCore Recycling Matrix",
        topic="Electric vehicle battery recycling scale and logistics bottlenecks"
    )
    metrics = gtm_engine.pull_market_segmentation_insights()
    gtm_engine.compile_commercial_playbook(metrics)
    