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
LINK_FILENAME=[]
ERROR_FILE_PATH= path_define.get_ERROR_FILE_PATH()
CRAWLEDLISTPATH = path_define.get_CRAWLEDLISTPATH()
CRAWLED_HTML_PATH = path_define.get_CRAWLED_HTML_PATH()

def get_html_content(url):
    try:
        counter= 1;
        html = urllib2.urlopen(url)
        content = BeautifulSoup(html,"html.parser")
        content.prettify()
        article_id = (url.split("/wiki/")[1])
        file_name=re.sub(r'-*_*', '', article_id)
        if file_name not in LINK_FILENAME:
            LINK_FILENAME.append(file_name)
        else:
            while(file_name in LINK_FILENAME):
                file_name = file_name+str(counter)
                counter = counter + 1
            LINK_FILENAME.append(file_name)
        out_file  = open(CRAWLED_HTML_PATH+"\\"+file_name+".txt",'w')
        out_file.write(url.encode('UTF-8')+"\n"+content.prettify().encode('UTF-8'))
        out_file.close()
        html.close()
        return content
    except Exception as e:
        logerror(e)
        return None


def fetch_all_links(current_crawl):
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
                    if url not in new_links_list:
                        new_links_list.append(url)
                        LINK_ANCHOR.update({url:link.text.encode("utf-8")})
    except Exception as e:
        logerror(e)
        return None
    return new_links_list

def merge_results(presentlist,newlist):
    for url in newlist:
        if url not in presentlist:
            presentlist.append(url)

def web_crawl(seed, max_depth,crawled_limit):
    frontier_crawl = [seed]#this list maintains
    visited = []
    next_depth_urls = [] #this list stores all unique urls for each depth
    depth = 1 #where seedpage is depth 1.
    try:
        while frontier_crawl and depth <= max_depth and len(visited) < crawled_limit:
            current_crawl = frontier_crawl.pop(0) #crawls the links from the top of the page
            if current_crawl not in visited:
               new_url_links = fetch_all_links(current_crawl)
               if new_url_links is not None:
                   merge_results(next_depth_urls, new_url_links)
                   visited.append(current_crawl)
                   time.sleep(1) #waiting policy for 1 second.
            if not frontier_crawl:
               frontier_crawl, next_depth_urls = next_depth_urls, [] #once frontrier or current depth list is empty, going to next depth.
               depth += 1
    except Exception as e:
        logerror(e)
        return visited
    return visited

def start():
    try:
        remove_files()
        depth = raw_input("> Enter the depth where depth starts from 1 \n>\t")
        crawled_limit = raw_input("> Enter the number limit of crawled urls\n>\t")
        seed_url="https://en.wikipedia.org/wiki/Sustainable_energy"
        crawledlist = web_crawl(seed_url,int(depth),int(crawled_limit))
        if crawledlist:
            out_file = open(CRAWLEDLISTPATH+"\crawled_list.txt",'a')
            count=1
            for url in crawledlist:
                out_file.write(str(count)+".\t" +url + "\n")
                count+=1
            print "The crawled_list.txt can be found in %s" %(CRAWLEDLISTPATH)
            print "The crawled list of htmls can be found in %s" %(CRAWLED_HTML_PATH)
            out_file.close()
        print "The error file can be found at %s" %(ERROR_FILE_PATH)
    except Exception as e:
        logerror(e)

start()
