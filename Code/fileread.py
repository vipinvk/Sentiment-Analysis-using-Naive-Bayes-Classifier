
import os
import json 

class dataread:
     '''
     This class will be used for reading/copying 
     the required data for this project
     '''

     def __init__(self):
          '''
          Setting the (absolute directory) path values for the files 
          '''
          cwd = os.path.dirname(os.path.realpath(__file__))
          rel_path = r"..\Data\\"
          self.data_path = os.path.join(cwd,rel_path)
          self.data_file=[]

     def read_file(self,label,data_file):
          '''
          Function for reading the files from Data directory.
          Inputs variables : label/folder name, path to the Data folder
          Return variables : file contents from the specified Folder
          '''
          self.data_file = data_file
          self.file_path = os.path.join(self.data_path,label)
          label = label[0:3]
          for filename in os.listdir(self.file_path):
               with open(str(self.file_path+"\\"+filename),mode='r',encoding="utf8") as file:
                    data=file.read()
                    self.data_file.append((data,str(label)))
          return self.data_file
'''
     def json_read(self,name):
          #Function for reading JSON file types 

          with open(str(self.data_path+"\\"+name),mode='r',encoding='utf-8') as file:
               jsondata = json.load(file)          
          return jsondata
'''