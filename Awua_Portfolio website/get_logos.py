import urllib.request
import urllib.parse
import json

def get_wiki_image(title):
    try:
        url = 'https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=' + urllib.parse.quote(title)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read()
        pages = json.loads(res)['query']['pages']
        return list(pages.values())[0]['original']['source']
    except Exception as e:
        return ""

def search_duckduckgo(query):
    try:
        url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        return res[:1000] # just to check
    except Exception as e:
        return str(e)

print('Shell:', get_wiki_image('Shell_plc'))
print('BUA Group:', get_wiki_image('BUA_Group'))
print('Seplat:', get_wiki_image('Seplat_Energy'))
print('Knight Frank:', get_wiki_image('Knight_Frank'))
print('NBC:', get_wiki_image('Nigerian_Bottling_Company'))
