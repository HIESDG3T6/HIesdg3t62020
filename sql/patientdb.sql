DROP SCHEMA IF EXISTS Patient;
create schema Patient; /*creating schema */
use Patient;


CREATE TABLE Patient /*creating course table*/
(
PatientID		varchar(100)		not null	,
PatientName		varchar(100)		not null	,
Email		varchar(100)					,
Telehandle	varchar(100)					,
PolicyNum	varchar(100)		not null    ,
username    varchar(100)		not null	,
pw    varchar(100)		not null	,
CONSTRAINT	course_pk	PRIMARY KEY (PatientID)
);

INSERT INTO `Patient` (`PatientID`, `PatientName`, `Email`, `Telehandle`, `PolicyNum`, `username`, `pw`) VALUES
('123456780', 'Jon', 'jonathan_lxh@hotmail.com', 'jonuggets', 'B2234567890', 'Jon', 'Jon'),
('123456781', 'Charlene', 'huifen.ong.2018@business.smu.edu.sg', 'charshaobao','B2234567891', 'Charlene', 'Charlene'),
('123456782', 'Charlotte', 'charlotte@gmail.com', 'charlotteong', 'B2234567892', 'Charlotte', 'Charlotte'),
('123456783', 'Jiamin', 'jiamin.tan.2017@business.smu.edu.sg', 'Tohjiamin', 'B2234567893', 'Jiamin', 'Jiamin'),
('123456784', 'Zhengnan', 'znzhang.2018@sis.smu.edu.sg', 'Zhengnannn', 'B2234567894', 'Zhengnan', 'Zhengnan'),
('123456785', 'Huijie', 'huijie.shan.2018@sis.smu.edu.sg', 'miya2yummy', 'B2234567895', 'Huijie', 'Huijie'),
('123456786', 'Lum Eng Kit', 'eklum@smu.edu.sg', 'eklum', 'B2234567896', 'Lum Eng Kit', 'Lum Eng Kit'),
('123456787', 'Faith', 'faith@gmail.com', '', 'B2234567897', 'Faith', 'Faith'),
('123456788', 'Jiang Ling Xiao', 'lxjiang@smu.edu.sg', '', 'B2234567898', 'Jiang Ling Xiao', 'Jiang Ling Xiao');