def main():
    total = 0.0

    counter = 0.0

    number = 0.0

    infile = open(r'C:\Users\me\Desktop\display\files\numbers.txt','r')

    for line in infile:

        counter = counter + 1

        number = float(line)

        total = total + number

    infile.close()
    average = total / counter
    print('Average is :',average)
main()