from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    import sklearn
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    import sqlite3

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title(" Classification of Cardiac Arrhythmia using SVM")
    root.configure(background="LightSkyBlue")
    
    record= tk.IntVar()
    preRR= tk.IntVar()
    postRR = tk.IntVar()
    pPeak = tk.IntVar()
    tPeak= tk.IntVar()
    rPeak = tk.IntVar()
    sPeak =  tk.IntVar()
    qPeak = tk.IntVar()
    qrs_interval = tk.IntVar()


    
    
    #===================================================================================================================



    def Detect():
        root = tk.Tk()

        root.geometry("800x850+250+5")
        root.title(" Classification of Cardiac Arrhythmia using SVM")
        root.configure(background="purple")
       
        
        
        
        e1=record.get()
        print(e1)
        e2=preRR.get()
        print(e2)
        e3=postRR.get()
        print(e3)
        e4=pPeak.get()
        print(e4)
        e5=tPeak.get()
        print(e5)
        e6=rPeak.get()
        print(e6)
        e7=sPeak.get()
        print(e7)
        e8=qPeak .get()
        print(e8)
        e9=qrs_interval.get()
        print(e9)
        
        sqliteConnection = sqlite3.connect('evaluation1.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
       
        f1=open("id.txt","r")
        id=f1.read()
        print("ID", id)
        f1.close()
    
        
        #########################################################################################
        
       
        from joblib import dump , load
        a1=load('D:\Cardiac_Final\cardiac arrythmia final code\cardiac arrythmia final code\card_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9]])
        print(v)
    
        if v[0]=='VEB':
           print("VEB(Ventricular ectopic beat)")
           yes = tk.Label(root,text=" Your Result : \n\n VEB(Ventricular ectopic beat. \n\n___Remedies___\n * Medication usually a beta blocker \n  or a calcium channel blocker \n * Help to control the area sending out the \n extra heart beats and improve symptoms.",background="purple",foreground="white",font=('times', 20, ' bold '),width=30)
           yes.place(x=500,y=50)
           
           sqliteConnection = sqlite3.connect('evaluation.db')
           #cursor = sqliteConnection.cursor()
           print("Connected to SQLite")
           
           r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
          #cursor.execute(sql_fetch_blob_query, (id))
           print(r_set)
           i=0
           for row in r_set:
              print("id=",row[0],)
              b=row[0]
              print(b)
              r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
              with open(r"report.txt", 'w') as f:
                  for row in r_set1:
                      line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                      f.write(line)
                      print(row[0],row[1],row[2])
              # for row in r_set1:
              from datetime import date

              today = date.today()
                
              # dd/mm/YY
              d1 = today.strftime("%d/%m/%Y")
              print("d1 =", d1)
              # datetime object containing current date and time
              from datetime import datetime

              now = datetime.now()
                 
              print("now =", now)
              # dd/mm/YY H:M:S
              dt_string = now.strftime("%H:%M:%S")
              print("time =", dt_string)
              Name = row[1]
              address = row[2]
              age = row[7]
              result = 'VEB(Ventricular ectopic beat'
              print(Name,address,age,result)
              conn = sqlite3.connect('evaluation.db')
              with conn:
                  cursor = conn.cursor()
                  cursor.execute(
                      'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                      (Name,address,age,result,d1,dt_string))

                  conn.commit()
                  #db.close()
            
                    
           
    
        if v[0]=='N':
           print("N(Normal)")
           yes = tk.Label(root,text="Your Result :\n\n N(Normal Beat). \n\n___Remedies___\n To avoid the triggers that \n cause the symptoms. Reduce stress.\n Try relaxation techniques,\n such as meditation, yoga or deep \n  breathing. Avoid stimulants.",background="purple",foreground="white",font=('times', 20, ' bold '),width=30)
           yes.place(x=500,y=50)
           
           sqliteConnection = sqlite3.connect('evaluation.db')
           #cursor = sqliteConnection.cursor()
           print("Connected to SQLite")
           
           r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
          #cursor.execute(sql_fetch_blob_query, (id))
           print(r_set)
           i=0
           for row in r_set:
              print("id=",row[0],)
              b=row[0]
              print(b)
              r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
              with open(r"report.txt", 'w') as f:
                  for row in r_set1:
                      line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                      f.write(line)
                      print(row[0],row[1],row[2])
              # for row in r_set1:
              from datetime import date

              today = date.today()
                
              # dd/mm/YY
              d1 = today.strftime("%d/%m/%Y")
              print("d1 =", d1)
              # datetime object containing current date and time
              from datetime import datetime

              now = datetime.now()
                 
              print("now =", now)
              # dd/mm/YY H:M:S
              dt_string = now.strftime("%H:%M:%S")
              print("time =", dt_string)
              Name = row[1]
              address = row[2]
              age = row[7]
              result = 'N(Normal)'
              print(Name,address,age,result)
              conn = sqlite3.connect('evaluation.db')
              with conn:
                  cursor = conn.cursor()
                  cursor.execute(
                      'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                      (Name,address,age,result,d1,dt_string))

                  conn.commit()
                  #db.close()
           
        if v[0]=='F':
              print("F (Fusion Beat)")
              yes = tk.Label(root,text="Your Result :\n \n Fusion Beat \n___Remedies___\n Fusion beats are typically benign.\n but can be helpful diagnostically \n such as in cases of ventricular tachycardia.",background="purple",foreground="white",font=('times', 20, ' bold '),width=30)
              yes.place(x=500,y=50)
              
              sqliteConnection = sqlite3.connect('evaluation.db')
              #cursor = sqliteConnection.cursor()
              print("Connected to SQLite")
              
              r_set = sqliteConnection.execute("select * from admin_registration where id =" + str(id) +"");
             #cursor.execute(sql_fetch_blob_query, (id))
              print(r_set)
              i=0
              for row in r_set:
                 print("id=",row[0],)
                 b=row[0]
                 print(b)
                 r_set1 = sqliteConnection.execute("select * from admin_registration where id =" + str(b) +"");
                 with open(r"report.txt", 'w') as f:
                     for row in r_set1:
                         line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-VEB(Ventricular ectopic beat)"#,row[3],row[4],row[5],row[6]
                         f.write(line)
                         print(row[0],row[1],row[2])
                 # for row in r_set1:
                 from datetime import date

                 today = date.today()
                   
                 # dd/mm/YY
                 d1 = today.strftime("%d/%m/%Y")
                 print("d1 =", d1)
                 # datetime object containing current date and time
                 from datetime import datetime

                 now = datetime.now()
                    
                 print("now =", now)
                 # dd/mm/YY H:M:S
                 dt_string = now.strftime("%H:%M:%S")
                 print("time =", dt_string)
                 Name = row[1]
                 address = row[2]
                 age = row[7]
                 result = 'F (Fusion Beat)'
                 print(Name,address,age,result)
                 conn = sqlite3.connect('evaluation.db')
                 with conn:
                     cursor = conn.cursor()
                     cursor.execute(
                         'INSERT INTO record(Username,age,address,result,date,time) VALUES(?,?,?,?,?,?)',
                         (Name,address,age,result,d1,dt_string))

                     conn.commit()
                     #db.close()
      
    
    frame_alpr = tk.LabelFrame(text="", width=800, height=700, bd=5, font=('times', 14, ' bold '),bg="LightSkyBlue")
    frame_alpr.grid(row=9, column=9)
    frame_alpr.place(x=430, y=30)       
       
    l1=tk.Label(root,text="record",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l1.place(x=500,y=50)
    record=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=record)
    record.place(x=1000,y=50)

    l2=tk.Label(root,text="preRR",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l2.place(x=500,y=100)
    preRR=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=preRR)
    preRR.place(x=1000,y=100)

    l3=tk.Label(root,text="postRR",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l3.place(x=500,y=150)
    postRR=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=postRR)
    postRR.place(x=1000,y=150)
    
    
    l4=tk.Label(root,text="pPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l4.place(x=500,y=200)
    pPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=pPeak)
    pPeak.place(x=1000,y=200)

    l5=tk.Label(root,text="tPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l5.place(x=500,y=250)
    tPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tPeak)
    tPeak.place(x=1000,y=250)

    l6=tk.Label(root,text="rPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l6.place(x=500,y=300)
    rPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=rPeak)
    rPeak.place(x=1000,y=300)
    
    
    l7=tk.Label(root,text="sPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l7.place(x=500,y=350)
    
    sPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sPeak)
    sPeak.place(x=1000,y=350)
    
   

    l8=tk.Label(root,text="qPeak",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l8.place(x=500,y=400)
    qPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qPeak)
    qPeak.place(x=1000,y=400)

    l9=tk.Label(root,text="qrs_interval",background="LightSkyBlue",font=('times', 20, ' bold '),width=25)
    l9.place(x=500,y=450)
    qrs_interval=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qrs_interval)
    qrs_interval.place(x=1000,y=450)

   
    

    
    
    # logo_label=tk.Label()
    # logo_label.place(x=0,y=55)


   

    button1 = tk.Button(root,text="Submit",command=Detect,bg ="red", fg = "white",font=('times', 20, ' bold '),width=10)
    button1.place(x=750,y=600)


    root.mainloop()

Train()