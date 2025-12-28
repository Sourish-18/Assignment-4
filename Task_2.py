data_write = str (input ("Enter the text to be written into the file: "))
with open ("output.txt", "w") as file_handler:
    file_handler.write (data_write + "\n")
    print ("Data successfully written into output.txt\n")

data_append = str (input ("Enter the additional text to be appended: "))
with open ("output.txt", "a") as file_handler:
    file_handler.write (data_append + "\n")
    print ("Data successfully appended\n")

try:
    with open ("output.txt", "r") as file_handler:
        print ("Final content of output.txt")
        print (file_handler.read())
except FileNotFoundError:
    print ("Error: The file 'output.txt' was not found")