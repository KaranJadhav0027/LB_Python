
def Reverse(No):
    Rev=0
    Digit=0
    while(No!=0):
        Digit=No%10
        Rev=Rev*10+Digit
        No=No//10
        
    return Rev
    
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=Reverse(Value)
    print(f"Reverse number of {Value} is {Ret}")   

if __name__=="__main__":
    main()