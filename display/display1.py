def main():
    try:
        filename = input('Enter file name: ')
        with open(filename, 'r') as infile:
            contents = infile.read()
            print(contents)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    main()