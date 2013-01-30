from fabric.api import local
import boto

def build():
    """Build the presentation."""
    #local("rst2s5.py aws-python-boto.rst aws-python-boto/index.html")
    local("python ../bin/rst-directive.py --stylesheet=pygments.css \
            --quiet \
            basic_python.rst > basic_python/index.html")

def upload():
    """Upload the presentation to the prepared location in S3"""
    c = boto.connect_s3()
    b = c.get_bucket('presentations.uberhip.com')
    k = boto.s3.key.Key(b)
    k.key = "aws-python-boto/index.html"
    k.set_contents_from_filename("aws-python-boto/index.html")
    k.set_acl('public-read')
    k.set_metadata('Content-Type','text/html')
