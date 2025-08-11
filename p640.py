
def Addition(Brr):
    sum=0
    for no in Brr:
        sum=sum+no

    return sum

def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    Ret=Addition(Arr)
    print(f"Addition of all element in List : {Ret}")
if __name__=="__main__":
    main()