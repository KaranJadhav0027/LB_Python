def Dispaly(No):
    i=1
    while(i<=No):
        print("\t*",end="")
        i=i+1 
    print("")  
def main():

    print("Enter Numnber :")
    Value=int(input())

    Dispaly(Value)
   
if __name__=="__main__":
    main()