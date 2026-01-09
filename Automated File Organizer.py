import os
import shutil

source_folder = "Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Excel": [".xlsx", ".xls"],
    "CSV": [".csv"]
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, file))
                moved = True
                break

        if not moved:
            os.makedirs("Others", exist_ok=True)
            shutil.move(file_path, os.path.join("Others", file))