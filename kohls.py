#!/usr/bin/python

from bs4 import BeautifulSoup

from urllib.request import Request, urlopen, FancyURLopener

import sys

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication



class Render(QWebPage):

	app = QApplication(sys.argv)

	def __init__(self, url):
		QWebPage.__init__(self)
		self.loadFinished.connect.(self._loadFinished)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def _loadFinished(self, result):
		self.frame = self.mainFrame()
		self.app.quit()




if __name__ == "__main__":
	
	req= Request(
		'https://www.kohls.com/catalog/clearance.jsp?CN=PriceType:Clearance&PPP=30',
		headers={'User-Agent': 'Mozilla/5.0'}
		)

	req2 = 'https://www.kohls.com/catalog/clearance.jsp?CN=PriceType:Clearance&PPP=30'

	
	page = Render(req2)
	src = page.html

	print(src)

	soup = BeautifulSoup(src, "html.parser")


	items = soup.findAll(class_='products_grid')

	for item in items:
		print(item)

	


	



'''
def render(source_html):
    """Return rendered HTML."""
    try:
        from PyQt5.QtCore import QEventLoop
        from PyQt5.QtWebEngineWidgets import QWebEngineView
        from PyQt5.QtWidgets import QApplication

        class Render(QWebEngineView):
            """Render HTML with PyQt5 WebEngine."""

            def __init__(self, html):
                self.html = None
                self.app = QApplication(sys.argv)
                QWebEngineView.__init__(self)
                self.loadFinished.connect(self._loadFinished)
                self.setHtml(html)
                while self.html is None:
                    self.app.processEvents(
                        QEventLoop.ExcludeUserInputEvents |
                        QEventLoop.ExcludeSocketNotifiers |
                        QEventLoop.WaitForMoreEvents)
                self.app.quit()

            def _callable(self, data):
                self.html = data

            def _loadFinished(self, result):
                self.page().toHtml(self._callable)
    except ImportError:
        from PyQt5.QtWebKitWidgets import QWebPage
        from PyQt5.QtWidgets import QApplication

        class Render(QWebPage):
            """Render HTML with PyQt5 WebKit."""

            def __init__(self, html):
                self.html = None
                self.app = QApplication(sys.argv)
                QWebPage.__init__(self)
                self.loadFinished.connect(self._loadFinished)
                self.mainFrame().setHtml(html)
                self.app.exec_()

            def _loadFinished(self, result):
                self.html = self.mainFrame().toHtml()
                self.app.quit()

    return Render(source_html).html

'''



