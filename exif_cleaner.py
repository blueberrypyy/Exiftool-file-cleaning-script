import os
import glob
import shutil as sh
from time import sleep


# list all files tagged with "_original"
def list_originals():
    if glob.glob('*_originals') is None:
        print('No files tagged with "original" found. Exitting program.')
        sleep(2)
        exit()
    else:
        print('\nAll files tagged with "_original":')
        print(glob.glob('*_original'), '\n')
        sleep(2)

# Remove all original files
def remove_originals():
    print('\n* Removing all original files *\n')
    sleep(2)
    for item in glob.glob('*_original'):
        print(item, '- removed')
        os.remove(item)
    print('\nAll original files successfully deleted.')


# Program running
while True:
    select = input('Select your choice:\n[1] - Delete all original files\n[2] - List all original files\n[q] - quit\n>> ')
    if select == '1':
        remove_originals() 
        break
    if select == '2':
        list_originals()
        continue
    if select == 'q':
        break

    else:
        print('\nInvalid selection, try again.\n')
        sleep(0.8)
        continue
