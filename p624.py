# input 721
# output:
#  1 2 7
def DisplayDigit(No):
    Digit=0

    while(No!=0):
        Digit=No%10
        No=No//10
        print(Digit)

def main():
    print("Enter Numnber :")
    Value=int(input())

    DisplayDigit(Value)
   
if __name__=="__main__":
    main()