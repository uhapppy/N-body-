import random
import math
import tkinter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

times=0
me=np.empty((0,4),int)
mt=np.empty((0,8),int)
planetliste=[]
class Simulation:
    def __init__(self):
        
        self.simulation = tkinter.Tk()
        self.simulation.geometry('1800x1000')
        self.simulation.title("simulation")
        self.simulation.configure(bg="gray")                    
        self.canvasphysic = tkinter.Canvas(self.simulation,bg="black")
        #button
        self.confirmation = tkinter.Button(self.simulation,text="start",command=self.nplanet,fg="black")
        self.resett = tkinter.Button(self.simulation,text="reset",command=self.reset,fg="black")
        self.look = tkinter.IntVar()
        self.trainer = tkinter.Checkbutton(self.simulation,text="voir les orbitre",onvalue=1,offvalue=0 ,variable=self.look)
        self.ale = tkinter.IntVar()
        self.aleatoire = tkinter.Checkbutton(self.simulation,text="planete aleatoire",onvalue=1,offvalue=0 , variable=self.ale)
        self.inter = tkinter.IntVar()
        self.interaction = tkinter.Checkbutton(self.simulation,text="interaction entre les planete",onvalue=1,offvalue=0,variable=self.inter)
        #label
        self.time = tkinter.StringVar()
        self.time.set("0")
        self.temps = tkinter.Label(self.simulation,textvariable=self.time)
        #pack 
        self.temps.pack()
        self.temps.place(x=1500, y=750 ,width=300,height=50)
        self.canvasphysic.pack(fill=tkinter.BOTH, expand=True)
        self.confirmation.pack()
        self.confirmation.place(x=1500,y=950,width=150,height=50)
        self.resett.pack()
        self.resett.place(x=1650,y=950,width=150,height=50)
        self.trainer.pack()
        self.trainer.place(x=1500, y=900 ,width=300,height=50 )
        self.aleatoire.pack()
        self.aleatoire.place(x=1500, y=850 ,width=300,height=50 )
        self.interaction.pack()
        self.interaction.place(x=1500, y=800 ,width=300,height=50)

        tkinter.mainloop()




    def nplanet(self):
        def _from_rgb(rgb):
            return "#%02x%02x%02x" % rgb
        me=np.empty((0,4),int)
        mt=np.empty((0,6),int)
        #valeur etoile
        

        # valeur de g  taux d'actualisation et nombre de planet a generer aleatoirement si choisis
        n = 50 #max environs 50
        time = 1
        g = 0.1

        #valeur planet intervalle caracteristique planet
        posx = 0 
        posy = 0 
        masse = 1
        rayon = 3
        vx = 0.0
        vy = 0.0
        posx2 = 1800 
        posy2 = 1000
        masse2 = 1
        rayon2 = 3
        vx2 = 0.0
        vy2 = 0.0

        #etoile custom 
        me = np.append(me,np.array([[900,500,100,20,]]),axis=0)
        me = np.append(me,np.array([[600,200,100,10,]]),axis=0)
        #planete aleatoire
        if self.ale.get()==1 :
            for i in range(n):
                mt=np.append(mt,np.array([[random.randint(posx,posx2),random.randint(posy,posy2),random.uniform(masse,masse2),random.randint(rayon,rayon2),random.uniform(vx,vx2),random.uniform(vy,vy2)]]),axis=0)
            planetliste.append(1)            
        #planet custom
        if self.ale.get()==0 :
               #mt = np.append(mt,np.array([[700,500,1,5,0.1,0.1]]),axis=0)
               mt = np.append(mt,np.array([[750,500,1,5,-0.1,-0.1]]),axis=0)
               planetliste.append(1)
        numberofrowetoile=np.shape(me)[0]
        numberofrowplanete=np.shape(mt)[0]
        #graph
        
        def task():
                global times
                times+=1
                self.time.set(times)
                if self.look.get()==0:
                    self.canvasphysic.delete("all")
                else :
                    pass
                if not planetliste:
                    self.reset()
                for i in range(0,numberofrowetoile):                    
                    self.canvasphysic.create_oval(me[i,0]-me[i,3],me[i,1]+me[i,3],me[i,0]+me[i,3],me[i,1]-me[i,3],fill="yellow")
                for i in range(0,numberofrowplanete):
                    b1 = abs(int(mt[i,5]*110))
                    g1 = abs(int(mt[i,4]*110))
                    R=255                                           
                    G=255-g1
                    B=255-b1
                    if b1 >= 255 :
                        B=0
                    if g1 >= 255 :
                        G=0
                    self.canvasphysic.create_oval(mt[i,0]-mt[i,3],mt[i,1]+mt[i,3],mt[i,0]+mt[i,3],mt[i,1]-mt[i,3],fill=_from_rgb((R,G,B)))
                    
                    t=g*mt[i,2]
                    ae = np.array([0,0])
                    at1 = np.array([0,0])
                    at2 = np.array([0,0])
                    #acceleration d'est etoile
                    if numberofrowetoile == 0 :
                        a0=0
                    else :
                        for n in range(0,numberofrowetoile):
                            d=me[n,:2]-mt[i,:2]
                            d2=math.sqrt(d@d)
                            ae = ae + ((t*me[n,2]*d)/d2**3)
                            if d2 <=5 :
                                ae=0
                        a0=ae
                    
                    #acceleration planete
                    if self.inter.get()==1:                    
                        for k in range(i+1,numberofrowplanete):
                            D=mt[k,:2]-mt[i,:2]
                            D2=math.sqrt(D@D)
                            at1 = at1 + ((t*mt[k,2]*D)/D2**3)
                            if D2 <=5 :
                                at1 = 0
                        a1 = at1
                        for r in range(0,i):
                            D1=mt[r,:2]-mt[i,:2]                            
                            D12=math.sqrt(D1@D1)
                            at2 = at2 + ((t*mt[r,2]*D1)/D12**3)
                            if D12 <= 5 :
                                at2 = 0

                        a2 = at2
                    else :
                        a1=0
                        a2=0
                    a=(a0+a1+a2)/mt[i,2]                    
                    mt[i,4:6] += a
                    mt[i,:2] += mt[i,4:6]
                    
                   
                self.simulation.after(time,task)              
        self.simulation.after(time,task)
    def reset(self):   
        self.canvasphysic.delete("all")
        planetliste.clear()
        global times
        times=0
        tkinter.mainloop()   
simulation1 = Simulation()
