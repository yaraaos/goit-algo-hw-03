import os
import shutil
import sys
from pathlib import Path

def copy_files(source, destination):
    try:
        # Створення директорії призначення
        os.makedirs(destination, exist_ok=True)
        
        # Перебір всіх файлів і директорій у source
        for item in os.listdir(source):
            full_path = os.path.join(source, item)
            if os.path.isdir(full_path):
                # Рекурсивний виклик функції для директорії
                copy_files(full_path, destination)
            else:
                # Визначення піддиректорії на основі розширення файлу
                ext = Path(item).suffix[1:] or "no_extension"
                ext_dir = os.path.join(destination, ext)
                os.makedirs(ext_dir, exist_ok=True)
                
                # Копіювання файлу в відповідну піддиректорію
                shutil.copy(full_path, ext_dir)
                print(f"Copied {item} to {ext_dir}")
                
    except Exception as e:
        print(f"Error processing {source}: {e}")

def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Виклик функції копіювання файлів
    copy_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()
