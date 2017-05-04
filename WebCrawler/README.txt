Assignment 1:
Goal: Implementing your own web crawler. Perform focused crawling

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.
The progrms are discussed below in brief:
-- Task1: A web crawler that starts from the following seed URL "https://en.wikipedia.org/wiki/Sustainable_energy" and crawls upto depth 5 or  maximum of 1000 unique URLs. Pages in a shallower depth are more important than deeper ones, also within each individual page, hyperlinks appearing earlier on the webpage should be crawled first.
-- Task2: The web crawler should be able to consume two arguments: a URL and a keyword to be matched against anchor text or text within a URL. It starts with the seed URL "https://en.wikipedia.org/wiki/Sustainable_energy" and crawls to a depth 5 at most using the keyword "solar". It should return at most 1000 URLs for each of the following:
	A: Breadth first crawling
	B: Depth first crawling
-- Task3: Repetation of the Task1 using the seed "https://en.wikipedia.org/wiki/Solar_power"

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL USAGE NOTES:

-- This file contains instructions about installing softwares and running the programs in Windows Environment.
-- The instructions in the file might not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
-- However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTALLATION GUIDE:

-- Download python 2.7.x from https://www.python.org/download/releases/2.7/
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
-- Open Command Prompt and upgrade pip using the following command: 'python -m pip install -U pip'
-- To check whether you have pip installed properly, just open the command prompt and type 'pip'
-- It should not throw an error, rather details regarding pip will be displayed.
-- Install BeautifulSoup by using the command 'pip install beautifulsoup4'

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTRUCTIONS TO RUN THE PROGRAM:

-- Create the desired folder structure where you wish to generate crawled list file
-- Create the desired folder structure where you wish to download the crawled htmls.
-- Create the desired folder structure where you wish to generate the errorLog.txt
-- Create the folder structure in the same drive where the code is, otherwise it might throw an access related error.
-- Mention the paths of your folders in path_define.py file. Example of the path structure can be seens in the -- path_define.py file

-- Open Windows PowerShell
-- Navigate to the directory having the programs
-- Run the program by using the command 'python <File_Name>.py'

OR

-- Navigate to the directory having the programs
-- Double click on the <FileName>.py file to run the program.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

DESIRED RESULTS:

-- First it will remove any file that exist in the desired folder structure, may that be crawled htmls or crawledlists.txt -- or errorLog.txt
-- The program creates a file named 'crawled_list.txt', in the mentioned path of your folder structure, which lists all -- the URLs that has been crawled.
-- The contents of all webpages that has been crawled are stored in html format along with their URLs.
-- The htmls are created in the directory mentioned for htmls in path_define.py
-- If any exception occurs, it is maintained in an errorLog.txt file in the directory mentioned in the path_define.py


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.youtube.com/watch?v=E7wB__M9fdw: How to scrape web pages using python.
-- https://www.youtube.com/watch?v=-E1SC_oz9m4 : How to use BeautifulSoup for extracting links from web pages.
-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming
-- https://learnpythonthehardway.org/book/ : Python Programming

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 8573109310
E-Mail: kumar.adi@husky.neu.edu