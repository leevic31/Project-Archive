CREATE TABLE IF NOT EXISTS `LanguageTrainingEnrolment`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier Type
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` varchar(255) NOT NULL,	-- Client Date of Birth (YYYY-MM-DD)
	`F` char(6) NOT NULL,		-- Postal Code where the service was received
	`G` varchar(255) NOT NULL,	-- Course Code
	`H` varchar(255) NOT NULL,	-- Date of Client's First Class (YYYY-MM-DD)
	`I` varchar(255) NOT NULL,	-- Official Language of Preference
	`J` ENUM('Yes', 'No') NOT NULL,	-- Support services received
	`K` ENUM('Yes', 'No'),		-- Care for newcomer children
	`L` varchar(40),		-- Child 1: Age
	`M` varchar(40),		-- Child 1: Type of Care
	`N` varchar(40),		-- Child 2: Age
	`O` varchar(40),		-- Child 2: Type of Care
	`P` varchar(40),		-- Child 3: Age
	`Q` varchar(40),		-- Child 3: Type of Care
	`R` varchar(40),		-- Child 4: Age
	`S` varchar(40),		-- Child 4: Type of Care
	`T` varchar(40),		-- Child 5: Age
	`U` varchar(40),		-- Child 5: Type of Care
	`V` ENUM('Yes', 'No'),		-- Transportation
	`W` ENUM('Yes', 'No'),		-- Provisions for disabilities
	`X` ENUM('Yes', 'No'),		-- Translation
	`Y` varchar(255),		-- Translation language Between
	`Z` varchar(255),		-- Translation language And
	`AA` varchar(255),		-- Interpretation
	`AB` varchar(255),		-- Between
	`AC` varchar(255),		-- And
	`AD` ENUM('Yes', 'No'),		-- Crisis Counselling
	`AE` varchar(255),		-- Reason for update
		-- 
);

