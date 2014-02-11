def test_url(marionette, test_info):
    url = marionette.get_url()
    print test_info
    assert url == "asdf", "error error arms flailing wildly"

def test_foo_1(marionette, test_info):
    url = marionette.get_url()
    assert True, "you shall pass"
    
def test_foo_2(marionette, test_info, foo):
    print foo
    url = marionette.get_url()
    assert True, "you shall pass"
