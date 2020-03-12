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
CREATE DATABASE IF NOT EXISTS `patient_history` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `patient_history`;

--

-- --------------------------------------------------------

--
-- Table structure for table `patient_history`
--

DROP TABLE IF EXISTS `patient_history`;
CREATE TABLE IF NOT EXISTS `patient_history` (
  `PID` int(11) NOT NULL,
  `AID` int(11) NOT NULL,
  `clinicName` varchar(100) NOT NULL,
  `PName` varchar(1000) NOT NULL,
  `contact` varchar(1000) DEFAULT NULL,
  `location` varchar(1000) DEFAULT NULL,
  `treatmentDetails` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`PID`,`AID`,`clinicName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient_history`
--

INSERT INTO `patient_history` (`PID`, `AID`, `clinicName`, `PName`, `contact`, `location`, `treatmentDetails`) VALUES
(1001, 8032020, 'famous Clinic', 'Amy', '12345678', 'Boon Lay', NULL),
(1002, 8032020, 'happy Clinic', 'Bob', '12345679', 'Boon Lay', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
