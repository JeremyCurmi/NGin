-- +migrate Up
CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   username VARCHAR(50) UNIQUE NOT NULL,
   email text UNIQUE NOT NULL,
   password text NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE model_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE machine_learning_types (
                             id SERIAL PRIMARY KEY,
                             name VARCHAR(50) NOT NULL,
                             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE model_versions (
    id SERIAL PRIMARY KEY,
    model_id int,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_models (
    user_id int,
    model_id int,
    constraint fk_user_id FOREIGN KEY(user_id) REFERENCES users (id),
    constraint fk_model_id FOREIGN KEY(model_id) REFERENCES models (id)
);

-- +migrate Down
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS model_types;
DROP TABLE IF EXISTS machine_learning_types;
DROP TABLE IF EXISTS models;
DROP TABLE IF EXISTS model_versions;
DROP TABLE IF EXISTS user_models;