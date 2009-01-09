from webtest import TestApp
from root import application

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
    """Root has a `intro` video"""
    res = app.get('/intro')
    assert 'div class="videoplayer" id="intro"' in res.body

