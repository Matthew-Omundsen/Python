#Author: Matthew Omundsen
#Date: 10/28/24
#Program description: reading writing files lab

#read each line of an input file containing 1 integer per line
#program will write the line to an output file if number is between 1-999

#ask user for name of input file
#ask user for name of output file
#ask user if they want to append or overwrite the output file
#write all lines from input file to the output file if number is 1-999
#print message to screen saying program completed
#assume each line contains 1 integer

#Asks user for input file
inputfile = input("What is the full name of your input file? (Include \n"
                  "the .txt string at the end) ")
infile = open(inputfile,'r') #opens input file

#Asks user for output file and opens it
outputfile = input("What is the full name of your output file? (Include"
            "\nthe .txt string at the end) ")

user_choice = input("Would you like to append or overwrite this file? \n"
                    "Type a to append or type w to overwrite.) ")
outfile = open(outputfile,user_choice)

for line in infile:#reads each line
    number = int(line)
    if number > 0 and number < 1000:
        outfile.write(line)#only writes line to outfile if number is 1-1000

infile.close()
outfile.close()

print("Program complete! Go look at your file")

        
