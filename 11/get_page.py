import urllib.request


def get_page(url: str):
    response = urllib.request.urlopen(url)
    raw = response.read()
    html = raw.decode("utf-8")
    return html
