CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
INSERT INTO nexus6 (name) VALUES ('Evan');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
