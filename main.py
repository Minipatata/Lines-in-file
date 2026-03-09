#Write a Python program that can calculate and return the total number of lines 
# present inside a file. First, you would be required to read the contents of the file
d=open("demo.txt","r")
count=0
for lines in d:
    print(lines)
    count=count+1
print(count)