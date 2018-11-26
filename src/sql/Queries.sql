
-- what percentage of the people that are being referred to employment services are between the ages of 20-24? 25-29? 30-34? Etc.

SELECT CASE
	WHEN (year(curdate()) - year(E)) between 20 and 24 then '20-24'
	WHEN (year(curdate()) - year(E)) between 25 and 29 then '25-29'
	WHEN (year(curdate()) - year(E)) between 30 and 34 then '30-34'
	WHEN (year(curdate()) - year(E)) between 35 and 39 then '35-39'
	WHEN (year(curdate()) - year(E)) between 40 and 44 then '40-44'
	WHEN (year(curdate()) - year(E)) between 45 and 49 then '45-49'
	WHEN (year(curdate()) - year(E)) between 50 and 54 then '50-54'
	WHEN (year(curdate()) - year(E)) between 55 and 59 then '55-59'
	WHEN (year(curdate()) - year(E)) between 60 and 64 then '60-64'
	WHEN (year(curdate()) - year(E)) between 65 and 69 then '65-69'
	ELSE 'other'
	END
	AS AgeGroup, count(*) as Count FROM `NeedAssessmentReferrals`
	GROUP BY AgeGroup
	ORDER BY AgeGroup;

-- who is actually going and receiving the services they have been referred to? For example, there could be 200 newcomers from India who have been referred to language services this year. However, only 150 newcomers from India might have been documented to actually receive this service.
SELECT L AS ServiceReceived, count(*) AS Count
	FROM `InformationAndOrientation`
	WHERE H = 'Hindi'
	GROUP BY ServiceReceived;

-- increase or decrease in the number of newcomers accessing services over time
SELECT Month(H) AS Month, count(*) AS Count
	FROM `LanguageTrainingEnrolment`
	WHERE year(H) = 2018
	GROUP BY Month
	ORDER BY Month
