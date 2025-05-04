CREATE TABLE IF NOT EXISTS app_user (
    user_id serial NOT NULL PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    weight NUMERIC,
    height NUMERIC
);

CREATE TABLE IF NOT EXISTS health_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    heart_rate INT NOT NULL,
    saturation INT NOT NULL,
    steps INT NOT NULL,
    calories FLOAT NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES app_user(user_id)
);

