from werkzeug import Response, ClosingIterator
from model import videos

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
        return ClosingIterator(response(environ, start_response))
    
    if video_name not in videos:
        start_response('404 NOT FOUND', [('Content-type', 'text/html')])
        content = [
            '<html><head><title>Not Found!!!</title></head>\n',
            '<body><h1>Go Away</h1>\n',
            '</body></html>'
            ]
    else:
        video = videos[video_name]
        start_response('200 OK', [('Content-type', 'text/html')])
        content = [
            '<html><head><title>Welcome to mint!</title></head>\n',
            '<body><h1>Welcome to mint!</h1>\n',
            video.get_html(),
            '</body></html>'
            ]
    return content

def appfactory(global_config, **local_config):
    return application