CREATE TABLE IF NOT EXISTS `InformationAndOrientation`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update Record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` varchar(255) NOT NULL,	-- Date of Birth (YYYY-MM-DD)
	`F` char(8) NOT NULL,		-- Postal Code where the service was received
	`G` varchar(255) NOT NULL,	-- Start Date of Service (YYYY-MM-DD)
	`H` varchar(255) NOT NULL,	-- Language of Service
	`I` varchar(255) NOT NULL,	-- Official Language of Preference
	`J` varchar(255) NOT NULL,	-- Type of Institution/Organization Where Client Received Services
	`K` varchar(255) NOT NULL,	-- Referred By
	`L` varchar(255) NOT NULL,	-- Services Received
	`M` varchar(255),		-- Total Length of Orientation
	`N` int unsigned,		-- Total Length of Orientation: Hours
	`O` int unsigned,		-- Total Length of Orientation: Minutes
	`P` varchar(255),		-- Number of Clients in Group
	`Q` ENUM('Yes', 'No'),		-- Directed at a specific Target Group
	`R` ENUM('Yes', 'No'),		-- Target Group: Children (0-14 yrs)
	`S` ENUM('Yes', 'No'),		-- Target Group: Youth (15-24 yrs)
	`T` ENUM('Yes', 'No'),		-- Target Group: Seniors
	`U` ENUM('Yes', 'No'),		-- Target Group: Gender-specific
	`V` ENUM('Yes', 'No'),		-- Target Group: Refugees
	`W` ENUM('Yes', 'No'),		-- Target Group: Ethnic/cultural/linguistic group
	`X` ENUM('Yes', 'No'),		-- Target Group: Deaf or Hard of Hearing
	`Y` ENUM('Yes', 'No'),		-- Target Group: Blind or Partially Sighted
	`Z` ENUM('Yes', 'No'),		-- Target Group: Lesbian, Gay, Bisexual, Transgender, Queer (LGBTQ)
	`AA` ENUM('Yes', 'No'),		-- Target Group: Families/Parents
	`AB` ENUM('Yes', 'No'),		-- Target Group: Clients with other impairments (physical, mental)
	`AC` ENUM('Yes', 'No'),		-- Target Group: Clients with international training in a regulated profession
	`AD` ENUM('Yes', 'No'),		-- Target Group: Clients with international training in a regulated trade
	`AE` ENUM('Yes', 'No'),		-- Target Group: Official Language minorities
	`AF` ENUM('Yes', 'No'),		-- Overview of Canada
	`AG` ENUM('Yes', 'No'),		-- Overview of Canada Referrals
	`AH` ENUM('Yes', 'No'),		-- Sources of Information
	`AI` ENUM('Yes', 'No'),		-- Sources of Information Referrals
	`AJ` ENUM('Yes', 'No'),		-- Rights and Freedoms
	`AK` ENUM('Yes', 'No'),		-- Rights and Freedoms Referrals
	`AL` ENUM('Yes', 'No'),		-- Canadian Law and Justice
	`AM` ENUM('Yes', 'No'),		-- Canadian Law and Justice Referrals
	`AN` ENUM('Yes', 'No'),		-- Important Documents
	`AO` ENUM('Yes', 'No'),		-- Important Documents Referrals
	`AP` ENUM('Yes', 'No'),		-- Improving English or French
	`AQ` ENUM('Yes', 'No'),		-- Improving English or French Referrals
	`AR` ENUM('Yes', 'No'),		-- Employment and Income
	`AS` ENUM('Yes', 'No'),		-- Employment and Income Referrals
	`AT` ENUM('Yes', 'No'),		-- Education
	`AU` ENUM('Yes', 'No'),		-- Education Referrals
	`AV` ENUM('Yes', 'No'),		-- Housing
	`AW` ENUM('Yes', 'No'),		-- Housing Referrals
	`AX` ENUM('Yes', 'No'),		-- Health
	`AY` ENUM('Yes', 'No'),		-- Health Referrals
	`AZ` ENUM('Yes', 'No'),		-- Money and Finances
	`BA` ENUM('Yes', 'No'),		-- Money and Finances Referrals
	`BB` ENUM('Yes', 'No'),		-- Transportation
	`BC` ENUM('Yes', 'No'),		-- Transportation Referrals
	`BD` ENUM('Yes', 'No'),		-- Communications and Media
	`BE` ENUM('Yes', 'No'),		-- Communications and Media Referrals
	`BF` ENUM('Yes', 'No'),		-- Community Engagement
	`BG` ENUM('Yes', 'No'),		-- Community Engagement Referrals
	`BH` ENUM('Yes', 'No'),		-- Becoming a Canadian Citizen
	`BI` ENUM('Yes', 'No'),		-- Becoming a Canadian Citizen Referrals
	`BJ` ENUM('Yes', 'No'),		-- Interpersonal Conflict
	`BK` ENUM('Yes', 'No'),		-- Interpersonal Conflict Referrals
	`BL` ENUM('Yes', 'No'),		-- Was Essential Skills and Aptitude Training Received as Part of this Service?
	`BM` ENUM('Yes', 'No'),		-- Computer skills
	`BN` ENUM('Yes', 'No'),		-- Document Use
	`BO` ENUM('Yes', 'No'),		-- Interpersonal Skills and Workplace Culture
	`BP` ENUM('Yes', 'No'),		-- Leadership Training
	`BQ` ENUM('Yes', 'No'),		-- Numeracy
	`BR` ENUM('Yes', 'No') NOT NULL,-- Was Life Skills or Responsibilities of Citizenship Information Received as Part of this Service?
	`BS` ENUM('Yes', 'No'),		-- Life Skills
	`BT` ENUM('Yes', 'No'),		-- Rights and Responsibilities of Citizenship (based on discover Canada)
	`BU` ENUM('Yes', 'No') NOT NULL,-- Support Services Received
	`BV` ENUM('Yes', 'No'),		-- Care for Newcomer Children
	`BW` varchar(255),		-- Child 1: Age
	`BX` varchar(255),		-- Child 1: Type of Care
	`BY` varchar(255),		-- Child 2: Age
	`BZ` varchar(255),		-- Child 2: Type of Care
	`CA` varchar(255),		-- Child 3: Age
	`CB` varchar(255),		-- Child 3: Type of Care
	`CC` varchar(255),		-- Child 4: Age
	`CD` varchar(255),		-- Child 4: Type of Care
	`CE` varchar(255),		-- Child 5: Age
	`CF` varchar(255),		-- Child 5: Type of Care
	`CG` ENUM('Yes', 'No'),		-- Transportation
	`CH` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`CI` ENUM('Yes', 'No'),		-- Translation
	`CJ` varchar(255),		-- Between
	`CK` varchar(255),		-- And
	`CL` ENUM('Yes', 'No'),		-- Interpretation
	`CM` varchar(255),		-- Between
	`CN` varchar(255),		-- And
	`CO` ENUM('Yes', 'No'),		-- Crisis Counselling
	`CP` varchar(255) NOT NULL,	-- End Date of Service (YYYY-MM-DD)
	`CQ` varchar(255)		-- Reason for update
		-- 
);

