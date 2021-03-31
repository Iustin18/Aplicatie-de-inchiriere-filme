from domain.val_clienti import ValClienti,ClientiValidatorException
from repository.repo_clienti import RepoClienti,ClientiRepositoryException
from service.serv_clienti import ServClienti
import unittest


class TestClientiService(unittest.TestCase):
    def setUp(self):
        self.serv=ServClienti(RepoClienti(),ValClienti())
        self.serv.creare_client(1, "iustin", 1234)
    
    def test_creare(self):
        self.assertTrue(self.serv.lungime()==1)
        self.assertRaises(ClientiValidatorException,self.serv.creare_client, "","",1234)
        self.assertRaises(ClientiRepositoryException,self.serv.creare_client, 1,"mihai", 1234)
        
    def test_stergere(self):
        self.assertRaises(ClientiRepositoryException, self.serv.sterg_client, 2)
        self.assertTrue(self.serv.lungime()==1)
        cl=self.serv.get_client(1)
        self.serv.sterg_client(1)
        self.assertTrue(self.serv.lungime()==0)
        self.assertEquals(cl.get_id(),1)
        self.assertTrue(cl.get_nume()=="iustin")
        self.assertTrue(cl.get_cnp()==1234)


if __name__ == '__main__':
 unittest.main()