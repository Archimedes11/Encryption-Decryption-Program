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


    
    
    datastr = infile.read() 
    
    
    datalst = datastr.split("\n")
    #print(list(datastr))
    num=(len(datalst)+1)
    x=""
    p=4
    
    header=datalst[0:3]
    print(header)
    
    for i in range(4,num):
        if p < len(datalst):
            x+=datalst[i]
            p+=1
            
        
    x=x.split()
    
    g=0
    h=9

    
    for i in range(messagelen):
        p=0
        for t in range(g,h,3):
            if p==0:
                number=messagelst[i]
                firstm,secondm,thirdm,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
                newnumber=first+second+firstm
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr
            
            if p==1:
                number=messagelst[i]
                firstm,secondm,thirdm,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
                newnumber=first+second+secondm
                newnumint=int(newnumber)
                newnumstr=str(newnumint)
                x[t]=newnumstr            

            if p==2:
                number=messagelst[i]
                firstm,secondm,thirdm,stringed=getdigits(number)
            
                number=x[t]
                first,second,third,stringed=getdigits(number)
                
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
    zz=z+"\n"+headertwo+"\n"+y
    print(zz)
    
    
    
    
   

    
    file = open("jellytext2.txt", 'w')
    file.write(zz + '\n') 
    
    infile.close()
    file.close()
    
    print("done")
      
    
      
        


    
    
    
       
    
        
        


           
    
insert()