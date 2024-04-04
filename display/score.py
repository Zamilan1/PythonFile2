def main ():
    high_score = 0 
    high_scorer = ''

    name = ''
    score = 0
    
    counter = 0
    infile = open(r'C:\Users\me\Desktop\display\files\score9.txt','r')

    name = infile.readline()

    while name != '': # not at the of the file
        counter = counter +1
        score = int(infile.readline())

        if score > high_score:
            high_score = score
            
            high_scorer = name.rstrip('\n')
        name = infile.readline()
    print('Name of the highest scorer:',high_scorer)
    print('Student score:',score)
    print('Number of records in file counter:',counter)
    infile.close()
main() 