CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE competitor_products (
    product_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    brand_name VARCHAR(150) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    region VARCHAR(100) NOT NULL,
    retail_price NUMERIC(10, 2) NOT NULL,
    estimated_monthly_sales_volume INT DEFAULT 0,
    technical_specs jsonb DEFAULT '{}'::jsonb,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE market_feedback (
    feedback_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES competitor_products(product_id) ON DELETE CASCADE,
    source_platform VARCHAR(100),
    raw_review_text TEXT NOT NULL,
    sentiment_score NUMERIC(3, 2),
    price_sensitivity_index INT,
    market_anomaly_flag INT DEFAULT 0,
    text_embedding vector(384),
    assigned_segment_id INT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE corporate_intelligence_matrix (
    intelligence_id SERIAL PRIMARY KEY,
    associated_topic VARCHAR(255) NOT NULL,
    identified_industry VARCHAR(150) NOT NULL,
    company_name VARCHAR(150) NOT NULL,
    stock_ticker VARCHAR(20) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    fiscal_year INT NOT NULL,
    disclosed_competitive_risks jsonb DEFAULT '[]'::jsonb,
    forward_looking_investments jsonb DEFAULT '[]'::jsonb,
    management_sentiment_score NUMERIC(3, 2),
    raw_summary_text TEXT NOT NULL,
    intelligence_embedding vector(384),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE academic_literature_matrix (
    paper_id SERIAL PRIMARY KEY,
    associated_topic VARCHAR(255) NOT NULL,
    title VARCHAR(500) NOT NULL,
    authors TEXT,
    publication_year INT,
    citation_count INT DEFAULT 0,
    journal_name VARCHAR(255),
    download_url TEXT,
    raw_abstract TEXT NOT NULL,
    quantitative_models_extracted jsonb DEFAULT '[]'::jsonb,
    identified_research_gaps TEXT NOT NULL,
    strategic_summary TEXT NOT NULL,
    paper_embedding vector(384),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_comp_specs_gin ON competitor_products USING gin (technical_specs);
CREATE INDEX idx_feedback_hnsw ON market_feedback USING hnsw (text_embedding vector_cosine_ops);