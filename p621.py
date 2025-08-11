def Dispaly(No):
    
    for i in range(1,No+1):
        print("*",end="\t")

    print("")    
        
def main():
    print("Enter Numnber :")
    Value=int(input())

    Dispaly(Value)
   
if __name__=="__main__":
    main()