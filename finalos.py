import pygame
import math
import sys
import time
from tkinter import *

from pygame.locals import*

def roundrobin():
    try:
        #frame2.pack_forget()
        global pb
        pb=[]
        global pbv
        pbv=[]
        #pa=[]
        inc=0
        
        #num1 = float(enter1.get())
        num2 = int(enter2.get())
        global result
        result = num2
        
        labelr = Label(frame1, text='Burst Time:').grid(row=10, column=8,columnspan=2)
        labelr = Label(frame1, text='Quantum:').grid(row=8, column=12,columnspan=2)
        global qur
        qur=Entry(frame1,bg="white")
        qur.grid(row=10, column=12)
        
        for i in range(0,result):
            inc+=1
            pb.append(Entry(frame1, bg='white'))
            pb[i].grid(row=inc+13, column=8)
##          pa.append(Entry(frame1, bg='white'))
##          pa[i].grid(row=x+9, column=12)
            
        ##print(pb[2].get())
        frame2.pack(side=BOTTOM)
        label3.config(text=str(result))

        btn2 = Button(frame1, text='OK', command=pp)
        btn2.grid(row=10, column=13)
    except ValueError:
        label3.config(text='Enter numeric values!')




################################################################


def thegame():
    pygame.init()
    
    screen  = pygame.display.set_mode((800,600))

    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    black = (0,0,0)
    pink = (255,100,100)
    yellow = (255,255,0)
    gray = (100,100,100)
    cyan = (0,255,255)
    color1 = (200,150,80)
    color2 = (80,150,200)
    color = red
    x = 50
    y = 50
    w = 10
    h = 30
    px = 0
    py = 0
    row = 0
    offset = 50
    u = 0
    c = 1
    diri = 1
    clock = pygame.time.Clock()
    fps  = 30
    simulator_end = False
    done = False
    once = True
    sch=0
    gantt = []
    suma = 0
##    schedule = []
##    schedule.append([])

    schedule = [["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",2000,red,1],["p1",1000,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1],["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1]]  
    
    cx = [50,150,150,50]
    cy = [50,100,200,300]

    index = [["p1",100,red],["p2",50,blue],["p3",80,green],["p4",20,yellow],["p5",40,pink],["p6",40,black],["p7",40,gray],["p8",40,cyan],["p9",40,color1],["p10",40,color2]]
    index1 = []
    
    for i in range(0,result):
        index[i][1]=pbv[i]*10
        index1.append(index[i])
    print(index1)
    
    for j in range(0,result):
        suma += (int(index[i][1]/quant)+1)

    print(quant)

    for i in range(0,result):
        print(index[i])
        ##print(schedule[i])
        i+=1


##roundrobin

    print("############"+str(index1))
    zero_count=result
    time_count=0
    dish = [False]*result
    i=0
##    schedule[0][0]=(index1[0][0])
##    schedule[0][1]=(index1[0][1])
##    schedule[0][2]=(index1[0][2])
##    schedule[0][3] = 1
    j=0
##    k=1
    updatej=0
    while zero_count!=0:
         if i == result:
             i=0
         if dish[i] == False:
             if index1[i][1] <= quant:
               #System.out.println(time_count+" p"+(i+1)+" "+(time_count+process[i])+" ");
                schedule[j][0]=index1[i][0]
                schedule[j][1]=index1[i][1]
                schedule[j][2]=index1[i][2]
                schedule[j][3] = 1
##                schedule[j]=index1[i]
                print("*1"+str(schedule[j]))
                ##schedule[j][3] = k
                time_count = time_count + index1[i][1]
                index1[i][1] -= quant
                j+=1
                dish[i] = True
                zero_count-=1
             else:
                #System.out.println(time_count+" p"+(i+1)+" "+(time_count+time)+" ");
                schedule[j][0]=(index1[i][0])
                schedule[j][1]=quant
                schedule[j][2]=(index1[i][2])
                schedule[j][3] = 1
                print("*2"+str(schedule[j]))
                j+=1
                time_count += quant
             index1[i][1] -= quant
             
             if index1[i][1] <= 0:
                 index1[i][1] = 0
         
         i+=1
         updatej=j

    print(updatej)

    for i in range(0,updatej):
        #print(index[i])
        print("#"+str(schedule[i]))
        i+=1

        
    #schedule = [["p1",40,red,1],["p2",40,blue,1],["p3",40,green,1],["p4",20,yellow,1],["p5",40,pink,1],["p1",40,red,1],["p2",10,blue,1],["p3",40,green,1],["p1",20,red,1]]  

    ##main loop
    while not simulator_end:
        screen.fill(white)
        tx,ty = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                simulator_end = True

        
        for items in index1:
            pygame.draw.rect(screen,items[2],(x,y,items[1],h))
            row+=1
            pygame.font.init()
            font  = pygame.font.SysFont("",20)
            text = font.render(items[0],True,black)   
            screen.blit(text,(x,y))

            x = x+items[1] + 50       
                
        x = 50
        y = 50
        row = 0

    ##    x = 200
    ##    y = 250
    ##    w = 10
    ##    h = 30
    ##    for items in schedule:
    ##        pygame.draw.rect(screen,items[2],(x,y,items[1],h))
    ##        x = x+items[1]
    ##
    ##    x = 200    

        if schedule[sch][3]:
            if once:
                process = schedule[sch][0]
                ind = int(process[1])-1
                index1[ind][1]=index1[ind][1]-schedule[sch][1]

                once = False
                
            for j in range(0,15):
                for i in  range(0,25):
                    for points in range(0,4):
                        ncr = math.factorial(3)/(math.factorial(3-points)*math.factorial(points))
                        px = px+math.pow(u,points)*math.pow((1-u),(3-points))*(cx[points]+i*(c))*ncr
                        py = py+math.pow(u,points)*math.pow((1-u),(3-points))*(cy[points]+j*(c))*ncr
                    pygame.draw.rect(screen,schedule[sch][2],(px,py,10,10))
                    px = 0
                    py = 0   
            u+=0.01
            
            c+=diri*(1)
            if c == 51 or c == 1:
                diri = diri*-1
                
            if u >=1.0:
                u = 0
                
        for element in gantt:
            pygame.draw.rect(screen,element[0],(element[2],300,element[1],h))
##            try:
##                pygame.draw.rect(screen,element[0],(element[2],300,element[1],h))
##            except IndexError:
##                print("Done")
            
        if c==1:
            schedule[sch][3] = 0
            print(schedule[sch])
            
            gantt.append([])
            gantt[sch].append(schedule[sch][2])
            gantt[sch].append(schedule[sch][1])
            if sch == 0:
                offset = 50
                gantt[sch].append(offset)
            else:
                offset  = offset + schedule[sch-1][1]
                gantt[sch].append(offset)
            sch+=1
            once = True
            if sch>=updatej:
                sch=8
                print("ok")
                
               
            
            
            
        pygame.display.update()
        clock.tick(80)

        
    pygame.quit()
    sys.exit()
    quit()

#####################################################################


#####################################################################


def pp():
    try:
        pbv[:]=[]
        global quant
        quant=int(qur.get());
        quant*=10
        print(quant)
        for i in range(0,result):
            pbv.append(int(pb[i].get()));
        print(pbv)
        thegame()
            
        
    except ValueError:
        label3.config(text='Enter numeric values!')

root = Tk()
root.minsize(width = 600, height = 600)
frame2=Frame(root)
frame1=Frame(root)

#frame1.maxsize(width=100,height=500)
labelr = Label(frame1, text='            ')
labelr.grid(row=0, column=0,columnspan=8)


label2 = Label(frame1, text='Enter number of processes:')
label2.grid(row=5, column=8,columnspan=3)
enter2 = Entry(frame1, bg='white')
enter2.grid(row=5, column=12,columnspan=3)


btn1 = Button(frame1, text='OK', command=roundrobin)
btn1.grid(row=5, column=16)

label3 = Label(frame1)
label3.grid(row=6, column=10)

frame1.pack(fill=BOTH,side=LEFT)



root.mainloop()


#############################################################







