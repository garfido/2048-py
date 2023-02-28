#2048
import random 
import keyboard as k
import time as t
print("2048 IN PYTHON")
print("sviluppatore: Alessio Gatti")
cell1 = 0
cell2 = 0
cell3 = 0
cell4 = 0
cell5 = 0
cell6 = 0
cell7 = 0
cell8 = 0
cell9 = 0
cell10 = 0
cell11 = 0
cell12 = 0
cell13 = 0
cell14 = 0
cell15 = 0
cell16 = 0
celle =[cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9,cell10,cell11,cell12,cell13,cell14,cell15,cell16]
repeat = 0
nuovo =1  
def somma_su():
    for i in range(3):
        t.sleep(0.05)
        #colonna 1
        if celle[0] == celle[4]:
            celle[0] = celle[0]*2
            celle[4] = 0

        if celle[4] == celle[8]:
            celle[4] = celle[4]*2
            celle[8] = 0
            
        if celle[8] == celle[12]:
            celle[8] = celle[8]*2
            celle[12] = 0
                        
                                
        #colonna 2
        if celle[1] == celle[5]:
            celle[1] = celle[1]*2
            celle[5] = 0

        if celle[5] == celle[9]:
            celle[5] = celle[5]*2
            celle[9] = 0
                        
        if celle[9] == celle[13]:
            celle[9] = celle[9]*2
            celle[13] = 0
                        
                                
        #colonna 3
        if celle[2] == celle[6]:
            celle[2] = celle[2]*2
            celle[6] = 0

        if celle[6] == celle[10]:
            celle[6] = celle[6]*2
            celle[10] = 0
                        
        if celle[10] == celle[14]:
            celle[10] = celle[10]*2
            celle[14] = 0
                        
        #colonna 4
        if celle[3] == celle[7]:
            celle[3] = celle[3]*2
            celle[7] = 0

        if celle[7] == celle[11]:
            celle[7] = celle[7]*2
            celle[11] = 0
                        
        if celle[11] == celle[15]:
            celle[11] = celle[11]*2
            celle[15] = 0


def schift_su():
    for i in range(3):
        t.sleep(0.05)
        #schift
        #colonna 1
        if celle[8] == 0 and celle[12] > 0:
            celle[8] = celle[12]
            celle[12] = 0

        if celle[4] == 0 and celle[8] > 0:
            celle[4] = celle[8]
            celle[8] = 0

        if celle[0] == 0 and celle[4] > 0:      
            celle[0] = celle[4]
            celle[4] = 0
        #colonna 2
        if celle[9] == 0 and celle[13] > 0:
            celle[9] = celle[13]
            celle[13] = 0

        if celle[5] == 0 and celle[9] > 0:
            celle[5] = celle[9]
            celle[9] = 0

        if celle[1] == 0 and celle[5] > 0:
            celle[1] = celle[5]
            celle[5] = 0
        #colonna 3
        if celle[10] == 0 and celle[14] > 0:
            celle[10] = celle[14]
            celle[14] = 0

        if celle[6] == 0 and celle[10] > 0:
            celle[6] = celle[10]
            celle[10] = 0

        if celle[2] == 0 and celle[6] > 0:      
            celle[2] = celle[6]
            celle[6] = 0
        #colonna 4
        if celle[11] == 0 and celle[15] > 0:
            celle[11] = celle[15]
            celle[15] = 0

        if celle[7] == 0 and celle[11] > 0:
            celle[7] = celle[11]
            celle[11] = 0

        if celle[3] == 0 and celle[7] > 0:
            celle[3] = celle[7]
            celle[7] = 0


def schift_giu():
    for i in range(3):
        t.sleep(0.05)
        #schift
        #colonna 1
        if celle[4] == 0 and celle[0] > 0:
            celle[4] = celle[0]
            celle[0] = 0

        if celle[8] == 0 and celle[4] > 0:
            celle[8] = celle[4]
            celle[4] = 0

        if celle[12] == 0 and celle[8] > 0:      
            celle[12] = celle[8]
            celle[8] = 0
        #colonna 2
        if celle[5] == 0 and celle[1] > 0:
            celle[5] = celle[1]
            celle[1] = 0

        if celle[9] == 0 and celle[5] > 0:
            celle[9] = celle[5]
            celle[5] = 0

        if celle[13] == 0 and celle[9] > 0:
            celle[13] = celle[9]
            celle[9] = 0
        #colonna 3
        if celle[6] == 0 and celle[2] > 0:
            celle[6] = celle[2]
            celle[2] = 0

        if celle[10] == 0 and celle[6] > 0:
            celle[10] = celle[6] 
            celle[6] = 0

        if celle[14] == 0 and celle[10] > 0:
            celle[14] = celle[10]
            celle[10] = 0
        #colonna 4
        if celle[7] == 0 and celle[3] > 0:
            celle[7] = celle[3]
            celle[3] = 0

        if celle[11] == 0 and celle[7] > 0:
            celle[11] = celle[7]
            celle[7] = 0

        if celle[15] == 0 and celle[11] > 0:
            celle[15] = celle[11]
            celle[11] = 0

def somma_giu():
    for i in range(3):
        t.sleep(0.05)
        #colonna 1 
        if celle[12] == celle[8]:
            celle[12] = celle[12]*2
            celle[8] = 0
        
        if celle[8] == celle[4]:
            celle[8] = celle[8] *2
            celle[4] = 0
        
        if celle[4] == celle[0]:
            celle[4] = celle[4]*2
            celle[0] = 0
        #colonna 2
        if celle[13] == celle[9]:
            celle[13] = celle[13]*2
            celle[9]
        
        if celle[9] == celle[5]:
            celle[9] = celle[9]*2
            celle[5] = 0

        if celle[5] == celle[1]:
            celle[5] = celle[5]*2
            celle[1] = 0
        #colonna 3
        if celle[14] == celle[10]:
            celle[14] = celle[14]*2
            celle[10] = 0

        if celle[10] == celle[6]:
            celle[10] = celle[10]*2
            celle[6] = 0

        if celle[6] == celle[2]:
            celle[6] = celle[6]*2
            celle[2] = 0
        #colonna 4
        if celle[15] == celle[11]:
            celle[15] = celle[15]*2
            celle[11] = 0
        
        if celle[11] == celle[7]:
            celle[11] = celle[11]*2
            celle[7] = 0

        if celle[7] == celle[3]:
            celle[7] = celle[7]*2
            celle[3] = 0

def somma_sinistra():
    for i in range(3):
        t.sleep(0.05)
        #riga 1
        if celle[2] == celle[3]:
            celle[2] = celle[2]*2
            celle[3] = 0

        if celle[1] == celle[2]:
            celle[1] = celle[1]*2
            celle[2] = 0
        
        if celle[0] == celle[1]:
            celle[0] = celle[0]*2
            celle[1] = 0
        #riga 2
        if celle[6] == celle[7]:
            celle[6] = celle[6]*2
            celle[7] = 0

        if celle[5] == celle[6]:
            celle[5] = celle[5]*2
            celle[6] = 0
        
        if celle[4] == celle[5]:
            celle[4] = celle[4]*2
            celle[5] = 0
        #riga 3
        if celle[10] == celle[11]:
            celle[10] = celle[10]*2
            celle[11] = 0

        if celle[9] == celle[10]:
            celle[9] = celle[9]*2
            celle[10] = 0
        
        if celle[8] == celle[9]:
            celle[8] = celle[8]*2
            celle[9] = 0
        #riga 4
        if celle[14] == celle[15]:
            celle[14] = celle[14]*2
            celle[15] = 0

        if celle[13] == celle[14]:
            celle[13] = celle[13]*2
            celle[14] = 0
        
        if celle[12] == celle[13]:
            celle[12] = celle[12]*2
            celle[13] = 0
def schift_sinistra():
    for i in range(3):
        t.sleep(0.05)
        #riga 1
        if celle[0] == 0 and celle[1] > 0:
            celle[0] = celle[1]
            celle[1] = 0

        if celle[1] == 0 and celle[2] > 0:
            celle[1] = celle[2]
            celle[2] = 0

        if celle[2] == 0 and celle[3] > 0:
            celle[2] = celle[3]
            celle[3] = 0
        #riga 2
        if celle[4] == 0 and celle[5] > 0:
            celle[4] = celle[5]
            celle[5] = 0
        
        if celle[5] == 0 and celle[6] > 0:
            celle[5] = celle[6]
            celle[6] = 0

        if celle[6] == 0 and celle[7] > 0:
            celle[6] = celle[7]
            celle[7] = 0
        #riga 3
        if celle[8] == 0 and celle[9] > 0:
            celle[8] = celle[9]
            celle[9] = 0
        
        if celle[9] == 0 and celle[10] > 0:
            celle[9] = celle[10]
            celle[10] = 0

        if celle[10] == 0 and celle[11] > 0:
            celle[10] = celle[11]
            celle[11] = 0
        #riga 4
        if celle[12] == 0 and celle[13] > 0:
            celle[12] = celle[13]
            celle[13] = 0
        
        if celle[13] == 0 and celle[14] > 0:
            celle[13] = celle[14]
            celle[14] = 0

        if celle[14] == 0 and celle[15] > 0:
            celle[14] = celle[15]
            celle[15] = 0

def schift_destra():
    for i in range(3):
        t.sleep(0.05)
        #riga 1
        if celle[3] == 0 and celle[2] > 0:
            celle[3] = celle[2]
            celle[2] = 0
            
        if celle[2] == 0 and celle[1] > 0:
            celle[2] = celle[1]
            celle[1] = 0
        
        if celle[1] == 0 and celle[0] > 0:
            celle[1] = celle[0]
            celle[0] = 0
        #riga 2
        if celle[7] == 0 and celle[6] > 0:
            celle[7] = celle[6]
            celle[6] = 0
        
        if celle[6] == 0 and celle[5] > 0:
            celle[6] = celle[5]
            celle[5] = 0

        if celle[5] == 0 and celle[4] > 0:
            celle[5] = celle[4]
            celle[4] = 0
        #riga 3
        if celle[11] == 0 and celle[10] > 0:
            celle[11] = celle[10]
            celle[10] = 0

        if celle[10] == 0 and celle[9] > 0:
            celle[10] = celle[9]
            celle[9] = 0

        if celle[9] == 0 and celle[8] > 0:
            celle[9] = celle[8]
            celle[8] = 0
        #riga 4
        if celle[15] == 0 and celle[14] > 0:
            celle[15] = celle[14]
            celle[14] = 0

        if celle[14] == 0 and celle[13] > 0:
            celle[14] = celle[13]
            celle[13] = 0

        if celle[13] == 0 and celle[12] > 0:
            celle[13] = celle[12]
            celle[12] = 0

def somma_destra():
    for i in range(3):
        t.sleep(0.05)
        #riga 1
        if celle[1] == celle[0]:
            celle[1] = celle[1]*2
            celle[0] = 0

        if celle[2] == celle[1]:
            celle[2] = celle[2]*2
            celle[1] = 0

        if celle[3] == celle[2]:
            celle[3] = celle[3]*2
            celle[2] = 0
        #riga 2
        if celle[5] == celle[4]:
            celle[5] = celle[5]*2
            celle[4] = 0
        
        if celle[6] == celle[5]:
            celle[6] = celle[6]*2
            celle[5] = 0
        
        if celle[7] == celle[6]:
            celle[7] = celle[7]*2
            celle[6] = 0
        #riga 3
        if celle[9] == celle[8]:
            celle[9] = celle[9]*2
            celle[8] = 0

        if celle[10] == celle[9]:
            celle[10] = celle[10]*2
            celle[9] = 0

        if celle[11] == celle[10]:
            celle[11] = celle[11]*2
            celle[10] = 0
        #riga 4
        if celle[13] == celle[12]:
            celle[13] = celle[13]*2
            celle[12] = 0

        if celle[14] == celle[13]:
            celle[14] = celle[14]*2
            celle[13] = 0

        if celle[15] == celle[14]:
            celle[15] = celle[15]*2
            celle[14] = 0
import os
clearConsole = lambda:os.system('cls')


while True:
    if k.is_pressed("w"):
        print("UP")
        somma_su()
        schift_su()
        somma_su()
        schift_su()
        printe=1
        nuovo = 1
    if k.is_pressed("s"):
        print("DOWN")
        somma_giu()
        schift_giu()
        somma_su()
        schift_giu()        
        printe=1
        nuovo = 1
    if k.is_pressed("a"):
        print("LEFT")
        somma_sinistra()
        schift_sinistra()
        somma_sinistra()
        schift_sinistra()
        printe=1
        nuovo=1
    if k.is_pressed("d"):
        print("RIGHT")
        somma_destra()
        schift_destra()
        somma_destra()
        schift_destra()
        printe=1
        nuovo=1







    

    if k.is_pressed("l") or repeat ==1 or nuovo==1:
        sium = random.randrange(0,15)
        if celle[sium] == 0:
            celle[sium]=celle[sium] =2
            printe = 1
            repeat = 0
            nuovo=0
        else:
            printe = 0
            repeat = 1
    
        

            




        
        if printe == 1:
            clearConsole()
            print("                                 ","--------------------------------------")
            print("                                 ","  |  ",celle[0],"  |  ",celle[1],"  |  ",celle[2],"  |  ",celle[3],"  |  ")
            print("                                 ","--------------------------------------")      
            print("                                 ","  |  ",celle[4],"  |  ",celle[5],"  |  ",celle[6],"  |  ",celle[7],"  |  ")
            print("                                 ","--------------------------------------")
            print("                                 ","  |  ",celle[8],"  |  ",celle[9],"  |  ",celle[10],"  |  ",celle[11],"  |  ")
            print("                                 ","--------------------------------------")
            print("                                 ","  |  ",celle[12],"  |  ",celle[13],"  |  ",celle[14],"  |  ",celle[15],"  |  ")
            print("                                 ","--------------------------------------")
            print(" ")  
            print(" ")  
        
    
