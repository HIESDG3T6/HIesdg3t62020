DROP TABLE IF EXISTS `map`;

DROP TABLE IF EXISTS `clinic`;
CREATE TABLE IF NOT EXISTS `clinic` (
  `clinicName` varchar(100) NOT NULL,
  `doctorName` varchar(100) NOT NULL,
  `groupedLocation` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `postalCode` int(6) NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `contactNumber` varchar(15) NOT NULL,
  PRIMARY KEY (`clinicName`, `doctorName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `clinicOpening`;
CREATE TABLE IF NOT EXISTS `clinicOpening` (
  `clinicName` varchar(100) NOT NULL,
  `openingDays` varchar(20) NOT NULL,
  `openingHour` varchar(10) NOT NULL,
  `closingHour` varchar(10) NOT NULL,
  PRIMARY KEY (`clinicName`, `openingDays`, `openingHour`),
  FOREIGN KEY (`clinicName`) REFERENCES `clinic`(`clinicName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- CREATE TABLE IF NOT EXISTS `map` (
--   `clinicName` varchar(100) NOT NULL,
--   `clinicOpening` varchar(100) NOT NULL,
--   PRIMARY KEY (`clinicName`, `clinicOpening`),
--   FOREIGN KEY (`clinicName`) REFERENCES `clinic`(`clinicName`),
--   FOREIGN KEY (`clinicOpening`) REFERENCES `clinicOpening`(`clinicName`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--
-- Inserting data for table `Clinic`
--

INSERT INTO `clinic` (`clinicName`, `doctorName`, `groupedLocation`, `address`,`postalCode`,`specialty`,`contactNumber`) VALUES
('okay clinic', 'Bob', 'Bukit Merah', '345 Bukit Merah Central #05-32',345678, 'Orthopedics','+65 12345678'),
('which clinic', 'Mike','Orchard', '234 Orchard Close #02-34', 234566, 'Pediatrics','+65 23456789'),
('okay clinic', 'April','Bukit Merah', '345 Bukit Merah Central #05-32',345678, 'Orthopedics','+65 12345678'),
('ohh clinic', 'JM','Jurong', '234 Jurong East St 13 #03-24',990984, 'Pediatrics','+65 12129090'),
('test clinic', 'Chicken','Changi', '432 Changi Place #02-34', 123678, 'Dialysis','+65 90901234');


--
-- Inserting data for table `clinicOpening`
--

INSERT INTO `clinicOpening` (`clinicName`, `openingDays`, `openingHour`, `closingHour`) VALUES
('okay clinic', 'Mon - Fri','08:00','13:00'),
('okay clinic', 'Sat','09:00','12:00'),
('okay clinic', 'Sun & Public Hols','Closed', 'Closed'),
('which clinic', 'Mon - Sat','08:00','13:00'),
('which clinic', 'Mon - Sat','15:00','17:00'),
('which clinic', 'Sun & Public Hols','08:00','11:00'),
('which clinic', 'Mon - Sat','18:00','21:00'),
('ohh clinic', 'Mon - Sun','08:00','17:00'),
('test clinic', 'Mon - Sun','07:00','13:00');


-- INSERT INTO `map` (`clinicName`, `clinicOpening`) VALUES
-- ('okay clinic', 'okay clinic'),
-- ('which clinic', 'which clinic'),
-- ('ohh clinic', 'ohh clinic'),
-- ('test clinic', 'test clinic');