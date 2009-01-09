
def application(environ, start_response):
    default_video = u'intro'
    video_name = environ[u'PATH_INFO'].strip(u'/') or default_video
    if video_name == u'flibble':
        start_response('404 NOT FOUND', [('Content-type', 'text/html')])
        content = [
            '<html><head><title>Not Found!!!</title></head>\n',
            '<body><h1>Go Away</h1>\n',
            '</body></html>'
            ]
    else:
        start_response('200 OK', [('Content-type', 'text/html')])
        content = [
            '<html><head><title>Welcome to mint!</title></head>\n',
            '<body><h1>Welcome to mint!</h1>\n',
            '<div class="videoplayer" id="%s"></div>' % video_name,
            '</body></html>'
            ]
    return content

def appfactory(global_config, **local_config):
    return application