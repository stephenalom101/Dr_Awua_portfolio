import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    req_kf = urllib.request.Request('https://logo.clearbit.com/knightfrank.com', headers={'User-Agent': 'Mozilla/5.0'})
    with open('logo_kf_official.png', 'wb') as f:
        f.write(urllib.request.urlopen(req_kf, context=ctx).read())
    print("KF success")
except Exception as e:
    print(e)
    
try:
    req_shell = urllib.request.Request('https://logo.clearbit.com/shell.com', headers={'User-Agent': 'Mozilla/5.0'})
    with open('logo_shell_official.png', 'wb') as f:
        f.write(urllib.request.urlopen(req_shell, context=ctx).read())
    print("Shell success")
except Exception as e:
    print(e)
