from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from PIL import ImageTk, Image
    import sklearn
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    import sqlite3

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title(" Classification of Cardiac Arrhythmia using SVM")
    root.configure(background="#B8E2F2")
    
    image2 = Image.open('10.jpg')
    image2 = image2.resize((1400, 800), Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=500, y=0) 
  
    
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
        root.configure(background="white")
       
        
        
        
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
           yes = tk.Label(root,text=" Your Result : \n\n VEB(Ventricular ectopic beat. \n\n___Remedies___\n * The best ways to prevent tachycardia are to maintain\n a healthy heart and prevent heart disease.\nIf you already have heart disease, monitor it and follow your treatment plan.\n Be sure youunderstand your treatment plan, and take all medications as prescribed. \nTake the following steps to keep the heart healthy:Eat a balanced, nutritious diet.\n A diet low in saturated and trans fats and rich in fruits, vegetables and whole grains helps keep the heart healthy.\n Exercise and maintain a healthy weight. \nBeing overweight increases the risk of developing heart disease.\n As a general goal, aim for at least 30 minutes of moderate exercise every day.\n Control blood pressure and cholesterol levels.\n Make lifestyle changes and take medicationsasprescribed to manage high blood pressure (hypertension) or high cholesterol.\n Control stress.\n Avoid unnecessary stress and learn strategies to manage and reduce stress.\n Don't use illegal drugs. Don't use stimulants, such as cocaine.\n If you need help stopping drug use or misuse, talk to your health care provider about an appropriate programfor you. \nGo to scheduled health checkups.\n Have regular physical exams and report any newsignsor symptoms to your health care provider.\n Limit alcohol.\n If you choose to drink alcohol, do so in moderation. \nFor healthy adults, that means up to one drink a day for women and up to two drinks a day for men. \nSome peoplemayneed to avoid alcohol entirely.\n Ask your health care provider how much alcohol, if any, is safefor you. \nLimit caffeine. If you drink caffeinated beverages, do so in moderation (no more than 1to2beverages daily).\n Stop smoking.\n If you smoke and can't quit on your own, talk to your health care provider about strategies or programs to help you break a smoking habit.\n Use over-the-counter medications with caution. \nSome cold and cough medications containstimulants that may increase the heart rate.\n Always tell your health care provider about themedications you take, including those bought without a prescription.",background="powder blue",foreground="white",font=('times', 20, ' bold '),width=30)
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
           yes = tk.Label(root,text="Your Result :\n\n N(Normal Beat). \n\n___Remedies___\n To avoid the triggers that \n cause the symptoms. Reduce stress.\n Try relaxation techniques,\n such as meditation, yoga or deep \n  breathing. Avoid stimulants.",background="powder blue",foreground="white",font=('times', 20, ' bold '),width=30)
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
              yes = tk.Label(root,text="Your Result :\n \n Fusion Beat \n___Remedies___\n Fusion Beat also known as Capture Beat occurs when a supraventricular and a ventricular impulse coincide to produce a hybrid complex.\n To maintain a healthy heart and prevent heart disease\n Take the following steps to keep the heart healthy: Stop smoking.\n If you smoke and can't quit on your own, talk to your health care provider about strategies or programs to help you break a smoking habit.\n Use over-the-counter medications with caution.\n Exercise and maintain a healthy weight.\n Being overweight increases the risk of developingheart disease.\n As a general goal, aim for at least 30 minutes of moderate exercise every day.\n Control blood pressure and cholesterol levels.\n Make lifestyle changes and take medicationsasprescribed to manage high blood pressure (hypertension) or high cholesterol.\n Control stress.\n If you need help stoppingdruguse or misuse, talk to your health care provider about an appropriate program for you.\n Go to scheduled health checkups.\n Have regular physical exams and report any new signsor symptoms to your health care provider.\n Limit alcohol.\n Limit caffeine.\n If you drink caffeinated beverages, do so in moderation (no more than 1 to 2 beverages daily).\n Some cold and cough medications containstimulants that may increase the heart rate.\n Always tell your health care provider about themedications you take, including those bought without a prescription.\nEat a balanced, nutritious diet. \nA diet low in saturated and trans fats and rich in fruits, vegetables and whole grains helps keep the heart healthy.\n If you choose to drink alcohol, do so in moderation.\n For healthy adults, thatmeans up to one drink a day for women and up to two drinks a day for men.\n Some peoplemayneed to avoid alcohol entirely.\n Ask your health care provider how much alcohol, if any, is safe for you.\n Avoid unnecessary stress and learn strategies to manage and reduce stress.\n Don't use illegal drugs.\n Don't use stimulants, such as cocaine.",background="powder blue",foreground="white",font=('times', 20, ' bold '),width=30)
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
      
       
            
       
    l1=tk.Label(root,text="record",background="white",font=('times', 20, ' bold '),width=10)
    l1.place(x=100,y=200)
    record=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=record)
    record.place(x=300,y=200)

    l2=tk.Label(root,text="preRR",background="white",font=('times', 20, ' bold '),width=10)
    l2.place(x=100,y=250)
    preRR=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=preRR)
    preRR.place(x=300,y=250)

    l3=tk.Label(root,text="postRR",background="white",font=('times', 20, ' bold '),width=10)
    l3.place(x=100,y=300)
    postRR=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=postRR)
    postRR.place(x=300,y=300)
    
    
    l4=tk.Label(root,text="pPeak",background="white",font=('times', 20, ' bold '),width=10)
    l4.place(x=100,y=350)
    pPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=pPeak)
    pPeak.place(x=300,y=350)

    l5=tk.Label(root,text="tPeak",background="white",font=('times', 20, ' bold '),width=10)
    l5.place(x=100,y=400)
    tPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tPeak)
    tPeak.place(x=300,y=400)

    l6=tk.Label(root,text="rPeak",background="white",font=('times', 20, ' bold '),width=10)
    l6.place(x=100,y=450)
    rPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=rPeak)
    rPeak.place(x=300,y=450)
    
    
    l7=tk.Label(root,text="sPeak",background="white",font=('times', 20, ' bold '),width=10)
    l7.place(x=100,y=500)
    
    sPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sPeak)
    sPeak.place(x=300,y=500)
    
   

    l8=tk.Label(root,text="qPeak",background="white",font=('times', 20, ' bold '),width=10)
    l8.place(x=100,y=550)
    qPeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qPeak)
    qPeak.place(x=300,y=550)

    l9=tk.Label(root,text="qrs_interval",background="WHITE",font=('times', 20, ' bold '),width=10)
    l9.place(x=100,y=600)
    qrs_interval=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qrs_interval)
    qrs_interval.place(x=300,y=600)
    
    l10=tk.Label(root,text="CARDIAC ARRHYTHMIA",background="#B8E2F2",font=('times', 30),width=22)
    l10.place(x=0,y=50)
    
    l11=tk.Label(root,text="CLASSIFICATION",background="#B8E2F2",font=('times', 30),width=20)
    l11.place(x=25,y=120)

    
    # qrs_interval=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=qPeak)
    # qrs_interval.place(x=500,y=400)
    
    
    # frame_alpr = tk.LabelFrame(root, text="  ", width=750, height=850, bd=5, font=('times', 14, ' bold '),bg="white")
    # frame_alpr.grid(row=0, column=0)
    # frame_alpr.place(x=830, y=0)

    
    
    # logo_label=tk.Label()
    # logo_label.place(x=0,y=55)


   

    button1 = tk.Button(root,text="Submit",command=Detect,bg ="red", fg = "white",font=('times', 20, ' bold '),width=20)
    button1.place(x=80,y=700)


    root.mainloop()

Train()