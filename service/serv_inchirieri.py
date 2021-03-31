from domain.entities import Inchiriere
from repository.repo_inchirieri import RepoInchirieri
from domain.val_inchirieri import ValInchirieri
from repository.repo_clienti import RepoClienti
from repository.repo_filme import RepoFilme
from domain.entities import Client,Film


class ServInchirieri:
    def __init__(self,repo_clienti,repo_filme,repo_inchirieri,val_inchirieri):
        """
        Inizializeaza o inchiriere
        """
        self.__repo_clienti=repo_clienti
        self.__repo_filme=repo_filme
        self.__repo_inchirieri=repo_inchirieri
        self.__val_inchirieri=val_inchirieri
        
    def adaugare_inchirieri(self,idi,idc,idf):
        """
        creaza o noua inchiriere
        input: idi- id inchiriere, idc-id client, idf-id film
        """
        cl=self.__repo_clienti.get_client(idc)
        fl=self.__repo_filme.get_film(idf)
        inc=Inchiriere(idi,cl,fl)
        self.__val_inchirieri.validator(inc)
        self.__repo_inchirieri.stocare(inc)
        return inc
    
    def lungime(self):
        """
        lungime lista
        """
        return self.__repo_inchirieri.size()
    
    def afisare_inchirieri(self):
        """
        afiseaza toate inchirierile
        """
        return self.__repo_inchirieri.ret_inc()
    
    def return_film(self,idi):
        """
        return inchiriere
        input idi-id inchiriere
        """
        self.__repo_inchirieri.retur(idi)
        return 1


def test_adaugare():
    cl=Client(1,'mihai',1234)
    fl=Film(1,"titanic","drama","barca")
    rep_c=RepoClienti()
    rep_f=RepoFilme()
    rep_c.stocare(cl)
    rep_f.stocare(fl)
    rep=RepoInchirieri()
    val=ValInchirieri()
    serv=ServInchirieri(rep_c,rep_f,rep,val)
    inc=serv.adaugare_inchirieri(1, 1, 1)
    assert inc.get_idi()==1
    assert inc.get_idc()==cl
    assert inc.get_idf()==fl
    l=serv.afisare_inchirieri()
    assert len(l)==1
    assert l[0]==inc
    
    try:
        inc=serv.adaugare_inchiriere(1,3,3)
        assert False
    except:
        assert True
        
test_adaugare()