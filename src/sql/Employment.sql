CREATE TABLE IF NOT EXISTS `Employment`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update Record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` DATE NOT NULL,		-- Date of Birth (YYYY-MM-DD)
	`F` char(6) NOT NULL,		-- Postal Code where the service was received
	`G` ENUM('Yes', 'No') NOT NULL,	-- Registration in an employment intervention
	`H` varchar(255),		-- A referral to
	`I` varchar(255) NOT NULL,	-- Language of Service
	`J` varchar(255) NOT NULL,	-- Official Language of Preference
	`K` varchar(255) NOT NULL,	-- Type of Institution/Organization Where Client Received Services
	`L` varchar(255) NOT NULL,	-- Referred By
	`M` DATE,			-- Referral Date (YYYY-MM-DD)
	`N` varchar(255) NOT NULL,	-- Employment Status
	`O` varchar(255) NOT NULL,	-- Education Status
	`P` varchar(255),		-- Occupation in Canada
	`Q` varchar(255),		-- Intended Occupation
	`R` varchar(255),		-- Intervention Type
	`S` varchar(255),		-- Long Term Intervention: Intervention Received
	`T` varchar(255),		-- Long Term Intervention: Status of Intervention
	`U` varchar(255),		-- Long Term Intervention: Reason For Leaving Intervention
	`V` DATE,			-- Long Term Intervention: Start Date (YYYY-MM-DD)
	`W` DATE,			-- Long Term Intervention: End Date (YYYY-MM-DD)
	`X` varchar(255),		-- Long Term Intervention: Size of Employer
	`Y` varchar(25),		-- Long Term Intervention: Placement Was
	`Z` varchar(255),		-- Long Term Intervention: Hours Per Week
	`AA` varchar(255),		-- Long Term Intervention: Client Met Mentor Regularly at
	`AB` varchar(255),		-- Long Term Intervention: Average Hours/Week in Contact with Mentor
	`AC` varchar(255),		-- Long Term Intervention: Profession/Trade For Which Services Were Received
	`AD` ENUM('Yes', 'No'),		-- Was Essential Skills and Aptitude Training Received as Part of this Service?
	`AE` ENUM('Yes', 'No'),		-- Computer skills
	`AF` ENUM('Yes', 'No'),		-- Document Use
	`AG` ENUM('Yes', 'No'),		-- Interpersonal Skills and Workplace Culture
	`AH` ENUM('Yes', 'No'),		-- Leadership Training
	`AI` ENUM('Yes', 'No'),		-- Numeracy
	`AJ` varchar(255),		-- Short Term Intervention: Service Received
	`AK` DATE,			-- Short Term Intervention: Date (YYYY-MM-DD)
	`AL` varchar(255),		-- Short Term Intervention: Service Received
	`AM` DATE,			-- Short Term Intervention: Date (YYYY-MM-DD)
	`AN` varchar(255),		-- Short Term Intervention: Service Received
	`AO` DATE,			-- Short Term Intervention: Date (YYYY-MM-DD)
	`AP` varchar(255),		-- Short Term Intervention: Service Received
	`AQ` DATE,			-- Short Term Intervention: Date (YYYY-MM-DD)
	`AR` varchar(255),		-- Short Term Intervention: Service Received
	`AS` DATE,			-- Short Term Intervention: Date (YYYY-MM-DD)
	`AT` ENUM('Yes', 'No'),		-- Support Services Received
	`AU` ENUM('Yes', 'No'),		-- Care for Newcomer Children
	`AV` varchar(40),		-- Child 1: Age
	`AW` varchar(40),		-- Child 1: Type of Care
	`AX` varchar(40),		-- Child 2: Age
	`AY` varchar(40),		-- Child 2: Type of Care
	`AZ` varchar(40),		-- Child 3: Age
	`BA` varchar(40),		-- Child 3: Type of Care
	`BB` varchar(40),		-- Child 4: Age
	`BC` varchar(40),		-- Child 4: Type of Care
	`BD` varchar(40),		-- Child 5: Age
	`BE` varchar(40),		-- Child 5: Type of Care
	`BF` ENUM('Yes', 'No'),		-- Transportation
	`BG` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`BH` ENUM('Yes', 'No'),		-- Translation
	`BI` varchar(255),		-- Between
	`BJ` varchar(255),		-- And
	`BK` ENUM('Yes', 'No'),		-- Interpretation
	`BL` varchar(255),		-- Between
	`BM` varchar(255),		-- And
	`BN` ENUM('Yes', 'No'),		-- Crisis Counselling
	`BO` int unsigned,		-- Time Spent With Client/Addressing Client's Employment Needs: Hours
	`BP` int unsigned,		-- Time Spent With Client/Addressing Client's Employment Needs: Minutes
	`BQ` varchar(255)		-- Reason for update
		-- 
);

