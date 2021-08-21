sentence =input("Enter your sentence : ")
space = 0
for i in range(len(sentence)):
    if sentence[i] == " ":
        space+=1

print("Your sentece has ",space+1,"words")