class Video(object):
    """A simple Video object"""
    def __init__(self, name, description, tags):
        self.name = name
        self.description = description
        self.tags = tags
    
    def __repr__(self):
        return u'<Video name=%s>' % self.name
    
    def get_html(self):
        markup = '<div class="videoplayer" id="%s"></div>\n' % self.name
        markup += '<div id="tags">%s</div>\n' % ', '.join([tag for tag in self.tags])
        return markup
    

videos = dict(
        intro = Video('intro', '', ['feature', 'intro',]),
        oil_on_ice = Video('oil_on_ice', '', ['feature', 'arctic', 'water',]),
        toxic_sperm = Video('toxic_sperm', '', ['feature', 'greenpeace',]),
)


def get_videos_with_tag(tag):
    """ Returns a list of video objects with the given tag
        >>> get_videos_with_tag('feature') # doctest:+ELLIPSIS
        [<Video name=...]
    """
    return [video for video in videos.values() if tag in video.tags]

def get_videos_with_tag_html(tag):
    """ Returns a list of video objects with the given tag
        >>> get_videos_with_tag_html('feature') # doctest:+ELLIPSIS
        u'<a href=...'
    """
    videos = get_videos_with_tag(tag)
    link = u'<a href="/%(name)s">%(name)s</a>'
    links = [link % {'name': video.name} for video in videos]
    return u'\n'.join(links)

