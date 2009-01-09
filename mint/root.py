import cgi

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    greeting = u"Welcome to mint!"
    content = [
        '<html><head><title>%s</title></head>\n' % greeting,
        '<body><h1>%s!</h1>\n' % greeting,
        ]
    content.append('</body></html>')
    return content

def appfactory(global_config, **local_config):
    return application