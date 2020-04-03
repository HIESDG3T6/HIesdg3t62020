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
