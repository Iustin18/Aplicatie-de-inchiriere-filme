from domain.entities import Client,Film
from domain.val_inchirieri import ValInchirieri,InchirieriValidatorException
from repository.repo_inchirieri import RepoInchirieri,InchirieriRepositoryException
from repository.repo_clienti import RepoClienti
from repository.repo_filme import RepoFilme
from service.serv_inchirieri import ServInchirieri
import unittest


class TestInchirieriService(unittest.TestCase):
    def setUp(self):
        self.serv=ServInchirieri(RepoClienti(),RepoFilme(),RepoInchirieri(),ValInchirieri())
        self.rep_c=RepoClienti()
        self.rep_f=RepoFilme()
        cl=Client(1,"iustin",1234)
        self.rep_c.stocare(cl)
        fl=Film(1,"titanic","drama","barca")
        self.rep_f.stocare(fl)
        self.serv.adaugare_inchirieri(1, 1, 1)
        
    def test_creare(self):
        self.assertTrue(self.serv.lungime()==1)

if __name__ == '__main__':
 unittest.main()