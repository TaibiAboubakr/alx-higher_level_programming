-- script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server
SET @table_name = 'first_table';

-- Get the CREATE TABLE statement from information_schema
SHOW CREATE TABLE first_table
