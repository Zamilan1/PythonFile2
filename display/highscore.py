def main():
    num_students = int(input('Enter the num studentt:'))
    outfile = open(r'C:\Users\me\Desktop\display\files\score92.txt','w')
    for i in range(num_students):
        name = input('Enter the student name:')
        score = int(input('Enter the score:'))
        outfile.write(name +'\n')
        outfile.write(str(score)+'\n')
    outfile.close()
main()