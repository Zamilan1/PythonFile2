def main():
    contents =""
    infile = open(r'C:\Users\me\Desktop\display\Files\numbers.txt','r')
    contents = infile.read()
    infile.close()
    print(contents)
main()