CREATE TABLE test_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL
);

INSERT INTO test_users (username, email, hashed_password) VALUES ('admin', 'admin@example.com', 'adminnotreallyhashed');