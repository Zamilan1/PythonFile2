# This is the main function that will be executed when the script is run
def main():
   # Initialize an empty string to store each line of the file
   line = ""
   # Initialize a counter variable to keep track of the line numbers
   counter = 0
       # Prompt user to enter the name of the file
   filename = input('Enter name of file\n')
   
   # Open the file with the given name and read-only permissions
   infile = open(r'C:\Users\me\Desktop\pythonFunction\Files\\' + filename, 'r')
   
   # Read the first line of the file
   line = infile.readline()
   # Increment the counter, since we have read the first line
   counter = 1
   
   # Iterate through the rest of the lines in the file
   for line in infile: 
       # Increment the counter for each line
       counter = counter + 1
       # Print the line number and the line itself
       print(counter, end='')
       print(':', end='')
       line = line.rstrip('\n')  # Remove any newline characters from the end of the line
       print(line)
   # Close the file after we are done reading from it
   infile.close()

# Call the main function to start the script
main()