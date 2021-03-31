
from domain.entities import Client
from repository.repo_clienti import RepoClienti
from domain.val_clienti import ValClienti



class ServClienti:
    def __init__(self,repo_clienti,val_clienti):
        """
        inizializeaza un nou client
        """
        self.__repo_clienti=repo_clienti
        self.__val_clienti=val_clienti
        
    def creare_client(self,Id,nume,cnp):
        """
        creaza un nou client
        Input: Id-id client, nume- nume client, cnp-cnp client
        """
        cl=Client(Id,nume,cnp)
        self.__val_clienti.validare(cl)
        self.__repo_clienti.stocare(cl)
        return cl
    
    def get_clienti(self):
        """
        returneaza o lista cu toti clienti
        """
        return self.__repo_clienti.get_clienti()
    
    def lungime(self):
        """
        reeturneaza lungimea listei
        """
        return self.__repo_clienti.size()
    
    def sterg_client(self,Id):
        """
        sterge un client
        inpput: id-id client de sters
        """
        self.__repo_clienti.delete_client(Id)
        
    def modific_client(self,Id,nume,cnp):
        """
        modifica client
        inout: Id- id client de modificat,nume-nume nou,cnp-cnp nou
        """
        cl=Client(Id,nume,cnp)
        self.__val_clienti.validare(cl)
        self.__repo_clienti.mod_client(cl)
        return cl
        
    def caut_client_id(self,Id):
        """
        cauta un client dupa id
        input: id-id client
        """
        return self.__repo_clienti.get_client_id(Id)
    
    def caut_client_nume(self,nume,x,lista):
        """
        cauta client dupa nume
        input: nume-nume client
        """
        return self.__repo_clienti.get_client_nume(nume,x,lista)
    
    def get_client(self,idc):
        return self.__repo_clienti.get_client(idc)


def testCreareClient():
    repo=RepoClienti()
    val=ValClienti()
    serv=ServClienti(repo,val)
    cl=serv.creare_client(1,"mihai",12345)
    assert cl.get_id()==1
    assert cl.get_nume()=="mihai"
    l=serv.get_clienti()
    assert len(l)==1
    assert l[0]==cl
    
    try:
        cl=serv.creare_client(1,'vlad',123)
        assert False
    except:
        assert True
    
    
    
testCreareClient()