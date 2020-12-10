
def getdigits(number):
    b=int(number)
    
    c=b//100
    
    d=b-(c*100)
    
    e=d//10
    
    f=b-((c*100)+(e*10))
    first=str(c)
    second=str(e)
    third=str(f)
    stringed=first+second+third
    nums=int(stringed)
  
    return (first,second,third,stringed)






def insert():
    
    print("")
    print("Inserting a message")
    print("")
    
    filename = input("Filename? ")
    
    OpenOk = False
    while not OpenOk :
        try :
            infile = open(filename, 'r')
            OpenOk = True
        except IOError :
            print("File will not open")
            filename = input("Filename? ")
    
    message=input("Message? ")
    messagelst = list(message)
    messagelen=len(messagelst)
    
    for i in range(0,messagelen):
            messagelst[i]=ord(messagelst[i]) 
    
    for i in range(0,messagelen):
        a=str(messagelst[i])
        b=int(a)
        if b <= 9:
            a="0"+a
        if b <=99:
            a="0"+a
        messagelst[i]=a
    
    
    messagelenstr=str(messagelen)
    a=messagelenstr
    if messagelen <= 9:
        a="0"+a
    if messagelen <=99:
        a="0"+a
    messagelenstr=a
    
    
    datastr = infile.read() 
    
    datalst = datastr.split("\n")
    num=(len(datalst)+1)
    x=""
    p=4
    
    header=datalst[0:3]
    
    
    for i in range(4,num):
        if p < len(datalst):
            x+=datalst[i]
            p+=1
            
        
    x=x.split()
    
    
    k=0
    for t in range(0,9,3):
        number=messagelenstr
        firstmls,secondmls,thirdmls,stringed=getdigits(number)
        
        number=x[t]
        first,second,third,stringed=getdigits(number)        
        
        if k==0:
            
            number=int(number)
                        
            if number>=100:
                newnumber=firstmls+second+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=10 and number<=99:
                newnumber=first+firstmls+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=0 and number<=9:
                newnumber=first+second+firstmls
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr                 
                            
                            
                            
                    
        if k==1:
            
            number=int(number)
                        
            if number>=100:
                newnumber=secondmls+second+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=10 and number<=99:
                newnumber=first+secondmls+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=0 and number<=9:
                newnumber=first+second+secondmls
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr            
        
        if k==2:
            
            number=int(number)
                        
            if number>=100:
                newnumber=thirdmls+second+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=10 and number<=99:
                newnumber=first+thirdmls+third
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            if number>=0 and number<=9:
                newnumber=first+second+thirdmls
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr        
        k+=1

    g=9
    h=19

    
    for i in range(messagelen):
        p=0
        for t in range(g,h,3):
            if p==0:
                number=messagelst[i]
                firstm,secondm,thirdn,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
                number=int(number)
                
                if number>=100:
                    newnumber=firstm+second+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=10 and number<=99:
                    newnumber=first+firstm+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=0 and number<=9:
                    newnumber=first+second+firstm
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr                 
                    
                    
                    
            
            if p==1:
                number=messagelst[i]
                firstm,secondm,thirdm,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
                number=int(number)
                
                if number>=100:
                    newnumber=secondm+second+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=10 and number<=99:
                    newnumber=first+secondm+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=0 and number<=9:
                    newnumber=first+second+secondm
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr            

            if p==2:
                number=messagelst[i]
                firstm,secondm,thirdm,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
                number=int(number)
                
                if number>=100:
                    newnumber=thirdm+second+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=10 and number<=99:
                    newnumber=first+thirdm+third
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr
                if number>=0 and number<=9:
                    newnumber=first+second+thirdm
                    newnumint=int(newnumber)
                    newnumstr=str(newnumint)
                    x[t]=newnumstr                
            
            p+=1
        h+=9
        g+=9
    
    
    for i in range(1,len(header)+2,2):
        header.insert(i,'\n')    
    
    for i in range(15,len(x),15):
        x.insert(i,'\n')
    headertwo=str((datalst[3]).lstrip())
      
    y=' '.join(x)
    spacebar=""
    z=spacebar.join(header)
    zz=z+"\n"+" "+headertwo+"\n"+" "+y
    
    file = open("jellytext2.ppm", 'w')
    file.write(zz + '\n') 
    
    infile.close()
    file.close()
    
    print("done")
insert()    