-- List privileges

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
