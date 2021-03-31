from domain.entities import Film
from repository.repo_filme import RepoFilme,FilmRepositoryException
import unittest


class TestfilmeRepository(unittest.TestCase):
    def setUp(self):
        self.repo=RepoFilme()
        self.repo.stocare(Film(1,"titanic","drama","barca"))
        
    def test_adaugare(self):
        self.assertTrue(self.repo.size()==1)
        self.assertRaises(FilmRepositoryException,self.repo.stocare, Film(1,"interstellar","sf","spatiu"))
        
    def test_stergere(self):
        self.assertRaises(FilmRepositoryException,self.repo.delete_film,2)
        self.assertTrue(self.repo.size()==1)
        self.repo.delete_film(1)
        self.assertTrue(self.repo.size()==0)

if __name__ == '__main__':
 unittest.main()