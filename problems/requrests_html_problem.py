
""" TESTING this module in wsl ubuntu

>>> res.html.render()
[W:pyppeteer.chromium_downloader] start chromium download.
Download may take a few minutes.
100%|███████████████| 108773488/108773488 [00:04<00:00, 23784068.80it/s]
[W:pyppeteer.chromium_downloader]
chromium download done.
[W:pyppeteer.chromium_downloader] chromium extracted to: /home/alexzander/.local/share/pyppeteer/local-chromium/588429
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/alexzander/.local/lib/python3.8/site-packages/requests_html.py", line 586, in render
    self.browser = self.session.browser  # Automatically create a event loop and browser
  File "/home/alexzander/.local/lib/python3.8/site-packages/requests_html.py", line 730, in browser
    self._browser = self.loop.run_until_complete(super().browser)
  File "/usr/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "/home/alexzander/.local/lib/python3.8/site-packages/requests_html.py", line 714, in browser
    self._browser = await pyppeteer.launch(ignoreHTTPSErrors=not(self.verify), headless=True, args=self.__browser_args)
  File "/home/alexzander/.local/lib/python3.8/site-packages/pyppeteer/launcher.py", line 306, in launch
    return await Launcher(options, **kwargs).launch()
  File "/home/alexzander/.local/lib/python3.8/site-packages/pyppeteer/launcher.py", line 167, in launch
    self.browserWSEndpoint = get_ws_endpoint(self.url)
  File "/home/alexzander/.local/lib/python3.8/site-packages/pyppeteer/launcher.py", line 228, in get_ws_endpoint
    with urlopen(url) as f:
  File "/usr/lib/python3.8/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.8/urllib/request.py", line 525, in open
    response = self._open(req, data)
  File "/usr/lib/python3.8/urllib/request.py", line 542, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "/usr/lib/python3.8/urllib/request.py", line 502, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.8/urllib/request.py", line 1379, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "/usr/lib/python3.8/urllib/request.py", line 1354, in do_open
    r = h.getresponse()
  File "/usr/lib/python3.8/http/client.py", line 1347, in getresponse
    response.begin()
  File "/usr/lib/python3.8/http/client.py", line 307, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.8/http/client.py", line 289, in _read_status
    raise BadStatusLine(line)
http.client.BadStatusLine: GET /json/version HTTP/1.1
"""


# issues
# https://www.google.com/search?safe=active&sxsrf=ALeKk01VCtX4PapsLxA3M0Lijv_OJ4KkAw%3A1614582790348&ei=BpQ8YIDnFNeHjLsPnLOb4As&q=requests_html+html+render+doesn%27t+work&oq=req&gs_lcp=Cgdnd3Mtd2l6EAMYATIECCMQJzIECCMQJzIECCMQJzIFCAAQkQIyBAgAEEMyBAguEEMyAggAMgIIADICCAAyBAgAEEM6BwgAEEcQsAM6CAguEMcBEKMCOgIILlDFnawBWMWgrAFg6KusAWgBcAJ4AIABmAGIAYoEkgEDMC40mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz

from requests_html import HTMLSession # pip install requests_html
# after i installed the module in python 3.6
# i got this error
"""
Traceback (most recent call last):
  File ".\problems.py", line 52, in <module>
    from requests_html import HTMLSession # pip install requests_html
  File "D:\Applications\python36\lib\site-packages\requests_html.py", line 9, in <module>
    from pyppeteer.launcher import launch, executablePath  # noqa: E402
  File "D:\Applications\python36\lib\site-packages\pyppeteer\launcher.py", line 18, in <module>
    from pyppeteer.browser import Browser
  File "D:\Applications\python36\lib\site-packages\pyppeteer\browser.py", line 12, in <module>
    from pyppeteer.connection import Connection
  File "D:\Applications\python36\lib\site-packages\pyppeteer\connection.py", line 12, in <module>
    import websockets
  File "D:\Applications\python36\lib\site-packages\websockets\__init__.py", line 3, in <module>
    from .auth import *
  File "D:\Applications\python36\lib\site-packages\websockets\auth.py", line 15, in <module>
    from .server import HTTPResponse, WebSocketServerProtocol
  File "D:\Applications\python36\lib\site-packages\websockets\server.py", line 49, in <module>
    from .protocol import WebSocketCommonProtocol
  File "D:\Applications\python36\lib\site-packages\websockets\protocol.py", line 18, in <module>
    from typing import (
ImportError: cannot import name 'Deque'
"""
# then i went in the module
# commented this part
"""
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    # Deque, <------------------------------
    Dict,
    Iterable,
    List,
    Optional,
    Union,
    cast,
)
"""
# and
"""
modified this
self.messages: Deque[Data] = collections.deque()

to this
self.messages = collections.deque()
"""
# and after that worked


from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=I22AqV9zV50"

session = HTMLSession()
response = session.get(url)
if response.status_code != 200:
    response.raise_for_status()

r"""
  [W:pyppeteer.chromium_downloader] start chromium download.
  Download may take a few minutes.
  [W:pyppeteer.chromium_downloader] chromium download done.
  [W:pyppeteer.chromium_downloader] chromium extracted to: C:\Users\dragonfire\.pyppeteer\local-chromium\533271
"""

response.html.render(timeout=20)

soup = BeautifulSoup(response.html.html, "html.render")
print(soup)

print("it worked")
session.close()
