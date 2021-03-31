from domain.entities import Client
from repository.repo_clienti import RepoClienti,ClientiRepositoryException
import unittest


class TestCaseClientiRepository(unittest.TestCase):
    def setUp(self):
        self.repo=RepoClienti()
        self.repo.stocare(Client(1,"iustin",1234))
        
    def test_adaugare(self):
        self.assertTrue(self.repo.size()==1)
        self.assertRaises(ClientiRepositoryException, self.repo.stocare, Client(1,"amalia",1234))
    
    def test_stergere(self):
        self.assertRaises(ClientiRepositoryException, self.repo.delete_client, 2)
        self.assertTrue(self.repo.size()==1)
        self.repo.delete_client(1)
        self.assertTrue(self.repo.size()==0)


if __name__ == '__main__':
 unittest.main()