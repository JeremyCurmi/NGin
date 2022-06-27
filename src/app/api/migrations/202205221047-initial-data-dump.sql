-- +migrate Up
INSERT INTO model_types (id, name) values (1, 'classification'), (2, 'regression');
INSERT INTO machine_learning_types (id, name) values (1, 'classical'), (2, 'Deep Learning');


-- +migrate Down
DELETE FROM model_types;
DELETE FROM machine_learning_types;