import sys

def analyze_files(i_file, o_file):
    try:
        
        with open(i_file, 'r') as input_file:
            content = input_file.read()

        
        with open(o_file, 'w') as output_file:
            output_file.write(content)

        print("File processing completed successfully.")
    except FileNotFoundError:
        print(f"Error: The input file '{i_file}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when writing to '{o_file}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python program.py {input_file_path} { output_file_path}")
        sys.exit(1)

    i_file = sys.argv[1]
    o_file = sys.argv[2]

    analyze_files(i_file, o_file)
