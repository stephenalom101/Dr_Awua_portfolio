import os

h = r'C:\Users\Alom\AppData\Roaming\Code\User\History'
if not os.path.isdir(h):
    print("History directory not found")
    exit(1)

files = []
for dp, dn, fn in os.walk(h):
    for f in fn:
        files.append(os.path.join(dp, f))

files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

for i in range(min(30, len(files))):
    path = files[i]
    size = os.path.getsize(path)
    print(f"{size} bytes: {path}")
