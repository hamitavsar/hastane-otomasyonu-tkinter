import model
from tkinter import messagebox
con = model.con
cur = model.cur

class Doctor():
    
    def saveDoctor(DoctorName=None,specialty=None,costOfAdmissin=None,nameOfTheReception=None,percentageOfDeductionsOnSalaries=None):
        try:
            costOfAdmissin = int(costOfAdmissin)
            percentageOfDeductionsOnSalaries = int(percentageOfDeductionsOnSalaries)
        except:
        #Ask to the teacher
            if (costOfAdmissin is not int) and (percentageOfDeductionsOnSalaries is not int):
                messagebox.showwarning ("ERROR","YOU MUST BE INSERT AN INTEGER VALUE IN THE COST AND PERCENTEAGE")
            elif costOfAdmissin is not int:
                messagebox.showwarning("ERROR","YOU MUST BE INSERT AN INTEGER IN THE COST")
            elif percentageOfDeductionsOnSalaries is not int:
                messagebox.showwarning("ERROR","YOU MUST BE INSERT AN INTEGER IN THE PERCENTAGE")
            return False
        if DoctorName == None or specialty == None or costOfAdmissin == None or nameOfTheReception == None or percentageOfDeductionsOnSalaries == None:
            messagebox.showwarning("ERROR","YOU MUST BE INSERT INFORMATION")
        else:
             cur.execute ("INSERT INTO DOCTORS(name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries) values (?,?,?,?,?);",(DoctorName,specialty,costOfAdmissin,nameOfTheReception,percentageOfDeductionsOnSalaries))
             con.commit()
             messagebox.showinfo("Success","{} is registered".format(DoctorName))
             return True
        
    def updateDoctor(id,name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries):
        id = int(id)
        if id < 1:
            messagebox.showinfo("ERROR","YOU MUST BE INSERT INFORMATION")
        else:    
            updateQuery="""UPDATE DOCTORS SET name=?,specialty=?,costOfAdmission =?,nameOfTheReception=?,percentageOfDeductionsOnSalaries=? WHERE id=?"""
            setValues =(name,specialty,costOfAdmission,nameOfTheReception,percentageOfDeductionsOnSalaries,id)
            con.execute(updateQuery,setValues)
            con.commit()
            return True
        
    def getDoctor():
        cur.execute("SELECT * FROM DOCTORS")
        data=cur.fetchall()
        return data
    
    def deleteDoctors(id,DataDoctorName):
        id = int(id)
        if id < 1:
            messagebox.showwarning("Attention",
                "You Must Be Select Doctor")
        else: 
            MsgBox = messagebox.askquestion("Attention!","You Want to Delete Doctor {} ?".format(DataDoctorName),icon='warning')
            if MsgBox == 'yes':
                cur.execute ("DELETE FROM DOCTORS WHERE id=?",(id,))
                cur.execute("DELETE FROM HISTORYOFPATENTS WHERE idDoctors1=?",(id,))
                con.commit()
                messagebox.showinfo("Success","{} is deleted.".format(DataDoctorName))
                return True

class Patients():

    def SavePatients(Name="",Surname="",BirthDay="",Adres=""):
        if Name == "" or Surname == "" or Adres == "":
            messagebox.showerror("ATTENTION","YOU'RE MUST TO INSERT DATA")
        else:
            cur.execute('INSERT INTO PATIENTS(patientName, patientSurname, dateOfBirthPatient,patientAdress) values(?,?,?,?)',(Name,Surname,BirthDay,Adres))
            con.commit()
            messagebox.showinfo("SUCCESS","{} is registered!".format(Name))
    
    def UpdatePatients(id,patientName, patientSurname, dateOfBirthPatient,patientAdress):
        id = int(id)
        if id < 1:
            messagebox.showwarning("Attention",
                "You Must Be Select Patients")
        else:
            updateQuery="""UPDATE PATIENTS SET patientName=?,patientSurname=?,dateOfBirthPatient =?,patientAdress=? WHERE id=?"""
            setValues =(patientName,patientSurname,dateOfBirthPatient,patientAdress,id)
            con.execute(updateQuery,setValues)
            con.commit()
            messagebox.showinfo("Success","{} is Updated.".format(patientName))
            return True
        
    def GetPatients():
        cur.execute("SELECT * FROM PATIENTS")
        data=cur.fetchall()
        return data

    def deletePatients(id,PatientsName):
        id = int(id)
        if id < 1:
            messagebox.showwarning("Attention",
                "You Must Be Select Patients")
        else: 
            MsgBox = messagebox.askquestion("Attention!","You Want to Delete Doctor {} ?".format(PatientsName),icon='warning')
            if MsgBox == 'yes':
                cur.execute ("DELETE FROM PATIENTS WHERE id=?",(id,))
                con.commit()
                messagebox.showinfo("Success","{} is deleted.".format(PatientsName))
                return True

class NewInspection():
    def saveInspection(idPatients,idDoctors1,dateOfAdmission,costOfAdmission):
        try: 
            idPatients = int(idPatients)
            idDoctors1 = int(idDoctors1)
            if idPatients < 1:
                messagebox.ERROR("Attention","You must be select patient")
            if idDoctors1 < 1:
                messagebox.ERROR("Attention","You must be select doctor")

            else:    
             cur.execute ("INSERT INTO HISTORYOFPATENTS(idPatients,idDoctors1,dateOfAdmission,costOfAdmission) values (?,?,?,?);",(idPatients,idDoctors1,dateOfAdmission,costOfAdmission))
             con.commit()
             messagebox.showinfo("Success","Rezervation Is Registered!")
             return True
        except:
            messagebox.showerror("Attention","You must be select patient or doctor")
    def UpdateInspection(idPatients,idDoctors1,dateOfAdmission,reservationDate,costOfAdmission):
        idPatients = int(idPatients)
        if idPatients < 1:
            messagebox.showwarning("Attention",
                "You Must Be Select Patients")
        else:
            updateQuery="""UPDATE PATIENTS SET idDoctors1=?,dateOfAdmission=?,reservationDate =?,costOfAdmission=? WHERE id=?"""
            setValues =(idDoctors1,dateOfAdmission,reservationDate,costOfAdmission,idPatients)
            con.execute(updateQuery,setValues)
            con.commit()
            messagebox.showinfo("Success","Rezervation is Updated.")
            return True
        
    def GetInspection():
        cur.execute("SELECT * FROM HISTORYOFPATENTS")
        data=cur.fetchall()
        return data

    def DeleteInspection(id):
        id = int(id)
        if id < 1:
            messagebox.showwarning("Attention",
                "You Must Be Select Patients")
        else: 
            MsgBox = messagebox.askquestion("Attention!","You Want to Delete Rezervation?",icon='warning')
            if MsgBox == 'yes':
                cur.execute ("DELETE FROM HISTORYOFPATENTS WHERE id=?",(id,))
                con.commit()
                messagebox.showinfo("Success","Rezervation is deleted.")
                return True
    def selectDoctor(id):
        cur.execute("SELECT name FROM DOCTORS WHERE id=?",(id,))
        data=cur.fetchall()
        return data[0][0]
    def selectPatients(id):
        cur.execute("SELECT patientName FROM PATIENTS WHERE id=?",(id,))
        data=cur.fetchall()
        return data[0][0]
    
  
    def makePrice(costOfAdmission,costfOfReception):
       costfOfReception = int(costfOfReception)
       costOfAdmission=int(costOfAdmission) 
       price = costOfAdmission
       Percentage = (costOfAdmission * costfOfReception) / 100
       price += (Percentage*0.13)
       return price