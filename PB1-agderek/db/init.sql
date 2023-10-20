USE secrets;

CREATE TABLE User (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(30) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY (username)
);

CREATE TABLE Secret (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    info VARCHAR(255) NOT NULL,
    user_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_name) REFERENCES User(username)
);

START TRANSACTIOn;

INSERT INTO User (username, password_hash) VALUES ("admin", "$argon2id$v=19$m=65536,t=3,p=4$S8qw3tIZL42JCd7dXxb8Sg$RGKdpN66YUNd4z9iFxaNZrYHdhCIwMf7D7DB96yUlBM");

INSERT INTO Secret (name, info, user_name) VALUES ("Test", "Test", "admin");
INSERT INTO Secret (name, info, user_name) VALUES ("Foo", "Bar", "admin")

COMMIT;