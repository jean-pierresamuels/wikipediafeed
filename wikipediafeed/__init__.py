from pyramid.config import Configurator
from views import *


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('feed', '/wikipedia/feed')
    config.scan('.views')
    return config.make_wsgi_app()