from domain.entities import Film
from domain.val_filme import ValFilme
from repository.repo_filme import RepoFilme


class ServFilme:
    def __init__(self,repo_filme,val_filme):
        """
        inizializeaza un nou film
        """
        self.__repo_filme=repo_filme
        self.__val_filme=val_filme
        
    def creare_film(self,Id,titlu,gen,descriere):
        """
        creaza un nou film
        Input: Id-id film, titlu- titlu film, gen-gen film, descriere-descriere film
        """
        fl=Film(Id,titlu,gen,descriere)
        self.__val_filme.validator(fl)
        self.__repo_filme.stocare(fl)
        return fl
    
    def get_filme(self):
        """
        returneaza o lista cu toate filmele
        """
        return self.__repo_filme.get_filme()
    
    def lungime(self):
        """
        lungimea listei
        """
        return self.__repo_filme.size()
    
    def sterg_film(self,Id):
        """
        sterge un film
        input: id-id film de sters
        """
        self.__repo_filme.delete_film(Id)
        
    def modific_film(self,Id,titlu,gen,descriere):
        """
        modifica filmul
        inout: Id- id film de modificat,titlu-titlu nou,gen-gen nou,descriere- descriere noua
        """
        fl=Film(Id,titlu,gen,descriere)
        self.__val_filme.validator(fl)
        self.__repo_filme.mod_film(fl)
        return fl
        
    def caut_film_id(self,Id):
        """
        cauta un film dupa id
        input: id-id film
        """
        return self.__repo_filme.get_film_id(Id)
    
    def caut_film_titlu(self,titlu,x,y):
        """
        cauta film dupa titlu
        input: titlu-titlu film
        """
        return self.__repo_filme.get_film_titlu(titlu,x,y)
    
    def get_film(self,id):
        return self.__repo_filme.get_film(id)


def testCreareFilme():
    repo=RepoFilme()
    val=ValFilme()
    serv=ServFilme(repo,val)
    fl=serv.creare_film(1,"titanic","drama","barca")
    assert fl.get_id()==1
    assert fl.get_titlu()=="titanic"
    l=serv.get_filme()
    assert len(l)==1
    assert l[0]==fl
    
    try:
        fl=serv.creare_client(1,'frozen',"cartoon","zapada")
        assert False
    except:
        assert True
    
    
    
testCreareFilme()
