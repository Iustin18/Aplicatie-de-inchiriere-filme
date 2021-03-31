from Sort.sorting import Sorting
from Sort.algorithms.bubble_sort import BubbleSort


class sortare:
    def __init__(self,repo_inchirieri,repo_clienti):
        self.__repo_inchirieri=repo_inchirieri
        self.__repo_clienti=repo_clienti
    
    def list_nume(self):
        """
        sorteaza lista de inchirieri dupa numele clientului
        """
        l=self.__repo_inchirieri.lista()
        u=[]
        for i in range (len(l)):
            ok=0
            for j in range(len(u)):
                if l[i][1].get_id()==u[j].get_id():
                    ok=1
            if ok==1:
                pass
            else:
                u.append(l[i][1])
        for i in range (len(u)):
            u[i]=u[i].get_nume()
        Sorting.sort(u,reverse=True,algorithm=BubbleSort,cmp=lambda a,b:a>b)
        return u
    
    def lista_top(self):
        """
        sorteaza lista de inchirieri dupa cele mai inchiriate filme
        """
        l=self.__repo_inchirieri.lista()
        u=[]
        for i in range (len(l)):
            ok=0
            for j in range(len(u)):
                if l[i][2].get_id()==u[j].get_id():
                    ok=1
            if ok==1:
                pass
            else:
                u.append(l[i][2])
        for i in range(len(u)):
            x=[]
            x.append(0)
            x.append(u[i])
            u[i]=x
                
        for i in range(len(u)):
            for j in range (len(l)):
                if u[i][1].get_id()==l[j][2].get_id():
                    u[i][0]=u[i][0]+1
                  
        Sorting.sort(u,algorithm=BubbleSort,reverse=True,cmp=lambda a,b:a>b)
        return u
        
            
    
    
    def list_numar(self):
        """
        sorteaza lista de inchirieri dupa numarul de inchirieri a fiecarui client
        """
        l=self.__repo_inchirieri.lista()
        u=[]
        for i in range (len(l)):
            ok=0
            for j in range(len(u)):
                if l[i][1].get_id()==u[j].get_id():
                    ok=1
            if ok==1:
                pass
            else:
                u.append(l[i][1])
        for i in range (len(u)):
            a=0
            x=[]
            for j in range (len(l)):
                if u[i].get_nume()==l[j][1].get_nume():
                    a=a+1
            x.append(a)
            x.append(u[i])
            u[i]=x
        Sorting.sort(u,algorithm=BubbleSort,cmp=lambda a,b:a>b)
        return u
            
                
    def lista_gen(self):
        """
        sorteaza lista de inchirieri dupa genul filmului
        """
        l=self.__repo_inchirieri.lista()
        u=[]
        for i in range (len(l)):
            if l[i][2].get_gen() in u:
                pass
            else:
                u.append(l[i][2].get_gen())
        for i in range (len(u)):
            a=0
            x=[]
            for j in range (len(l)):
                if u[i]==l[j][2].get_gen():
                    a=a+1
            x.append(a)
            x.append(u[i])
            u[i]=x
        Sorting.sort(u,algorithm=BubbleSort,cmp=lambda a,b:a>b)
        return u
    
    

        


