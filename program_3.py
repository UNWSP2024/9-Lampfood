#Elliott Morris, 3/24/2026, Average Numbers.py

#Function to sum all numbers in the file
def sum_numbers_from_file(filename):
    total = 0

    #Opens the file and gets the count
    try:
        with open(filename, 'r') as file:
            for line_number,line in enumerate(file):
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"Skipping line {line_number} due to an invalid value: {line.strip()}")

        #Displays the total
        print(f"\nSum of all numbers from file: {total}")

    #Handling for all errors
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not read '{filename}' due to encoding issues.")
    except IOError:
        print(f"Error: Could not read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    filename = "numbers.txt"
    sum_numbers_from_file(filename)

if __name__ == '__main__':
    main()
