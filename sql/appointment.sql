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