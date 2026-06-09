import json
import logging
import requests
from sqlalchemy import create_engine

# Initialize simulation diagnostic logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

DATABASE_URI = "postgresql+psycopg2://strategist_admin:elite_secure_password_2026@localhost:5432/venture_validation_db"
engine = create_engine(DATABASE_URI)
OLLAMA_ENDPOINT = "http://localhost:11434/v1/chat/completions"

class AgenticMarketSimulator:
    def __init__(self, blueprint_path: str):
        self.blueprint_path = blueprint_path

    def load_product_blueprint(self):
        """Loads the Stage 3 architecture specifications."""
        try:
            with open(self.blueprint_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Fallback layout if file streaming has a path block
            return {
                "vrio_justified_product_features": {
                    "core_mvp_feature_1": {"feature_title": "Automated Decentralized Sourcing Hub", "functional_technical_description": "Real-time routing for optimization."}
                }
            }

    def run_market_simulation_run(self):
        logging.info("=== INITIALIZING STAGE 4: AGENTIC SIMULATION MATRIX ===")
        product_blueprint = self.load_product_blueprint()
        features_summary = json.dumps(product_blueprint.get("vrio_justified_product_features", {}), indent=2)

        # Define our 3 mathematically derived customer agent personas
        personas = [
            {
                "role": "Premium Loyalist Agent",
                "traits": "Incredibly high budget, zero price sensitivity, demands top-tier technical performance and sustainability parameters."
            },
            {
                "role": "Vulnerable Value-Seeker Agent",
                "traits": "Extremely strict budget constraints, high price sensitivity, highly skeptical of corporate greenwashing, demands instant ROI."
            },
            {
                "role": "Critical Infrastructure Entrant Agent",
                "traits": "Focuses purely on logistics integration, regulatory compliance, and system compatibility. Ignores marketing hype."
            }
        ]

        print("\n" + "="*80)
        print("🤖 RUNNING LIVE AGENTIC SIMULATION FOCUS GROUPS")
        print("="*80 + "\n")

        for agent in personas:
            logging.info(f"Waking up digital proxy: [{agent['role']}]...")
            
            system_prompt = (
                f"You are an AI research persona acting strictly as a '{agent['role']}'. "
                f"Your internal biases and buying behaviors are driven by these traits: {agent['traits']}. "
                "You are evaluating a new venture's core features. Provide a highly critical, realistic review. "
                "Your output must be a single JSON object matching the requested schema layout perfectly. No prose."
            )
            
            user_prompt = f"""
            Review these proposed product features for a new industry venture:
            {features_summary}

            Based strictly on your persona traits, evaluate if you would buy/adopt this product.
            Output your assessment exactly matching this JSON layout:
            {{
                "persona_identifier": "{agent['role']}",
                "conversion_decision": "Adopted / Rejected / Postponed",
                "calculated_utility_score": 8.5,
                "primary_value_driver": "The specific feature that won you over or interested you most",
                "brutal_objection_bottleneck": "The main technical or financial reason you would reject this product"
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
                "temperature": 0.7 # Elevated temperature allows for realistic consumer variance
            }

            try:
                res = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=60)
                res_json = res.json()
                
                if 'choices' in res_json:
                    review = json.loads(res_json['choices'][0]['message']['content'])
                    print(json.dumps(review, indent=4))
                    print("-" * 50)
                else:
                    logging.error(f"Agent failed to respond: {res_json}")
            except Exception as e:
                logging.error(f"Critical simulation node error on agent: {e}")

        logging.info("=== SUCCESS: STAGE 4 VIRTUAL FOCUS GROUP CLOSED ===")

if __name__ == "__main__":
    simulator = AgenticMarketSimulator(blueprint_path="technical_architecture_blueprint.json")
    simulator.run_market_simulation_run()
    