import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from wikipediafeed.views import home
        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual({}, response)

    def test_feed_no_url(self):
        from wikipediafeed.views import feed
        request = testing.DummyRequest(params={'feed_url': ''})
        response = feed(request)
        self.assertEqual('No url were submitted...', response['error'])

    def test_feed_incorrect_url_submitted(self):
        from wikipediafeed.views import feed
        params = {'feed_url': 'http://www.google.com'}
        request = testing.DummyRequest(params=params)
        response = feed(request)
        self.assertEqual('Url not a wikipedia domain...', response['error'])

    def test_feed_invalid_url_submitted(self):
        from wikipediafeed.views import feed
        params = {'feed_url': 'google.com'}
        request = testing.DummyRequest(params=params)
        response = feed(request)
        self.assertEqual('Invalid url entered...', response['error'])

    def test_feed_no_table_content(self):
        from wikipediafeed.views import feed
        params = {'feed_url': 'http://de.wikipedia.org/wiki/Germany'}
        request = testing.DummyRequest(params=params)
        response = feed(request)
        self.assertEqual('No Table of Content Found from the url...',
                         response['error'])

    def test_feed_table_content_present(self):
        from wikipediafeed.views import feed
        params = {'feed_url': 'https://en.wikipedia.org'
                              '/wiki/Supercell_(video_game_company)'}
        request = testing.DummyRequest(params=params)
        response = feed(request)
        self.assertEqual('', response['error'])


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from wikipediafeed import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<h2>Welcome To Wikipedia Feed</h2>', res.body)

    def test_feed(self):
        res = self.testapp.get('/wikipedia/feed', status=200)
        print res.body
        self.assertIn(b'<h2>Feedsdf Response</h2>', res.body)