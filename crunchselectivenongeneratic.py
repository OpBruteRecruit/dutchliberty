#import data (Tkinter)
from Tkinter import *
#main
root = Tk()
#gui configration (weith, hight, title, enz)
app = Frame(root)
app.grid()
root.title("woordenlijst lijn gen.  selectief niet gegenereerd ")
root.geometry("780x360")


#firts label
label1 = Label(root, text="minimale lengte wachtwoorden")
label1.grid(row = 0, column =0)


#input %s
svalue = StringVar() 
w = Entry(root,textvariable=svalue)
w.grid(row = 1, column = 0)

#second label
label2 = Label(root, text="maximale lengte wachtwoorden")
label2.grid(row = 2, column = 0)

#input %r
rvalue = StringVar() 
v = Entry(root,textvariable=rvalue)
v.grid(row = 3, column = 0)

#tirth label
label3 = Label(root, text="alle karacters die gegenereerd worden")
label3.grid(row = 4, column = 0)

#input %sr
srvalue = StringVar() 
x = Entry(root,textvariable=srvalue)
x.grid(row = 5, column = 0)

#fourth label
label4 = Label(root, text = "selectieve modus:\n( als de selectiefe modus = 16@@@@, en de karacters = 0-9 zal de uitkomst 160000-169999 zijn\nprobeer een 1e keer met minimaal 6 & maximaal 6, selectief 13@@@@ \nWAARSCHUWING: minimaale & maximale lengte wachtwoorden moeten het zelfde aantal karactershebben als in selective modus ")
label4.grid(row = 6, column = 0)

#input %sel1
selovalue = StringVar() 
q = Entry(root,textvariable=selovalue)
q.grid(row = 9, column = 0)

#fifth label
label4 = Label(root, text="bestands naam")
label4.grid(row = 11, column = 0)

#input %q
qvalue = StringVar()
y = Entry(root,textvariable=qvalue)
y.grid(row = 12, column = 0)

#sixth label
label5 = Label(root, text="  kopieer lijn hieronder naar een ander terminal ")
label5.grid(row = 13, column = 0)

#sevend label
label6 = Label(root, text = "  gebruik ctrl + c om te kopieren en rechtermuisknop -paste- om te plakken")
label6.grid(row = 14, column = 0)

#output
Text = Text(root,width = 25, height = 1, wrap = NONE)
Text.grid(row = 15, column = 0, columnspan = 2)


def hardprintfirst():
	#all inputs to variables
	input1 = "crunch %s "   %svalue.get()
	input2 = "%s"   %rvalue.get()
	input3 = "%s"   %srvalue.get()
	input4 = "%s"	%selovalue.get()
	input5 = "%s"   %qvalue.get()

	#all preconfiguered carracters
	car1 = " -t "
	car2 = " -o "
	car3 = " /root/Desktop/"
	car4 = ".txt"
	carBlank = " "
	OUTPUT = (input1) + (input2) + (carBlank) + (input3) + (car1) + (input4) + (car2) + (car3) + (input5) + (car4)
	Text.delete(0.0,END)
	Text.insert(0.0,OUTPUT)

#button
try:
  img1 = PhotoImage(file="/pic/anonops.png")
  img1COMPRSD = img1.subsample(21,21)
  hardprintbutton2 = Button(root,text="genereer",command=hardprintfirst)
  hardprintbutton2.grid()
  hardprintbutton2.config(image=bulletimgCOMPRSD,compound=RIGHT)
except:
  hardprintbutton2 = Button(root,text="genereer",command=hardprintfirst)
  hardprintbutton2.grid()











root.mainloop()
