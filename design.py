from tkinter import *
from tkinter import font,ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
import model
import controller
import pandas
from datetime import date


model.autoCreateTable()
root = Tk()
root.title(string=None)
root.title('KHARKIV HOSPITAL')




class Doctors():
    
    def New_Create_Doctor():
        newWindow = tk.Toplevel(root)
        newWindow.geometry("350x300")
        newWindow.title("Create New Doctor")
        #Doctor Name
        doctor_name_label=Label(newWindow,text="Doctor Name: ")
        doctor_name_label.pack()
        doctor_name=Entry(newWindow,width=50)
        doctor_name.pack()
        #Doctor Specialty
        doctor_speciality_label=Label(newWindow,text="Specialty: ")
        doctor_speciality_label.pack()
        doctor_speciality=Entry(newWindow,width=50)
        doctor_speciality.pack()
        #Cost Of Admission
        Cost_Of_Admission_label=Label(newWindow,text="Cost: ")
        Cost_Of_Admission_label.pack()
        Cost_Of_Admission=Entry(newWindow,width=50)
        Cost_Of_Admission.pack()
        
        #Name Of The Reception
        
        Name_Of_The_Reception_label=Label(newWindow,text="Reception Name: ")
        Name_Of_The_Reception_label.pack()
        Name_Of_The_Reception=Entry(newWindow,width=50)
        Name_Of_The_Reception.pack()
        
        #Percenteage
        
        Percentage_label=Label(newWindow,text="Percentage: ")
        Percentage_label.pack()
        Percentage=Entry(newWindow,width=50)
        Percentage.pack()

        
        def click():
            DataDoctorName=doctor_name.get()
            DataSpeciality=doctor_speciality.get()
            DataCost=Cost_Of_Admission.get()
            DataReception=Name_Of_The_Reception.get()
            DataPercentage=Percentage.get()
            if controller.Doctor.saveDoctor(DataDoctorName,DataSpeciality,DataCost,DataReception,DataPercentage) == True:
                doctor_name.delete(0,END)
                doctor_speciality.delete(0,END)
                Cost_Of_Admission.delete(0,END)
                Name_Of_The_Reception.delete(0,END)
                Percentage.delete(0,END)
            
        #Save Button
        RegisterDoctor = Button(newWindow,text="Save Doctor", command=click)
        RegisterDoctor.pack()

    def Update_Delete_Doctor():
        newWindow = tk.Toplevel(root)
        newWindow.title(string=None)
        newWindow.title('DOCTORS')
        tree_frame = Frame(newWindow)
        tree_frame.pack(pady=20)
         #Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)
        tree = ttk.Treeview(tree_frame, column=("ID", "Name", "Specialty","Cost","Reception","Percentage"), show='headings', height=5,yscrollcommand=tree_scroll.set)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Specialty")
        
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Cost")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Reception")
        tree.column("# 6", anchor=CENTER)
        tree.heading("# 6", text="Percentage")
        # Insert the data in Treeview widget
        #DataDoctors
        data=controller.Doctor.getDoctor()
        for datas in data:
            tree.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5]))

        tree.pack(padx=0.4, pady=0.2)

        #Configure the scrollbar
        tree_scroll.config(command=tree.yview)
        #Doctor ID
        doctor_id = Label(newWindow,text=0)
        doctor_id.pack()
        #Doctor Name
        doctor_name_label=Label(newWindow,text="Doctor Name: ")
        doctor_name_label.pack()
        doctor_name=Entry(newWindow,width=50)
        doctor_name.pack()
        #Doctor Specialty
        doctor_speciality_label=Label(newWindow,text="Specialty: ")
        doctor_speciality_label.pack()
        doctor_speciality=Entry(newWindow,width=50)
        doctor_speciality.pack()
        #Cost Of Admission
        Cost_Of_Admission_label=Label(newWindow,text="Cost: ")
        Cost_Of_Admission_label.pack()
        Cost_Of_Admission=Entry(newWindow,width=50)
        Cost_Of_Admission.pack()
        
        #Name Of The Reception
        
        Name_Of_The_Reception_label=Label(newWindow,text="Reception Name: ")
        Name_Of_The_Reception_label.pack()
        Name_Of_The_Reception=Entry(newWindow,width=50)
        Name_Of_The_Reception.pack()
        
        #Percenteage
        
        Percentage_label=Label(newWindow,text="Percentage: ")
        Percentage_label.pack()
        Percentage=Entry(newWindow,width=50)
        Percentage.pack()
        #Send the information model for updateing proccess
        def Update():
            DataDoctorid=doctor_id['text']
            
            DataDoctorName=doctor_name.get()
            DataSpeciality=doctor_speciality.get()
            DataCost=Cost_Of_Admission.get()
            DataReception=Name_Of_The_Reception.get()
            DataPercentage=Percentage.get()
            
            if controller.Doctor.updateDoctor(DataDoctorid,DataDoctorName,DataSpeciality,DataCost,DataReception,DataPercentage) == True:
                        
                doctor_id['text']="0"
                doctor_name.delete(0,END)
                doctor_speciality.delete(0,END)
                Cost_Of_Admission.delete(0,END)
                Name_Of_The_Reception.delete(0,END)
                Percentage.delete(0,END)
       
        def DeleteDoctor():
            DataDoctorid=doctor_id['text']
            DataDoctorName=doctor_name.get()
           
            
            if controller.Doctor.deleteDoctors(DataDoctorid,DataDoctorName)==True:
                DataDoctorid=str(doctor_id)
                doctor_id['text']="0"
                doctor_name.delete(0,END)
                doctor_speciality.delete(0,END)
                Cost_Of_Admission.delete(0,END)
                Name_Of_The_Reception.delete(0,END)
                Percentage.delete(0,END)
                tree.delete(*tree.get_children())
                data=controller.Doctor.getDoctor()
                for datas in data:
                      tree.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5]))

                tree.pack(padx=0.4, pady=0.2)

           
            
           # controller.Doctor.updateDoctor(DataDoctorid)
        def select_record():
          #  doctor_id.deletecommand(0,END)
            doctor_name.delete(0,END)
            doctor_speciality.delete(0,END)
            Cost_Of_Admission.delete(0,END)
            Name_Of_The_Reception.delete(0,END)
            Percentage.delete(0,END)

            selected = tree.focus()
            values = tree.item(selected,'values')
            doctor_id['text']=values[0]
            doctor_name.insert(0,values[1])
            doctor_speciality.insert(0,values[2])
            Cost_Of_Admission.insert(0,values[3])
            Name_Of_The_Reception.insert(0,values[4])
            Percentage.insert(0,values[5])
            
        SelectData=Button(newWindow,text="Select Doctor",command=select_record)
        SelectData.pack()
        #Save Button
        UpdateDoctor = Button(newWindow,text="Update Doctor", command=Update)
        UpdateDoctor.pack()
        DeleteDoctor = Button(newWindow, text="Delete Doctor",command=DeleteDoctor)
        DeleteDoctor.pack()
class Patients():
    def NewPatients():
        body = MainMenu.body_frame
        newWindow = tk.Toplevel(body)
        newWindow.geometry("350x400")
        newWindow.title(string=None)
        newWindow.title('Patients')
        #Patients Name
        patients_name_label=Label(newWindow,text="Name: ")
        patients_name_label.pack()
        patients_name=Entry(newWindow,width=50)
        patients_name.pack()
        #Patients Surname
        patients_surname_label=Label(newWindow,text="Surname: ")
        patients_surname_label.pack()
        patients_surname=Entry(newWindow,width=50)
        patients_surname.pack()
        #Patients Birtday
        date_of_birth_label=Label(newWindow,text="Birthday: ")
        date_of_birth_label.pack()
        date_of_birth = Calendar(newWindow, selectmode="day",year=2021,month=11,day=21)
        date_of_birth.pack()
        #date_of_birth=Entry(newWindow,width=50)
        #date_of_birth.pack()
        
        #Patients Adress
        
        patients_adress_label=Label(newWindow,text="Adress: ")
        patients_adress_label.pack()
        patients_adress=Entry(newWindow,width=50)
        patients_adress.pack()
        
        

        
        def click():
            DataPatientsName=patients_name.get()
            DataPatientsSurname=patients_surname.get()
            DataBirthDay=date_of_birth.get_date()
            DataPatientsAdress=patients_adress.get()
            if controller.Patients.SavePatients(DataPatientsName,DataPatientsSurname,DataBirthDay,DataPatientsAdress) == True:
                patients_name.delete(0,END)
                patients_surname.delete(0,END)
                date_of_birth._reset_day(0,END)
                patients_adress.delete(0,END)
                
            
        #Save Button
        RegisterPatients = Button(newWindow,text="Save Patients",command=click)
        RegisterPatients.pack()

        
    def Update_Delete_Patients():
        newWindow = tk.Toplevel(root)
        newWindow.title(string=None)
        newWindow.title('PATIENTS')
        tree_frame = Frame(newWindow)
        tree_frame.pack(pady=20)
         #Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)
        tree = ttk.Treeview(tree_frame, column=("ID", "Name", "Surname","Birthday","Adress"), show='headings', height=5,yscrollcommand=tree_scroll.set)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Surname")
        
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Birthday")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Adress")
        # Insert the data in Treeview widget
        #DataDoctors
        data=controller.Patients.GetPatients()
        for datas in data:
            tree.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))

        tree.pack(padx=0.4, pady=0.2)

        #Configure the scrollbar
        tree_scroll.config(command=tree.yview)
        #Patients ID
        Patients_id = Label(newWindow,text=0)
        Patients_id.pack()
        #Patients Name
        patients_name_label=Label(newWindow,text="Name: ")
        patients_name_label.pack()
        patients_name=Entry(newWindow,width=50)
        patients_name.pack()
        #Patients Surname
        patients_surname_label=Label(newWindow,text="Surname: ")
        patients_surname_label.pack()
        patients_surname=Entry(newWindow,width=50)
        patients_surname.pack()
        #Patients Birtday
        date_of_birth_label=Label(newWindow,text="Birthday: ")
        date_of_birth_label.pack()
        date_of_birth = DateEntry(newWindow, selectmode="day",year=2021,month=11,day=21)
        date_of_birth.pack()
        #date_of_birth=Entry(newWindow,width=50)
        #date_of_birth.pack()
        
        #Patients Adress
        
        patients_adress_label=Label(newWindow,text="Adress: ")
        patients_adress_label.pack()
        patients_adress=Entry(newWindow,width=50)
        patients_adress.pack()
        
        #Send the information model for updateing proccess
        def Update():
            DataPatientsid=Patients_id['text']
            
            DataPatientsName=patients_name.get()
            DataPatientsSurname=patients_surname.get()
            DataBirthDay=date_of_birth.get_date()
            DataPatientsAdress=patients_adress.get()
            
            if controller.Patients.UpdatePatients(DataPatientsid,DataPatientsName,DataPatientsSurname,DataBirthDay,DataPatientsAdress) == True:
                        
                Patients_id['text']="0"
                patients_name.delete(0,END)
                patients_surname.delete(0,END)
                #date_of_birth.set_date()
                tree.delete(*tree.get_children())
                patients_adress.delete(0,END)
                data=controller.Patients.GetPatients()
                for datas in data:
                      tree.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))

                tree.pack(padx=0.4, pady=0.2)
       
        def DeleteDoctor():
            DataPatientsid=Patients_id['text']            
            DataPatientsName=patients_name.get()
           
            
            if controller.Patients.deletePatients(DataPatientsid,DataPatientsName)==True:
                DataPatientsid=str(Patients_id)
                Patients_id['text']="0"
                patients_name.delete(0,END)
                patients_surname.delete(0,END)
                patients_adress.delete(0,END)
                tree.delete(*tree.get_children())
                data=controller.Patients.GetPatients()
                for datas in data:
                      tree.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))

                tree.pack(padx=0.4, pady=0.2)

           
            
           # controller.Doctor.updateDoctor(DataDoctorid)
        def select_record():
          #  doctor_id.deletecommand(0,END)
            Patients_id['text']="0"
            patients_name.delete(0,END)
            patients_surname.delete(0,END)
            patients_adress.delete(0,END)

            selected = tree.focus()
            values = tree.item(selected,'values')
            Patients_id['text']=values[0]
            patients_name.insert(0,values[1])
            patients_surname.insert(0,values[2])
            date_of_birth.set_date(values[3])
            patients_adress.insert(0,values[4])
           
            
        SelectData=Button(newWindow,text="Select Patient",command=select_record)
        SelectData.pack()
        #Save Button
        UpdateDoctor = Button(newWindow,text="Update Patient", command=Update)
        UpdateDoctor.pack()
        DeleteDoctor = Button(newWindow, text="Delete Patient",command=DeleteDoctor)
        DeleteDoctor.pack()

class Inspection():
    def newInspection():
        newWindow = tk.Toplevel(root)
        newWindow.title('New Inspection')
        newWindow.geometry("1290x650")
        #Table Doctors
        left_frame = Frame(newWindow,bg='#212121')
        left_frame.place(relx=0.01, rely=0.01) 
        TextDoctor = Label(left_frame,text="DOCTORS")
        TextDoctor.pack()   
        tree_scroll = Scrollbar(left_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)
        Doctor = ttk.Treeview(left_frame, column=("ID", "Name", "Specialty","Cost","Reception","Percentage"), show='headings', height=5,yscrollcommand=tree_scroll.set)
        Doctor.column("# 1", anchor=CENTER)
        Doctor.heading("# 1", text="ID")
        Doctor.column("# 2", anchor=CENTER)
        Doctor.heading("# 2", text="Name")
        Doctor.column("# 3", anchor=CENTER)
        Doctor.heading("# 3", text="Specialty")
        
        Doctor.column("# 4", anchor=CENTER)
        Doctor.heading("# 4", text="Cost")
        Doctor.column("# 5", anchor=CENTER)
        Doctor.heading("# 5", text="Reception")
        Doctor.column("# 6", anchor=CENTER)
        Doctor.heading("# 6", text="Percentage")
        # Insert the data in Treeview widget
        #DataDoctors
        data=controller.Doctor.getDoctor()
        for datas in data:
            Doctor.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5]))

        Doctor.pack(padx=0.4, pady=0.2)

        #Configure the scrollbar
        tree_scroll.config(command=Doctor.yview)

        #Right Frame
        Right_frame = Frame(newWindow,bg='#212121')
        Right_frame.place(relx=0.01, rely=0.30)   
        TextPatients = Label(Right_frame,text="PATIENTS")
        TextPatients.pack()  
        #Patients Data Column Start Here
        tree_scroll = Scrollbar(Right_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)
        Patients = ttk.Treeview(Right_frame, column=("ID", "Name", "Surname","Birthday","Adress"), show='headings', height=5,yscrollcommand=tree_scroll.set)
        Patients.column("# 1", anchor=CENTER)
        Patients.heading("# 1", text="ID")
        Patients.column("# 2", anchor=CENTER)
        Patients.heading("# 2", text="Name")
        Patients.column("# 3", anchor=CENTER)
        Patients.heading("# 3", text="Surname")
        
        Patients.column("# 4", anchor=CENTER)
        Patients.heading("# 4", text="Birthday")
        Patients.column("# 5", anchor=CENTER)
        Patients.heading("# 5", text="Adress")
        # Insert the data in Treeview widget
        #DataPatients
        data=controller.Patients.GetPatients()
        for datas in data:
            Patients.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))

        Patients.pack(padx=0, pady=1)

        #Configure the scrollbar
        tree_scroll.config(command=Patients.yview)

        #Information About Selected Doctors
        InformationDoctor= Frame(newWindow)
        InformationDoctor.place(relx=0.01,rely=0.60)
        HeadlineDoctor=Label(InformationDoctor,text="DOCTORS INFORMATION")
        HeadlineDoctor.pack()
        Doctorid=Label(InformationDoctor,text=0)
        Doctorid.pack()
        Doctorname=Label(InformationDoctor)
        Doctorname.pack()
        DoctorSpecialty=Label(InformationDoctor)
        DoctorSpecialty.pack()
        Cost=Label(InformationDoctor)
        Cost.pack()
        Reservation=DateEntry(InformationDoctor)
        Reservation.pack()
        #Information About Selected Patients
        InformationPatients= Frame(newWindow)
        InformationPatients.place(relx=0.16,rely=0.60)
        HeadlinePatients = Label(InformationPatients,text="PATIENTS INFORMATION")
        HeadlinePatients.pack()
        Patientsid=Label(InformationPatients,text=0)
        Patientsid.pack()
        Patientsname=Label(InformationPatients)
        Patientsname.pack()
        PatientsBirthday=Label(InformationPatients)
        PatientsBirthday.pack()
        PatientsAdress=Label(InformationPatients)
        PatientsAdress.pack()

        def select_record():
          #  doctor_id.deletecommand(0,END)
            Doctorid['text']="0"

            selected = Doctor.focus()
            values = Doctor.item(selected,'values')
            Doctorid['text']=values[0]
            Doctorname['text']=values[1]
            DoctorSpecialty['text']=values[2]
            Cost['text']=controller.NewInspection.makePrice(values[3],values[5]) 
            

            SelecetedPatients = Patients.focus()
            PatientsValues = Patients.item(SelecetedPatients,'values')
            Patientsid['text']=PatientsValues[0]
            Patientsname['text']=PatientsValues[1]
            PatientsBirthday['text']=PatientsValues[2]
            PatientsAdress['text']=PatientsValues[3]

        
       
        def click():
            DataPatientId=Patientsid['text']
            DataDoctorId=Doctorid['text']
            DataDate=Reservation.get_date()
            DataCost=Cost['text']
            if controller.NewInspection.saveInspection(DataPatientId,DataDoctorId,DataDate,DataCost) == True:
                Doctorid['text']='0'
                Doctorname['text']=''
                DoctorSpecialty['text']=''
                Cost['text']='' 
                #Data Revreshing
                Patients.delete(*Patients.get_children())
                data=controller.Patients.GetPatients()
                for datas in data:
                    Patients.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))
                Patientsid['text']='0'
                Patientsname['text']=''
                PatientsBirthday['text']=''
                PatientsAdress['text']=''

        FrameButtons = Frame(newWindow)
        FrameButtons.place(relx=0.01,rely=0.82)
        SelectData=Button(FrameButtons,text="Select",command=select_record)
        SelectData.pack() 
        #Save Button
        RegisterPatients = Button(FrameButtons,text="Save Patients",command=click)
        RegisterPatients.pack()

        
    def Delete_Patients():
       newWindow = tk.Toplevel(root)
       newWindow.title('Delete Inspection')
       newWindow.geometry("1000x450")
      
       Patients = ttk.Treeview(newWindow, column=("ID","Patients", "DOCTORS", "Date","Cost"), show='headings', height=5)
       Patients.column("# 1", anchor=CENTER)
       Patients.heading("# 1", text="ID")
       Patients.column("# 2", anchor=CENTER)
       Patients.heading("# 2", text="Patients")
       Patients.column("# 3", anchor=CENTER)
       Patients.heading("# 3", text="DOCTORS")
       Patients.column("# 4", anchor=CENTER)
       Patients.heading("# 4", text="Date")   
       Patients.column("# 5", anchor=CENTER)
       Patients.heading("# 5", text="Cost")   
       # Insert the data in Treeview widget
       datas = controller.NewInspection.GetInspection()
       for data in datas:
           Patients.insert('', 'end', text="1", values=(data[0],controller.NewInspection.selectPatients(data[1]),controller.NewInspection.selectDoctor(data[2]), data[3],data[4]))
       Patients.pack()   
       
       #Send the information model for updateing proccess
       
      
       
       def DeletePatients():
            selected = Patients.focus()
            values = Patients.item(selected,'values')
            PatientID=values[0]
            
            if controller.NewInspection.DeleteInspection(PatientID) == True:
                Patients.delete(*Patients.get_children())
                data=controller.Patients.GetPatients()
                for datas in data:
                      Patients.insert('', 'end', text="1", values=(datas[0],datas[1],datas[2],datas[3],datas[4]))
               

           
            
       
            
       
       DeletePatients = Button(newWindow, text="Delete Patient",command=DeletePatients)
       DeletePatients.pack()

class Export():
    today = date.today()
    def ExportDoctors():
       
        data = pandas.DataFrame(controller.Doctor.getDoctor(),columns=['ID','Name','Specialty','Cost','Reception','Percentage'])
        dataToExcel = pandas.ExcelWriter("Data-Doctor {0}.xlsx".format(Export.today), engine='xlsxwriter')
        data.to_excel(dataToExcel)
        dataToExcel.save()
    
    def ExportPatients():
        data = pandas.DataFrame(controller.Patients.GetPatients(),columns=['ID','Name','Surname','Birthday','Adress'])
        dataToExcel = pandas.ExcelWriter("Data-Patients {0}.xlsx".format(Export.today), engine='xlsxwriter')
        data.to_excel(dataToExcel)
        dataToExcel.save()

    """def ExportHistory():
        PatientsName = []
        DoctorsName = []
        DataTime=[]
        DataCost=[]
        
        allData = controller.NewInspection.GetInspection()
        for i in allData:
            
            PatientsName.append(controller.NewInspection.selectPatients(i[1]))
            DoctorsName.append(controller.NewInspection.selectDoctor(i[2]))
            DataTime.append(i[3])
            DataCost.append(i[4])
            
            
        data = pandas.DataFrame( columns=['Patients','Doctors','Date','Cost',PatientsName,DoctorsName,DataTime,DataCost])
        dataToExcel = pandas.ExcelWriter("Data-Patients-History-{0}.xlsx".format(Export.today), engine='xlsxwriter')
        data.to_excel(dataToExcel)
        dataToExcel.save()"""
class MainMenu():
  canvas = Canvas(root, height=450, width=750)
  canvas.pack()
  #for make a menu 
  menu=Menu(root)
  root.config(menu=menu)

  #Menu Doctor  Start
  Doctor_Menu=Menu(menu)
  Doctor_Menu.add_command(label="New Doctor",command=Doctors.New_Create_Doctor)
  Doctor_Menu.add_command(label="Update/Delete Doctor",command=Doctors.Update_Delete_Doctor)
  
  menu.add_cascade(label="Doctor", menu=Doctor_Menu)
  #Menu Doctor End

  #Menu Patients  Start
  Patients_Menu=Menu(menu)
  Patients_Menu.add_command(label="New Patient",command=Patients.NewPatients)
  Patients_Menu.add_command(label="Update/Delete Patient",command=Patients.Update_Delete_Patients)
  
  menu.add_cascade(label="Patient", menu=Patients_Menu)
  #Menu Patients End
  
  #Menu Patients History  Start
  Patients_Menu=Menu(menu)
  Patients_Menu.add_command(label="New Inspection ",command=Inspection.newInspection)
  Patients_Menu.add_command(label="Delete Inspection ",command=Inspection.Delete_Patients)
  
  menu.add_cascade(label="Inspection", menu=Patients_Menu)
  #Menu Patients Historys End

  #Menu Export  Start
  Export_Menu=Menu(menu)
  Export_Menu.add_command(label="Export Doctor Data ",command=Export.ExportDoctors)
  Export_Menu.add_command(label="Export Patients Data ",command=Export.ExportPatients)
  #Export_Menu.add_command(label="Export History Data ",command=Export.ExportHistory)
  
  menu.add_cascade(label="Export", menu=Export_Menu)
  #Menu Export End
  
  #TOP FRAME START
  top_frame = Frame(root,bg='#212121')
  top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
  MyName = Label(top_frame,text="Hamit AVSAR",bg='white',font="Verdana 12 bold")
  MyName.pack(padx=0.4, pady=0.2, side=RIGHT)
  
  
  #TOP FRAME END

  #BODY START
  body_frame=Frame(root,bg='#323232')
  body_frame.place(relx=0, rely=0.1,relheight=1,relwidth=1)
  sayHi=Label(body_frame,text="HEY! TODAY YOU ARE LOOKING SO BEAUTIFUL!", font="Arial 14 bold ")
  sayHi.pack(pady=150)
  #BODY END
  



root.mainloop()
