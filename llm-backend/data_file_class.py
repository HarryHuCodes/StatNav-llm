from datetime import datetime 



class Data_file:


    def __init__(self, name, file_type, created_on, content, organization, details=None, importance=None,  document_id=-1):
        self.doc_name = name                 
        self.doc_type = file_type                  
        self.last_modified = created_on    
        self._doc_content = content               
        self.doc_details = details                 
        self.doc_id = document_id
        self.organization = organization    
        self.doc_importance = importance     #bool
    """  if size is None:
            self.size = "no limit"        
        else:
            self.size = size       """                   #int 
     


#Method to convert obj instance into dictionary

    def to_dict(self):

        file_dict = {
           "doc_id": self.doc_id,
           "organization": self.organization,
           "doc_name": self.name,
           "doc_type": self.type,
           "doc_content" : self._doc_content,
           "last_modified": self.last_modified,
           "doc_details": self.doc_details,
           "doc_importance" : self.doc_importance
        }  
       
        return file_dict
    


    def set_details(self, file_description):
        self.doc_details = file_description

    def get_details(self):
        return self.doc_details
    
    def get_content(self):
        return self._doc_content

    def modify_datetime(self, new_time):
        self.last_modified = new_time

    def get_datetime(self):
        return self.last_modified
    
    def get_doc_details(self):
        if(self.doc_details == None):
            self.doc_details = "Not mentioned"
        return self.doc_details


    def mark_importance(self, important):
        self.doc_importance = important
