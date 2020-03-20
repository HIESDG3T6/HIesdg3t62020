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

INSERT INTO `clinic` (`clinicName`, `doctorName`, `groupedLocation`, `address`, `postalCode`, `specialty`, `contactNumber`, `opening`) VALUES
('another clinic', 'Smart', 'Bukit Merah', '234 Bukit Merah Place #03-32', 345678, 'General Practice', '+65 12456789', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('ohh clinic', 'JM', 'Jurong', '234 Jurong East St 13 #03-24', 990984, 'Pediatrics', '+65 12129090', 'Mon - Sun: 8AM - 5PM'),
('okay clinic', 'April', 'Bukit Merah', '345 Bukit Merah Central #05-32', 345678, 'Gynecology', '+65 12345678', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('jmisagod clinic', 'Bob', 'Bukit Merah', '455 Bukit Merah Central #02-31', 377899, 'Neurology', '+65 12223322', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('5th clinic', 'Amy', 'Bukit Merah', '435 Bukit Merah Central #02-21', 377899, 'Urology', '+65 12223322', 'Mon - Fri: 8AM - 1PM, Sat: 9AM - 12PM, Sun & Public Hols: Closed'),
('test clinic', 'Chicken', 'Jurong', '432 Jurong Place #02-34', 123678, 'Otolaryngology', '+65 90901234', 'Mon - Sun: 9AM - 6PM'),
('which clinic', 'Mike', 'Orchard', '234 Orchard Close #02-34', 234566, 'Internal Medicine', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('wew clinic', 'Banana', 'Orchard', '222 Orchard Close #02-34', 123454, 'Allergology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('sian clinic', 'Yoyo', 'Orchard', '333 Orchard Close #02-34', 999000, 'Gastroenterology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('1 clinic', 'May', 'Orchard', '333 Orchard Close #02-34', 999000, 'Pulmonology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('2 clinic', 'Son', 'Jurong', '333 Jurong Close #02-34', 999030, 'Dermatology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('3 clinic', 'Cheese', 'Orchard', '333 Orchard Close #02-34', 999000, 'Cardiology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('4 clinic', 'Ice', 'Orchard', '333 Orchard Close #02-34', 999000, 'Psychiatry', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('6 clinic', 'Cream', 'Bras Basah', '333 Bras Close #02-34', 999000, 'Surgery', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('8 clinic', 'Health', 'Bras Basah', '333 Basah Close #02-34', 999000, 'General Practice', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM'),
('10 clinic', 'Wong', 'Bras Basah', '333 BB Close #02-34', 999000, 'Rheumatology', '+65 23456789', 'Mon - Sat: 8AM - 1PM & 4PM - 8PM, Sun & Public Hols: 8AM - 11AM');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
