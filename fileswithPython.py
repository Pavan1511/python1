#use open funtion to handle files with read or write permissions
file = open("examplefile.txt",'r') # open file examplefile.txt with read permissions

content = file.read() # read the file content

print(content) # print the content