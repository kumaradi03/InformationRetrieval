import urllib2
from bs4 import BeautifulSoup
import re
import time
import urlparse
from initialremove import remove_files
from errorlogging import logerror
import path_define

#Global variables
LINK_ANCHOR={}
LINK_FILENAME={}
ERROR_FILE_PATH= path_define.get_ERROR_FILE_PATH()
CRAWLEDLISTPATH = path_define.get_CRAWLEDLISTPATH()
CRAWLED_HTML_PATH = path_define.get_CRAWLED_HTML_PATH()

def get_html_content(url):
    try:
        html = urllib2.urlopen(url)
        content = BeautifulSoup(html,"html.parser")
        content.prettify()
        if LINK_ANCHOR.has_key(url):
            file_name= re.sub(r'[\W]', '_', LINK_ANCHOR[url])#replacing space from anchor name
        else:
            file_name= re.sub(r'[\W]', '_', url)#replacing special characters
        LINK_FILENAME.update({url:file_name+".html"})
        out_file  = open(CRAWLED_HTML_PATH+"\\"+file_name+".html",'w')
        out_file.write(url.encode('UTF-8')+"\n"+content.prettify().encode('UTF-8'))
        out_file.close()
        return content
    except Exception as e:
        logerror(e)


def fetch_all_links(current_crawl,keyword):
    base_url = "https://en.wikipedia.org"
    pattern = re.compile('^/wiki/')
    new_links_list=[]
    try:
        html_content = get_html_content(current_crawl)
         #stores all the links within the bodyContent of the page excluding the administrative links
         #and the 1st regex excludes any links containing # or any other links starting other than wiki
        links = html_content.find("div",{"id":"bodyContent"}).find_all('a',href=pattern)
        for link in links:
                if ":" not in link.get('href'):
                    url=urlparse.urljoin(base_url,link.get('href'))
                    if "#" in link.get('href') :
                        url = url [: url.index('#')]
                    anchor=link.text.encode("utf-8")
                    match = re.search(r'.*{0}.*'.format(keyword), url, re.I)
                    keywordsearch = re.search(r'.*{0}.*'.format(keyword), anchor, re.I)
                    if (url not in new_links_list) and (match or keywordsearch):
                        new_links_list.append(url)
                        LINK_ANCHOR.update({url:anchor})
    except Exception as e:
        logerror(e)
    return new_links_list




def merge_results(presentlist,newlist):
    for url in newlist:
        if url not in presentlist:
            presentlist.append(url)

def web_crawl(url, max_depth,crawled_limit,keyword,visited):
    current_depth=1
    try:
        if current_depth <= max_depth and len(visited) < crawled_limit:
            frontier_crawl=fetch_all_links(url,keyword)
            if url not in visited:
                visited.append(url)
            for new_url in frontier_crawl:
                if len(visited) < crawled_limit and max_depth > current_depth:
                     if new_url not in visited :
                         merge_results(visited, web_crawl(new_url, max_depth-1,crawled_limit,keyword,visited))
                else:
                     break
            time.sleep(1) #waiting policy for 1 second.
        else:
            return []
    except Exception as e:
        logerror(e)
        return visited
    return visited

def start():
    try:
        remove_files()
        depth = raw_input("> Enter the depth where depth starts from 1 \n>\t")
        crawled_limit = raw_input("> Enter the number limit of crawled urls\n>\t")
        keyword = raw_input("> Enter the focused keyword\n>\t")
        seed_url="https://en.wikipedia.org/wiki/Sustainable_energy"
        crawledlist = web_crawl(seed_url,int(depth),int(crawled_limit),str(keyword),[])
        out_file = open(CRAWLEDLISTPATH+"\crawled_list.txt",'a')
        count=1
        for url in crawledlist:
            out_file.write(str(count)+".\t" +url + "\n")
            count+=1
        if crawledlist:
            print "The crawled_list.txt can be found in %s" %(CRAWLEDLISTPATH)
            print "The crawled list of htmls can be found in %s" %(CRAWLED_HTML_PATH)
        print "The error file can be found at %s" %(ERROR_FILE_PATH)
        out_file.close()
    except Exception as e:
        logerror(e)

start()
