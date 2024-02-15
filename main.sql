CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    password BLOB,
    creationDate DATE
);

CREATE TABLE salts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idUser INT,
    salt BLOB,
    FOREIGN KEY (idUser) REFERENCES users(id)
);

CREATE TABLE eras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE levels(
    id INT AUTO_INCREMENT PRIMARY KEY,
    idEra INT,
    num INT,
    difficulty INT,
    FOREIGN KEY (idEra) REFERENCES eras(id)
);

CREATE TABLE saves (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idUser INT,
    coins INT,
    idLevel INT,
    items INT,
    FOREIGN KEY (idUser) REFERENCES users(id),
    FOREIGN KEY (idLevel) REFERENCES levels(id)
);