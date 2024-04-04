def main():
   
   line = ''

   total = 0.0

   number = 0.0

   infile = open(r'C:\Users\me\Desktop\display\files\numbers.txt','r')

   for line in infile:
      
      number = float(line)

      total = total + number

   infile.close()
   
   print('Total from this file is :',total)
   
main()


