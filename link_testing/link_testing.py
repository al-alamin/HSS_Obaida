"""
This will scrawl the website defined in the global variable url
when start_scaping method is called it will load the global list 
visited list and external link list
when test_external_url method is call it'll try to test the urls
in the external_url list and print out the urls that dont return status_code 200
This is for python3
pip install mechanicalsoup

"""

from urllib.parse import urljoin
import mechanicalsoup

# Set the startingpoint for the spider and initialize
# the a mechanize browser object

# url of the website to be crawled
url = "http://www.mystudynotebook.com/"
# the a mechanize browser object. Through this browser
# we'll make get request to different urls 
# Other python's libray can be used to make this get request.
br = mechanicalsoup.Browser()

# Queue of urls. Url will be poped from here and visit. All the urls in a page
# will be pushed here
urls = [url]
# list of all the urls that has been visited to avoid repeated visit to
# the same url
visited = [url]
# to keep track of external urls mentioned in this site. this urls will be
# tested later
external_url = []
"""
    br will make a get request to the url and source html will be returned.
    In that html we'll parse all the a tag with href attribute.
    So in the html page there are part like <a> href="javascript:void(0);" </a>
    or <a> href="login" </a>
    If we take these usls and try to visit them. Then either we'll get invalid urls
    or fall into recursive loop.

    I looked into the mystudynotebooks urls and found this urls in a tag's href field
    So I am avoiding them to make the crawl faster.
"""
unnecessary_url = ["login", 'logout',
                   'javascript:void(0);', 'www.facebook.com', 'mailto:support']

"""
    This is just a helper method 
    parameter take a url
    return if that url is in unnecessary_url list
    if that url is in unnecessary_url list then that url will not be visited discarded
"""


def check_if_unnecessary_url(url):
    for u_url in unnecessary_url:
        if(u_url in url):
            return True
    return False


# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
#   this will load up the global list of visited_url, external_url, etc
'''
    This will scrawl the website defined in the global variable url
    This method will recursively visit all the urls and load up globar variable 
    visited list and external link list
'''


def start_scraping():
    print("Going to scrap url {0} ".format(url))

    # urls is queue of urls. This while loop will run until this queue is empty
    while len(urls) > 0:
        print("cur urls: {0} external_urls_found: {1}".format(
            len(urls), len(external_url)))
        # making a get request to the that url
        page = br.get(urls[0])
        urls.pop(0)
        # Going to loop throug all tha a tag with href attribute
        for a in page.soup.find_all('a', href=True):
            # print("Found the URL:", a['href'])
            '''
                urljoin is a very useful thing. In a webpage a lot of times relative 
                urls are used in a tag's href field
                This urljoin is joining these relative urls with base website urls.
                Fascinating part is this urljoin method is handing all other join cases
                like if base urls are given then it will join only once it'll take care
                of slashes.

                http://stackoverflow.com/questions/10893374/python-confusions-with-urljoin
                from urllib.parse import urljoin
                >>> urljoin('some', 'thing')
                'thing'
                >>> urljoin('http://some', 'thing')
                'http://some/thing'
                >>> urljoin('http://some/more', 'thing')
                'http://some/thing'
                >>> urljoin('http://some/more/', 'thing') # just a tad / after 'more'
                'http://some/more/thing'
                urljoin('http://some/more/', '/thing')
                'http://some/thing'


            '''
            newurl = urljoin(url, a['href'])
            if(check_if_unnecessary_url(a['href'])):
                # print("\n ******this url is unnecessary", newurl, "\n")
                continue
            # after url join if the base url still is not in newurl then the new 
            # url is external url
            if(url not in newurl):
                if(newurl not in external_url):
                    # print("\n ******this external url", newurl, "\n")
                    external_url.append(newurl)
            # after urljoin if base url is in new url then it is internal url
            # then will newurl will pushed to url Queue and visited url list
            if newurl not in visited and url in newurl:
                urls.append(newurl)
                visited.append(newurl)

# for Debug
external_url = ['https://twitter.com/sayeedsajal', 'https://www.linkedin.com/in/mdabuobaida', 'https://www.tamu.edu/', 'http://www.whitecanvassoft.com', 'http://redbus2us.com/what-is-statement-of-purpose-sop-why-is-it-so-important/', 'http://grad.berkeley.edu/admissions/apply/statement-purpose/', 'https://grad.ucla.edu/asis/agep/advsopstem.pdf', 'https://ed.stanford.edu/sites/default/files/statement-of-purpose_u.d_2013.pdf', 'http://mystudynotebook.com', 'https://www.coursera.org/learn/study-in-usa', 'https://www.notefull.com/productsmain.php', 'https://www.ielts.org/about-the-test/test-format',
                'http://www.msinus.com/content/gre-universities-486/', 'http://gradschool.about.com/od/overviewtimetable/a/Should-You-Email-Professors-At-Potential-Graduate-Programs.htm', 'http://redbus2us.com/4-tips-to-email-professors-for-graduate-school-admission-in-usa/', 'https://www.quora.com/How-does-contacting-a-professor-before-applying-factor-into-graduate-admissions', 'http://www.atozbulletin.com/2013/09/list-of-all-us-universities-based-on.html', 'http://www.greatvaluecolleges.net/50-great-affordable-college-towns-in-the-u-s/', 'https://cameron.slb.com/onesubsea', 'http://flickr.com/mybd', 'http://www.nihossain.com/', 'http://psc.tamu.edu/']

'''
    This method will visit the urls in global variable external_url.
    Then check if that url is returning 200.
    call start_scrapting method before callin this method because start_scraping
    method will load up the global variable external_url list
'''
def test_external_url():

    print("Going to test the external usls found in {0}".format(url))
    total = len(external_url)
    for cur_url in external_url:
        # header is added otherwise some external website rejects request
        page = br.get(cur_url, headers={'User-Agent': 'Mozilla/5.0'})
        # print(page)
        if(page.status_code != 200):
            print("url: {0} has returned: {1}".format(
                cur_url, page.status_code))

        print("urls remaining: {0}".format(total))
        total -= 1


# start_scraping()
test_external_url()

print("Visited urls")
print(visited)
print("\n\n\n\n\n")
print('External urls')
print(external_url)
