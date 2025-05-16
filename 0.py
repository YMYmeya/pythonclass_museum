import os
import platform
from pathlib import Path

FOLDER = Path('./my_folder')

# 创建文件夹（如果不存在）
try:
    FOLDER.mkdir(exist_ok=True)
    print(f"Folder '{FOLDER}' created or already exists")
except Exception as e:
    print(f"Error creating folder: {e}")
    exit(1)

# 创建10个文本文件
for i in range(10):
    file_path = FOLDER / f"{i}.txt"
    try:
        file_path.touch()  # 创建空文件
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")

# 打开文件夹（跨平台支持）
try:
    if platform.system() == "Windows":
        os.startfile(FOLDER)
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open "{FOLDER}"')
    else:  # Linux
        os.system(f'xdg-open "{FOLDER}"')
except Exception as e:
    print(f"Error opening folder: {e}")