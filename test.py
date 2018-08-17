from bfurlparser import urlparse
from time import time


class Fatal(Exception):
    pass

class NoMatches(Fatal):
    """This is thrown when a regular expression or tag match has failed. Thrown inRepsonse.py"""
    name = 'no_matches'

# we parse the url into basic components in order to transform it into a canonical form
def parse_url_bf(url):
    o = None
    try:
        o = urlparse(url)
    except Exception as e:
        print "FAIL: ", e
        raise NoMatches("invalid url %s" % (url, )) 

    return (
        o['proto'],
        o['hostname'],
        o['port'],
        o['path'],
        o['query'],
        o['fragment']
    )

def fetch_url_parts_bf(url):
    # support quoted urls as inputs
    (protocol, host, port, path, get, fragment) = parse_url_bf(url)
    return (protocol, host, port, path, get, fragment)

print fetch_url_parts_bf("https://")
print fetch_url_parts_bf("http://www.sapo.pt")
print fetch_url_parts_bf("http://www.sapo.pt:99")
print fetch_url_parts_bf("http://www.sapo.pt:99#something")
print fetch_url_parts_bf("http://www.sapo.pt#something")
print fetch_url_parts_bf("http://www.sapo.pt/#something")
print fetch_url_parts_bf("http://www.sapo.pt/a/path/file?a_argument=a_value&another_argument=another_value#something")
print fetch_url_parts_bf("http://www.sapo.pt/a/path/file#something")



# load test

if 1:
    print ""
    print "SPEED TEST:"
    print "bf:"
    start = time()
    for x in range(1, 500000):
        fetch_url_parts_bf("http://www.sapo.pt/a/path/file?a_argument=a_value&another_argument=another_value#something")
    spent = time() - start
    print "  Took: {}".format(spent)
