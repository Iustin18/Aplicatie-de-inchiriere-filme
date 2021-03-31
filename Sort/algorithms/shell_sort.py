from Sort.generic_sort import GenericSort

class ShellSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)

    def sort(self):
        n = len(self.col) 
        gap = n/2
        while gap > 0: 
            for i in range(gap,n): 
                temp = self.col[i] 
                j = i 
                while  j >= gap and self.col[j-gap] >temp: 
                    self.col[j] = self.col[j-gap] 
                    j -= gap 
                self.col[j] = temp 
            gap /= 2
