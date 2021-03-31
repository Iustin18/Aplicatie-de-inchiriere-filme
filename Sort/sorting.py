from Sort.algorithms.algorithm import Algorithm


class Sorting(object):
    
    @staticmethod
    def sort(col, key=None, reverse=False, algorithm=Algorithm.BUBBLE_SORT,cmp=lambda a,b:a>b):
        sorting_alg = algorithm(col, key, reverse,cmp)
        sorting_alg.sort()