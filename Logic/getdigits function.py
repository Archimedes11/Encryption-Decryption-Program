def getdigits(number):
    b=number
    
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



def main():
    number=int(input("Num? "))
    first,second,third,stringed=getdigits(number)
    print(first)
    print(second)
    print(third)
    print(stringed)

main()
    