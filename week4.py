def modify_content(content):
    """
    Modify the content of the file.
    For now, this function converts all text to uppercase.
    """
    return content.upper()

def main():
    input_filename = input("Enter the name of the file to read from: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified = modify_content(content)

        # Create new output filename
        output_filename = "modified_" + input_filename

        # Write modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified)

        print(f"\n✅ File processed successfully!")
        print(f"➡️  Modified content written to: {output_filename}")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"\n❌ Error: You don’t have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()