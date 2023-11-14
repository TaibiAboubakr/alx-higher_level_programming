-- script that converts hbtn_0c_0 database to UTF8 
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
use hbtn_0c_0;
UPDATE first_table
SET name = CONVERT(name USING utf8);
