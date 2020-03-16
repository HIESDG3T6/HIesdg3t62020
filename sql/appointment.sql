DROP SCHEMA IF EXISTS Appointment;
create schema Appointment;
use Apointment;

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
    `customerID` varchar(100) NOT NULL,
    `clinicID` varchar(100) NOT NULL,
    `doctorID` varchar(100) NOT NULL,
    `appointmentDate` DATE NOT NULL,
    `appointmentTime` TIME NOT NULL,

    CONSTRAINT appointment_pk PRIMARY KEY(`customerID`, `appointmentDate`, `appointmentTime`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;