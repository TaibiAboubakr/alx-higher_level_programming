-- script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT1,
	name VARCHAR(256) NOT NULL
);