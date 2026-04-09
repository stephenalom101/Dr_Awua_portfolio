import base64

with open('tmp_seplat_b64.txt', 'r') as f:
    b64 = f.read().strip()

with open('logo_seplat.png', 'wb') as f:
    f.write(base64.b64decode(b64))

with open('tmp_shell_b64.txt', 'r') as f:
    b64 = f.read().strip()

with open('logo_shell.png', 'wb') as f:
    f.write(base64.b64decode(b64))
