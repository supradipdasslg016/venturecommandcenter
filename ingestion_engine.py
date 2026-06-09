import os
import io
import requests
import pdfplumber
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# Initialize path configuration loading
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

class IndianMarketIngestionPipeline:
    def __init__(self):
        # 1. Initialize local persistent database directory inside your project folder
        self.chroma_client = chromadb.PersistentClient(path="./vcc_vector_db")
        
        # 2. Set up the local free embedding model configuration layer
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        # 3. Create or access our structured target data collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="nse_bse_transcripts",
            embedding_function=self.embed_fn
        )

    def run_targeted_transcript_discovery(self, market_topic: str):
        """Queries SerpApi for any research topic across the entire NSE/BSE filing grid."""
        print(f"📡 Initializing global dynamic RAG search for query: '{market_topic}'...")
        
        # 1. Strip out academic filler words so Google can match corporate jargon naturally
        clean_term = market_topic.lower()
        for filler in ["purchase behaviour of", "consumer adoption of", "market research on"]:
            clean_term = clean_term.replace(filler, "")
        clean_term = clean_term.strip()
        
        # 2. UNIVERSAL GOOGLE DORK: Targets transcripts for ANY topic directly on Indian Stock Exchanges
        search_query = f'"{clean_term}" "transcript" filetype:pdf (site:nseindia.com OR site:bseindia.com)'
        
        url = "https://serpapi.com/search"
        params = {
            "engine": "google",
            "q": search_query,
            "api_key": SERPAPI_KEY
        }
        
        try:
            response = requests.get(url, params=params, timeout=15)
            search_results = response.json()
            
            organic_results = search_results.get("organic_results", [])
            if not organic_results:
                print(f"⚠️ No public exchange disclosures located for macro keyword: '{clean_term}'.")
                return False

            processed_count = 0
            for result in organic_results[:3]: # Processes top 3 industry filings found
                pdf_url = result.get("link")
                title = result.get("title", "Exchange Disclosure Document")
                snippet = result.get("snippet", "NSE/BSE Corporate Filing")
                
                if pdf_url and pdf_url.endswith(".pdf"):
                    print(f"📥 Discovered Industry Filing URL: {pdf_url}")
                    self.stream_and_index_pdf(pdf_url, title, snippet)
                    processed_count += 1
            
            return processed_count > 0

        except Exception as e:
            print(f"❌ Critical breakdown inside search network loop: {e}")
            return False
        