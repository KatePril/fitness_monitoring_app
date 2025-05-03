CREATE DATABASE IF NOT EXISTS fitness_db;

CREATE TABLE IF NOT EXISTS app_user
(
    user_id serial NOT NULL PRIMARY KEY,
    username character varying(80) NOT NULL,
    email character varying(50) NOT NULL UNIQUE,
    password text NOT NULL,
    weight numeric(5,2),
    height numeric(5,2)
);

CREATE TABLE health_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    heart_rate INT NOT NULL,
    saturation INT NOT NULL,
    steps INT NOT NULL,
    calories FLOAT NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);
