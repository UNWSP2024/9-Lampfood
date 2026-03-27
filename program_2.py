#Elliott Morris, 3/23/2026, Random Number File Writer.py

import random

def get_number_count():
    #Get a number between 1 and 1000 from the user
    while True:
        try:
            count = int(input("How many random numbers do you want to generate? (1 - 1000): "))
            if 1 <= count <= 1000:
                return count
            else:
                print("Please enter a number between 1 and 1000")
        except ValueError:
            print("Please enter a valid integer (whole number)")

def write_to_file(count, filename):
    #Write random numbers to a file
    try:
        with open(filename, "w") as file:
            for i in range(count):
                file.write(str(random.randint(1, 100)) + "\n")
                print(f"{count} random numbers written to {filename}")
    except IOError:
        print("Error: There was a problem writing to the file.")
    except PermissionError:
        print(f"Error: You do not have permission to write to this location")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    filename = "random_numbers.txt"
    count = get_number_count()
    write_to_file(count, filename)

if __name__ == "__main__":
    main()
