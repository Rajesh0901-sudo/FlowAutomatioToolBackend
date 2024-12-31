
from utils.check_existing_file import check_file_status
import os
import csv

def make_file_path(folder_path,db_name,tableName,flow_name):

    new_file_name = flow_name + '_' + db_name + '_' + tableName + '.csv'

    new_folder_path = os.path.join(folder_path,'CSV_Files')

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    
    file_path = os.path.join(new_folder_path,new_file_name)

    print("New file name is-",new_file_name)

    return file_path

def save_results_to_csv(db_name,tableName,column_names, rows,folder_path, file_name,flow_name):

    if file_name == (None, ''):
        response = 'File name is empty'
        print(response)
        return 0
    
    elif column_names == (None, ''):
        response = 'Header name is empty'
        print(response)
        return 0
    
    elif rows == (None, ''):
        response = 'No Data Found to Save in Doc'
        print(response)
        return 0
    
    # checking the directory and making file path
    file_path = make_file_path(folder_path,db_name,tableName,flow_name)
    if_exisiting_doc = check_file_status(file_path)


    print("File Path",file_path," if Existing-",if_exisiting_doc)

    #if if_exisiting_doc == 1:
       
    #elif if_exisiting_doc == 2:
       
    #else:
        #print("Got and error")
        #return 0
    
    
    with open (file_path,'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        for row in rows:
            writer.writerow(row)

        print(f"Results saved to {file_path}")

   