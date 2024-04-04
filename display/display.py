def main():
  filename = input('Enter file name')
  infile = open(r'C:\Users\me\Desktop\pythonfunction\Files\\'+filename,'r')
  contents = infile.read()
  print(contents)
  infile.close()
main()