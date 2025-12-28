try: 
    with open ("sample.txt", "r") as file_handler:
        
        print ("Reading file content: ")
        line_1 = file_handler.readline()
        line_2 = file_handler.readline()
        line_3 = file_handler.readline()
        line_4 = file_handler.readline()

        print (f"Line 1: {line_1}")
        print (f"Line 2: {line_2}")
        print (f"Line 3: {line_3}")
        print (f"Line 4: {line_4}")

except FileNotFoundError:
    print (f"Error: The file 'sample.txt' was not found")