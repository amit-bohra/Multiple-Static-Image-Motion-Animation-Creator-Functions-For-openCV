import cv2
import time
import random
speed=4
def getFirstImage(name):
    global speed
    a=cv2.imread(r'{}'.format(name))
    lenx=len(a[1,:])
    leny=len(a[:,1])
    modx=lenx%speed
    mody=leny%speed
    if(modx!=0 or mody!=0):
        if modx!=0:
            lenx+=modx
        if mody!=0:
            leny+=mody
        a=cv2.resize(a,(lenx,leny),interpolation=cv2.INTER_AREA)
    return a
r=getFirstImage('main.jpg')
imagex=len(r[1,:])
imagey=len(r[:,1])
def getAnotherImage(name):
    a=cv2.imread(r'{}'.format(name))
    global imagex, imagey
    a=cv2.resize(a,(imagex,imagey),interpolation=cv2.INTER_AREA)
    return a
s=getAnotherImage('two.jpg')
t=getAnotherImage('three.jpg')
u=getAnotherImage('one.jpg')
dino=cv2.imread(r'dino.jpg')
population=[r,s,t,u]
i=population[0].copy()
flag=0
flag2=0
flag3=1
old_i=population[0].copy()
while(True):
    count=0
    if(flag==1):
        count=-1
    random.shuffle(population)
    while(count<len(population)-1):
        x=0
        recount=count+1
        j=population[recount].copy()
        while(x!=len(j[1,:])):
            x+=speed
            a=0
            b=speed
            d=len(i[1,:])
            c=d-b
            copy1=j[:,a:b].copy()
            copy2=j[:,b:d].copy()
            copy3=i[:,b:d].copy()
            new_var=0
            while(new_var<1):
                ranger=range(0,994)
                i[387:390,:]=0
                range1=random.choice(ranger)
                i[392:395,range1:range1+6]=45
                new_var+=1
            cv2.imshow('show',i)
            key=cv2.waitKey(10)
            i[:,a:c]=copy3
            i[:,c:]=copy1
            j[:,a:c]=copy2
            if flag2==0:
                old_i[320:420,100:200]=i[320:420,100:200].copy()
                flag2=1
            if flag2==1 and flag3==1:
                i[320:420,100:200]=dino.copy()
            if key==ord('w'):
                flag3=0
            if flag3==0:
                i[320:420,100:200]=old_i[320:420,100:200]
                pixcounter=0
                while(pixcounter<100):
                    a1=320-pixcounter
                    b1=420-pixcounter
                    delay=0
                    while(delay!=1000):
                        delay+=1
                        pass
                    pixcounter+=1
                    q1=i[a1:b1,100:200].copy()
                    i[a1:b1,100:200]=q1
                    i[320-pixcounter:420-pixcounter,100:200]=dino.copy()
                    
        count+=1
        flag=1
    
    
                
