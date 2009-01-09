from werkzeug import Response, ClosingIterator
from model import videos

html_page = '<html><head><title>%(title)s</title></head><body>%(body)s</body></html>'


def application(environ, start_response):
    default_video = u'intro'
    video_name = environ[u'PATH_INFO'].strip(u'/') or default_video
    
    response = Response(mimetype='text/html')
    if video_name.startswith('tags'):
        tag_name = video_name.split('/', 1)[1]
        body = tag_name
        body += '\n'
        body += '\n'.join([video.name for video in videos.values() if tag_name in video.tags])
        response = Response(body, mimetype='text/html')
    
    elif video_name not in videos:
        #start_response('404 NOT FOUND', [('Content-type', 'text/html')])
        content = html_page % dict(title='Not Found!!!', body='<h1>Go Away</h1>')
        response = Response(content, '404 NOT FOUND', mimetype='text/html')
        
    else:
        video = videos[video_name]
        #start_response('200 OK', [('Content-type', 'text/html')])
        content = html_page % dict(title='Welcome to mint!', body='<h1>Welcome to mint!</h1>' + video.get_html())
        response = Response(content, mimetype='text/html')
    return ClosingIterator(response(environ, start_response))

def appfactory(global_config, **local_config):
    return application