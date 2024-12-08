import os

def check_file_status(file_name):

    try:
        if os.path.exists(file_name):
            print("File exists appending it to the last")
            return 1
        
        else:

            print("File does not exist creaing new file")
            return 2
        
    except Exception as e:
        print("An error occured while fetching document",e)
        return 0
        
