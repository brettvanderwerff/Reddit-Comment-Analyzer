import praw
import time

'''Instantiates the reddit object from the praw class Reddit.
'''

reddit = praw.Reddit(client_id='Your id goes here',
                     client_secret='Your secret goes here',
                     user_agent='Your agent goes here',
                     username='your username goes here',
                     password='your password goes here')

def generate_redditor_list():
    '''Function uses praw to call Reddit's API and get a list of the authors of 2000 recent submissions in
    r/all and returns the authors as a list for temporary use.
    '''
    redditor_list = []
    while len(redditor_list) <2000:
        time.sleep(10)
        for submission in reddit.subreddit('all').new(limit=None):
            if str(submission.author) not in redditor_list:
                redditor_list.append(str(submission.author))
                print('Writing redditor #{} to temporary list.'.format(len(redditor_list)))
    return redditor_list

def write_redditor_list(redditor_list):
    '''Function writes the temporary list of redditors gotten from generate_redditor_list function to the disk.
    '''
    with open('random_redditor_list.txt', 'a', encoding='utf-8') as write_obj:
        counter = 0
        for item in redditor_list:
            counter += 1
            print('Writing redditor #{} from temporary list to computer.'.format(counter))
            write_obj.write(item + '\n')

def run():
    '''Function runs script.
    '''
    redditor_list = generate_redditor_list()
    write_redditor_list(redditor_list=redditor_list)









