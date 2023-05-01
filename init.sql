CREATE DATABASE IF NOT EXISTS covid;
USE covid;
CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  regno VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  vaccinated ENUM('Yes', 'No') NOT NULL
);
INSERT INTO students (regno, name, vaccinated) VALUES ('123456', 'John', 'Yes'), ('789012','Jane','No');