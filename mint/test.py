from webtest import TestApp, AppError
from root import application
from nose.tools import assert_raises, assert_true

app = TestApp(application)

def test_valid_root():
    res = app.get('/')
    assert "200" in res.status

def test_root_not_404():
    """Root does not return Not Found"""
    res = app.get('/')
    assert "404" not in res.status

def test_mint_in_body():
    """Root contains `mint` in body text"""
    res = app.get('/')
    assert "mint" in res.body

def test_intro_video_on_root():
    """Root has a `intro` video"""
    res = app.get('/')
    assert 'div class="videoplayer" id="intro"' in res.body

def test_intro_video_page():
    """`/intro` has a `intro` video"""
    res = app.get('/intro')
    assert 'div class="videoplayer" id="intro"' in res.body

def test_flibble_page_returns_404():
    """`/flibble` isn't a page"""
    assert_raises(
        AppError,
        app.get,
        '/flibble'
    )
    print u'who the hell called their video `flibble`'

def test_oil_on_ice_video(res=None):
    """`/oil_on_ice` video exists and has tags"""
    if not res:
        res = app.get('/oil_on_ice')
    assert_true(
     'div class="videoplayer" id="oil_on_ice"' in res.body,
     "Oil on Ice video should be there"
    )
    assert_true(
     'div id="tags"' in res.body,
     "Tags div should be there"
    )
    
    for tag in ['feature', 'arctic', 'water']:
        assert_true(
            tag in res.body,
            "%s tag should be in body" % tag
        )
    

def test_tag_page():
    """check contents of a tag page | check links on page return real video pages"""
    res = app.get('/tags/feature')
    assert_true(
        '200' in res.status,
        u'Server should return OK'
    )
    print res
    assert_true(
        'feature' in res.body,
        u'correct tag should be in body'
    )
    assert_true(
        'intro' in res.body,
        u'intro should be a featured video'
    )
    
    res = res.click('oil_on_ice')
    test_oil_on_ice_video(res)
    


def test_rules_the_world():
    print u'well done you broke the mould'
    assert True


