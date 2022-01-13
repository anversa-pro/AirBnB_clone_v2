-- Create a Mysql server to be test with:
-- Database hbnb_test_db
-- New user hbnb_dev with password hbnb_test_pwd
-- user hbnb_test_db with al grand privleges
-- Db performance_schema with select PRIVILEGES


CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED  BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.*
    TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.*
    TO 'hbnb_test'@'localhost';
