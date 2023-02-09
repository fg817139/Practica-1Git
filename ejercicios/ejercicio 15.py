def determine_polidrome(text):
    text = str(text).lower().replace('','')
    return text==text[::-1]
text = str(input("please enter the string"))
answert= determine_polidrome(text)

if answert:
    print("yes, it is a")
else:
    print("no")
