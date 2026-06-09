import json
import logging
import requests
from sqlalchemy import create_engine

# Initialize elite technical architecture diagnostic logs
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s")

DATABASE_URI = "postgresql+psycopg2://strategist_admin:elite_secure_password_2026@localhost:5432/venture_validation_db"
engine = create_engine(DATABASE_URI)
OLLAMA_ENDPOINT = "http://localhost:11434/v1/chat/completions"

class ProductArchitectureBlueprintEngine:
    def __init__(self, venture_name: str, industry_focus: str):
        self.venture_name = venture_name
        self.industry_focus = industry_focus

    def generate_technical_specification_blueprint(self):
        """Translates market strategy assets into technical feature specifications."""
        logging.info(f"Analyzing strategic assets to map technical blueprint for {self.venture_name}...")
        
        system_prompt = (
            "You are a Chief Technology Officer (CTO) and Principal Enterprise Architect. "
            "You translate high-level business strategy into granular, production-ready system designs. "
            "Your output MUST be a single, valid JSON object matching the requested schema layout perfectly. "
            "Do not include any chat commentary or markdown blocks outside the JSON structural lines."
        )
        
        user_prompt = f"""
        Construct a definitive Technical Architecture Blueprint and Product Requirements Document (PRD) 
        for a venture named '{self.venture_name}' operating in the '{self.industry_focus}' sector.
        
        Your engineering design must cover microservice endpoints, database schemas, and core feature specifications.

        Format your final response exactly like this JSON structure:
        {{
            "system_architecture_overview": {{
                "architectural_pattern": "e.g., Event-Driven Microservices / Hexagonal Architecture",
                "core_infrastructure_stack": ["List of core infrastructure components, servers, caching, queues"],
                "api_gateway_routing_protocol": "e.g., gRPC / REST with OAuth2 Mutual TLS parameters"
            }},
            "microservices_endpoint_backlog": [
                {{
                    "service_name": "Name of the microservice",
                    "http_method": "GET / POST / PUT / DELETE",
                    "api_endpoint_route": "/api/v1/resource",
                    "functional_payload_schema": {{ "key": "data_type" }},
                    "engineering_rationale": "Why this specific microservice is required based on Stage 2 strategy"
                }}
            ],
            "vrio_justified_product_features": {{
                "core_mvp_feature_1": {{
                    "feature_title": "Descriptive title of feature 1",
                    "functional_technical_description": "Detailed engineering functional requirements",
                    "vrio_defensibility_link": "How this feature maps back to Value, Rarity, and Inimitability targets"
                }},
                "core_mvp_feature_2": {{
                    "feature_title": "Descriptive title of feature 2",
                    "functional_technical_description": "Detailed engineering functional requirements",
                    "vrio_defensibility_link": "How this feature maps back to Value, Rarity, and Inimitability targets"
                }}
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
            "temperature": 0.2
        }

        try:
            res = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
            res_json = res.json()
            
            if 'choices' not in res_json:
                logging.error(f"⚠️ Architecture compilation layout unexpected: {res_json}")
                return

            blueprint = json.loads(res_json['choices'][0]['message']['content'])
            
            # Export the architecture blueprint directly to a clean JSON document for the development team
            output_filename = "technical_architecture_blueprint.json"
            with open(output_filename, "w") as f:
                json.dump(blueprint, f, indent=4)
                
            print("\n" + "="*80)
            print(f"🏗️ THE TECHNICAL PRD & ARCHITECTURE BLUEPRINT FOR {self.venture_name.upper()}")
            print("="*80 + "\n")
            print(json.dumps(blueprint, indent=4))
            print("\n" + "="*80)
            logging.info(f"=== SUCCESS: ARCHITECTURE MASTER SPECIFICATION SAVED TO {output_filename} ===")
            
        except Exception as e:
            logging.error(f"Architecture Core configuration blueprinting failure: {e}")

if __name__ == "__main__":
    arch_engine = ProductArchitectureBlueprintEngine(
        venture_name="ElectroCore Recycling Matrix",
        industry_focus="CleanTech Lithium Battery Infrastructure Optimization"
    )
    arch_engine.generate_technical_specification_blueprint()
    