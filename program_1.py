#Elliott Morris, 3/23/2026, Item Counter.py

def count_file_lines(filename):
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                # Strip whitespace to ignore blank lines
                if line.strip():
                    count += 1

            return count

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not read '{filename}' due to encoding issues.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

def main():
    filename = "names.txt"
    result = count_file_lines(filename)
    if result is not None:
        print(f"There are {result} names in {filename}.")
    else:
        print("The program could not complete successfully.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    main()
