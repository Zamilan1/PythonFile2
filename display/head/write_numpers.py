def main():

    numbers= [1,2,3,4,5,6,7]
    
    outfile = open(r'C:\Users\me\Desktop\display\files\numbers.txt','w')  #opens the file in read mode
    for item in numbers:
        outfile.write(str(item)+'\n')   #converts number to string and adds a newline character before writing it to
    outfile.close()
main()