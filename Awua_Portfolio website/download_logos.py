import urllib.request

logos = {
  'shell_logo.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Shell_logo.svg/200px-Shell_logo.svg.png',
  'bua_logo.png': 'https://www.buagroup.com/wp-content/uploads/2019/12/BUA-Group-Logo.png',
  'seplat_logo.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Seplat_Energy_Plc_Logo.jpg/200px-Seplat_Energy_Plc_Logo.jpg',
  'coca_cola_logo.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Coca-Cola_logo.svg/200px-Coca-Cola_logo.svg.png',
  'knight_frank_logo.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Knight_Frank_Logo_2.svg/300px-Knight_Frank_Logo_2.svg.png',
  'nbc_logo.jpg': 'https://ng.coca-colahellenic.com/etc.clientlibs/cchbc/clientlibs/clientlib-base/resources/images/logos/CCHBC_logo_white.svg'
}

for name, url in logos.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(name, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print('Downloaded', name)
    except Exception as e:
        print('Failed', name, e)
