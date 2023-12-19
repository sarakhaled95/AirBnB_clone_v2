-- script that prepares a MySQL server for the project

-- create data base hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant rant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
