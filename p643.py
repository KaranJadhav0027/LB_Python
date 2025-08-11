
def CountEvemOdd(Brr):
    EvenCount=0
    OddCount=0
    for no in Brr:
        if(no%2==0):
            EvenCount+=1
        else:
            OddCount+=1

    return EvenCount,OddCount

def main():
    print("Enter the number of element")
    Length=int(input())
    
    Arr=[]
    print("Please enter the elements")
    for i in range(1,Length+1):
        no=int(input())
        Arr.append(no)
        
    Even,Odd=CountEvemOdd(Arr)
    print(f"Number of Even element in List  are: {Even}")
    print(f"Number of Even element in List  are: {Odd}")

    
if __name__=="__main__":
    main()