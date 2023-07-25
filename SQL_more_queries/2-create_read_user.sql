-- Creates database and user in MySQL server

-- Creates the database hbtn_2
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
    
-- Creates user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges to user
GRANT SELECT ON 'hbtn_0d_2'.*
      TO 'user_0d_2'@'localhost';