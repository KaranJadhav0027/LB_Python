
def occuranceDigit(No):
    count=0
    Digit=0
    while(No!=0):
        Digit=No%10
        if(Digit==5):
            count=count+1
        No=No//10
        
    return count
    
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=occuranceDigit(Value)
    print(f"Frequency of {Value} is {Ret}")   

if __name__=="__main__":
    main()