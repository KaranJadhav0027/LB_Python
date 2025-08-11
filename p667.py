def StrUpr(data):

    output=""
    for ch in data:
        if(ch >='a' and ch <='z'):
            output=output+chr(ord(ch)-32)
        else:
           output=output+ch
                         
    return output

def main():
    print("Enter a String")
    str=input()

    strX=StrUpr(str)
    print(f"updateed String  in {str} is  {strX}")
        
if __name__=="__main__":
    main()