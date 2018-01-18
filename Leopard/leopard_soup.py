from bs4 import BeautifulSoup # Parsing Source HTML
import urllib.request # Opening Webpage
import global_vars #./global vars
from time import strftime, gmtime # time library for files
import logger # logs events to file

### Selective cook ###
# Selects a leopard from user input. Poor kitty! >:
def pick_leopard_to_cook():
    #https://www.reddit.com/r/VideoGameReviews/comments/771lp2/switch_kamiko_55_a_five_dollar_hidden_gem_on_the/
    spots = input("Enter a gaming review URL: ");
    cook_leopard(spots)
# end def pick_leopard

#### Connect and retrieve article ####
# @param spots = the url where the reddit article exists
def cook_leopard(spots):
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

    write_claws_to_file(claws)
#### end def cook_leopard

#### Store the article in a file ####
# @param claws = tasty leopard soup to be stored in a file
def write_claws_to_file(claws):
    #### Output #####
    # Writing claws to file
    crispy_kitten = global_vars.review_file_path + "ck_"+strftime("%m-%d-%y-%H-%M-%S", gmtime())+".txt"
    leopard_txt = open(crispy_kitten,"w+")
    leopard_txt.write(claws)
    leopard_txt.close()
    logger.log_event(crispy_kitten + " created.")
#end def write_claws_to_file

#### Verify the URL is original. ####
# @param spots = the url to check for originality
# @return = if the URL exists in urls.txt
def verify_spots(spots):
    
    # Before we start counting the words, we verify that the URL is unique
    isFound = False

    # First we open the file in read mode and check if the url exists in urls.txt
    urls_txt = open(global_vars.urls_txt,"r+")
    if spots in urls_txt.read():
        isFound = True
        print("<!> ERROR: Redundant URL >>> Spots found in url.txt <!>")
    urls_txt.close()

    #if isFound: # if the url exists, exit the program.
        #raise SystemExit

    if not isFound: # if the url is not found, we append it to urls.txt
        urls_txt = open(global_vars.urls_txt,"a+")
        urls_txt.write(spots + "\n")
        urls_txt.close()
        
    return isFound
### end def verify_url


