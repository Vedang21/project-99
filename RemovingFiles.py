import os
import shutil
import time

def main():
    #initialising the count
    deleted_folders_count=0
    deleted_files_count=0

    #specify the path
    path="/Users/Sandeep-lappy/Desktop/AngryBirdsStage7/bye/"
    isexist=os.path.exists(path)
    print(isexist)

    #specify the days
    days=30

    #converting days to seconds
    #time.time() returns current time in seconds
    seconds=time.time()-(days*24*60*60)

    #checking whether the file is present in the path
    if os.path.exists(path):

        #iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):

            #comparing the days
            if seconds>=get_file_or_folder_age(root_folder):
                
                #removing the folder
                remove_folder(root_folder)
                deleted_folders_count +=1

                #breaking after removing the folder
                break

            else:

                #checking folder from root folder
                for folder in folders:

                    #folder path
                    folder_path=os.path.join(root_folder, folder)

                    #comparing the days
                    if seconds>=get_file_or_folder_age(folder_path):
                        
                        #removing the folder
                        remove_folder(root_folder)
                        deleted_folders_count +=1

                for file in files:

                    #file path
                    file_path=os.path.join(root_folder, file)

                    #comparing the days
                    if seconds>=get_file_or_folder_age(file_path):
                        
                        #removing the path
                        remove_file(file_path)
                        deleted_files_count +=1

        else:

            #if the path is not a directory

            #comparing the days
            if seconds>=get_file_or_folder_age(file_path):
                        
                #removing the path
                remove_file(file_path)
                deleted_files_count +=1

    else:

        #file/folder not found
        print("path is not found")

    print("total folders deleted: ")
    print(deleted_folders_count)
    print("total files deleted: ")
    print(deleted_files_count)

def remove_folder(path):

    #removing the folder
    if not shutil.rmtree(path):

        #successful message
        print("Folder deleted successfully")

    else:

        #failure message
        print("Unable to delete the folder")

def remove_file(path):

    #removing the folder
    if not os.remove(path):

        #successful message
        print("File deleted successfully")

    else:

        #failure message
        print("Unable to delete the file")

def get_file_or_folder_age(path):

    #getting current time of the files/folders
    #time will be in seconds
    ctime=os.stat(path).st_ctime

    #returning the time
    return ctime

if __name__ == '__main__':
    main()
    print("hi")