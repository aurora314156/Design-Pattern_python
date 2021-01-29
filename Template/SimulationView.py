from ReaderView import ReaderView

class SimulationView(ReaderView):
    def _displayPage(self, content):
        print("擬真翻頁:", content)