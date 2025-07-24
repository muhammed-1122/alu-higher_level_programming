-- List privileges of user_0d_1 and user_0d_2
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'pass';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'pass';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

