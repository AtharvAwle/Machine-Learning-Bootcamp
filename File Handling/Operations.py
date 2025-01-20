# Reading a file using python
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','r') as file:
    content = file.read()
    print(content)
    

# Read the file line by line
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','r') as file:
    for line in file:
        print(line)
        print(line.strip())  #.strip() removes the new line character
        
        

# Writing a File (overwriting ke saath)
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','w') as file:
    file.write("This is new statement with the new line char\n")
    file.write("Hello this is atharv awle\n")


# write a file (without overwriting) - Append operation
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','a') as file:
    file.write("Append operation\n")
    file.write("this is the next new line\n")
    
    
# writing the list of lines
l1 = ["first line\n" , "second line\n" , "third line\n" , "fourth line"]
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','a') as file:
    file.writelines(l1)


# Writing from one file to another file
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/atharv.txt','r') as file:
    content = file.read()
with open('/Users/atharvawle/Desktop/Machine Learning Bootcamp/File Handling/destination.txt','w') as file:
    file.write(content)
