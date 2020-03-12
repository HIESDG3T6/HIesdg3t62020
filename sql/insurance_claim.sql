DROP TABLE IF EXISTS Insurance_Claim;
CREATE DATABASE Insurance_Claim;

CREATE TABLE insurance_claim(
    ClaimID int PRIMARY KEY,
    PatientID int,
    ClinicID int,
    ClaimDate DATE,
    Medicine text,
    BillAmount FLOAT,
    ClaimedAmount FLOAT,
    ClaimStatus VARCHAR(255),
    RefundStatus VARCHAR(255)
);


