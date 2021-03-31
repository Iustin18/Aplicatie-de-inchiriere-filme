from domain.val_filme import ValFilme,FilmValidatorException
from repository.repo_filme import RepoFilme,FilmRepositoryException
from service.serv_filme import ServFilme
import unittest


class TestFilmeService(unittest.TestCase):
    def setUp(self):
        self.serv=ServFilme(RepoFilme(),ValFilme())
        self.serv.creare_film(1, "titanic", "drama", "barca")
        
    def test_creare(self):
        self.assertTrue(self.serv.lungime()==1)
        self.assertRaises(FilmValidatorException,self.serv.creare_film, "","","","barca")
        self.assertRaises(FilmRepositoryException,self.serv.creare_film, 1,"interstellar","sf","spatiu")
        
    def test_stergere(self):
        self.assertRaises(FilmRepositoryException,self.serv.sterg_film, 2)
        self.assertTrue(self.serv.lungime()==1)
        fl=self.serv.get_film(1)
        self.serv.sterg_film(1)
        self.assertTrue(self.serv.lungime()==0)
        self.assertEqual(fl.get_id(),1)
        self.assertTrue(fl.get_titlu()=="titanic")
        self.assertTrue(fl.get_gen()=="drama")
        self.assertTrue(fl.get_descriere()=="barca")
        
        


if __name__ == '__main__':
 unittest.main()