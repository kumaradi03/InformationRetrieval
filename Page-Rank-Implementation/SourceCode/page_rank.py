from math import log
import operator
from errorlogging import logerror


#Global variables

# S is the set of sink nodes, i.e. pages that do not have outlinks
S=[]

# M is the inlinks dictionary containing p (page) as key and all its inlinks as list value
M={}

# L is the outlinks dictionary containing q (page) as key and the total number of outlinks as value.
L={}

# PR is the dictionary containing pages and their respective page ranks of all the unique pages crawled
PR={}

# NEWPR is the set of temporary page ranks calculated of all the unique pages crawled
NEWPR={}


def populate_inlinks_dict(lines):
    try:
        for line in lines:
            words=line.split();
            M[words[0]]=words[1:] # populating the inlinks dictionary
    except Exception as e:
        logerror(e)

def populate_outlinks_dict():
    try:
        for p in M.keys(): # iterating through all the unique crawled pages
            for q in M.get(p): # iterating through the list of inlinks for p page
                if L.has_key(q): # checking whether the particular inlink is already in outlink dict
                    L[q]+=1 # if the particular page q already exists in outlink dict, then increment the counter
                else:
                    L[q]=1 # if the particular page q does not exist in outlink dict, then initiate the counter from 1
    except Exception as e:
        logerror(e)

def populate_sink_pages():
    try:
        for p in M.keys():  # iterating through all the unique crawled pages
            if not L.has_key(p): # checking whether the particular page p has any outlink
                S.append(p)
    except Exception as e:
        logerror(e)

def populate_page_rank():
    try:
        total_pages = float(len(M.keys())) # making it float because the value will be required to calculate PR
        for p in M.keys():
            PR[p]=1.0/total_pages #Initiating the value of page rank for each page as 1/total number of pages
    except Exception as e:
        logerror(e)

def cal_perplexity():
    try:
        entropy=0.0 # initiating the value of entropy to 0.0
        for p in PR.keys():
            entropy -= PR[p]*log(PR[p],2)
        return 2**entropy
    except Exception as e:
        logerror(e)


def calc_page_rank():
    try:
        # total_pages is the total number of unique crawled pages
        total_pages = float(len(M.keys())) # making it float because the value will be required to calculate PR
        # d is the dammping factor/teleportation factor
        d=0.85
        perplexity = 0.0 #initial value of perplexity
        convergence_count = 0 #initializing the convergence_count to 0
        iteration_count = 0 # will track the total number of iterations required to converge
        while  convergence_count < 4:
            sinkPR = 0.0
            for p in S:
                sinkPR += PR[p]
            for p in M.keys():
                NEWPR[p] = (1.0 - d)/total_pages #teleportation factor
                NEWPR[p] += (d*sinkPR/total_pages) # spreading the remaining sinkPR evenly
                for q in M[p]: #traversing through the inlinks of page p
                    NEWPR[p] += d*PR[q]/L[q] # add share of PageRank from inlinks
            for page in M.keys():
                PR[page] = NEWPR[page] # setting the new PageRank
            new_perplexity = cal_perplexity()
            if abs(new_perplexity - perplexity) < 1.0 :
                convergence_count +=1
            else:
                convergence_count = 0
            perplexity = new_perplexity
            iteration_count+=1
            outfile = open("perplexity_per_round.txt","a")
            outfile.write("Perplexity value: "+ str(perplexity) + " for the iteration: " + str(iteration_count)+"\n")
            outfile.close

    except Exception as e:
        logerror(e)

def sort_pages_rank():
    try:
        spr={}
        spr = sorted(PR.iteritems(), key=operator.itemgetter(1), reverse=True)
        sorted_file = open("SortedPage.txt","a")
        if(len(spr)<50) :
            for sp in range(len(spr)):
                sorted_file.write(str(spr[sp]) + "\n")
        else:
            for sp in range(50):
                sorted_file.write(str(spr[sp]) + "\n")
        sorted_file.close()
    except Exception as e:
        logerror(e)

def sort_pages_inlink():
    try:
        inlink_rank = {}
        for p in M:
            inlink_rank[p] = len(M.get(p))
        inlink_rank = sorted(inlink_rank.iteritems(), key=operator.itemgetter(1),reverse=True)
        inlink_file = open("InlinkPageRank.txt","a")
        for ir in range(5):
            inlink_file.write(str(inlink_rank[ir]) + " \n")
        inlink_file.close()
    except Exception as e:
        logerror(e)

def number_of_sinks():
    try:
        print ("Number of Sinks: "+ str(len(S)))
        return float(len(S))
    except Exception as e:
        logerror(e)

def number_of_sources():
    try:
        c=0
        for p in M:
            if not M[p]:
                c+=1
        print ("Number of Sources: "+ str(c))
        return float(c)
    except Exception as e:
        logerror(e)

def start():
    try:
        inlinks_file_path = raw_input("> Enter the path to the inlink graph file with proper extension. \n>\t")
        inlinks_file = open(inlinks_file_path,"r")
        lines = inlinks_file.readlines()
        populate_inlinks_dict(lines)
        populate_outlinks_dict()
        populate_sink_pages()
        populate_page_rank()
        calc_page_rank()
        sort_pages_rank()
        sort_pages_inlink()
        print "================================================================="
        print "========================STATISTICS=============================== \n"
        sinks = number_of_sinks()
        sources = number_of_sources()
        total_pages = len(M.keys())
        print ("Total number of pages = " + str(total_pages))
        print ("Proportion of Sinks = " + str(sinks/float(len(M.keys()))))
        print ("Proportion of Sources = " + str(sources/float(len(M.keys()))))
        print "================================================================="
        print "================================================================="

    except Exception as e:
        logerror(e)

start()
