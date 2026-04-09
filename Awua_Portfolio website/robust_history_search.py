import os
import sys

root = r'C:\Users\Alom\AppData\Roaming\Code\User\History'

def search():
    for r, d, files in os.walk(root):
        for f in files:
            path = os.path.join(r, f)
            try:
                # Look for files larger than 28KB and smaller than 30KB
                size = os.path.getsize(path)
                if 28000 < size < 30000:
                    # Let's read it and check if it contains "Awua"
                    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        if "Awua" in content:
                            print(f"FOUND: {path} (Size: {size})")
            except Exception as e:
                pass

search()
