CREATE TABLE users (
   id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
   guid varchar(255) UNIQUE NOT NULL,
   name varchar(255) NOT NULL,
   email varchar(255) NOT NULL,
   password varchar(255),
   createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX unq_users_email ON users (email);
