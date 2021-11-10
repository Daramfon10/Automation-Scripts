"""
Approach for one file:
- Open the file and loop through the lines in the file.
- find the word in the line array.
- check if the substring exist in the string.
- print "word found" if the word has been found  
"""
#Enter the file path that you want to check in the 
inputFilesPathToCheck = "ENTER FILE PATH HERE"
searchWord = "ENTER SEARCH WORD HERE"

def searchFile():
    with open(inputFilesPathToCheck,"r") as f:
        for line in f:
            if searchWord in line:
                print("The word has been found")
                break


searchFile()





