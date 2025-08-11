# input 721
# output:
#  10
def SumDigit(No):
    Digit=0
    sum=0
    while(No!=0):
        Digit=No%10
        sum=sum+Digit
        No=No//10
    return sum  

def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=SumDigit(Value)
    print(f"Digit Sum {Ret}")
   
if __name__=="__main__":
    main()