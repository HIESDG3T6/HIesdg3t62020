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
CREATE DATABASE IF NOT EXISTS `Insurance_Claim` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Insurance_Claim`;


--
-- Table structure for table `Insurance_Claim`
--
DROP TABLE IF EXISTS `Insurance_Claim`;
CREATE TABLE IF NOT EXISTS `Insurance_Claim`(
    `ClaimID` INT NOT NULL PRIMARY KEY,
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
    `Corrid` INT NOT NULL PRIMARY KEY,
    `ClaimID` INT,
    `reply_Status` INT,
    `Approval_url` varchar(10000)
);

