
def Minimum(Brr):
    Max=Brr[0]

    for no in Brr:
        if Max>no:
            Max=no

    return Max

def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    Ret=Minimum(Arr)
    print(f"Minimun element in List : {Ret}")
if __name__=="__main__":
    main()