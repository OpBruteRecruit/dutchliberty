'''
please note,the creators Torshammer or Torshelper are never responsible of usege of there products in any kind of way
'''
from Tkinter import *
root = Tk()
app = Frame(root)
app.grid
root.title("Torshelper")
root.geometry("255x400")



############################################################################################
##################help tab      ############################################################
############################################################################################

def officialhelp():
 from Tkinter import *
 officialhelproot = Tk()
 officialhelpapp = Frame(officialhelproot)
 officialhelpapp.grid
 officialhelproot.title("officiele help")

 OFFICIALHELPtext ="/*\n * Tor's Hammer \n * Slow POST DoS Testing Tool\n * entropy [at] phiral.net\n * Anon-ymized via Tor\n * We are Legion.\n */\n\n./torshammer.py -t <target> [-r <threads> -p <port> -T -h]\n-t|--target <Hostname|IP>\n-r|--threads <Number of threads> Defaults to 256\n-p|--port <Web Server Port> Defaults to 80\n-T|--tor Enable anonymising through tor on 127.0.0.1:9050\n-h|--help Shows this help\n\nEg. ./torshammer.py -t 192.168.1.100 -r 256"

 ofhelpText = Text(officialhelproot,width = 60, height = 16, wrap = NONE)


 ofhelpText.grid(row = 12, column = 0, columnspan = 2)

 ofhelpText.insert(0.0,OFFICIALHELPtext)


 officialhelproot.mainloop()

############################################################################################
##################end help tab      ########################################################
############################################################################################
print"[-] ignore upper error "
print"[-] do not colse this terminal, the programm will crash"

#firts label
label1 = Label(root, text="TORSHELPER")
label1.grid(row = 0, column =0)

#second label
label2 = Label(root, text="officiele help:")
label2.grid(row = 1, column =0)

#first button
button1 = Button(root, text = "officiele help tab", command=officialhelp)
button1.grid(row = 2, column = 0)

#thirt label
label3 = Label(root, text="doelwit (url or ip)")
label3.grid(row = 3, column = 0)

#first entry [host/ip]
host = StringVar() 
ip = Entry(root,textvariable=host)
ip.grid(row = 4, column = 0)

#empty
empty1 = Label(root, text=" ")
empty1.grid(row = 5, column = 0)

#fourth label
label4 = Label(root, text="aantal aanvallen (standaart = 256)")
label4.grid(row = 6, column = 0)

#second entry [threads/attacks] 
threads = StringVar() 
attacks = Entry(root,textvariable=threads)
attacks.grid(row = 7, column = 0)

#empty
empty2 = Label(root, text=" ")
empty2.grid(row = 8, column = 0)

#fifth label
label5 = Label(root, text="port(standaart = 80)")
label5.grid(row = 9, column = 0)

#third entry [port] 
port = StringVar() 
ports = Entry(root,textvariable=port)
ports.grid(row = 10, column = 0)

#empty
empty3 = Label(root, text=" ")
empty3.grid(row = 11, column = 0)

#sixth label
label6 = Label(root, text="via tor j/n (wanneer ja type = -T of --tor\nwanner NEE laat leeg")
label6.grid(row = 12, column = 0)

#fourth entry [Tor] 
Tor = StringVar() 
T = Entry(root,textvariable=Tor)
T.grid(row = 13, column = 0)


#empty
empty4 = Label(root, text=" ")
empty4.grid(row = 14, column = 0)

#seventh label
label7 = Label(root, text="voor tor optie heeft u niet passe Torbrowser nodig)\n \n kopieer en plak:")
label7.grid(row = 15, column = 0)

#output
Text = Text(root,width = 25, height = 1, wrap = NONE)
Text.grid(row = 16, column = 0, columnspan = 2)


#main gen.
def Torshammergen():
	#inputs
	input1 = "%s"	%host.get()
	input2 = "%s"	%threads.get()
	input3 = "%s"	%port.get()
	input4 = "%s"	%Tor.get()
	#defaults
	if input2 == "":
	 input2 = "256"

	if input3 == "":
	 input3 = "80"

	#preconfigured 
	PYTHON = "python "
	PATH = "/root/dutchliberty"
	TORSHAMMER = "/torshammer.py "
	char1 = "-t "
	char2 = "-r "
	char3 = "-p "
	char4 = ""

	
	#space between input3 & input4(yes that fucked up little space gets 6 lines of code)
	if input4 == "":
	 char4 = ""
	elif input4 == "-T":
	 char4 = " "
	elif input4 == "--tor":
	 char4 = " "

	#main output
	OUTPUT = (PYTHON) + (PATH) + (TORSHAMMER) + (char1) + (input1) + (char2) + (input2) + (char3) + (input3) + (char4) + (input4)
	Text.delete(0.0,END)
	Text.insert(0.0,OUTPUT)

	#input errors	
	#host
	if input1 == "":
	 print"[-] FOUT"
	 HOSTERROR = "FOUT: website link vereist"
	 Text.delete(0.0,END)
	 Text.insert(0.0,HOSTERROR)


	#tor
	if input4 == "":
	 print"[-] Tor config: empty"
	elif input4 == "-T":
	 print"[-] Tor config: set (-T)"
	elif input4 == "--tor":
	 print"[-] Tor config: set (--tor)"
	else:
	 TORERROR = "FOUT: tor ingeef moet leeg zij,-T of --tor"
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORERROR)

	#torproject protection
	if input1 =="https://www.torproject.org/":
	 TORPROTECT = "wij beschermen tor, als het niet bevalt kan je de tering krijgen"
	 print(TORPROTECT)
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORPROTECT)	
	 quit()
	if input1 =="www.torproject.org/":
	 TORPROTECT = "wij beschermen tor, als het niet bevalt kan je de tering krijgen"
	 print(TORPROTECT)
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORPROTECT)	
	 quit()
	if input1 =="https://www.torproject.org":
	 TORPROTECT = "wij beschermen tor, als het niet bevalt kan je de tering krijgen"
	 print(TORPROTECT)
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORPROTECT)	
	 quit()
	if input1 =="www.torproject.org":
	 TORPROTECT = "wij beschermen tor, als het niet bevalt kan je de tering krijgen"
	 print(TORPROTECT)
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORPROTECT)
	 quit()
	if input1 =="38.229.72.16":
	 TORPROTECT = "wij beschermen tor, als het niet bevalt kan je de tering krijgen"
	 print(TORPROTECT)
	 Text.delete(0.0,END)
	 Text.insert(0.0,TORPROTECT)
	 quit()

#button2
button2 = Button(root, text = "genereer",command=Torshammergen)
button2.grid(row = 17, column = 0)

#end
root.mainloop()
