"""
This will scrawl the website defined in url
when start_scaping method is called it will load
the global list visited list and external link list
when test_external_url method is call it'll try to test the urls
in the external_url list and print out the urls that dont return status_code 200
This is for python3
pip install mechanicalsoup

"""

from urllib.parse import urljoin
import mechanicalsoup

# Set the startingpoint for the spider and initialize
# the a mechanize browser object
url = "http://www.mystudynotebook.com/"
br = mechanicalsoup.Browser()

# create lists for the urls in que and visited urls
urls = [url]
visited = [url]
# to keep track of external urls mentioned in this site. this urls will be
# tested later
external_url = []
"""
    This list of unnecessary urls are kept to keep track of unnessary urls that can not be checked by a bot like fb
    This also helps to prevent recursive loop in the urls.
    like the bot tries to check every users with login?url
    if any suburl contains these url then that url will be discarded ie. will not be checked
"""
unnecessary_url = ["login", 'logout',
                   'javascript:void(0);', 'www.facebook.com', 'mailto:support']


def check_if_unnecessary_url(url):
    for u_url in unnecessary_url:
        if(u_url in url):
            return True
    return False


# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
#   this will load up the global list of visited_url, external_url, etc
def start_scraping():
    print("Going to scrap url {0} ".format(url))

    while len(urls) > 0:
        print("cur urls: {0} external_urls_found: {1}".format(
            len(urls), len(external_url)))
        page = br.get(urls[0])
        urls.pop(0)
        for a in page.soup.find_all('a', href=True):
            # print("Found the URL:", a['href'])
            newurl = urljoin(url, a['href'])
            if(check_if_unnecessary_url(a['href'])):
                # print("\n ******this url is unnecessary", newurl, "\n")
                continue
            if(url not in newurl):
                if(newurl not in external_url):
                    # print("\n ******this external url", newurl, "\n")
                    external_url.append(newurl)
            if newurl not in visited and url in newurl:
                urls.append(newurl)
                visited.append(newurl)


# external_url = ['https://twitter.com/sayeedsajal', 'https://www.linkedin.com/in/mdabuobaida', 'https://www.tamu.edu/', 'http://www.whitecanvassoft.com', 'http://redbus2us.com/what-is-statement-of-purpose-sop-why-is-it-so-important/', 'http://grad.berkeley.edu/admissions/apply/statement-purpose/', 'https://grad.ucla.edu/asis/agep/advsopstem.pdf', 'https://ed.stanford.edu/sites/default/files/statement-of-purpose_u.d_2013.pdf', 'http://mystudynotebook.com', 'https://www.coursera.org/learn/study-in-usa', 'https://www.notefull.com/productsmain.php', 'https://www.ielts.org/about-the-test/test-format',
#                 'http://www.msinus.com/content/gre-universities-486/', 'http://gradschool.about.com/od/overviewtimetable/a/Should-You-Email-Professors-At-Potential-Graduate-Programs.htm', 'http://redbus2us.com/4-tips-to-email-professors-for-graduate-school-admission-in-usa/', 'https://www.quora.com/How-does-contacting-a-professor-before-applying-factor-into-graduate-admissions', 'http://www.atozbulletin.com/2013/09/list-of-all-us-universities-based-on.html', 'http://www.greatvaluecolleges.net/50-great-affordable-college-towns-in-the-u-s/', 'https://cameron.slb.com/onesubsea', 'http://flickr.com/mybd', 'http://www.nihossain.com/', 'http://psc.tamu.edu/']


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


start_scraping()
test_external_url()

print("Visited urls")
print(visited)
print("\n\n\n\n\n")
print('External urls')
print(external_url)
