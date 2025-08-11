def Addition(No):
    
    sum=0
    for i in range(1,No+1):
        sum=sum+i
    return sum
        
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret= Addition(Value)
    print(f"Addition is :{Ret}")
   
if __name__=="__main__":
    main()