from watch import parse

def test_non():
    assert parse('<iframe src="https://vimeo.com/12345"></iframe>') == None

def test_link():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
