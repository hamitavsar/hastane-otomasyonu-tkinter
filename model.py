import sqlite3
from sqlite3.dbapi2 import Cursor

con =sqlite3.connect("lab.db")
cur = con.cursor()

def autoCreateTable():
    cur.execute('''
    
        CREATE TABLE IF NOT EXISTS DOCTORS(
            id integer PRIMARY KEY,
            name text NOT NULL,
            specialty text NOT NULL,
            costOfAdmission integer NOT NULL,
            nameOfTheReception text NOT NULL,
            percentageOfDeductionsOnSalaries integer NOT NULL
            
        )
    
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS HISTORYOFPATENTS(
            id integer PRIMARY KEY NOT NULL,
            idPatients int  NOT NULL,
            idDoctors1 int  NOT NULL,
            dateofAdmission text NOT NULL,
           
            costOfAdmission int NOT NULL,
            FOREIGN KEY (idPatients)  REFERENCES PATIENTS (id)
            FOREIGN KEY (idDoctors1)   REFERENCES DOCTORS  (id)
           
             
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS PATIENTS(
        id integer PRIMARY KEY,
        patientName text NOT NULL,
        patientSurname text NOT NULL,
        dateOfBirthPatient date NOT NULL,
        patientAdress text NOT NULL
       
        )
    ''')

def autoMakeData():

    #Auto creater make some Doctors 
    cur.executescript ("""    
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Alex Ibrahimovic','Therapist',100,'Hamit Avsar',10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Natalia Alexandrova','Pyhsicologist',150,'Can', 10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Kerem ER','Cardiologist',450,'Yagiz Ali', 15);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Bora Samdanli','Cardiologist',450,'Hasan Sabbah', 10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Dmitry','Surgeon',200,'Yagiz Bora',10);
    INSERT INTO DOCTORS(name, specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values ('Natasa','Surgeon',200,'Atahan',15);
    """)
    cur.executescript("""
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Cabbar','Donergil','16-05-1990','Ankara');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Bora','Samdanli','16-05-1998','Kharkiv');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Kemal','Donmez','1-01-1999','Istanbul');
    INSERT INTO PATIENTS(patientName,patientSurname,dateOfBirthPatient,patientAdress) values ('Tayyar','Yılmaz','12-03-1995','Antalya');
    
    """)
 