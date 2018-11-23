CREATE TABLE `LanguageTrainingExit`(
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier Type
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` DATE NOT NULL,		-- Client Date of Birth (YYYY-MM-DD)
	`F` varchar(255) NOT NULL,	-- Course Code
	`G` varchar(255) NOT NULL,	-- Client's Training Status
	`H` DATE,			-- Date Client Exited Course (YYYY-MM-DD)
	`I` varchar(25),		-- Reason for Exiting course
	`J` varchar(25),		-- Listening CLB Level
	`K` varchar(25),		-- Speaking CLB Level
	`L` varchar(25),		-- Reading CLB Level
	`M` varchar(25),		-- Writing CLB Level
	`N` ENUM('Yes', 'No') NOT NULL,	-- Was a Certificate issued to the client?
	`O` varchar(25),		-- Listening level indicated on Certificate
	`P` varchar(25),		-- Speaking level indicated on Certificate
	`Q` ENUM('Yes', 'No') NOT NULL,	-- Support services received
	`R` ENUM('Yes', 'No'),		-- Care for newcomer children
	`S` varchar(40),		-- Child 1: Age
	`T` varchar(40),		-- Child 1: Type of Care
	`U` varchar(40),		-- Child 2: Age
	`V` varchar(40),		-- Child 2: Type of Care
	`W` varchar(40),		-- Child 3: Age
	`X` varchar(40),		-- Child 3: Type of Care
	`Y` varchar(40),		-- Child 4: Age
	`Z` varchar(40),		-- Child 4: Type of Care
	`AA` varchar(40),		-- Child 5: Age
	`AB` varchar(40),		-- Child 5: Type of Care
	`AC` ENUM('Yes', 'No'),		-- Transportation
	`AD` ENUM('Yes', 'No'),		-- Provisions for disabilities
	`AE` ENUM('Yes', 'No'),		-- Translation
	`AF` varchar(255),		-- Translation language Between
	`AG` varchar(255),		-- Translation language And
	`AH` ENUM('Yes', 'No'),		-- Interpretation
	`AI` varchar(255),		-- Between
	`AJ` varchar(255),		-- And
	`AK` ENUM('Yes', 'No'),		-- Crisis Counselling
	`AL` varchar(255),		-- Reason for update
		-- 
	PRIMARY KEY (`C`, `D`)
);

