CREATE TABLE IF NOT EXISTS User(
	AgencyName VARCHAR(80),
	AgencyAddress VARCHAR(80),
	UserEmail VARCHAR(80),
	UserPassword VARCHAR(80),
	UserName VARCHAR(80),
	UserType ENUM('TEQHigh', 'TEQLow', 'Agency'),

	PRIMARY KEY (UserEmail)
	);

INSERT INTO User
(AgencyName, AgencyAddress, UserEmail, UserPassword, UserName, UserType)
VALUES
('ABC', '101 Grovein Street', 'c01group12@gmail.com', 'password', 'Bob', 'Agency'),
('ABC', '101 Grovein Street', 'agency02@agency.ca', 'password', 'Mary', 'Agency'),
('TEQLIP', '120 Beetle Street', 'teq01@teq.ca', 'password', 'Alice', 'TEQHigh'),
('TEQLIP', '120 Beetle Street', 'teq02@teq.ca', 'password', 'Charlie', 'TEQLow');
