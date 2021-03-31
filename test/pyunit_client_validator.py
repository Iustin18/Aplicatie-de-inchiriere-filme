from domain.entities import Client
from domain.val_clienti import ValClienti,ClientiValidatorException
import unittest


class TestClientiValidator(unittest.TestCase):
    def setUp(self):
        self.val=ValClienti()
        
    def test_validare(self):
        self.assertRaises(ClientiValidatorException, self.val.validare, Client("","iustin",1234))
        self.assertRaises(ClientiValidatorException, self.val.validare, Client("1","",1234))
        self.assertRaises(ClientiValidatorException, self.val.validare, Client("1","iustin",""))
        self.val.validare(Client(1,"iustin",1234))
        
    
if __name__ == '__main__':
 unittest.main()