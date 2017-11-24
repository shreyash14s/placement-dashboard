create DATABASE p_dashboard;

use p_dashboard;

-- Not needed
-- CREATE TABLE cgpa_list (
--     usn VARCHAR(15) NOT NULL,
--     cgpa_student FLOAT CHECK(cgpa_student>0 and cgpa_student<=10),
--     PRIMARY KEY(usn,cgpa_student)
-- );

CREATE TABLE student (
    name VARCHAR(120) NOT NULL,
    usn VARCHAR(15) NOT NULL,
    stream ENUM('CSE','IS','EEE','ECE','ME','BT','CV'),
    age INTEGER CHECK (age > 18),
    tenth_percentage FLOAT CHECK (tenth_percentage>=0 and tenth_percentage<=100),
    twelfth_percentage FLOAT CHECK (tenth_percentage>=0 and tenth_percentage<=100),
    cgpa FLOAT CHECK (cgpa_student>0 and cgpa_student<=10.0),
    email_id VARCHAR(50) NOT NULL,
    resume_link VARCHAR(320),
    PRIMARY KEY (usn)
)

CREATE TABLE company (
    name VARCHAR(120) NOT NULL,
    company_id INTEGER NOT NULL AUTO_INCREMENT,
    test_date DATE NOT NULL,
    interview_date DATE NOT NULL,
    tier INTEGER CHECK (tier>=1 and tier<=3),
    website VARCHAR(320),
    postal_address VARCHAR(500),
    company_sector VARCHAR(50),
    PRIMARY KEY (company_id)
)

CREATE TABLE registrations
(
    company_id INT NOT NULL,
    usn VARCHAR(15) NOT NULL,
    PRIMARY KEY(company_id,usn),
    FOREIGN KEY (company_id) REFERENCES company_details(company_id),
    FOREIGN KEY (usn) REFERENCES student_details(usn)
);

-- DROP DATABASE p_dashboard;
