import shutil
import os

# Enter username
user = 'edberthandjaja'

# Desktop Cleaning
desktop_path = '/Users/' + user + '/Desktop'
desktop_folders = {
    'ScreenShots': 'Screenshot',
    'School': ['Math', 'Comp', 'Gen']
}

for folder, prefixes in desktop_folders.items():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Created folder: {folder}')
    
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path):
            for prefix in prefixes:
                if file.startswith(prefix):
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f'Moved {file} to {folder}')
                    break  # Move to next file after first match

# Downloads Cleaning
downloads_path = '/Users/' + user + '/Downloads'
downloads_folders = {
    'Installers': 'dmg',
    'Images': ['png', 'jpeg', 'jpg', 'heic']
}

for folder, extensions in downloads_folders.items():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Created folder: {folder}')
    
    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)
        if os.path.isfile(file_path):
            for ext in extensions:
                if file.lower().endswith(ext):
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f'Moved {file} to {folder}')
                    break  # Move to next file after first match
