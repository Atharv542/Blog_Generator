import zipfile
import os

def create_zip(files: dict):
    zip_path = "generated_project.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for path, content in files.items():
            full_path = f"temp/{path}"
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

            zipf.write(full_path, path)

    return zip_path