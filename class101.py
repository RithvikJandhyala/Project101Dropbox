import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,excess_Token):
        self.excess_Token = excess_Token
    def uploadFiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.excess_Token)
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    excess_token = 'sl.BM0_UBCvlJJBWLYKA56DCldoYqANYFlS77g-925kctEKZYNYNV6SRybPboZgI5CnwrrJRNcgCLdQM3Rt9MAYjIaOQlKu1_oSChKePFSqE-L641puVKQ_btBy8POF4tB5HT3rAKs'
    transferData = TransferData(excess_token)
    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to the dropbox: ')
    transferData.uploadFiles(file_from,file_to)
    print('files have been moved')

main()
    
