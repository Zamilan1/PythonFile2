def main():
    line = ""
    counter = 0
    file_name = input('Enter name of file')
    infile = open(r'C:\Users\me\Desktop\pythonFunction\Files\\' +file_name,'r')
    line = infile.readline()
    counter = 1
    while line != "" and counter <=5:
        line =line.rstrip('\n')
        print(line)
        line = infile.readline()
        counter = counter +1
        infile.close()
main()  