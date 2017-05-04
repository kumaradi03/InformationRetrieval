Assignment 4:
Goal: Introduction to Lucene. Retrieval and scoring using Cosine Similarity.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.
The progrms are discussed below in brief:
-- Task1: Index and retrieve documents with higher scores using Lucene Search model.
-- Task2: Retrieve and sort documents using only Cosine Similarity to score in Vector Space Model.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL USAGE NOTES:

-- This file contains instructions about installing softwares and running the programs in Windows Environment.
-- The instructions in the file might not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
-- However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTALLATION GUIDE:

-- Download python 2.7.x from https://www.python.org/download/releases/2.7/
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
-- Open Command Prompt and upgrade pip using the following command: 'python -m pip install -U pip'
-- To check whether you have pip installed properly, just open the command prompt and type 'pip'
-- It should not throw an error, rather details regarding pip will be displayed.
-- Install BeautifulSoup by using the command 'pip install beautifulsoup4'
-- If for some reason the installation fails due to the absence of certain package, just install that package using 'pip install name_of_that_package'

-- Install JAVA SE6 or above if not already installed in the system from http://www.oracle.com/technetwork/java/javase/index-137561.html#windows
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add new variable in 'PATH' -> [Home directory of Java]\jdk[version number]\bin;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL INSTRUCTIONS:

-- Please maintain the folder and file structure inside 'source_code' folder, as it is very important for the the codes of both the tasks to work.
-- The generated corpus from the previous assignment would be present in the folder 'generated_corpus'. The corpus is feeded into both Lucene model and VSM model. But if one wishes to re-generate the corpus and test, one can follow the following steps :-
	-- The folder 'downloaded_docs' inside 'source_code' contains the 1000 documents that have been downloaded in .txt format during HW1 - Task1.	
	-- Run the python file 'Task1.py' by using the command 'python Task1.py' in windows powershell or command prompt
	-- The corpus will be generated from the downloaded documents present in 'downloaded_docs' and be stored in 'generated_corpus' document wise.
-- The code for Task1 implementation 'HW4.java' is provided in 'source_code' folder along with all the jars needed for the code to run inside folder 'java_jars'
-- Lucene.jar is the runnable jar of the given code which can work independently from a command prompt and doesn't need any IDE setup or dependency on the jars.
-- The Top 5 explaination and Implementation report can be found inside 'Explaination' folder

INSTRUCTIONS TO RUN THE PROGRAM FOR TASK1:

-- There are two ways to run Task1 code.

-- The easy way is to open command prompt and traverse inside the 'source_code' directory and then use command 'java -jar Lucene.jar'
-- Enter the relative path to the 'source_code' folder, for Ex- "C:\Users\Rahulpyne\Solution\source_code" in the command prompt
-- The code would use corpus from folder 'generated_corpus' and 'query.txt' inside 'source_code' to generate the desired 4 tables for all given 4 queries in a single file named 'Lucene_doc_score.txt' inside the 'doc_score' folder.

OR

-- The other way is to setup a new JAVA project in any IDE(preferrably Eclipse Mars) and add the dependencies to the jars provided in 'java_jars' folder along with the correct jdk environment for 1.6 or above.
-- Place the 'HW4.java' file inside the src folder of the project and run the program.
-- Enter the relative path to the 'source_code' folder, for Ex- "C:\Users\Rahulpyne\Solution\source_code"
-- The code would use corpus from folder 'generated_corpus' and 'query.txt' inside 'source_code' to generate the desired 4 tables for all given 4 queries in a single file named 'Lucene_doc_score.txt' inside the 'doc_score' folder.


INSTRUCTIONS TO RUN THE PROGRAM FOR TASK2:
	
-- Run the python file 'index_generator.py' by using the command 'python index_generator.py' in windows powershell or command prompt
-- The program takes no input and uses the corpus present in the folder 'generated_corpus' and the 'query.txt' present in the 'source_code' folder to create the desired 4 tables for all given 4 queries in a single file named 'VSM_doc_score.txt' inside the 'doc_score' folder.


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://lucene.apache.org/core/4_0_0/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html - TFIDFSimilarity using Lucene Model.
-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming
-- https://learnpythonthehardway.org/book/ : Python Programming
-- http://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html : For stop words.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 8573109310
E-Mail: kumar.adi@husky.neu.edu