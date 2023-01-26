import docx
import os

def change_author(folder_path, new_author):
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            doc = docx.Document(file_path)
            doc.core_properties.author = new_author
            doc.save(file_path)

# Change the author of all .docx files in the 'documents' folder to 'what_name_do_you_want'
change_author('folder_path', 'what_name_do_you_want')