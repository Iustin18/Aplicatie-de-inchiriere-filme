from domain.entities import Inchiriere,Client,Film
from repository.repo_inchirieri import RepoInchirieri,InchirieriRepositoryException
import unittest


class TestInchirieriRepository(unittest.TestCase):
    def setUp(self):
        self.repo=RepoInchirieri()
        cl=Client(1,"iustin",1234)
        fl=Film(1,"titanic","drama","barca")
        self.repo.stocare(Inchiriere(1,cl,fl))
        
    def test_adaugare(self):
        self.assertTrue(self.repo.size()==1)
        cl=Client(1,"iustin",1234)
        fl=Film(1,"titanic","drama","barca")
        self.assertRaises(InchirieriRepositoryException,self.repo.stocare,Inchiriere(1,cl,fl))
        
    def test_return(self):
        self.assertRaises(InchirieriRepositoryException, self.repo.retur, 2)
        self.assertTrue(self.repo.size()==1)
        self.repo.retur(1)
        self.assertTrue(self.repo.size()==0)


if __name__ == '__main__':
 unittest.main()