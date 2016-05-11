from pyramid.view import view_config

import urllib2
import logging
import validators
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)
BASE_TEMPLATES = 'templates/'


@view_config(route_name='home', renderer='{0}welcome.pt'
             .format(BASE_TEMPLATES))
def home(request):
    """
    Landing page for the wikipedia-feed
    """
    log.debug('In Home View')
    return {}


@view_config(route_name='feed', renderer='{0}feed_response.pt'
             .format(BASE_TEMPLATES))
def feed(request):
    """
    View that process the posted submitted_url
    """
    log.debug('In Feed View')
    view_response = dict(table_of_content='', error='')
    # get url submitted
    if request.POST.get('feed_url'):
        feed_url = request.POST.get('feed_url')
        if not validators.url(feed_url):
            view_response['error'] = 'Invalid url entered...'
            return view_response
        if 'wikipedia.org/' not in feed_url:
            # check if the url submitted a wikipedia url
            view_response['error'] = 'Url not a wikipedia domain...'
            return view_response
        response = urllib2.urlopen(feed_url)
        # retrieve the html page
        html = response.read()
        # convert the html to xml-format
        soup = BeautifulSoup(html, "lxml")
        # Get the table content with specific tag and class
        view_response['table_of_content'] = soup.find('div', class_="toc")
    else:
        # return error that no url entered
        view_response['error'] = 'No url were submitted...'
        return view_response
    if not view_response['table_of_content']:
        # return error that table of content found
        view_response['error'] = 'No Table of Content Found from the url...'
    return view_response