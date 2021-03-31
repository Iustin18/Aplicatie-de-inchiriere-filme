from domain.entities import Client, Film
from repository.repo_clienti import RepoClienti
from repository.repo_filme import RepoFilme
from repository.repo_inchirieri import RepoInchirieri
from domain.val_inchirieri import ValInchirieri
from service.serv_inchirieri import ServInchirieri
from sortare.sort import sortare


class ServRapoarte:
    def __init__(self,repo_inchirieri,sortare):
        self.__repo__inchirieri=repo_inchirieri
        self.__sortare=sortare
        
    def lista_nume(self):
        """
        returneaza o lista sortata dupa nume
        """
        return self.__sortare.list_nume()
    
    def lista_numar(self):
        """
        sorteaza lista de inchirieri dupa numarul de inchirieri a fiecarui client
        """
        return self.__sortare.list_numar()
            
    def top(self):
        """
        sorteaza lista de inchirieri dupa cele mai inchiriate filme
        """
        return self.__sortare.lista_top()
    
    def lista_gen(self):
        """
        sorteaza lista de inchirieri dupa genul filmului
        """
        return self.__sortare.lista_gen()
    
def testListaNume():
    
    rep_c=RepoClienti()
    rep_f=RepoFilme()
    repo=RepoInchirieri()
    sort=sortare(repo,rep_c)
    val=ValInchirieri()
    serv=ServInchirieri(rep_c,rep_f,repo,val)
    cl=Client(1,'vlad',12345)
    fl=Film(1,'titanic','dram','barca')
    rep_c.stocare(cl)
    rep_f.stocare(fl)
    serv.adaugare_inchirieri(1,1,1)
    cl=Client(2,"mihai",1222)
    fl=Film(2,"avatar","sf","cascas")
    rep_c.stocare(cl)
    rep_f.stocare(fl)
    serv.adaugare_inchirieri(2,1,2)
    serv.adaugare_inchirieri(3,2,2)
    cl=Client(3,"amalia",1222)
    fl=Film(3,"intertellar","sf","cascas")
    rep_c.stocare(cl)
    rep_f.stocare(fl)
    serv.adaugare_inchirieri(4,3,3)
    serv.adaugare_inchirieri(5,3,2)
    fl=Film(4,"froz","cart","zap")
    rep_f.stocare(fl)
    serv.adaugare_inchirieri(6,1,4)
    serv2=ServRapoarte(repo,sort)
    l=serv2.top()
    assert l[0][1]==rep_f.get_film(1)
    l=serv2.lista_nume()
    assert l[1]==rep_c.get_client(2).get_nume()
    l=serv2.lista_numar()
    assert l[0][1]==rep_c.get_client(2)
    l=serv2.lista_gen()
    assert l[0][1]=='dram'
    
    
testListaNume()


