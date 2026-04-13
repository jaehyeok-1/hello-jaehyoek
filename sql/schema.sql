CREATE TABLE IF NOT EXISTS games (
    game_id TEXT PRIMARY KEY,
    game_date DATE NOT NULL,
    stadium TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    status TEXT NOT NULL, -- played, rainout, canceled_other
    scheduled_start_time TIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS weather_hourly (
    station_id TEXT NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    precip_mm DOUBLE PRECISION,
    humidity_pct DOUBLE PRECISION,
    wind_mps DOUBLE PRECISION,
    temp_c DOUBLE PRECISION,
    weather_code TEXT,
    PRIMARY KEY (station_id, observed_at)
);

CREATE TABLE IF NOT EXISTS stadium_station_map (
    stadium TEXT PRIMARY KEY,
    station_id TEXT NOT NULL,
    distance_km DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS game_weather_features (
    game_id TEXT PRIMARY KEY,
    precip_3h_sum DOUBLE PRECISION,
    precip_6h_sum DOUBLE PRECISION,
    humidity_avg_3h DOUBLE PRECISION,
    wind_max_3h DOUBLE PRECISION,
    temp_avg_3h DOUBLE PRECISION,
    target_rainout INTEGER NOT NULL
);
