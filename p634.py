
def CheckPerfect(No):
    sum=0 
    for i in range(1,(No//2)+1):
        if(No%i==0):
            sum+=i
    return(sum==No)
        
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=CheckPerfect(Value)

    if(Ret):
        print(f"{Value} is perfect Number")
    else:
        print(f"{Value} is Not perfect Number")

if __name__=="__main__":
    main()