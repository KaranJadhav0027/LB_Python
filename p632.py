
def SumFactors(No):
    sum=0 
    for i in range(1,(No//2)+1):
        if(No%i==0):
            sum+=i
    return sum

def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=SumFactors(Value)

    print(f"Summation of Factors of {Value} is :{Ret}")

if __name__=="__main__":
    main()