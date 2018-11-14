CREATE TABLE IF NOT EXISTS `Template`(
    TemplateID INT NOT NULL AUTO_INCREMENT,
    TemplateName varchar(80),
    PRIMARY KEY(TemplateID)
    );

INSERT INTO `Template` (TemplateName) VALUES
('NeedAssessmentReferrals'),
('CommunityConnection'),
('InformationAndOrientation'),
('Employment'),
('LanguageTrainingEnrolment'),
('LanguageTrainingSetup'),
('LanguageTrainingExit');
