import urllib.request


def getexcuse():
    return (
        urllib.request.urlopen('https://ohjelmointitekosyyt.fi/')
        .read()
        .decode('UTF-8')
        .split('<p class="excuse"><a href=".">')[1]
        .split('</a></p>')[0]
    )
