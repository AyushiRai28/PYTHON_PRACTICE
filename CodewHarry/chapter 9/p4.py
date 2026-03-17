# replace words
word = "love"
with open("file.txt" , "r") as f:
          content = f.read()

contentnew = content.replace(word , "#"* len(word))
with open("file.txt" , "w") as f:
        f.write(contentnew)          