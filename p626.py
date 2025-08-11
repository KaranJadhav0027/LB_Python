
def CountEvenDigit(No):
    Digit=0
    Count=0
    while(No!=0):
        Digit=No%10
        if(Digit%2==0):
            Count=Count+1
        No=No//10
    return Count 

def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=CountEvenDigit(Value)
    print(f"Number of Even digit in {Value} are  {Ret}")
   
if __name__=="__main__":
    main()