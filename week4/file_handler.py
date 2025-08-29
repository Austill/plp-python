def read_and_write_file(input_file, output_file):
    try:
        # Read content from input file
        with open(input_file, 'r') as f:
            content = f.read()

        # Modify content (example: uppercase)
        modified_content = content.upper()

        # Write to output file
        with open(output_file, 'w') as f:
            f.write(modified_content)

        print(f"✅ File '{input_file}' read successfully. Modified version written to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read/write.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# ---- Main Program ----
if __name__ == "__main__":
    input_file = input("Enter the filename to read: ")
    output_file = "modified_" + input_file
    read_and_write_file(input_file, output_file)
