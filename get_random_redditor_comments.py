import requests
import time

def get_redditor_list():
    '''Function opens a list of redditors previously saved to the disk.
    '''
    with open('random_redditor_list.txt', 'r') as file_obj:
        redditor_list = []
        for line in file_obj:
            redditor_list.append(line.strip('\n'))
    return redditor_list

def get_recent_comment(redditor):
    '''Function uses Pushshift Reddit API (https://github.com/pushshift/api) to obtain the most recent comment of
    a specified redditor.
    '''
    request = requests.get('https://api.pushshift.io/reddit/search/comment/?author={}&sort=desc&size=1'.format(redditor))
    request_json = request.json()
    comment = request_json['data'][0]['body']
    time.sleep(1)
    return comment

def get_redditor_comment_list():
    '''Function generates a temporary list of redditor comments.
    '''
    redditor_list = get_redditor_list()
    comment_list = []
    for redditor in redditor_list:
            if len(comment_list) < 10:
                try:
                    comment = get_recent_comment(redditor=redditor)
                    comment_list.append(comment)
                    print('Writing redditor comment #{} to temporary list.'.format(len(comment_list)))
                except IndexError:
                    print('This redditor\'s most recent comment was unavailable, skipping to the next redditor in the list.')
                    continue
    return comment_list

def write_corpus(comment_list):
    '''Function writes the temporary list of redditor comments gotten from the get_redditor_comment_list funciton
    to the disk.
    '''
    with open('random_redditor_comments.txt', 'a', encoding='utf-8') as write_obj:
        counter = 0
        for item in comment_list:
            counter += 1
            print('Writing redditor comment #{} from temporary list to computer.'.format(counter))
            write_obj.write(item + '\n')

def run():
    '''Function runs the script.
    '''
    comment_list = get_redditor_comment_list()
    write_corpus(comment_list=comment_list)














