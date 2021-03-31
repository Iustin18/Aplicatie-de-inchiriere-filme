from Sort.generic_sort import GenericSort


class BubbleSort(GenericSort):
    def __init__(self, col, key, reverse,cmp):
        super().__init__(col, key, reverse,cmp)
        
    def sort(self):
        for i in range (len(self.col)-1):
            for j in range (i+1,len(self.col)):
                try:
                    x=self.col[i][0]
                    y=self.col[j][0]
                except:
                    x=self.col[i]
                    y=self.col[j]
                if self._cmp(x,y):
                    self.col[i],self.col[j]=self.col[j],self.col[i]