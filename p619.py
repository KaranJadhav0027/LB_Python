def Dispaly(No):
    i=1
    while(i<=No):
        print("*")
        i=i+1 
        
def main():
    print("Enter Numnber :")
    Value=int(input())

    Dispaly(Value)
   
if __name__=="__main__":
    main()