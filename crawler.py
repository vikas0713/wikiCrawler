import urllib2
from bs4 import BeautifulSoup



disease=urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_diseases_(A)')
bs=BeautifulSoup(disease)
[s.extract() for s in bs('table')]
data=bs.find('div',attrs={'id':'mw-content-text'}).findAll('li')
for a in data:
    if None in a:
        pass
    else:
        li=a.findAll('a')
        for i in li:
            v=i.text
            m=v.encode('utf-8')
            url=i['href']
            try:
                html=urllib2.urlopen('http://en.wikipedia.org'+url)
                bs=BeautifulSoup(html)
                try:
                    data=bs.find('div',attrs={'id':'mw-content-text'}).findAll('p',limit=1)
                    for j in data:
                        b= j.text
                        b=b.encode('utf-8')
                        print "name:",v,"description:",b

                except:
                    print "there is error"
            except:
                pass

db.close()
