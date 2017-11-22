
create DATABASE p_dashboard;

use p_dashboard;

CREATE TABLE cgpa_list
(
    usn VARCHAR(15) NOT NULL,
    cgpa_student FLOAT CHECK(cgpa_student>0 and cgpa_student<=10),
    PRIMARY KEY(usn,cgpa_student)


);
CREATE TABLE student_details
(
    name VARCHAR(120) NOT NULL,
    usn VARCHAR(320) NOT NULL, 
    stream SET('CSE','IS','EEE','ECE','ME','BT','CV'),
    age INT CHECK(age>18),
    tenth_percentage FLOAT check(tenth_percentage>=0 and tenth_percentage<=100),
    twelfth_percentage FLOAT check(twelfth_percentage>=0 and twelfth_percentage<=100),
    cgpa_student FLOAT CHECK(cgpa_student>0 and cgpa_student<=10.0),
    email_id VARCHAR(50) NOT NULL,
    PRIMARY KEY(usn),
    FOREIGN KEY  (usn,cgpa_student) REFERENCES cgpa_list(usn,cgpa_student) ON UPDATE CASCADE,
    resume_link VARCHAR(320)

);



CREATE TABLE company_details
(
    name VARCHAR(120) NOT NULL,
    company_id INT  AUTO_INCREMENT ,
    test_date DATE NOT NULL,
    interview_date DATE NOT NULL,
    tier INT CHECK( tier >=1 and tier<=3),
    website VARCHAR(320),
    postal_address VARCHAR(500),
    company_sector VARCHAR(50),
    PRIMARY KEY(company_id)

);
 
CREATE TABLE registrations
(
    company_id INT NOT NULL,
    usn VARCHAR(15) NOT NULL,
    PRIMARY KEY(company_id,usn),
    FOREIGN KEY (company_id) REFERENCES company_details(company_id),
    FOREIGN KEY (usn) REFERENCES student_details(usn)
);

-- DROP DATABASE p_dashboard;