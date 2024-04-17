import shutil
import os

# Enter username
user = 'edberthandjaja'

# Handle Desktop Cleaning
# Screenshots
if not os.path.exists('/Users/' + user + '/Desktop/ScreenShots'):
    #os.makedirs('/Users/' + user + '/Desktop/ScreenShots')
    print('Creating folder')
# School
elif not os.path.exists('/Users/' + user + '/Desktop/School'):
    #os.makedirs('/Users/' + user + '/Desktop/School')
    print('Creating folder')
    

files_on_desktop = os.listdir('/Users/' + user + '/Desktop')
for file in files_on_desktop:
    file_dir_desktop = '/Users/' + user + '/Desktop' + '/' + file
    if file.startswith('Screenshot'):
        #shutil.move(file_dir_desktop, '/Users/' + user + '/Desktop/ScreenShots')
        print(f'Moving {file}...')
    elif file.startswith('Math') or file.startswith('Comp') or file.startswith('Gen'):
        #shutil.move(file_dir_desktop, '/Users/' + user + '/Desktop/School')
        print(f'Moving {file}...')

# Handle Downloads Cleaning
# Installers
if not os.path.exists('/Users/' + user + '/Downloads/Installers'):
    #os.makedirs('/Users/' + user + '/Desktop/Installers')
    print('Creating folder')
# Images
if not os.path.exists('/Users/' + user + '/Downloads/Images'):
    #os.makedirs('/Users/' + user + '/Desktop/Images')
    print('Creating folder')

files_on_downloads = os.listdir('/Users/' + user + '/Downloads')
for file in files_on_downloads:
    file_dir_downloads = '/Users/' + user + '/Desktop' + '/' + file
    
    if file.endswith('dmg'):
        #shutil.move(file_dir_downloads, '/Users/' + user + '/Desktop/Installers')
        print(f'Moving {file}...')
    elif file.endswith('png') or file.endswith('jpeg') or file.endswith('HEIC') or file.endswith('jpg'):
        #shutil.move(file_dir_downloads, '/Users/' + user + '/Desktop/Images')
        print(f'Moving {file}...')
