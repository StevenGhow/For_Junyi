oriStr = input("input:")
word = oriStr.split(" ")
newWord = []
for i in word:
    newWord.append(i[::-1])

newStr = " ".join(newWord)
print(newStr)