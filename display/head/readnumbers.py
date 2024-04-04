
def main():
    infile = open(r'C:\Users\me\Desktop\display\files\numbers.txt','r')
    numbers = infile.readline().split()  # split the line into a list of strings
    infile.close()
    numbers = [int(num) for num in numbers]  # convert the list of strings into a list of integers
    print(numbers)
main()