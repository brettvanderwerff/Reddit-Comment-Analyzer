import requests
import time

class ObtainRedditorComments():
    '''Class obtains a specified number of comments from a specified redditor using the
     Pushshift Reddit API (https://github.com/pushshift/api). Using this API allows the user to bypass comment request
     limits of PRAW.
     '''
    def __init__(self, redditor_name, comment_limit):
        self.redditor_name = redditor_name
        self.comment_limit = comment_limit
        self.base_url = 'https://api.pushshift.io/reddit/comment/search?author={}' \
                        '&sort=desc&sort_type=created_utc&size=100&{}{}'

    def write_corpus(self, corpus):
        '''Function writes corpus of comments to the disk under name of the redditor for which comments
        are obtained for.
        '''
        print('Writing to file {}.txt'.format(self.redditor_name))
        with open('{}.txt'.format(self.redditor_name), 'w', encoding='utf-8') as file_object:
            for item in corpus:
                file_object.write(item + '\n')

    def get_first_utc(self):
        '''Function obtains timestamp for a recent, arbitrarily chosen comment (alpha comment).
        get_first_page and get_next_page functions work to scroll through more recent and older
        comments all relative to this alpha comment.
        '''
        utc_request = requests.get(self.base_url.format(self.redditor_name, '', ''))
        utc_request_json = utc_request.json()
        return utc_request_json['data'][-1]['created_utc']

    def get_first_page(self, utc):
        '''Function scrolls to comments more recent than the alpha comment of the get_first_utc response.
        '''
        print('Getting a page of comments.')
        first_page_request = requests.get(self.base_url.format(self.redditor_name, 'after=', utc))
        first_page_request_json = first_page_request.json()
        first_page_request_json
        corpus = []
        for item in first_page_request_json['data']:
            corpus.append(item['body'])
            if len(corpus) == self.comment_limit:
                break
            else:
                continue
        return corpus

    def get_next_pages(self, utc, corpus):
        '''Function scrolls to comments older than the alpha comment of the get_first_utc response.
        '''
        sub_request = requests.get(self.base_url.format(self.redditor_name, 'before=', utc))
        sub_request_json = sub_request.json()
        utc = sub_request_json['data'][-1]['created_utc']
        for item in sub_request_json['data']:
            corpus.append(item['body'])
            if len(corpus) == self.comment_limit:
                break
            else:
                continue
        time.sleep(20)
        return utc, corpus

    def get_all_pages(self):
        '''Function obtains all desired comments by a redditor(limit specified by the user under comment_limit
        argument of class). Function writes collection of comments to the disk when either the limit is reached
        or there are no more comments. This is the only method of this class intended for call.
        '''
        utc = self.get_first_utc()
        corpus = self.get_first_page(utc)
        while True:
            try:
                if len(corpus) == self.comment_limit:
                    self.write_corpus(corpus)
                    print('{} total comments found'.format(len(corpus)))
                    exit()
                else:
                    print('Getting a page of comments.')
                    utc, corpus = self.get_next_pages(utc, corpus)
            except IndexError:
                self.write_corpus(corpus)
                print('Cannot find anymore comments, {} total comments found.'.format(len(corpus)))
                exit()




