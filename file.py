def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nFile read successfully!\n")
    except FileNotFoundError:
        print("❌ Error: File not found.")
        return
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    # Modify content: make it uppercase (you can change this logic!)
    modified_content = content.upper()

    output_filename = input("Enter a name for the output file: ")

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}' successfully.")
    except PermissionError:
        print("❌ Error: You don't have permission to write to this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while writing: {e}")

if __name__ == "__main__":
    main()