from abc import ABCMeta, abstractmethod

class ReaderView(metaclass=ABCMeta):
    '''Reader'''
    def __init__(self):
        self.__curPageNum = 1
    
    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return '第' + str(pageNum) + '頁的內容'

    def prevPage(self):
        '''Prev'''
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        '''Next'''    
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)
    
    @abstractmethod
    def _displayPage(self, content):
        '''display page'''
        pass


