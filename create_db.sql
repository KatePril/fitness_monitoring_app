CREATE TABLE IF NOT EXISTS app_user (
    user_id serial NOT NULL PRIMARY KEY,
    username VARCHAR(80) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    weight NUMERIC,
    height NUMERIC
);

INSERT INTO app_user(username, email, password, weight, height)
VALUES
    ('johndoe', 'johndoe@example.com', 'hashed_password_123', 75.5, 180),
    ('janedoe', 'janedoe@example.com', 'hashed_password_456', 62.0, 165),
    ('froglady', 'froglady@example.com', 'hashed_password_789', 68.2, 172);

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

