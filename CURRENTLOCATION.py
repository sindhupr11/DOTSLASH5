import csv
import random as r
import time
import CURRENTCSVSPLITTER,motorread

def qread():
    with open("QINDEX.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        row=len(data) 
        a=data[row-2][0]
        
        print(row)
        csvfile.close()
        print("done")
        return a


def put1 (temp,hum,moist,crx,cry,qindex,motorstate):
    with open("CURRENT.csv",mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([temp,hum,moist,crx,cry,qindex,motorstate]) 
        csvfile.close()
        print("done")


x=1
y=1
con=0
while(1):
    

    if con==0:
        for a in range (1,4):
            for b in range (1,4):
                temp=r.randint(28,30)
                hum=r.randint(75,80)
                moist=r.randint(80,90)
                qindex=r.randint(1,6) #1-5 moisture  (6, red)

                crx=a
                cry=b
                motorstate=motorread.motorstate()
                time.sleep(1)
                put1(temp,hum,moist,crx,cry,qindex,motorstate)
                CURRENTCSVSPLITTER.do()

                
        

    if con==1:
        temp=r.randint(28,30)
        hum=r.randint(75,80)
        moist=r.randint(80,90)
        
        crx=input('ENTER THE X COORDINATE : ')
        cry=input('ENTER THE Y COORDINATE : ')
        qindex=qread()
        #delay
        put1(temp,hum,moist,crx,cry,qindex)
        CURRENTCSVSPLITTER.do()
