from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Rent import Rent
from Sale import Sale



class Housing(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        
        self.master.title("Scrape Your Needs [Housing]")

        img=PhotoImage(file="image\logoimage.gif")
        lblLogo = Label(self.master, image=img, bg='white')
        lblLogo.image=img
        lblLogo.grid(row=0, column=0,columnspan=4,sticky=E+W)

        lbl = Label(self.master, text='                                                                                  a python scrapper', bg='black', fg='white', borderwidth = 0,font=3)
        lbl.grid(row=1, column=0, columnspan=4 ,sticky=E+W)
        
        #l1=Label(self.master,text="Title",bg="white",padx='2',pady='4', font = 5)
        #l1.grid(row=2,column=0,columnspan=2)

        #self.d1=ttk.Combobox(self.master,state="readonly",values=["Software Developer","Software Tester","Designer","Data Analyst"], font = 5)
        #self.d1.current(0)
        #self.d1.grid(row=2,column=2,columnspan=2)
        l21=Label(self.master,text="",bg="white",padx='2',pady='4', font = 5)
        l21.grid(row=2,column=0,columnspan=2)
                
        l2=Label(self.master,text="Location",bg="white",padx='2',pady='4', font = 5)
        l2.grid(row=3,column=0,columnspan=2)

        self.d2=ttk.Combobox(self.master,state="readonly",values=["Delhi","Bengluru","Kochi","Pune","Hyderabad"], font = 5)
        self.d2.current(0)
        self.d2.grid(row=3,column=2,columnspan=2)
        
        l3=Label(self.master,text="For",bg="white",padx='2',pady='4', font = 5)
        l3.grid(row=4,column=0,columnspan=2)

        self.d3=ttk.Combobox(self.master,state="readonly",values=["Rent","Sale"], font = 5)
        self.d3.current(0)
        self.d3.grid(row=4,column=2,columnspan=2)
        
        l22=Label(self.master,text="",bg="white",padx='2',pady='4', font = 5)
        l22.grid(row=5,column=0,columnspan=2)
        
        
        b2=Button(self.master,text="Find",command=self.find_job,padx=2,pady=5, bg='light slate gray',fg= 'white', width=10, borderwidth = 1,font=5, activebackground='grey', activeforeground='white')
        b2.grid(row=6,column=3)
        self.master.grid_rowconfigure(5,weight=5)

        l23=Label(self.master,text="",bg="white",padx='2',pady='4', font = 5)
        l23.grid(row=7,column=0,columnspan=2)

        lblFooter1 = Label(self.master, text='Scrape Your Residental Needs', bg='light slate gray', fg='black',width=50, borderwidth = 0,font=3)
        lblFooter1.grid(row=8, column=0, columnspan=4 ,sticky=E+W)

        msg = "@Copyright Anonymous" # tools that are quick and easy to use and allow you to search based on the type of job you're looking for, your location, and other criteria. \n\n There are also sites that focus on certain types of positions or match you with employers. These sites are worth incorporating into your job search, because not all employers list on every website, even though it may seem that way. Don't limit yourself to just one job website, because each job site only lists jobs from particular websites or companies.\n\nJob Scrapper provides you job search engines like Indeed.com and SimplyHired.com that pull listings from many different sources.So go ahead and find your a job where you fits in...."

        lblFooter = Label(self.master, text=msg, bg='black', fg='white',width=50, borderwidth = 7,font=3,padx="0",wraplength=450 )
        lblFooter.grid(row=9, column=0, columnspan=4 ,sticky=E+W)
        
        


    def find_job(self):
        #title = self.d1.current()
        loc = self.d2.current()
        site = self.d3.current()


        iA0='https://www.olx.in/delhi_g2001152/for-rent-houses-apartments_c1723'
        iB0='https://www.olx.in/bangalore-highway_g5455316/for-rent-houses-apartments_c1723'
        iC0='https://www.olx.in/kochi_g4058873/for-rent-houses-apartments_c1723'
        iD0='https://www.olx.in/pune_g4059014/for-rent-houses-apartments_c1723'
        iE0='https://www.olx.in/hydrabadi-basti_g5318820/for-rent-houses-apartments_c1723'
        
        
        iA1='https://www.olx.in/delhi_g2001152/for-sale-houses-apartments_c1725'
        iB1='https://www.olx.in/bangalore-highway_g5455316/for-sale-houses-apartments_c1725'
        iC1='https://www.olx.in/kochi_g4058873/for-sale-houses-apartments_c1725'
        iD1='https://www.olx.in/pune_g4059014/for-sale-houses-apartments_c1725'
        iE1='https://www.olx.in/pune_g4059014/for-sale-houses-apartments_c1725'
        

       


        rent=[iA0,iB0,iC0,iD0,iE0]
        
        sale=[iA1,iB1,iC1,iD1,iE1]
            
    
        if site==0:
            url=rent[loc]
        
            a=Rent(url)
            a.retrive_housing()
        elif site==1:
            url=sale[loc]
        
            a=Sale(url)
            a.retrive_housing()

      


