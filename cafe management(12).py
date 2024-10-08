from tkinter import *
import random
import datetime
import time
from tkinter import messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background="red")


Tops=Frame(root, width=1350, height=100, bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root, width=900, height=650,bd=8,relief="raise")
f1.pack(side=LEFT)

f2=Frame(root, width=440, height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1, width=900, height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1, width=900, height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2, width=440, height=650,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2, width=440, height=50,bd=16,relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a, width=400, height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a, width=400, height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)


f2aa=Frame(f2a, width=450, height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a, width=450, height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)


Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")


#==================Methods===================
def CostofItem():
    
    Item1=float(E_Coke.get())
    Item2=float(E_Lemonade.get())
    Item3=float(E_Ice_Coke.get())
    Item4=float(E_Tea.get())
    Item5=float(E_Fruit_Juices.get())
    Item6=float(E_Coffee.get())
    Item7=float(E_Iced_Tea.get())
    Item8=float(E_Soup.get())

    Item9=float(E_Chocolate_Cake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Fruit_Cake.get())
    Item13=float(E_Britannia_Cake.get())
    Item14=float(E_Cadbury_Cake.get())
    Item15=float(E_Sponge_Cake.get())
    Item16=float(E_Queen_Park_Cake.get())

    PriceofDrinks=(Item1*35)+(Item2*60)+(Item3*100)+(Item4*20)+(Item5*40)+(Item6*45)+(Item7*80)+(Item8*30)
    PriceofCakes=(Item9*300)+(Item10*500)+(Item11*600)+(Item12*250)+(Item13*60)+(Item14*300)+(Item15*400)+(Item16*700)
    DrinksPrice="₹",str("%.2f"%(PriceofDrinks))
    CakesPrice="₹",str("%.2f"%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="₹",str("%.2f"%(50))
    ServiceCharge.set(SC)

    SubTotalofITEMS="₹",str("%.2f"%(PriceofDrinks+PriceofCakes+50))
    SubTotal.set(SubTotalofITEMS)

    Tax="₹",str("%.2f"%((PriceofDrinks+PriceofCakes+50)*2.00))
    PaidTax.set(Tax)
    TT=((PriceofDrinks+PriceofCakes+50)*2.00)
    TC="₹",str("%.2f"%(PriceofDrinks+PriceofCakes+50+TT))
    TotalCost.set(TC)




def qExit():
    qExit= messagebox.askyesno("QUIT SYSTEM","DO YOU WANT TO QUIT")
    if qExit>0:
        root.destroy()
        return

def Reset():
    PaidTax.set(" ")
    SubTotal.set(" ")
    TotalCost.set(" ")
    CostofDrinks.set(" ")
    CostofCakes.set(" ")
    ServiceCharge.set(" ")
    txtReceipt.delete("1.0",END)

    E_Coke.set("0")
    E_Lemonade.set("0")
    E_Ice_Coke.set("0")
    E_Tea.set("0")
    E_Fruit_Juices.set("0")
    E_Coffee.set("0")
    E_Iced_Tea.set("0")
    E_Soup.set("0")
    E_Chocolate_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Fruit_Cake.set("0")
    E_Britannia_Cake.set("0")
    E_Cadbury_Cake.set("0")
    E_Sponge_Cake.set("0")
    E_Queen_Park_Cake.set("0")


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtCoke.configure
    txtLemonade.configure
    txtIce_Coke.configure
    txtTea.configure
    txtFruit_Juices.configure
    txtCoffee.configure
    txtIced_Tea.configure
    txtSoup.configure
    txtChocolate_Cake.configure
    txtRed_Velvet_Cake.configure
    txtBlack_Forest_Cake.configure
    txtFruit_Cake.configure
    txtBritannia_Cake.configure
    txtCadbury_Cake.configure
    txtSponge_Cake.configure
    txtQueen_Park_Cake.configure


def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(1,1000)
    randomRef=str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t\t"+Receipt_Ref.get()+"\t\t"+DateOfOrder.get()+"\n")
    txtReceipt.insert(END,"Items\t\t\t\t\t"+"Cost of Items \n\n")
    txtReceipt.insert(END,"Coke:\t\t\t\t\t"+ E_Coke.get()+"\n")
    txtReceipt.insert(END,"Lemonade:\t\t\t\t\t"+E_Lemonade.get()+"\n")
    txtReceipt.insert(END,"Iced_Coke:\t\t\t\t\t"+E_Ice_Coke.get()+"\n")
    txtReceipt.insert(END,"Tea:\t\t\t\t\t"+ E_Tea.get()+"\n")
    txtReceipt.insert(END,"Fruit_Juices:\t\t\t\t\t"+E_Fruit_Juices.get()+"\n")
    txtReceipt.insert(END,"Coffee:\t\t\t\t\t"+E_Coffee.get()+"\n")
    txtReceipt.insert(END,"Iced_Tea:\t\t\t\t\t"+E_Iced_Tea.get()+"\n")
    txtReceipt.insert(END,"Soup:\t\t\t\t\t"+E_Soup.get()+"\n")
    txtReceipt.insert(END,"Chocolate_cake:\t\t\t\t\t"+ E_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,"Red Velvet cake:\t\t\t\t\t"+E_Red_Velvet_Cake.get()+"\n")
    txtReceipt.insert(END,"Black forest cake:\t\t\t\t\t"+E_Black_Forest_Cake.get()+"\n")
    txtReceipt.insert(END,"Fruit Cake:\t\t\t\t\t"+E_Fruit_Cake.get()+"\n")
    txtReceipt.insert(END,"Britannia cake\t\t\t\t\t"+ E_Britannia_Cake.get()+"\n")
    txtReceipt.insert(END,"Cadbury cake:\t\t\t\t\t"+E_Cadbury_Cake.get()+"\n")
    txtReceipt.insert(END,"Sponge cake:\t\t\t\t\t"+E_Sponge_Cake.get()+"\n")
    txtReceipt.insert(END,"Queen Park cake:\t\t\t\t\t"+E_Queen_Park_Cake.get()+"\n")
    txtReceipt.insert(END,"Cost of Drinks:\t\t"+ CostofDrinks.get()+"\tTax Paid:\t\t"+PaidTax.get()+"\n")
    txtReceipt.insert(END,"Cost of Cakes:\t\t"+ CostofCakes.get()+"\tSubTotal:\t\t"+SubTotal.get()+"\n")
    txtReceipt.insert(END,"Service Charge:\t\t"+ServiceCharge.get()+"\tTotalCost:\t\t"+TotalCost.get()+"\n")

#=====================Heading==============
lblInfo=Label(Tops,font=("Edwardian Script ITC",50,"bold"),text="  Cafe Management System  ",bd=10)
lblInfo.grid(row=0,column=0)


#==============calculator================

def chkbutton_value():
    if(var1.get==1):
        txtCoke.configure
    elif var1.get()==0:
        txtCoke.configure
        E_Coke.set("0")
    if(var2.get==1):
        txtLemonade.configure
    elif var2.get()==0:
        txtLemonade.configure
        E_Lemonade.set("0")
    if(var3.get==1):
        txtIce_Coke.configure
    elif var3.get()==0:
        txtIce_Coke.configure
        E_Ice_Coke.set("0")
    if(var4.get==1):
        txtTea.configure
    elif var4.get()==0:
        txtTea.configure
        E_Tea.set("0")
    if(var5.get==1):
        txtFruit_Juices.configure
    elif var5.get()==0:
        txtFruit_Juices.configure
        E_Fruit_Juices.set("0")
    if(var6.get==1):
        txtCoffee.configure
    elif var6.get()==0:
        txtCoffee.configure
        E_Coffee.set("0")
    if(var7.get==1):
        txtIced_Tea.configure
    elif var7.get()==0:
        txtIced_Tea.configure
        E_Iced_Tea.set("0")
    if(var8.get==1):
        txtSoup.configure
    elif var8.get()==0:
        txtSoup.configure
        E_Soup.set("0")
    if(var9.get==1):
        txtChocolate_Cake.configure
    elif var9.get()==0:
        txtChocolate_Cake.configure
        E_Chocolate_Cake.set("0")
    if(var10.get==1):
        txtRed_Velvet_Cake.configure
    elif var10.get()==0:
        txtRed_Velvet_Cake.configure
        E_Red_Velvet_Cake.set("0")
    if(var11.get==1):
        txtBlack_Forest_Cake.configure
    elif var11.get()==0:
        txtBlack_Forest_Cake.configure
        E_Black_Forest_Cake.set("0")
    if(var12.get==1):
        txtFruit_Cake.configure
    elif var12.get()==0:
        txtFruit_Cake.configure
        E_Fruit_Cake.set("0")
    if(var13.get==1):
        txtBritannia_Cake.configure
    elif var13.get()==0:
        txtBritannia_Cake.configure
        E_Britannia_Cake.set("0")
    if(var14.get==1):
        txtCadbury_Cake.configure
    elif var14.get()==0:
        txtCadbury_Cake.configure
        E_Cadbury_Cake.set("0")
    if(var15.get==1):
        txtSponge_Cake.configure
    elif var15.get()==0:
        txtSponge_Cake.configure
        E_Sponge_Cake.set("0")
    if(var16.get==1):
        txtQueen_Park_Cake.configure
    elif var16.get()==0:
        txtQueen_Park_Cake.configure
        E_Queen_Park_Cake.set("0")
    
    

#================Variables==================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateOfOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofDrinks=StringVar()
CostofCakes=StringVar()
ServiceCharge=StringVar()




E_Coke=StringVar()
E_Lemonade=StringVar()
E_Ice_Coke=StringVar()
E_Tea=StringVar()
E_Fruit_Juices=StringVar()
E_Coffee=StringVar()
E_Iced_Tea=StringVar()
E_Soup=StringVar()
E_Chocolate_Cake=StringVar()
E_Red_Velvet_Cake=StringVar()
E_Black_Forest_Cake=StringVar()
E_Fruit_Cake=StringVar()
E_Britannia_Cake=StringVar()
E_Cadbury_Cake=StringVar()
E_Sponge_Cake=StringVar()
E_Queen_Park_Cake=StringVar()




E_Coke.set("0")
E_Lemonade.set("0")
E_Ice_Coke.set("0")
E_Tea.set("0")
E_Fruit_Juices.set("0")
E_Coffee.set("0")
E_Iced_Tea.set("0")
E_Soup.set("0")

E_Chocolate_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Fruit_Cake.set("0")
E_Britannia_Cake.set("0")
E_Cadbury_Cake.set("0")
E_Sponge_Cake.set("0")
E_Queen_Park_Cake.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))





#=================================Drinks======================

Coke=Checkbutton(f1aa,text="Coke\t",variable=var1, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=0,column=0,sticky=W)
Lemonade=Checkbutton(f1aa,text="Lemonade\t",variable=var2, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=1,column=0,sticky=W)
Ice_Coke=Checkbutton(f1aa,text="Ice_Coke\t",variable=var3, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=2,column=0,sticky=W)
Tea=Checkbutton(f1aa,text="Tea\t",variable=var4, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=3,column=0,sticky=W)
Fruit_Juices=Checkbutton(f1aa,text="Fruit_Juices\t",variable=var5, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=4,column=0,sticky=W)
Coffee=Checkbutton(f1aa,text="Coffee\t",variable=var6, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=5,column=0,sticky=W)
Iced_Tea=Checkbutton(f1aa,text="Iced_Tea\t",variable=var7, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=6,column=0,sticky=W)
Soup=Checkbutton(f1aa,text="Soup\t",variable=var8, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=7,column=0,sticky=W)
# =====================Cakes======================

Chocolate_Cake=Checkbutton(f1ab,text="Chocolate_Cake\t",variable=var9, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=0,column=0,sticky=W)
Red_Velvet_Cake=Checkbutton(f1ab,text="Red_Velvet_cake\t",variable=var10, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=1,column=0,sticky=W)
Black_Forest_Cake=Checkbutton(f1ab,text="Black_Forest_cake\t",variable=var11, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=2,column=0,sticky=W)
Fruit_Cake=Checkbutton(f1ab,text="Fruit_Cake\t",variable=var12, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=3,column=0,sticky=W)
Britannia_Cake=Checkbutton(f1ab,text="Britannia_Cake\t",variable=var13, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=4,column=0,sticky=W)
Cadbury_Cake=Checkbutton(f1ab,text="Cadbury_Cake\t",variable=var14, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=5,column=0,sticky=W)
Sponge_Cake=Checkbutton(f1ab,text="Sponge_Cake\t",variable=var15, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=6,column=0,sticky=W)
Queen_Park_Cake=Checkbutton(f1ab,text="Queen_Park_cake\t",variable=var16, onvalue=1, offvalue=0,
                  font=("arial",18,"bold")).grid(row=7,column=0,sticky=W)
#====================================enter widget for Drinks=========
txtCoke= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Coke)
txtCoke.grid(row=0,column=1)
txtLemonade= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Lemonade)
txtLemonade.grid(row=1,column=1)
txtIce_Coke= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Ice_Coke)
txtIce_Coke.grid(row=2,column=1)
txtTea= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Tea)
txtTea.grid(row=3,column=1)
txtFruit_Juices= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Fruit_Juices)
txtFruit_Juices.grid(row=4,column=1)
txtCoffee= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Coffee)
txtCoffee.grid(row=5,column=1)
txtIced_Tea= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Iced_Tea)
txtIced_Tea.grid(row=6,column=1)
txtSoup= Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Soup)
txtSoup.grid(row=7,column=1)





#============enter widget  for Cakes===========
txtChocolate_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Chocolate_Cake)
txtChocolate_Cake.grid(row=0,column=1)
txtRed_Velvet_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Red_Velvet_Cake)
txtRed_Velvet_Cake.grid(row=1,column=1)
txtBlack_Forest_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Black_Forest_Cake)
txtBlack_Forest_Cake.grid(row=2,column=1)
txtFruit_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Fruit_Cake)
txtFruit_Cake.grid(row=3,column=1)
txtBritannia_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Britannia_Cake)
txtBritannia_Cake.grid(row=4,column=1)
txtCadbury_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Cadbury_Cake)
txtCadbury_Cake.grid(row=5,column=1)
txtSponge_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Sponge_Cake)
txtSponge_Cake.grid(row=6,column=1)
txtQueen_Park_Cake= Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Queen_Park_Cake)
txtQueen_Park_Cake.grid(row=7,column=1)


#============================ cost Item Information===========
lblCostofDrinks=Label(f2aa,font=("arial",16,"bold"),text="Cost Of Drinks",bd=8,anchor="w")
lblCostofDrinks.grid(row=2,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2,column=1,sticky=W)

lblCostofCakes=Label(f2aa,font=("arial",16,"bold"),text="Cost Of Cakes",bd=8,anchor="w")
lblCostofCakes.grid(row=3,column=0,sticky=W)
txtCostofCakes=Entry(f2aa,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=CostofCakes)
txtCostofCakes.grid(row=3,column=1,sticky=W)

lblServiceCharge=Label(f2aa,font=("arial",16,"bold"),text="Service Charge",bd=8,anchor="w")
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=ServiceCharge)
txtServiceCharge.grid(row=4,column=1,sticky=W)

#==========================Payment Information====================
lblPaidTax=Label(f2ab,font=("arial",16,"bold"),text="Tax",bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1,sticky=W)

lblSubTotal=Label(f2ab,font=("arial",16,"bold"),text="Subtotal",bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1,sticky=W)

lblTotalCost=Label(f2ab,font=("arial",16,"bold"),text="Total",bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=2,justify="left",textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1,sticky=W)
#==================Infomation===========
lblReceipt=Label(ft2,font=("arial",12,"bold"),text="Receipt",bd=2,anchor="w")
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt= Text(ft2,width=59,height=22,bg="white",bd=8,font=("arial",11,"bold"))
txtReceipt.grid(row=1,column=0)


#=================Buttons=========
btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",11,"bold"),width=5,
                text="Total",command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",11,"bold"),width=5,
                text="Receipt",command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",11,"bold"),width=5,
                text="Reset",command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",11,"bold"),width=5,
                text="Exit",command=qExit).grid(row=0,column=3)

root.mainloop()
