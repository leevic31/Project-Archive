CREATE TABLE IF NOT EXISTS `CommunityConnection`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update Record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` DATE NOT NULL,		-- Date of Birth (YYYY-MM-DD)
	`F` char(6) NOT NULL,		-- Postal Code where the service was received
	`G` varchar(255) NOT NULL,	-- Language of Service
	`H` varchar(255) NOT NULL,	-- Official Language of Preference
	`I` varchar(255) NOT NULL,	-- Referred By
	`J` varchar(255) NOT NULL,	-- Activity Under Which Client Received Services
	`K` varchar(255) NOT NULL,	-- Type of Institution/Organization Where Client Received Services
	`L` varchar(255),		-- Type of Event Attended
	`M` varchar(255),		-- Type of Service
	`N` varchar(255) NOT NULL,	-- Main Topic/Focus of the Service Received
	`O` varchar(255) NOT NULL,	-- Service Received
	`P` varchar(100),		-- Number of Unique Participants
	`Q` ENUM('Yes', 'No'),		-- Did Volunteers from the Host Community Participate in the Activity
	`R` ENUM('Yes', 'No'),		-- Directed at a Specific Target Group
	`S` ENUM('Yes', 'No'),		-- Target Group: Children (0-14 yrs)
	`T` ENUM('Yes', 'No'),		-- Target Group: Youth (15-24 yrs)
	`U` ENUM('Yes', 'No'),		-- Target Group: Senior
	`V` ENUM('Yes', 'No'),		-- Target Group: Gender-specific
	`W` ENUM('Yes', 'No'),		-- Target Group: Refugees
	`X` ENUM('Yes', 'No'),		-- Target Group: Ethnic/cultural/linguistic group
	`Y` ENUM('Yes', 'No'),		-- Target Group: Deaf or Hard of Hearing
	`Z` ENUM('Yes', 'No'),		-- Target Group: Blind or Partially Sighted
	`AA` ENUM('Yes', 'No'),		-- Target Group: Lesbian, Gay, Bisexual, Transgender, Queer (LGBTQ)
	`AB` ENUM('Yes', 'No'),		-- Target Group: Families/Parents
	`AC` ENUM('Yes', 'No'),		-- Target Group: Other impairments (physical, mental)
	`AD` ENUM('Yes', 'No'),		-- Target Group: Clients with international training in a regulated profession
	`AE` ENUM('Yes', 'No'),		-- Target Group: Clients with international training in a regulated trade
	`AF` ENUM('Yes', 'No'),		-- Target Group: Official language minorities
	`AG` varchar(255),		-- Status of Service
	`AH` varchar(255),		-- Reason for Leaving Service
	`AI` DATE NOT NULL,		-- Start Date (YYYY-MM-DD)
	`AJ` DATE,			-- End Date (YYYY-MM-DD)
	`AK` DATE,			-- Projected End Date (YYYY-MM-DD)
	`AL` ENUM('yes', 'no') NOT NULL,-- Was Essential Skills and Aptitudes Training Received as Part of the Service?
	`AM` ENUM('Yes', 'No'),		-- Computer Skills
	`AN` ENUM('Yes', 'No'),		-- Document Use
	`AO` ENUM('Yes', 'No'),		-- Interpersonal Skills and Workplace Culture
	`AP` ENUM('Yes', 'No'),		-- Leadership Training
	`AQ` ENUM('Yes', 'No'),		-- Life Skills
	`AR` ENUM('Yes', 'No'),		-- Numeracy
	`AS` varchar(255) NOT NULL,	-- Support Services Received
	`AT` ENUM('Yes', 'No'),		-- Care for Newcomer Children
	`AU` varchar(40),		-- Child 1: Age
	`AV` varchar(40),		-- Child 1: Type of Care
	`AW` varchar(40),		-- Child 2: Age
	`AX` varchar(40),		-- Child 2: Type of Care
	`AY` varchar(40),		-- Child 3: Age
	`AZ` varchar(40),		-- Child 3: Type of Care
	`BA` varchar(40),		-- Child 4: Age
	`BB` varchar(40),		-- Child 4: Type of Care
	`BC` varchar(40),		-- Child 5: Age
	`BD` varchar(40),		-- Child 5: Type of Care
	`BE` ENUM('Yes', 'No'),		-- Transportation
	`BF` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`BG` ENUM('Yes', 'No'),		-- Translation
	`BH` varchar(255),		-- Between
	`BI` varchar(255),		-- And
	`BJ` ENUM('Yes', 'No'),		-- Interpretation
	`BK` varchar(255),		-- Between
	`BL` varchar(255),		-- And
	`BM` ENUM('Yes', 'No'),		-- Crisis Counselling
	`BN` varchar(255),		-- Total Length of Service: Hours
	`BO` varchar(255),		-- Total Length of Service: Minutes
	`BP` varchar(255),		-- Reason for update
		-- 
	PRIMARY KEY (`C`, `D`)
);

