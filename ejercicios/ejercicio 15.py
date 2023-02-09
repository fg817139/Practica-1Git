def determine_polidrome(text):
    text = str(text).lower().replace('','')
    return text==text[::-1]
text = str(input("please enter the string"))
answer= determine_polidrome(text)

if answer:
    print("yes, it is a")
else:
    print("no")
