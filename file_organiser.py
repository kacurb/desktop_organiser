import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

folder_path = "C:/Users/urban/Desktop"
files = os.listdir(folder_path)

for file in files:
    print(file)

pdf_folder = os.path.join(folder_path, "PDF")
scr_folder = os.path.join(folder_path, "screeny")
jupyter_folder = os.path.join(folder_path, "jupyter")

if not os.path.exists(pdf_folder):
    os.mkdir(pdf_folder)
if not os.path.exists(scr_folder):
    os.mkdir(scr_folder)
if not os.path.exists(jupyter_folder):
    os.mkdir(jupyter_folder)

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    elif file.lower().endswith(('.pdf')):
        shutil.move(file_path, os.path.join(pdf_folder, file))
    elif file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        shutil.move(file_path, os.path.join(scr_folder, file))
    elif file.lower().endswith(('.ipynb')):
        shutil.move(file_path, os.path.join(jupyter_folder, file))