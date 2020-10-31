import os


def print_file_content(path_to_file, ec):
    # Read content
    with open(path_to_file, "r", encoding=ec) as file:
        content = file.read()

    # Print the content
    print(content)


encoding = "utf-8"
file_name = "words.txt"

# If file exists delete it (So we can run same script multiple times)
if os.path.exists(file_name):
    os.remove(file_name)

# Create a file in write mode and write to it
with open(file_name, "w") as file:
    file.write("David \n")

# Print the file content
print_file_content(file_name, encoding)

# Append hebrew content
with open(file_name, 'a', encoding=encoding) as file:
    file.write('שלום לכולם')

# Print the file content
print_file_content(file_name, encoding)
