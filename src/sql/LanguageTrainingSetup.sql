CREATE TABLE IF NOT EXISTS `LanguageTrainingSetup`(
	`TimeStamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`A` varchar(255),		-- Processing Details
	`B` BIGINT(8),			-- Update record ID
	`C` varchar(255) NOT NULL,	-- Course Code
	`D` varchar(255),		-- Notes
	`E` varchar(255) NOT NULL,	-- Course Held On An Ongoing Basis
	`F` varchar(255) NOT NULL,	-- Official Language of Course
	`G` varchar(255) NOT NULL,	-- Format of Training Provided
	`H` varchar(255),		-- Classes Held At
	`I` TINYINT unsigned,		-- In-Person Instruction (%)
	`J` TINYINT unsigned,		-- Online/Distance Instruction (%)
	`K` int unsigned NOT NULL,	-- Total Number of Spots in Course
	`L` int unsigned NOT NULL,	-- Number of IRCC-Funded Spots in Course
	`M` varchar(100) NOT NULL,	-- New Students Can Enrol in the Course
	`N` ENUM('Yes', 'No') NOT NULL,	-- Support Services Available for Client in this Course
	`O` ENUM('Yes', 'No'),		-- Care for Newcomer Children
	`P` ENUM('Yes', 'No'),		-- Transportation
	`Q` ENUM('Yes', 'No'),		-- Provisions for Disabilities
	`R` DATE NOT NULL,		-- Course Start Date (YYYY-MM-DD)
	`S` DATE NOT NULL,		-- Course End Date (YYYY-MM-DD)
	`T` ENUM('Yes', 'No'),		-- Schedule: Morning
	`U` ENUM('Yes', 'No'),		-- Schedule: Afternoon
	`V` ENUM('Yes', 'No'),		-- Schedule: Evening
	`W` ENUM('Yes', 'No'),		-- Schedule: Weekend
	`X` ENUM('Yes', 'No'),		-- Schedule: Anytime
	`Y` ENUM('Yes', 'No'),		-- Schedule: Online
	`Z` FLOAT NOT NULL,		-- Instructional Hours Per Class
	`AA` int unsigned NOT NULL,	-- Classes Per Week
	`AB` int unsigned,		-- Weeks of Instruction
	`AC` int unsigned,		-- Weeks of Instruction Per Year
	`AD` varchar(100) NOT NULL,	-- Dominant Focus of the Course
	`AE` ENUM('Yes', 'No') NOT NULL,-- Course Directed at a Specific Target Group
	`AF` ENUM('Yes', 'No'),		-- Children (0-14 yrs)
	`AG` ENUM('Yes', 'No'),		-- Youth (15-24 yrs)
	`AH` ENUM('Yes', 'No'),		-- Senior
	`AI` ENUM('Yes', 'No'),		-- Gender-specific
	`AJ` ENUM('Yes', 'No'),		-- Refugees
	`AK` ENUM('Yes', 'No'),		-- Official language minorities
	`AL` ENUM('Yes', 'No'),		-- Ethnic/cultural/linguistic group
	`AM` ENUM('Yes', 'No'),		-- Deaf or Hard of Hearing
	`AN` ENUM('Yes', 'No'),		-- Blind or Partially Sighted
	`AO` ENUM('Yes', 'No'),		-- Clients with other impairments (physical, mental)
	`AP` ENUM('Yes', 'No'),		-- Lesbian, Gay, Bisexual, Transgender, Queer (LGBTQ)
	`AQ` ENUM('Yes', 'No'),		-- Families/Parents
	`AR` ENUM('Yes', 'No'),		-- Clients with international training in a regulated profession
	`AS` ENUM('Yes', 'No'),		-- Clients with international training in a regulated trade
	`AT` ENUM('Yes', 'No') NOT NULL,-- Materials Used in Course
	`AU` ENUM('Yes', 'No'),		-- Citizenship preparation
	`AV` ENUM('Yes', 'No'),		-- PBLA language companion
	`AW` varchar(255),		-- Contact Name
	`AX` int unsigned NOT NULL,	-- Street Number
	`AY` varchar(255) NOT NULL,	-- Street Name
	`AZ` varchar(255) NOT NULL,	-- Street Type
	`BA` varchar(255),		-- Street Direction
	`BB` varchar(255),		-- Unit/Suite
	`BC` varchar(255) NOT NULL,	-- Province
	`BD` varchar(255) NOT NULL,	-- City
	`BE` char(6) NOT NULL,		-- Postal Code (A#A#A#)
	`BF` varchar(20) NOT NULL,	-- Telephone Number (###-###-####)
	`BG` varchar(255),		-- Telephone Extension
	`BH` varchar(255) NOT NULL,	-- Email Address
	`BI` varchar(8),		-- Listening Skill Level 1
	`BJ` varchar(8),		-- Listening Skill Level 2
	`BK` varchar(8),		-- Listening Skill Level 3
	`BL` varchar(8),		-- Listening Skill Level 4
	`BM` varchar(8),		-- Listening Skill Level 5
	`BN` varchar(8),		-- Listening Skill Level 6
	`BO` varchar(8),		-- Listening Skill Level 7
	`BP` varchar(8),		-- Listening Skill Level 8
	`BQ` varchar(8),		-- Listening Skill Level 9
	`BR` varchar(8),		-- Listening Skill Level 10
	`BS` varchar(8),		-- Listening Skill Level 11
	`BT` varchar(8),		-- Listening Skill Level 12
	`BU` varchar(8),		-- Speaking Skill Level 1
	`BV` varchar(8),		-- Speaking Skill Level 2
	`BW` varchar(8),		-- Speaking Skill Level 3
	`BX` varchar(8),		-- Speaking Skill Level 4
	`BY` varchar(8),		-- Speaking Skill Level 5
	`BZ` varchar(8),		-- Speaking Skill Level 6
	`CA` varchar(8),		-- Speaking Skill Level 7
	`CB` varchar(8),		-- Speaking Skill Level 8
	`CC` varchar(8),		-- Speaking Skill Level 9
	`CD` varchar(8),		-- Speaking Skill Level 10
	`CE` varchar(8),		-- Speaking Skill Level 11
	`CF` varchar(8),		-- Speaking Skill Level 12
	`CG` varchar(8),		-- Reading Skill Level 1
	`CH` varchar(8),		-- Reading Skill Level 2
	`CI` varchar(8),		-- Reading Skill Level 3
	`CJ` varchar(8),		-- Reading Skill Level 4
	`CK` varchar(8),		-- Reading Skill Level 5
	`CL` varchar(8),		-- Reading Skill Level 6
	`CM` varchar(8),		-- Reading Skill Level 7
	`CN` varchar(8),		-- Reading Skill Level 8
	`CO` varchar(8),		-- Reading Skill Level 9
	`CP` varchar(8),		-- Reading Skill Level 10
	`CQ` varchar(8),		-- Reading Skill Level 11
	`CR` varchar(8),		-- Reading Skill Level 12
	`CS` varchar(8),		-- Reading Skill Level 13
	`CT` varchar(8),		-- Reading Skill Level 14
	`CU` varchar(8),		-- Reading Skill Level 15
	`CV` varchar(8),		-- Reading Skill Level 16
	`CW` varchar(8),		-- Reading Skill Level 17
	`CX` varchar(8),		-- Writing Skill Level 1
	`CY` varchar(8),		-- Writing Skill Level 2
	`CZ` varchar(8),		-- Writing Skill Level 3
	`DA` varchar(8),		-- Writing Skill Level 4
	`DB` varchar(8),		-- Writing Skill Level 5
	`DC` varchar(8),		-- Writing Skill Level 6
	`DD` varchar(8),		-- Writing Skill Level 7
	`DE` varchar(8),		-- Writing Skill Level 8
	`DF` varchar(8),		-- Writing Skill Level 9
	`DG` varchar(8),		-- Writing Skill Level 10
	`DH` varchar(8),		-- Writing Skill Level 11
	`DI` varchar(8),		-- Writing Skill Level 12
	`DJ` varchar(8),		-- Writing Skill Level 13
	`DK` varchar(8),		-- Writing Skill Level 14
	`DL` varchar(8),		-- Writing Skill Level 15
	`DM` varchar(8),		-- Writing Skill Level 16
	`DN` varchar(8),		-- Writing Skill Level 17
		-- 
	PRIMARY KEY (`C`, `D`)
);

