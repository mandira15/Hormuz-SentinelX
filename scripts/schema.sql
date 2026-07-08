-- economies table
CREATE TABLE IF NOT EXISTS economies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region VARCHAR(255),
    gdp_usd NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- import_sources table
CREATE TABLE IF NOT EXISTS import_sources (
    id SERIAL PRIMARY KEY,
    economy_id INT REFERENCES economies(id),
    source_country VARCHAR(255) NOT NULL,
    commodity VARCHAR(100) NOT NULL, -- e.g., 'Crude', 'LNG'
    volume NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- chokepoints table
CREATE TABLE IF NOT EXISTS chokepoints (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitude NUMERIC,
    longitude NUMERIC,
    risk_level INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- resilience_scores table
CREATE TABLE IF NOT EXISTS resilience_scores (
    id SERIAL PRIMARY KEY,
    economy_id INT REFERENCES economies(id),
    score NUMERIC NOT NULL,
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- scenarios table
CREATE TABLE IF NOT EXISTS scenarios (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- scenario_results table
CREATE TABLE IF NOT EXISTS scenario_results (
    id SERIAL PRIMARY KEY,
    scenario_id INT REFERENCES scenarios(id),
    economy_id INT REFERENCES economies(id),
    impact_score NUMERIC NOT NULL,
    details JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
