import os

# Define the directory path and the output text file path
directory_path = "C:\\Users\\XPS 8900\\Documents\\ActivePresenter\\Untitled1\\HTML5"
output_file_path = "C:\\Users\\XPS 8900\\Documents\\ActivePresenter\\Untitled1\\HTML5\\filenames.txt"

# Get the list of filenames from the directory
filenames = os.listdir(directory_path)

# Write the filenames to the text file
with open(output_file_path, 'w') as file:
    for filename in filenames:
        file.write(filename + '\n')
