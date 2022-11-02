import requests
import io
from lxml import etree
import wget

url = open("URL", "r")
pars = open("pars", "w")
parsed = []

data = requests.get(url.read()).text

parser = etree.HTMLParser()
tree = etree.parse(io.StringIO(data), parser)
for im in tree.xpath('//a'):
    parsed.append(im.get('href'))

res = [i for i in parsed if i is not None]

count = 0
while len(res) > count:
    pars.write(res[count])
    pars.write('\n')
    count = count + 1

pars.close()

word = '/upload/iblock/724'
with open(r'pars', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
            value = line

downloadLink = "https://www.muiv.ru" + value

response = wget.download(downloadLink, "timetable.xls")

print(downloadLink)
