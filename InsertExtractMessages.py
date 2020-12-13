

  #Purpose: To turn a character into a number and then find the hundreds, tens, and ones plase.
  #Pre-conditions: getdigits function receives either a number or a string of a number.
  #Post-conditions:To return four values: The hundreds, tens, and ones place of the number and then the number sting. 

def getdigits(number):
    #Do calculations to find the hundreds tens and ones place, and then find the stringed version of those.
    b=int(number)
    
    c=b//100
    
    d=b-(c*100)
    
    e=d//10
    
    f=b-((c*100)+(e*10))
    
    #Turn all the variables into strings
    first=str(c)
    second=str(e)
    third=str(f)
    stringed=first+second+third
    nums=int(stringed)
  
    #return the hundreds tens and ones digits of the number given.
    return (first,second,third,stringed)

#please hire me




#Purpose: To insert a secret message into a .ppm file
#Pre-conditions: User enters an i or I when asked if they want to insert or extract.s
#Post-conditions:The program will encode a secret message from the user into a .ppm file.
def insert():
    
    #Print header
    print("")
    print("Inserting a message")
    print("")
    
    #Get the filename from the the user.
    filename = input("Filename? ")
    
    #If the filename is a correct file then proceed else get a new filename.
    OpenOk = False
    while not OpenOk :
        try :
            infile = open(filename, 'r')
            OpenOk = True
        except IOError :
            print("File will not open")
            filename = input("Filename? ")
    
    #ask the user for the message they want to encode.
    message=input("Message? ")
    messagelst = list(message)
    messagelen=len(messagelst)
    
    #turn the message into ACII characters
    for i in range(0,messagelen):
            messagelst[i]=ord(messagelst[i]) 
    
    #add zeros to make all digits 3 numbers long
    for i in range(0,messagelen):
        a=str(messagelst[i])
        b=int(a)
        if b <= 9:
            a="0"+a
        if b <=99:
            a="0"+a
        messagelst[i]=a
    
    
    #add zeros to make all digits 3 numbers long
    messagelenstr=str(messagelen)
    a=messagelenstr
    if messagelen <= 9:
        a="0"+a
    if messagelen <=99:
        a="0"+a
    messagelenstr=a
    
    #get the data from a file
    datastr = infile.read() 
    
    #split up the lines of the file.
    datalst = datastr.split("\n")
    num=(len(datalst)+1)
    
    #Set k to an empty space and p to 4
    x=""
    p=4
    
    #distinguish the header of the program so that the .ppm will actually work
    header=datalst[0:3]
    
    
    #add the strings in the datalst into the variable x
    for i in range(4,num):
        if p < len(datalst):
            x+=datalst[i]
            p+=1
            
    #split up the lines of the list   
    x=x.split()
    
    
    k=0
    
    #change the numbers of the first part of the code for the length of the message
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

    
    #change the numbers of the rest of the numbers in the file to the coded message
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
    
    
    #add in new lines so that the picture file will actually display
    for i in range(1,len(header)+2,2):
        header.insert(i,'\n')    
    
    #add in new lines so that the picture file will actually display
    for i in range(15,len(x),15):
        x.insert(i,'\n')
    
    #strip the whitespacefrom part of the header so that the picture will display
    headertwo=str((datalst[3]).lstrip())
    
    #get the header to look nice and then save all of the file to the variable zz  
    y=' '.join(x)
    spacebar=""
    z=spacebar.join(header)
    zz=z+"\n"+" "+headertwo+"\n"+" "+y
    
    #write the new message to the file.
    file = open(filename, 'w')
    file.write(zz + '\n') 
    
    #cloase the file
    file.close()
    
    #let the user know that the insertion is done.
    print("Done insertion")
    




    #Purpose: To extract a coded message into a program
    #Pre-conditions: the user chooses to extract a message.
    #Post-conditions: A message in the file is displayed to the user.
def extract():
    print("")
    print("Extracting a hidden message")
    print("")
    
    #get a filename
    filename = input("Filename? ")
    
    #try to open the file, if it wont open get another file name
    OpenOk = False
    while not OpenOk:
        try :
            infile = open(filename, 'r')
            OpenOk = True
        except IOError :
            print("File will not open")
            filename = input("Filename? ")
    
    #save the data from the file
    datastr = infile.read() 
    datalst = datastr.split("\n")
    num=(len(datalst)+1)
    x=""
    p=4
    
    #get the header
    header=datalst[0:3]
    
    #add the data from the datalst into the variable x
    for i in range(4,num):
        if p < len(datalst):
            x+=datalst[i]
            p+=1
    
    #split the code up into seperate numbers
    x=x.split()
    
    
    
    k=0
    b=""
    
    
    for t in range(0,9,3):
        
        number=x[t]
        first,second,third,stringed=getdigits(number)        
        num=int(number)
        if num>=100:
            b+=first
        if num<=99 and num>=10:
            b+=second
        if num<=9:
            b+=third
        
        
            
    messagelen=b
    messagelenint=int(messagelen)
    
    
    g=9
    h=19
    c=""
    
    messagelst=[""]
    
    #recieve the actual message itself
    for i in range(messagelenint):
        for t in range(g,h-1,3):
            
            number=x[t]
            
            first,second,third,stringed=getdigits(number)        
            
            num=int(number)
            
            if num>=100:
                c+=first
            if num<=99 and num>=10:
                c+=second
            if num<=9:
                c+=third 
        
        g+=9
        h+=9       
            
        messagelst.insert(i,c)
        c=""
               
    messagelst.remove('')      

    spacebar=""
    
    #turn the message from numbers into actual ascii characters
    for i in range(messagelenint):
        messagelst[i]=chr(int(messagelst[i]))
    
    message=spacebar.join(messagelst)
    messagelenstr=str(messagelenint)
    
    #display to the user
    print("")
    print("The length of the message is " + messagelenstr)
    print("The message is " + message)
    print("")
    
        
    
    
    



#Purpose: To either insert a coded message into a file or decode a message from a file.
#Pre-conditions: User enters whether they want to insert or extract a message
#Post-conditions:The message is either inserted or extracted from the file.
def main():
    print("Steganography Assistant")
    #ask the user if they want to insert or extract.
    insertorextract=input("Do you want to insert a message or extract one (I/E)? ")
    
    #if they dont enter an i,I,e, or E then get a new input.
    while insertorextract != "i" and insertorextract != "I" and insertorextract != "e" and insertorextract != "E":
        print("Please enter an I or an E")
        insertorextract = input("Do you want to insert a message or extract one (I/E)?")
    
    #if they enter an i or I then insert else extract        
    if insertorextract == "i" or insertorextract == "I":
        insert()
    else:
        extract()
    print("Thanks for your business")
main()


    
