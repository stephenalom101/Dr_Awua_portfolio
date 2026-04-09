import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Downloading Knight Frank Logo...")
try:
    req_kf = urllib.request.Request(
        'https://logowik.com/content/uploads/images/knight-frank7568.jpg', 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    )
    with open('logo_knight_frank.jpg', 'wb') as f:
        f.write(urllib.request.urlopen(req_kf, context=ctx).read())
    print("Knight Frank Success!")
except Exception as e:
    print("KF error:", e)

print("Downloading Shell Logo...")
try:
    req_shell = urllib.request.Request(
        'https://companieslogo.com/downloads/logos/Shell_logo.png', 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    )
    with open('logo_shell.png', 'wb') as f:
        f.write(urllib.request.urlopen(req_shell, context=ctx).read())
    print("Shell Success!")
except Exception as e:
    print("Shell error:", e)
