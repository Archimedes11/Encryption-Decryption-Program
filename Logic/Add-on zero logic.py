
def main():
    x=input("Enter a number: ")
    y=int(x)
    if y <= 9:
        x="0"+x
    if y <=99:
        x="0"+x
    print(x)
    z=x.split()
    print(z)
main()

