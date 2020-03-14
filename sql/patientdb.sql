DROP SCHEMA IF EXISTS Patient;
create schema Patient; /*creating schema */
use Patient;


CREATE TABLE Patient /*creating course table*/
(
PatientID		varchar(255)		not null	,
PatientName		varchar(255)		not null	,
Email		varchar(100)					,
Telehandle	varchar(100)					,
PolicyNum	varchar(100)		not null    ,
CONSTRAINT	course_pk	PRIMARY KEY (PatientID)
);

INSERT INTO `Patient` (`PatientID`, `PatientName`, `Email`, `Telehandle`, `PolicyNum`) VALUES
('123456780', 'Jon', 'jonathan_lxh@hotmail.com', 'jonuggets', 'B2234567890'),
('123456781', 'Charlene', 'huifen.ong.2018@business.smu.edu.sg', 'charshaobao','B2234567891'),
('123456782', 'Charlotte', 'charlotte@gmail.com', 'charlotteong', 'B2234567892'),
('123456783', 'Jiamin', 'jiamin.tan.2017@business.smu.edu.sg', 'Tohjiamin', 'B2234567893'),
('123456784', 'Zhengnan', 'znzhang.2018@sis.smu.edu.sg', 'Zhengnannn', 'B2234567894'),
('123456785', 'Huijie', 'huijie.shan.2018@sis.smu.edu.sg', 'miya2yummy', 'B2234567895'),
('123456786', 'Lum Eng Kit', 'eklum@smu.edu.sg', 'eklum', 'B2234567896'),
('123456787', 'Faith', 'faith@gmail.com', '', 'B2234567897'),
('123456788', 'Jiang Ling Xiao', 'lxjiang@smu.edu.sg', '', 'B2234567898');