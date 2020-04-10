DROP SCHEMA IF EXISTS Appointment;
create schema Appointment;
use Appointment;

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
	`AID` int AUTO_INCREMENT,
    `customerID` varchar(100) NOT NULL,
    `clinicID` varchar(100) NOT NULL,
    `doctorID` varchar(100) NOT NULL,
    `appointmentDate` DATE NOT NULL,
    `appointmentTime` TIME NOT NULL,

    CONSTRAINT appointment_pk PRIMARY KEY(`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 13, 2020 at 10:35 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `clinic`
--
DROP SCHEMA IF EXISTS clinic;
create schema clinic;
use clinic;

DROP TABLE IF EXISTS `clinic`;
CREATE TABLE IF NOT EXISTS `clinic` (
  `clinicName` varchar(100) NOT NULL,
  `doctorName` varchar(100) NOT NULL,
  `groupedLocation` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `postalCode` int(6) NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `contactNumber` varchar(15) NOT NULL,
  `opening` varchar(200) NOT NULL,
  PRIMARY KEY (`clinicName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clinic`
--

INSERT INTO `clinic` (`clinicName`, `groupedLocation`, `address`, `postalCode`, `specialty`, `contactNumber`, `opening`) VALUES
('I-HEALTH MEDICAL CLINIC', 'Balestier', '30 Bendemeer Road #01-883', 330030, 'General Practice', '+65 12456789', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('PLUSHEALTH MEDICAL CLINIC & SURGERY', 'Balestier', '89 Whampoa Drive #01-841', 320089, 'Pediatrics', '+65 12129090', 'Mon - Sun: 8AM - 5PM'),
('APOLLO MEDICAL CENTRE', 'Little India', '668 Chander Road #01-24', 210668, 'Gynecology', '+65 12345678', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('OGL MEDICAL CENTERS', 'Novena', '10 Sinaran Drive #10-31', 307506, 'Neurology', '+65 12223322', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('HEALTHWAY MEDICAL (NOVENA MEDICAL CENTRE) ', 'Novena', '10 Sinaran Drive #09-36', 307506, 'Urology', '+65 12223322', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('C K TAN FAMILY CLINIC & SURGERY PTE LTD ', 'Toa Payoh', '125 Lorong 1 Toa Payoh #01-537', 310125, 'Otolaryngology', '+65 90901234', 'Mon - Sun: 9AM - 6PM'),
('DOCTOR JAY MEDICAL CENTRE', 'Orchard', '115 Killiney Road', 239553, 'Internal Medicine', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('MINMED HEALTH SCREENERS ', 'Orchard', '290 Orchard Road #16-04/09/10', 238859, 'Allergology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('NEWCASTLE CLINIC PTE LTD', 'Orchard', '541 Orchard Road #18-02A', 238881, 'Gastroenterology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('SHENTON MEDICAL GROUP (TOA PAYOH)', 'Toa Payoh', '126 Lorong 1 Toa Payoh #01-561', 310178, 'Pulmonology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('WAN MEDICAL CLINIC', 'Bedok', '416 Bedok North Avenue 2 #01-21', 460416, 'Dermatology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('OEI FAMILY CLINIC', 'Pasir Ris', '625 Elias Road #02-316', 510625, 'Cardiology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('TAI SENG CLINIC', 'Paya Lebar', '11 Irving Place #01-09/10', 369551, 'Psychiatry', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('HEARTLAND FAMILY CLINIC', 'Yishun', '333C Yishun Street 31 #01-167', 763333, 'Surgery', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('LIN & SONS CLINIC & SURGERY PTE LTD', 'Choa Chu Kang', '18 Teck Whye Lane #01-97', 680018, 'General Practice', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('PIONEER MEDICARE', 'Jurong West', '3 Soon Lee Street #01-08', 627606, 'Rheumatology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


--
-- Create Database: `Insurance_Claim`
--
DROP SCHEMA IF EXISTS Insurance_Claim;
CREATE SCHEMA IF NOT EXISTS `Insurance_Claim` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Insurance_Claim`;


--
-- Table structure for table `Insurance_Claim`
--
DROP TABLE IF EXISTS `Insurance_Claim`;
CREATE TABLE IF NOT EXISTS `Insurance_Claim`(
    `ClaimID` INT PRIMARY KEY AUTO_INCREMENT,
    `PatientID` varchar(100) NOT NULL,
    `ClinicName` varchar(100) NOT NULL,
    `ClaimDate` DATETIME NOT NULL,
    `Medicine` TEXT DEFAULT NULL,
    `BillAmount` decimal(10,2) NOT NULL,
    `ClaimedAmount` decimal(10,2) NOT NULL,
    `ClaimStatus` varchar(13) NOT NULL,
    `RefundStatus` varchar(13) DEFAULT NULL
);



--
-- Dumping data for table `book`
--

INSERT INTO `Insurance_Claim` (`ClaimID`, `PatientID`, `ClinicName`, `ClaimDate`,`Medicine`,`BillAmount`,`ClaimedAmount`,`ClaimStatus`,`RefundStatus`) VALUES
('1', '123456780', 'okay clinic', '2020-01-27 12:01:00',NULL,58.1,58.1,'Close','Approved'),
('2', '123456781', 'which clinic', '2020-01-30 14:01:00','panadol',28,28,'Close','Approved'),
('3', '123456782', 'okay clinic', '2020-01-30 13:01:00','probiotics',33.1,15,'Close','Approved'),
('4', '123456783', 'ohh clinic', '2020-01-31 22:01:00','aspirin',33.2,33.2,'Close','Rejected'),
('5', '123456784', 'okay clinic', '2020-02-01 10:01:00','panadol',53.2,53.2,'Open','Pending');


--
-- Table structure for table `Insurance_Claim`
--
DROP TABLE IF EXISTS `refund`;
CREATE TABLE IF NOT EXISTS `refund`(
    `Corrid` varchar(100) NOT NULL PRIMARY KEY,
    `ClaimID` INT,
    `reply_Status` varchar(100),
    `Approval_url` varchar(10000)
);

DROP SCHEMA IF EXISTS Notification;
create schema Notification; /*creating schema */
use Notification;


CREATE TABLE UserChatID /*creating course table*/
(
TelegramHandle  varchar(100)    not null,
ChatID	int(100)    not null				,
CONSTRAINT	notification_pk	PRIMARY KEY (TelegramHandle)
);


-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 10, 2020 at 02:24 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Create Database: `patient_history`
--
DROP SCHEMA IF EXISTS patient_history;
CREATE SCHEMA IF NOT EXISTS `patient_history` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `patient_history`;

--

-- --------------------------------------------------------

--
-- Table structure for table `patient_history`
--

DROP TABLE IF EXISTS `patient_history`;
CREATE TABLE IF NOT EXISTS `patient_history` (
  `PID` varchar(100) NOT NULL,
  `AID` varchar(100) NOT NULL,
  `Medication` varchar(1000) DEFAULT NULL,
  `BillAmount` varchar(1000) DEFAULT NULL,
  `claimAmount` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
INSERT INTO `patient_history` (`PID`, `AID`, `Medication`, `BillAmount`, `claimAmount`) VALUES
('123456780', '1', 'help', '13', '12');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


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