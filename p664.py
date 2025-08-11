def Replace(data):
    
    i=0
    for i in range(len(data)):
        if(data[i]=='a'):
            data[i]='_'  #error ()
        
def main():
    print("Enter a String")
    str=input()

    Replace(str)
    print(f"updateed String  in {str}")
        
if __name__=="__main__":
    main()