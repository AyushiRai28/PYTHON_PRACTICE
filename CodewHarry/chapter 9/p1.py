# check if a word is present in your text
f = open("file.txt")
content = f.read()
if("love" in content):
    print("The word LOVE is pressnt in the content")

else:
    print("The word LOVE is not present in the content")

 
f.close()