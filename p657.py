def CountVowels(data):
    
    Count=0
    for ch in data:
        if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'or 
            ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
            Count+=1
    return Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountVowels(str)
    print(f"Frequency of Vowels in {str} is  {Ret}")
        
if __name__=="__main__":
    main()