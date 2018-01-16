from bs4 import BeautifulSoup # Parsing Source HTML
import urllib.request # Opening Webpage

### choose url ###
#"https://www.reddit.com/r/VideoGameReviews/comments/771lp2/switch_kamiko_55_a_five_dollar_hidden_gem_on_the/"
spots = input("Enter a gaming review URL: ");

#### urllib.request ####
# the default urllib request object is heavily limitied via reddit.
# By creating unique 'User-Agent' we can work around this limitation,
# otherwise we get Error: 429 - Too many requests
req = urllib.request.Request(
    url=spots,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
page = urllib.request.urlopen(req)

#### Beautiful Soup ####
soup = BeautifulSoup(page,"html.parser")
soup.prettify()# Makes the html readable

# Find the content of the reddit review
tail = soup.findAll("div",class_="md")# <div class="md">

paw = tail[1]# The one we want is the second occurence.
             # We can navigate through the comments by incrementing tail.
            
claws = paw.get_text()# Clean tags from the paw soup
print(claws)

#### Output #####
# Writing claws to file
furrl_name = "leopard.txt"
furrl = open(furrl_name,"w")
furrl.write(claws)
furrl.close()



