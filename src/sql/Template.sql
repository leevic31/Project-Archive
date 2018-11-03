use c43;

create table `Template`(
    TemplateID INT NOT NULL AUTO_INCREMENT,
    TemplateName varchar(80),
    PRIMARY KEY(TemplateID)
    );

insert into `Template` (TemplateName) values
('NeedAssessmentReferrals'),
('CommunityConnection'),
('InformationAndOrientation'),
('Employment'),
('LanguageTrainingEnrolment'),
('LanguageTrainingSetup'),
('LanguageTrainingExit');
