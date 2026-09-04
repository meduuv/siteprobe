from siteprobe import host, status_family

def test_host():
    assert host("https://example.com/a") == "example.com"

def test_status_family():
    assert status_family(201) == "2xx"
    assert status_family(503) == "5xx"
