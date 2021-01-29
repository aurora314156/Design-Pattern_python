from ReaderView import ReaderView

class SmoothView(ReaderView):
    def _displayPage(self, content):
        print("左右平移:", content)