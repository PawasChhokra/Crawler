import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import time

##test = "<html><div>test</div><ul><li>1</li><li>2</li><li>3</li></ul></html>"
##soup = BeautifulSoup(test)
###print(soup.prettify())
##lis = soup.ul.find_all()
###print(lis)
##p = []
##i=1
##for li in lis:
##    p.insert(int(li.text), i)
##    i=i+1
##    
###        print( int((li.text.encode("utf-8")))+1)
##print(p)


##rate = []
##userrate = []
##url = []
##review = []
##ranking = []

##img = []
url = []
lis = []

print("Enter the URL you want to collect information from.")
FURL = input()
URL = FURL

start = time.time()
##start = time.process_time()

##URL = "http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html"

while(True):
    try:
        web = urllib.request.urlopen(URL)
        break
    except:
        print("Caught URLopen Exception. Opening URL again.")
        continue
s = web.read()
web.close()


soup = BeautifulSoup(s)
count = soup.find_all("div", class_="orphan   hotelsCount")
pgcount = int(count[0].b.get_text())


##print(pgcount)
##print(type(pgcount))

while True:

    try:
        web = urllib.request.urlopen(URL)
    except:
        print("Caught URLopen Exception. Opening URL again.")
        continue
##    print(URL)
    s = web.read()
    web.close()

    #print(s)
    soup = BeautifulSoup(s)
    #print(soup.prettify())
    #divs = soup.find_all("div", class_="listing wrap")
    ##divs = soup.find_all("a", class_="property_title")
    ###print(divs)
    supper = soup.find_all("div", class_="listing wrap")
    ####print(len(super))


    
    #for item in super:
    #print(super[0])
    ##span = super[0].find_all("span", class_="more")
    ##print(span)
    ##more = span.find_all("a", class_="more")
    ##print(more)
    ##print(span[0].find_all(text=re.compile("reviews")))

    sp = soup.prettify()
    x = ((sp.split('var lazyImgs = ['))[1].split(']')[0])


    for item in supper:
        pt = item.find_all("a", class_="property_title")
        relurl = pt[0]['href']

        if(relurl in url):
            continue

        dic = {}

        absurl = urllib.parse.urljoin(URL,relurl)
        dic['Hotel URL'] = absurl
        url.append(relurl)
        
        strn = pt[0].string.replace("\n","")           
        if(pt == []):
            dic['Hotel Name'] = None
        else:
            dic['Hotel Name'] = strn

        it = item.find_all("img", class_="sprite-ratings-gry")
        if(it == []):
            dic['Star Rating'] = None
        else:
            dic['Star Rating'] = it[0]['alt']

        span = item.find_all("span", class_="more")
        if(span == []):
            dic['Number of Hotel Reviews'] = None
        else:
            dic['Number of Hotel Reviews'] = span[0].find_all("a")[0].string.replace("\n","")

##        review.append(span[0].find_all(text=re.compile("reviews")))#[0].replace("\n",""))

        sr = item.find_all("img", class_="sprite-ratings")
        if(sr == []):
            dic['User Rating'] = None
        else:
            dic['User Rating'] = sr[0]['alt'].replace("\n","")

        sl = item.find_all("div", class_="slim_ranking")
        if(sl == []):
            dic['Hotel Ranking'] = None
        else:
            dic['Hotel Ranking'] = sl[0].string

        pi = item.find_all("img", class_="photo_image")
        if(pi == []):
            dic['Hotel Image URL'] = None
        else:
##            y = pi[0]['id']
            dic['Hotel Image URL'] = x.split(pi[0]['id'])[1].split('"data":"')[1].split('"}')[0] 

        lis.append(dic)

                            
    ##y = super[0].find_all("img", class_="photo_image")[0]['id']
    ##z = x.split(y)[1].split('"data":"')[1].split('"}')[0] 
    ##img.append(z)

    if(len(lis) == pgcount):
        break
    if(soup.find_all("span", class_="guiArw pageEndNext") != [] and len(lis) != pgcount):
        print("End of list. Starting again!")
        URL = FURL                
    else:
##        print(soup.find_all("a", class_="guiArw sprite-pageNext "))
        URL = urllib.parse.urljoin(URL,soup.find_all("a", class_="guiArw sprite-pageNext ")[0]['href'])



print(time.time() - start)

##for i in range(len(lis)):
##    print(lis[i])
##    print('\n')
print(len(lis))

##for i in range(len(name)):
##    print("Hotel name: ", name[i])
##    print("Hotel detail URL: ", url[i])
##    print("Star rating: ", rate[i])
##    print("Number of hotel reviews: ", review[i])
####    print(type(review[i]))
##    print("User rating: ", userrate[i])                        
##    print("Hotel rankings: ", ranking[i])
##    print("Hotel image link: ", img[i])
##    print("\n")
##                            
##print(len(name))
##print(len(url))
##print(len(rate))
##print(len(review))
##print(len(userrate))                        
##print(len(ranking))
##print(len(img))

        
##print(super[0])
##span = super[0].find_all("span", class_="more")
##print(span)

    
##for item in divs:
##    name.append(divs[i].string)
##    relurl = divs[i]['href']
##    absurl = urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html',relurl)
##    url.append(absurl)
##    rating = super[i].find_all("img", class_="sprite-ratings-gry")
##    if len(rating) == 0:
##        rate.append('NA')
##    else:
##        rate.append(rating[i]['alt'])
##    i=i+1
    #print(divs[0]['href'])
##print(name)
##print(len(url))

##for item in super:
##    if(item.find_all("img", class_="sprite-ratings-gry") == []):
##        rate.append(None)
##    else:
##        rate.append(item.find_all("img", class_="sprite-ratings-gry")[0]['alt'])
##
##print(len(rate))
##print(rate)

##rating = super[0].find_all("img", class_="sprite-ratings-gry")
##if(rating == []):
##    print("okay")
##rate.append(rating[i]['alt'])
##print(rate)

##relurl=divs[0]['href']
##print(relurl)
##absurl=urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html',relurl)
##print(absurl)
