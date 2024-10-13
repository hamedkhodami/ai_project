import webbrowser
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from customtkinter import *

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt




class App(CTkFrame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.Crearewidget()

    def Crearewidget(self):

        #picturs
        self.homePic=PhotoImage(file="pl/form/home.png")
        self.IconHmoe= PhotoImage(file="pl/form/home2.png")
        self.picst1= PhotoImage(file="pl/form/st1.png")
        self.picst2= PhotoImage(file="pl/form/st2.png")
        self.picst3= PhotoImage(file="pl/form/st3.png")
        self.picst4= PhotoImage(file="pl/form/st4.png")
        self.picst5= PhotoImage(file="pl/form/st5.png")





    #labelMainFrame
        self.layer_1=Frame(self.master,width=1125,height=870,background="white")
        self.layer_1.place(x=0,y=0)

        self.mainlabel=Label(self.layer_1,text="پیشبینی قیمت خانه",background="white",font="Calibri 40 bold")
        self.mainlabel.place(x=490,y=250)

        self.piclabel=Label(self.layer_1,image=self.homePic,background="white")
        self.piclabel.place(x=200,y=350)

        #buttenMainFreme
        self.btnPredictAll=CTkButton(self.layer_1, text=" پیش بینی از لیست ", fg_color="black", hover_color="#3627B5",command=self.OPEN_listframe)
        self.btnPredictAll.configure(height=100, width=215, corner_radius=20,font=("Arial",20,"bold") , anchor="center")
        self.btnPredictAll.place(x=450, y=300)

        self.btnPredictOne=CTkButton(self.layer_1, text="پیش بینی به صورت دستی", fg_color="black", hover_color="#C40202",command=self.OPEN_manuallframe)
        self.btnPredictOne.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnPredictOne.place(x=450, y=410)



    #ManuallFrame
        self.manuallframe=Frame(self.layer_1,width=1125,height=870,background="white")
        self.manuallframe.place(x=0,y=0)
        self.manuallframe.place_forget()

        self.backHomeAtManualFrame=Button(self.manuallframe,image=self.IconHmoe,command=self.GoHomeAtManuallFrame,background="white")
        self.backHomeAtManualFrame.place(x=70,y=70)

        #Area
        self.Area_lbl=Label(self.manuallframe,text="مساحت",font="arial 25 bold")
        self.Area_lbl.config(padx=10, pady=10, bg="white")
        self.Area_lbl.place(x=900,y=100)
        self.Area_entry=IntVar()
        self.area_entry=CTkEntry(self.manuallframe,width=200,height=30, textvariable=self.Area_entry, justify=CENTER
                                 ,corner_radius=20,border_color="black",placeholder_text_color="black"
                                 ,bg_color="white",fg_color="white",text_color="black")
        self.area_entry.place(x=500, y=90)

        #Rooms
        self.Rooms_lbl=Label(self.manuallframe,text="تعداد اتاق ها",font="arial 25 bold")
        self.Rooms_lbl.config(padx=10, pady=10, bg="white")
        self.Rooms_lbl.place(x=900,y=170)
        self.Rooms_combo=IntVar()
        self.values_Rooms = self.GetRoomValue()
        self.rooms_combo=CTkComboBox(self.manuallframe,width=200,height=30, variable=self.Rooms_combo,values=self.values_Rooms,
                                     state="readonly", justify="center",font=("Arial",20,"bold"),dropdown_hover_color="#24BA50",border_color="black",
                                     text_color="black",fg_color="white",dropdown_fg_color="white",dropdown_text_color="black",dropdown_font=("Arial",20,"bold"))
        self.rooms_combo.place(x=500, y=150)

        #Floors
        self.Floors_lbl=Label(self.manuallframe,text="طبقه",font="arial 25 bold")
        self.Floors_lbl.config(padx=10, pady=10, bg="white")
        self.Floors_lbl.place(x=900,y=240)
        self.Floors_combo=IntVar()
        self.values_Floors = self.GetFloorValue()
        self.floors_combo=CTkComboBox(self.manuallframe,width=200,height=30, variable=self.Floors_combo,values=self.values_Floors,
                                     state="readonly", justify="center",font=("Arial",20,"bold"),dropdown_hover_color="#24BA50",border_color="black",
                                     text_color="black",fg_color="white",dropdown_fg_color="white",dropdown_text_color="black",dropdown_font=("Arial",20,"bold"))
        self.floors_combo.place(x=500, y=200)

        #Location
        self.Location_lbl=Label(self.manuallframe,text="منطقه",font="arial 25 bold")
        self.Location_lbl.config(padx=10, pady=10, bg="white")
        self.Location_lbl.place(x=900,y=310)
        self.Location_combo=StringVar()
        self.values_Location = ['منطقه یک','منطقه دو','منطقه سه','منطقه چهار','منطقه پنج']
        self.location_combo=CTkComboBox(self.manuallframe,width=200,height=30, variable=self.Location_combo,values=self.values_Location,
                                     state="readonly", justify="center",font=("Arial",20,"bold"),dropdown_hover_color="#24BA50",border_color="black",
                                     text_color="black",fg_color="white",dropdown_fg_color="white",dropdown_text_color="black",dropdown_font=("Arial",20,"bold"))
        self.location_combo.place(x=500, y=250)


        #btns
        #predictbtn
        self.btnPredictInManuallList=CTkButton(self.manuallframe, text="ثبت", fg_color="black", hover_color="#C40202",command=self.ManualPredict)
        self.btnPredictInManuallList.configure(height=50, width=400, corner_radius=20,font=("Arial",20,"bold") , anchor="center")
        self.btnPredictInManuallList.place(x=450, y=300)

        #area1btn
        self.btnShowloc1=CTkButton(self.manuallframe, text="منطقه یک", fg_color="black", hover_color="#C40202",command=self.Showloc1)
        self.btnShowloc1.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnShowloc1.place(x=150, y=100)



        #area2btn
        self.btnShowloc2=CTkButton(self.manuallframe, text="منطقه دو", fg_color="black", hover_color="#C40202",command=self.Showloc2)
        self.btnShowloc2.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnShowloc2.place(x=150, y=200)

        #area3btn
        self.btnShowloc3=CTkButton(self.manuallframe, text="منطقه سه", fg_color="black", hover_color="#C40202",command=self.Showloc3)
        self.btnShowloc3.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnShowloc3.place(x=150, y=300)

        #area4btn
        self.btnShowloc4=CTkButton(self.manuallframe, text="منطقه چهار", fg_color="black", hover_color="#C40202",command=self.Showloc4)
        self.btnShowloc4.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnShowloc4.place(x=150, y=400)

        #area5btn
        self.btnShowloc5=CTkButton(self.manuallframe, text="منطقه پنج", fg_color="black", hover_color="#C40202",command=self.Showloc5)
        self.btnShowloc5.configure(height=100, width=200, corner_radius=20,font=("Arial",20,"bold") ,anchor="center")
        self.btnShowloc5.place(x=150, y=500)

        #framearea1
        self.loc1frame=Label(self.manuallframe,width=1000,height=700,image=self.picst1)
        self.loc1frame.place(x=70,y=70)
        self.loc1frame.place_forget()

        #framearea2
        self.loc2frame=Label(self.manuallframe,width=1000,height=700,image=self.picst2)
        self.loc2frame.place(x=70,y=70)
        self.loc2frame.place_forget()

        #framearea3
        self.loc3frame=Label(self.manuallframe,width=1000,height=700,image=self.picst3)
        self.loc3frame.place(x=70,y=70)
        self.loc3frame.place_forget()

        #framearea4
        self.loc4frame=Label(self.manuallframe,width=1000,height=700,image=self.picst4)
        self.loc4frame.place(x=70,y=70)
        self.loc4frame.place_forget()

        #framearea5
        self.loc5frame=Label(self.manuallframe,width=1000,height=700,image=self.picst5)
        self.loc5frame.place(x=70,y=70)
        self.loc5frame.place_forget()

        #btncloseframe
        self.btnCloseloc1=CTkButton(self.loc1frame, text="x", fg_color="black", hover_color="red",command=self.Closeloc1)
        self.btnCloseloc1.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseloc1.place(x=0, y=0)

        self.btnCloseloc2=CTkButton(self.loc2frame, text="x", fg_color="black", hover_color="red",command=self.Closeloc2)
        self.btnCloseloc2.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseloc2.place(x=0, y=0)

        self.btnCloseloc3=CTkButton(self.loc3frame, text="x", fg_color="black", hover_color="red",command=self.Closeloc3)
        self.btnCloseloc3.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseloc3.place(x=0, y=0)

        self.btnCloseloc4=CTkButton(self.loc4frame, text="x", fg_color="black", hover_color="red",command=self.Closeloc4)
        self.btnCloseloc4.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseloc4.place(x=0, y=0)

        self.btnCloseloc5=CTkButton(self.loc5frame, text="x", fg_color="black", hover_color="red",command=self.Closeloc5)
        self.btnCloseloc5.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseloc5.place(x=0, y=0)






    #listFrame
        self.listframe=Frame(self.layer_1,width=1125,height=870,background="white")
        self.listframe.place(x=0,y=0)
        self.listframe.place_forget()

        self.backHomeAtListFrame=Button(self.listframe,image=self.IconHmoe,command=self.GoHomeAtListFrame,background="white")
        self.backHomeAtListFrame.place(x=50,y=50)


        self.btnShowPlot=CTkButton(self.listframe, text="نمودار رگرسیون", fg_color="black", hover_color="#3627B5", command=self.Show_plot)
        self.btnShowPlot.configure(height=50,width=300,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnShowPlot.place(x=130,y=30)

        self.btnMeanFromCsv=CTkButton(self.listframe,text="میانگین",fg_color="black",hover_color="#3627B5",command=self.Show_mean)
        self.btnMeanFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnMeanFromCsv.place(x=50,y=100)

        self.btnStandardDevaitionFromCsv=CTkButton(self.listframe,text="انحراف معیار",fg_color="black",hover_color="#3627B5",command=self.Show_std_dev)
        self.btnStandardDevaitionFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnStandardDevaitionFromCsv.place(x=170,y=100)

        self.btnVarianceFromCsv=CTkButton(self.listframe,text="واریانس",fg_color="black",hover_color="#3627B5",command=self.Show_variance)
        self.btnVarianceFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnVarianceFromCsv.place(x=320,y=100)

        self.btnMinMaxFromCsv=CTkButton(self.listframe,text="حداکثر و حداقل قیمت",fg_color="black",hover_color="#3627B5",command=self.Shoq_min_max)
        self.btnMinMaxFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnMinMaxFromCsv.place(x=450,y=100)

        self.btnQuartilesFromCsv=CTkButton(self.listframe,text="چارک ها",fg_color="black",hover_color="#3627B5",command=self.Show_quartiles)
        self.btnQuartilesFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnQuartilesFromCsv.place(x=650,y=100)

        self.btnCorrelationFromCsv=CTkButton(self.listframe,text="همبستگی",fg_color="black",hover_color="#3627B5",command=self.Show_correlation)
        self.btnCorrelationFromCsv.configure(height=50,width=100,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnCorrelationFromCsv.place(x=780,y=100)

            #frameCsv
        self.csvframe=Frame(self.listframe,width=950,height=400,background="white")
        self.csvframe.place(x=100,y=250)
        self.csvframe.place_forget()

        self.btnShowdata=CTkButton(self.listframe,text="مشاهده ی مشخصات واحد های آپارتمانی در کرمان",fg_color="black",hover_color="#3627B5",command=self.ShowCsvFrame)
        self.btnShowdata.configure(height=50,width=300,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnShowdata.place(x=450,y=30)

        self.btnshowtblcsv=CTkButton(self.csvframe,text="برای نمایش جدول کلیک کنید",fg_color="white"
                                     ,text_color="black",hover_color="#3627B5",command=self.Show_data)
        self.btnshowtblcsv.configure(height=200,width=200,corner_radius=20,font=("Arial",20,"bold"),anchor="center")
        self.btnshowtblcsv.place(x=250,y=70)

        self.btnCloseCsvFrame=CTkButton(self.csvframe, text="x", fg_color="black", hover_color="red",command=self.CloseCsvFrame)
        self.btnCloseCsvFrame.configure(height=5, width=5, corner_radius=20,anchor="center")
        self.btnCloseCsvFrame.place(x=0, y=0)


        #function

    #mainFrameFunction
    def OPEN_manuallframe(self):
        self.manuallframe.place(x=0,y=0)

    def OPEN_listframe(self):
        self.listframe.place(x=0,y=0)

    def GoHomeAtManuallFrame(self):
        self.manuallframe.place_forget()
        self.layer_1.place(x=0,y=0)

    def GoHomeAtListFrame(self):
        self.listframe.place_forget()
        self.layer_1.place(x=0,y=0)


    #manuallFrameFunction
    def Is_numeric(char):
        return char.isdigit

    def ManualPredict(self):
        area=self.Area_entry.get()
        rooms=self.Rooms_combo.get()
        floor=self.Floors_combo.get()
        location=self.Location_combo.get()
        if not area or not rooms or not floor or not location:
            messagebox.showerror("خطا","لطفا فیلد خالی مورد نظر را پر کنید")
            return
        if area <50 or area > 250:
            messagebox.showerror("خطا در مساحت مورد نظر","مساحت مورد نظر باید بین 50 نا 250 متر مربع باشد")
            return
        def calculate_price(area, rooms, floor, location):
            bas = {
                'منطقه یک': 1000000000,
                'منطقه دو': 5000000000,
                'منطقه سه': 2000000000,
                'منطقه چهار': 3000000000,
                'منطقه پنج': 4000000000
            }
            base_price = bas[location]
            area_factor = (area / 50) * 100000000
            room_factor = rooms * 200000000
            floor_factor = (12 - floor) * 50000000
            return base_price + area_factor + room_factor + floor_factor
        predicted_price=calculate_price(area,rooms,floor,location)
        formated_price = "{:,}".format(int(predicted_price))
        messagebox.showinfo("پیشبینی قیمت با موفقیت انجام شد",f"قیمت پیشبینی شده: {formated_price} تومان ")
        self.Area_entry.set("")
        self.Rooms_combo.set("")
        self.Floors_combo.set("")
        self.Location_combo.set("")


    def GetRoomValue(self):
        counter = []
        for item in range(1,7):
            counter.append(str(item))
        return counter

    def GetFloorValue(self):
        counter = []
        for item in range(1,13):
            counter.append(str(item))
        return counter

    def Showloc1(self):
        self.loc1frame.place(x=70, y=70)

    def Showloc2(self):
        self.loc2frame.place(x=70, y=70)

    def Showloc3(self):
        self.loc3frame.place(x=70, y=70)

    def Showloc4(self):
        self.loc4frame.place(x=70, y=70)

    def Showloc5(self):
        self.loc5frame.place(x=70, y=70)

    def Closeloc1(self):
        self.loc1frame.place_forget()

    def Closeloc2(self):
        self.loc2frame.place_forget()

    def Closeloc3(self):
        self.loc3frame.place_forget()

    def Closeloc4(self):
        self.loc4frame.place_forget()

    def Closeloc5(self):
        self.loc5frame.place_forget()




    #listFrameFunction
    def Show_mean(self):
        df=pd.read_csv("KermanAparteman.csv")
        df['Price']=df['Price'].str.replace(',','').astype(float)
        mean_price=np.mean(df['Price'])
        mean_area=np.mean(df['Area'])
        mean_room=np.mean(df['Rooms'])
        mean_floor=np.mean(df['Floors'])
        messagebox.showinfo("میانگین",f"میانگین قیمت ها:{mean_price}\nمیانگین مساحت ها:{mean_area}\nمیانگین تعداد اتاق ها:{mean_room}\nمیانگین بودن در طبقه ها:{mean_floor}\n")

    def Show_std_dev(self):
        df = pd.read_csv("KermanAparteman.csv")
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        std_dev_price=np.std(df['Price'])
        std_dev_area=np.std(df['Area'])
        messagebox.showinfo("انحراف معیار",f"انحراف معیار فیمت {std_dev_price}\n انحراف معیار  مساحت {std_dev_area} ")


    def Show_variance(self):
        df = pd.read_csv("KermanAparteman.csv")
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        var_price = np.var(df['Price'])
        var_area = np.var(df['Area'])
        messagebox.showinfo("واریانس",f"واریانس قیمت {var_price}\n واریانس  مساحت {var_area} ")



    def Shoq_min_max(self):
        df = pd.read_csv("KermanAparteman.csv")
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        max_price=np.max(df['Price'])
        min_price=np.min(df['Price'])
        messagebox.showinfo("بیشترین و کمترین قیمت",f"حداکثر فیمت {max_price}\n حداقل  قیمت {min_price} ")


    def Show_quartiles(self):
        df = pd.read_csv("KermanAparteman.csv")
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        q1=np.percentile(df['Price'],25)
        q3=np.percentile(df['Price'],75)
        messagebox.showinfo("چارک ها",f"چارک اول قیمت {q1}\n چارک سوم قیمت {q3} ")


    def Show_correlation(self):
        df = pd.read_csv("KermanAparteman.csv")
        df['Price']=df['Price'].str.replace(',','').astype(float)
        correlation=df[['Area','Price']].corr()
        messagebox.showinfo("همبستگی",f"همبستگی بین مساحت و قیمت {correlation.loc['Area','Price']}")

    def Show_plot(self):
        plt.close("all")
        df=pd.read_csv("KermanAparteman.csv")
        location_mapping= {'منطقه یک':1,'منطقه دو':2,'منطقه سه':3,'منطقه چهار':4,'منطقه پنج':5}
        df['Location_num']= df['location'].map(location_mapping)
        df['Price']=df['Price'].str.replace(',','').astype(float)
        X=df[['Area']]
        y=df['Price']
        model=LinearRegression()
        model.fit(X,y)
        x_range=np.linspace(X.min(),X.max(),100).reshape(-1,1)
        y_pred=model.predict(x_range)
        plt.figure(figsize=(10,6))
        plt.scatter(df['Area'],df['Price'],c=df['Location_num'],cmap='viridis',label='Area vs Price')
        plt.plot(x_range,y_pred,color='red',label='Regression Line')
        plt.title("مساحت در مقابل قیمت",)
        plt.xlabel("مساحت(متر مربع)")
        plt.ylabel("قیمت(تومان)")
        plt.colorbar(label='location')
        plt.legend()
        plt.show()

    def Show_data(self):
        df=pd.read_csv("KermanAparteman.csv")
        tree=ttk.Treeview(self.csvframe,columns=list(df.columns),show="headings")

        for col in df.columns:
            tree.heading(col,text=col)
            tree.column(col,width=100)
        for index,row in df.iterrows():
            tree.insert("","end",values=list(row))

        scroll=ttk.Scrollbar(self.csvframe,orient="vertical",command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.place(x=20,y=50,width=900,height=300)
        scroll.place(x=920,y=50,height=300)

    def ShowCsvFrame(self):
        self.csvframe.place(x=100,y=250)

    def CloseCsvFrame(self):
        self.csvframe.place_forget()


