def main():
    infile = open(r'C:\Users\me\Desktop\display\files\cities.txt','r') #open the file for reading
    cities = infile.readlines()

    infile.close()

    index = 0

    while index < len(cities):

        cities[index] = cities[index].rstrip('\n')

        index += 1

        print(cities)
main()