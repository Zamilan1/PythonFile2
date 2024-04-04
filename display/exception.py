def main ():

    total = 0.0
    counter = 0.0
    number = 0.0



    try:

        infile = open(r'C:\Users\me\Desktop\display\files\numbers.txt','r')
        for line in infile:
            counter  = counter + 1 
            number = float(line)
            total = total +number
        infile.close()
        average = total /average
        print('The average is:',average)

    except IOError:
        print('An Error Occured while you trying Read the file')
    
    except ValueError:
        print('Non Numeric Data found in the file')
    except:
        print('An error Occured')
main()

