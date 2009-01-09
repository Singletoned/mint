import cgi

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    content = [
        '<html><head><title>Welcome to mint!</title></head>\n',
        '<body><h1>Welcome to mint!</h1>\n',
        '<div class="videoplayer" id="intro"></div>',
        '</body></html>'
        ]
    return content

def appfactory(global_config, **local_config):
    return application