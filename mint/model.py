class Video(object):
    """A simple Video object"""
    def __init__(self, name, description, tags):
        self.name = name
        self.description = description
        self.tags = tags
    
    def __str__(self):
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
