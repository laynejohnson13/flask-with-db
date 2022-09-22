####Creates SQLite DB 

import sqlite3

##Connecting to sqlite
connect = sqlite3.connect('./Patients.db')

##DB object
db = connect.cursor()

##delete patient_table if it already exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

##Creating table

table = """ CREATE TABLE patient_table (
    mrn VARCHAR(25) NOT NULL,
    firstname CHAR(25) NOT NULL,
    lastname CHAR(25) NOT NULL,
    dob CHAR(25) NOT NULL,
    sex CHAR(25) NOT NULL,
    zipcode CHAR(25) NOT NULL,
    contactinformation VARCHAR(25) NOT NULL,
    insuranceprovider CHAR(25) NOT NULL ); """

table 


db.execute(table)
connect.commit()


###Insert data into patients table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('53535', 'Debbie', 'Jones', '01/18/1965', 'Female', '11942', '631-888-9999', 'Magnacare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('87483', 'John', 'Smith', '10/17/1999', 'Male', '11968', '631-111-2222', 'United Healthcare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('93217', 'Margaret', 'Rich', '06/23/1988', 'Female', '11944', '631-333-4444', 'Aetna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('64287', 'Link', 'Johnson', '02/18/2001', 'Male', '11945', '631-555-6666', 'Cigna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('24242', 'Stephen', 'Nicks', '03/22/1999', 'Male', '11971', '631-999-0000', 'Magnacare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('53544', 'Zachary', 'Powers', '09/07/2003', 'Male', '11991', '631-444-1111', 'Cigna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('09482', 'Theresea', 'Portokalos', '01/11/1973', 'Female', '11900', '631-777-6666', 'Aetna')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, zipcode, contactinformation, insuranceprovider) values('74648', 'Louise', 'Corbett', '05/01/2010', 'Female', '11951', '631-111-7777', 'CareFirst')")

connect.commit()

##Close connection
connect.close()