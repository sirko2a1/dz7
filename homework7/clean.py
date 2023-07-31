import os
import shutil

def clean(folder_path):
    categos = {
        '.txt': 'Text',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.pdf': 'Documents',
        '.xls': 'Spreadsheets',
        '.xlsx': 'Spreadsheets',
        '.ppt': 'Presentations',
        '.pptx': 'Presentations',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.mp4': 'Video',
        '.avi': 'Video',
        '.zip': 'Compressed',
        '.rar': 'Compressed'
    }

    files = os.listdir(folder_path)

    for file in files:
        ext = os.path.splitext(file)[1]

        if ext in categos:
            category = categos[ext]

            subfolder_path = os.path.join(folder_path, category)
            if not os.path.exists(subfolder_path):
                os.mkdir(subfolder_path)

            file_path = os.path.join(folder_path, file)
            shutil.move(file_path, subfolder_path)

def main():
    folder_path = input('патх фолдера: ')

    clean(folder_path)

    print('клінінг був завершений')
