
#-- Les imports ---#
import socket,sys,threading,time
import pyspeedtest
from tkinter import *
from pythonping import ping



#--- Paramétrage de l'interface graphique--#
root=Tk()
root.geometry("500x700+20+20")
root.configure(bg='#222222')
root.title('Notre Application')

m1c = 'gold'
bgc = '#222222'
dbg = '#000000'
fgc = '#111111'
root.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc,activeForeground=bgc, highlightColor=m1c, highlightBackground=m1c)


nom = ''
ip = ''


host = {}


#-- definition des fonctions--#


def tab1():

#------------------------------------------------------------------tab2----------------------------------------------------------
    def tab2():
        label1.destroy()
        button1.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        label2=Label(root, text='PING TESTER', font=('Helvetica', 16, 'underline'), bg="#0D9ED4" )
        label2.place(x = 180, y = 10 )
        label2.pack(fill=X)
        
        def get_ping():
            resultat = ping(e.get(), verbose=True)
            res.set(resultat)

        res = StringVar()
        label3=Label(root, text="Entrer L'URL ou L'IP :",font=('Helvetica', 16))
        label3.place(x = 16, y = 90)
        e = Entry(root)
        e.place(x = 230, y = 95, width=150)
        button7 = Button(root, text="TESTER", command=get_ping, activebackground='red', bg="#0D9ED4")
        button7.place(x=390, y=91, width=90)
        label4=Label(root, text="Resultat :", font=('Helvetica', 16))
        label4.place(x = 16, y = 158)
        label8 = Label(root, text = "[ ........................................................ ]")
        label8.place(x = 200, y = 165)
        label5=Label(root, text="", textvariable=res, bg='white')
        label5.place(x = 150, y = 230, width=300, height=250 )
        
 
        
        def back():
            label2.destroy()
            label3.destroy()
            label5.destroy()
            label8.destroy()
            label4.destroy()
            button2.destroy()
            button7.destroy()
            e.destroy()
            tab1()
        button2 = Button(root, text='MENU', font=('Time_New_Roman', 16), command=back,activebackground='red', bg="#0D9ED4")
        button2.pack(side=BOTTOM, fill=X)
#--------------------------------------------------------tab3-------------------------------------------------------------------------------
    def tab3():
        label1.destroy()
        button1.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        

        
        # ==== Scanning Functions ====
        def scanPort(target, port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                c = s.connect_ex((target, port))
                if c == 0:
                    m = ' Le Port %d \test [ouvert]' % (port,)
                    log.append(m)
                    ports.append(port)
                    listbox.insert("end", str(m))
                    updateResult()
                s.close()
            except OSError: print('> Too many open sockets. Port ' + str(port))
            except:
                c.close()
                s.close()
                sys.exit()
            sys.exit()
            
        def updateResult():
            rtext = " [ " + str(len(ports)) + " / " + str(ip_f) + " ] ~ " + str(target)
            L27.configure(text = rtext)
        
        def startScan():
            global ports, log, target, ip_f
            clearScan()
            log = []
            ports = []
            
            ip_s = int(L5.get())
            ip_f = int(L25.get())
            

            try:
                target = socket.gethostbyname(str(L3.get()))
                log.append(' IP Adr.:\t' + str(target))
                log.append(' Ports: \t[ ' + str(ip_s) + ' / ' + str(ip_f) + ' ]')
                log.append('\n')
                # Lets start scanning ports!
                while ip_s <= ip_f:
                    try:
                        scan = threading.Thread(target=scanPort, args=(target, ip_s))
                        scan.setDaemon(True)
                        scan.start()
                    except: time.sleep(0.01)
                    ip_s += 1
            except:
                m = '> Target ' + str(L3.get()) + ' not found.'
                log.append(m)
                listbox.insert(0, str(m))
                
        
        def clearScan():
            listbox.delete(0, 'end')
                
        
        # ==== Les Labels ====
        L1 = Label(root, text = "Port Scanner",  font=("Helvetica", 16, 'underline'), bg="#0D9ED4")
        L1.place(x = 16, y = 10)
        L1.pack(fill=X)
        
        L2 = Label(root, text = "Target: ", font=("Helvetica", 16))
        L2.place(x = 16, y = 90)
        
        L3 = Entry(root, text = "localhost", font=("Helvetica", 16))
        L3.place(x = 180, y = 90)
        L3.insert(0, "")
        
        L4 = Label(root, text = "Ports: ", font=("Helvetica", 16))
        L4.place(x = 16, y = 158)
        
        L5 = Entry(root, text = "1", font=("Helvetica", 16))
        L5.place(x = 180, y = 158, width = 95)
        L5.insert(0, "")
        
        L25 = Entry(root, text = "1024", font=("Helvetica", 16))
        L25.place(x = 290, y = 158, width = 95)
        L25.insert(0, "")
        
        L26 = Label(root, text = "Resulta: ", font=("Helvetica", 16))
        L26.place(x = 16, y = 220)
        L27 = Label(root, text = "[ ... ]")
        L27.place(x = 180, y = 220)
        
        
        
        # ==== Ports list ====
        frame = Frame(root)
        frame.place(x = 16, y = 275, width = 370, height = 300)
        listbox = Listbox(frame, width = 59, height = 13, bg = "white")
        listbox.place(x = 0, y = 0)
        listbox.bind('<<ListboxSelect>>')
        
        
        # ==== Buttons / Scans ====
        B1 = Button(root, text = "Start Scan", command=startScan, bg="#0D9ED4")
        B1.place(x = 16, y = 500, width = 170)

        
        
        def back():
            button2.destroy()
            L1.destroy()
            L2.destroy()
            L3.destroy()
            L3.destroy()
            L4.destroy()
            L5.destroy()
            L25.destroy()
            L26.destroy()
            L27.destroy()
            
            listbox.destroy()
            
            
            B1.destroy()
            
            
            
            tab1()
        button2 = Button(root, text='MENU ', font=('Time_New_Roman', 16), command=back,activebackground='red', bg="#0D9ED4")
        button2.pack(side=BOTTOM, fill=X) 
#-----------------------------------------tab4-----------------------------------------------------------------------------
    def tab4():
        label1.destroy()
        button1.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        
        label0=Label(root, text='Scan du réseau', font=('Helvetica', 16, 'underline'), bg="#0D9ED4" )
        label0.place(x = 180, y = 10 )
        label0.pack(fill=X)
        
        
        
        
        
        def Scan_reseau():
            class NetscanThread(threading.Thread):
                def __init__(self, address):
                    self.address = address
                    threading.Thread.__init__(self)
                def run(self):
                    self.lookup(self.address)
                def lookup(self, address):
                    try:
                        hostname, alias, _ = socket.gethostbyaddr(address)
                        global host
                        host[address] = hostname
                    except socket.herror:
                        host[address] = None
            if __name__ == '__main__':
                addresses = []
                for ping in range(1, 254):
                    addresses.append("192.168.1." + str(ping))
                threads = []
                netscanthreads = [NetscanThread(address) for address in addresses] 
                for thread in netscanthreads :
                    thread.start()
                    threads.append(thread)
                for t in threads:
                    t.join()
            result = ''
            for address, hostname in host.items():
                if (hostname != None):
                    result= result + address+ '=>'+ hostname + "\n"
                res.set(result)
        res=StringVar()
        label3=Label(root, text="Faire un Scan du réseau :",font=('Helvetica', 16))
        label3.place(x = 16, y = 90)
        button7 = Button(root, text="Scanner", command=Scan_reseau, activebackground='red', bg="#0D9ED4")
        button7.place(x=280, y=91, width=90)
        label4=Label(root, text="Resultat :", font=('Helvetica', 16))
        label4.place(x = 16, y = 158)
        label8 = Label(root, text = "[ ........................................................ ]")
        label8.place(x = 200, y = 165)
        label5=Label(root, text="", textvariable= res, bg='white',font=('Helvetica', 12))
        scrollbar = Scrollbar(label5)
        scrollbar.pack(side=RIGHT, fill=Y)
        label5.place(x = 150, y = 230, width=300, height=250 )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def back():
            label0.destroy()
            label3.destroy()
            label8.destroy()
            label5.destroy()
            label4.destroy()
            label8.destroy()
            label3.destroy()
            button7.destroy()
            button0.destroy()
            
            tab1()
        button0 = Button(root, text='MENU', font=('Time_New_Roman', 16), command=back,activebackground='red', bg="#0D9ED4")
        button0.pack(side=BOTTOM, fill=X)
#--------------------------------------------------------------tab5-----------------------------------------------------------


    def tab5():
        label1.destroy()
        button1.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
        button6.destroy()
        
        label0=Label(root, text='INFO', font=('Helvetica', 16, 'underline'), bg="#0D9ED4" )
        label0.place(x = 180, y = 10 )
        label0.pack(fill=X)
        
        
        
        

        
        def get_Host_name_IP():
            try:
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                nom = host_name
                ip = host_ip
            except:
                print("Unable to get Hostname and IP")
                
            res_nom.set(nom)
            res_ip.set(ip)
            
            
            
        res_nom=StringVar()
        res_ip=StringVar()
        label3=Label(root, text="Adresse IP de  la SemaBox :",font=('Helvetica', 16))
        label3.place(x = 16, y = 90)
        button7 = Button(root, text="Voir", command=get_Host_name_IP, activebackground='red', bg="#0D9ED4")
        button7.place(x=190, y=300, width=90)
        label4=Label(root, text="Nom de la SemaBox (DNS):", font=('Helvetica', 16))
        label4.place(x = 16, y = 158)
        label33=Label(root, text="", textvariable= res_ip, bg='white',font=('Helvetica', 12))
        label33.place(x = 300, y = 80, width=200, height=50 )
        label5=Label(root, text="", textvariable= res_nom, bg='white',font=('Helvetica', 12))
        label5.place(x = 300, y = 150, width=200, height=50 )
        
        def speedtest():
            st = pyspeedtest.SpeedTest("www.google.com")
            resultat =  str(round((st.download() / 1000 / 1000), 2)) + " Mbit/s"
            res.set(resultat)



        res= StringVar()


        label44=Label(root, text="Test de débit:", font=('Helvetica', 16))
        label44.place(x = 16, y = 220)
        label55=Label(root, text="", textvariable= res, bg='white',font=('Helvetica', 12))
        label55.place(x = 300, y = 220, width=200, height=50 )
        button00 = Button(root, text="Tester", command=speedtest, activebackground='red', bg="#0D9ED4")
        button00.place(x=300, y=300, width=90)

        
        
        def back():
            label0.destroy()
            label3.destroy()
            label33.destroy()
            label5.destroy()
            label55.destroy()
            label4.destroy()
            label44.destroy()
            label3.destroy()
            button7.destroy()
            button0.destroy()
            button00.destroy()
            
            tab1()
        button0 = Button(root, text='MENU', font=('Time_New_Roman', 16), command=back,activebackground='red', bg="#0D9ED4")
        button0.pack(side=BOTTOM, fill=X)



























#-------------------------------------------------------------------------------------------------------
    label1=Label(root, text='MENU', font=('Helvetica', 16), bg="#0D9ED4")
    label1.pack(fill=X)
    
    button1=Button(root, text='SemaBox', font=('Helvetica', 16), command='',activebackground='red', bg="#0D9ED4")
    button1.pack(side=BOTTOM, fill=X)
    
    button3=Button(root, text='Scanne du réseau',  width = 25,height=8, command= tab4,activebackground='red', bg="#0D9ED4")
    button3.place(x = 26, y = 160)
    
    button4=Button(root, text='Scanner les ports',  width = 25, height=8, command= tab3,activebackground='red', bg="#0D9ED4")
    button4.place(x = 275, y = 160)
    
    button5=Button(root, text='INFO DE LA SEMABOX',  width = 25, height=8, command= tab5,activebackground='red', bg="#0D9ED4")
    button5.place(x = 26, y = 370)
    
    button6=Button(root, text='Test de connexion',  width = 25, height=8, command= tab2,activebackground='red', bg="#0D9ED4")
    button6.place(x = 275, y = 370)  
    
    
    
    
    

    
tab1()
root.mainloop()