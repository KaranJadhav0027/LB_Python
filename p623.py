def Factorial(No):
    
    Fact=1
    for i in range(1,No+1):
        Fact=Fact*i
    return Fact
        
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret= Factorial(Value)
    print(f"Addition is :{Ret}")
   
if __name__=="__main__":
    main()