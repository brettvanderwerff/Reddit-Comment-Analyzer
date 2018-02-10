'''Program brings together all the data collection modules that were created to obtain both the comment history
of a redditor of interest and random comments for comparision.
'''

from get_redditor_of_interest_comments import ObtainRedditorComments
import get_random_redditor_list
import get_random_redditor_comments

def collect_data(redditor_name):
    '''Function runs all the scripts needed to collect data from the redditor of interest and random redditors.
    '''
    print('Obtaining Reddit comments for {}'.format(redditor_name) + ' This may take several minutes.')
    frieswiththat_comments = ObtainRedditorComments(redditor_name=redditor_name, comment_limit=1000)
    frieswiththat_comments.get_all_pages()
    print('Obtaining comments from random redditors, this may take several minutes.')
    get_random_redditor_list.run()
    get_random_redditor_comments.run()

if __name__ == '__main__':
    collect_data('FriesWithThat')
