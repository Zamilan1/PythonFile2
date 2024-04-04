def main():
    cities = [ 'Dublin', ' Cork','Belfast', 'Galway']
#r ---> raw data   'w'---> write
    outfile = open(r'C:\Users\me\Desktop\display\files\cities.txt','w')

    for item in cities:

        outfile.write(item + '\n')

    outfile.close()

main()