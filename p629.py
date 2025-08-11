
def occuranceDigit(No):
    count4=0
    count5=0
    count7=0
    Digit=0

    while(No!=0):
        Digit=No%10
        if(Digit==4  ):
            count4=count4+1
        elif(Digit==5):
            count5=count5+1
        elif(Digit==7):
            count7=count7+1
        No=No//10
        
    return count4,count5,count7
    
def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret4,Ret5,Ret7=occuranceDigit(Value)
    print(f"Frequency of 4 is {Ret4} in {Value}") 
    print(f"Frequency of 5 is {Ret5} in {Value}")  
    print(f"Frequency of 7 is {Ret7} in {Value}")    

if __name__=="__main__":
    main()