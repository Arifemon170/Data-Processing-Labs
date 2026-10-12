word=input("input a word")
vw=set()
sp=0
for x in word.lower():
    if x in "aeiou":
        vw.add(x)
    elif x ==" ":
        sp+=1
        
print("number of charecters:",len(word))
print("number of vowels:",len(vw))
print("number of spaces:",sp)




        