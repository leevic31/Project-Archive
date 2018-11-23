CREATE TABLE IF NOT EXISTS `NeedAssessmentReferrals`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update Record ID
	`C` varchar(255) NOT NULL,	-- Unique Identifier
	`D` BIGINT(8) NOT NULL,		-- Unique Identifier Value
	`E` DATE NOT NULL,		-- Date of Birth (YYYY-MM-DD)
	`F` char(6) NOT NULL,		-- Postal Code where the service was received
	`G` DATE NOT NULL,		-- Start Date of Assessment (YYYY-MM-DD)
	`H` varchar(255) NOT NULL,	-- Language of Service
	`I` varchar(255) NOT NULL,	-- Official Language of Preference
	`J` varchar(255) NOT NULL,	-- Type of Institution/Organization Where Client Received Services
	`K` varchar(255) NOT NULL,	-- Referred By
	`L` ENUM('Yes', 'No'),		-- Increase knowledge of: Life in Canada
	`M` ENUM('Yes', 'No'),		-- Increase knowledge of: Life in Canada Referrals
	`N` ENUM('Yes', 'No'),		-- Increase knowledge of: Community and Government Services
	`O` ENUM('Yes', 'No'),		-- Increase knowledge of: Community and Government Services Referrals
	`P` ENUM('Yes', 'No'),		-- Increase knowledge of: Working in Canada
	`Q` ENUM('Yes', 'No'),		-- Increase knowledge of: Working in Canada Referrals
	`R` ENUM('Yes', 'No'),		-- Increase knowledge of: Education in Canada
	`S` ENUM('Yes', 'No'),		-- Increase knowledge of: Education in Canada Referrals
	`T` ENUM('Yes', 'No'),		-- Increase the following: Social networks
	`U` ENUM('Yes', 'No'),		-- Increase the following: Social networks Referrals
	`V` ENUM('Yes', 'No'),		-- Increase the following: Professional networks
	`W` ENUM('Yes', 'No'),		-- Increase the following: Professional networks Referrals
	`X` ENUM('Yes', 'No'),		-- Increase the following: Access to local community services
	`Y` ENUM('Yes', 'No'),		-- Increase the following: Access to local community services Referrals
	`Z` ENUM('Yes', 'No'),		-- Increase the following: Level of community involvement
	`AA` ENUM('Yes', 'No'),		-- Increase the following: Level of community involvement Referrals
	`AB` ENUM('Yes', 'No'),		-- Improve Language Skills
	`AC` ENUM('Yes', 'No'),		-- Improve Language Skills Referrals
	`AD` varchar(255),		-- Improve Language Skills to
	`AE` ENUM('Yes', 'No'),		-- Improve Other Skills
	`AF` ENUM('Yes', 'No'),		-- Improve Other Skills Referrals
	`AG` varchar(255),		-- Improve Other Skills to
	`AH` ENUM('Yes', 'No'),		-- Find employment
	`AI` ENUM('Yes', 'No'),		-- Find employment Referrals
	`AJ` varchar(255),		-- Find employment: TimeFrame
	`AK` varchar(255),		-- Find employment: Minimum one year's work experience?
	`AL` varchar(255),		-- Find employment: Intends to work in an occupation
					-- 	corresponding to which National Occupation Classification skill level?
	`AM` varchar(255),		-- Find employment: Intends to obtain credential recognition or obtain license to work in Canada?
	`AN` ENUM('Yes', 'No', 'Unknown/Not sure') NOT NULL,		-- Client intends to become a Canadian citizen?
	`AO` ENUM('Yes', 'No') NOT NULL,-- Support services may be required
	`AP` varchar(255),		-- Care for Newcomer Children
	`AQ` ENUM('Yes', 'No'),		-- Transportation
	`AR` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`AS` ENUM('Yes', 'No'),		-- Translation
	`AT` ENUM('Yes', 'No'),		-- Interpretation
	`AU` ENUM('Yes', 'No'),		-- Crisis Counselling
	`AV` ENUM('Yes', 'No') NOT NULL,-- Non-IRCC program services needed
	`AW` ENUM('Yes', 'No'),		-- Food/Clothing/Other Material Needs
	`AX` ENUM('Yes', 'No'),		-- Food/Clothing/Other Material Needs Referrals
	`AY` ENUM('Yes', 'No'),		-- Housing/Accommodation
	`AZ` ENUM('Yes', 'No'),		-- Housing/Accommodation Referrals
	`BA` ENUM('Yes', 'No'),		-- Health/Mental Health/Well Being
	`BB` ENUM('Yes', 'No'),		-- Health/Mental Health/Well Being Referrals
	`BC` ENUM('Yes', 'No'),		-- Financial
	`BD` ENUM('Yes', 'No'),		-- Financial Referrals
	`BE` ENUM('Yes', 'No'),		-- Family Support
	`BF` ENUM('Yes', 'No'),		-- Family Support Referrals
	`BG` ENUM('Yes', 'No'),		-- Language (Non-IRCC)
	`BH` ENUM('Yes', 'No'),		-- Language (Non-IRCC) Referrals
	`BI` ENUM('Yes', 'No'),		-- Education/Skills Development
	`BJ` ENUM('Yes', 'No'),		-- Education/Skills Development Referrals
	`BK` ENUM('Yes', 'No'),		-- Employment-related
	`BL` ENUM('Yes', 'No'),		-- Employment-related Referrals
	`BM` ENUM('Yes', 'No'),		-- Legal Information and Services
	`BN` ENUM('Yes', 'No'),		-- Legal Information and Services Referrals
	`BO` ENUM('Yes', 'No'),		-- Community Services
	`BP` ENUM('Yes', 'No'),		-- Community Services Referrals
	`BQ` ENUM('Yes', 'No') NOT NULL,-- Support Services Received
	`BR` ENUM('Yes', 'No'),		-- Care for Newcomer Children
	`BS` varchar(40),		-- Child 1: Age
	`BT` varchar(40),		-- Child 1: Type of Care
	`BU` varchar(40),		-- Child 2: Age
	`BV` varchar(40),		-- Child 2: Type of Care
	`BW` varchar(40),		-- Child 3: Age
	`BX` varchar(40),		-- Child 3: Type of Care
	`BY` varchar(40),		-- Child 4: Age
	`BZ` varchar(40),		-- Child 4: Type of Care
	`CA` varchar(40),		-- Child 5: Age
	`CB` varchar(40),		-- Child 5: Type of Care
	`CC` ENUM('Yes', 'No'),		-- Transportation
	`CD` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`CE` ENUM('Yes', 'No'),		-- Translation
	`CF` varchar(255),		-- Between
	`CG` varchar(255),		-- And
	`CH` ENUM('Yes', 'No'),		-- Interpretation
	`CI` varchar(255),		-- Between
	`CJ` varchar(255),		-- And
	`CK` ENUM('Yes', 'No'),		-- Crisis Counselling
	`CL` ENUM('Yes', 'No') NOT NULL,-- Settlement Plan completed and shared with client
	`CM` DATE NOT NULL,		-- End Date of Assessment (YYYY-MM-DD)
	`CN` varchar(255),		-- Reason for update
		-- 
	PRIMARY KEY (`C`, `D`)
);

