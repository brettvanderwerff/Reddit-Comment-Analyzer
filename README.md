# Naive-Bayes-Reddit-Comment-Analyzer

This project uses machine learning to discriminate between comments made by a specific redditor of interest and random comments by other redditors.

The concept for this project was inspired by the article “Social Media Writing Style Fingerprint” by Yadav et al. 2017 (https://arxiv.org/ftp/arxiv/papers/1712/1712.04762.pdf).

This project is my first attempt at machine learning, so I detailed my approach and learning process at my blog adventureswithpie at:
https://adventureswithpie.wordpress.com/2018/02/11/first-adventures-in-machine-learning-with-naive-bayes/
Check it out if you are interested. There is quite a bit of detail on the logic behind each script in the blog post. 
~~~~~~~~~~~~~
Dependencies:
~~~~~~~~~~~~~

nltk==3.2.5

pandas==0.22.0

praw==5.3.0

requests==2.18.4

scipy==1.0.0

scikit_learn==0.19.1

~~~~~~~~~~~~~~~~~~~~~~~~
How to run this program:
~~~~~~~~~~~~~~~~~~~~~~~~

1.	Clone repository.
2. Install dependencies
3.	Get a reddit account, client id, client secret, and user agent. Many guides exist online for doing this, the official PRAW documentation is not a bad place to start (https://praw.readthedocs.io/en/latest/getting_started/quick_start.html). Once these credentials are gotten, they need to be plugged into the get_random_redditor_list.py script.
4.	Run collect_data.py, this script writes a txt file to the disk with a collection of comments from the redditor of interest and another txt file for a collection of comments from random redditors, these files are required for the next step. API calls in this script are throttled and it should take several minutes to run.
5.	Run naïve_bayes.py, this script will return a percentage score of how accurately the classifier can distinguish between comments made by the redditor of interest or a random redditor. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How to configure this program:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.	FriesWithThat is the default redditor of interest, but this can be changed by passing a different redditor name into the collect_data function of the collect_data.py script
2.	1000 comments are collected for the redditor of interest by default, this can be changed by adjusting the comment_limit argument of the ObtainRedditorComments class in the collect_data.py script. You may have to consider that some redditors have a small comment history.
3.	The amount of comments gotten from random redditors can be toggled by changing the if len(comment_list) statement in the get_redditor_comment_list function of the get_random_redditor_comments.py script. The while len(redditor_list) statement in the generate_redditor_list function of the get_random_redditor_list.py script should be about double the len(comment_list) setting in get_random_redditor_comments.py. This circumvents issues with redditors making comments in private subreddits that are not available.  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bugs:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These seems to be a bug with the Pushift reddit API (https://github.com/pushshift/api) that returns an erroneous statement  (https://pastebin.com/e8fEw4sE or something similar to this) when getting comments for the redditor of interest. This gets written to the txt file of comments for the redditor of interest. Simply remove this before analysis with naive bayes. 


