# import zipfile
# import os
#
#
# file_list = os.listdir(".")
# for file in file_list:
#     if zipfile.is_zipfile(file):
#         z = zipfile.ZipFile(file, 'r')
#         if zipfile.is_zipfile(z):
#             k = zipfile.ZipFile(z, 'r')
