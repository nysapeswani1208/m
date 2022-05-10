from tkinter import *
root= Tk()

root.title("Driver Licence")
root.geometry("400x200")

ID=Label(root,text="ID=")
Birth=Label(root,text="BIRTH=")
PIN=Label(root,text="PIN NO.=")
ADD=Label(root,text="ADDRESS=")
AUTHORIZATION=Label(root,text="AUTHORIZATION TO DRIVE WHICH VEHICAL=")



def add():
    ID["text"]="ID=NYSA"
    Birth["text"]="BIRTH= 12 AUGUST,2010"
    PIN["text"]="PIN NO.=45661288"
    ADD["text"]="ADDRESS=MUMBAI,INDIA"
    AUTHORIZATION["text"]="AUTHORIZATION TO DRIVE WHICH VEHICAL=4 WHEELER"

btn = Button(root, text="Add", command=add)
btn.pack()
    
show_result.pack()
root.mainloop()

