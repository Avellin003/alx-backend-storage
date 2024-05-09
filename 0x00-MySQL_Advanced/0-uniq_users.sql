-- creates a table with these columns
-- id, email, name
-- makes sure that an email is unique
-- makes sure that the id is unique and increments
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
)

