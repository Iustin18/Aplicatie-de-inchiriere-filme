from domain.entities import Inchiriere
from domain.val_inchirieri import ValInchirieri,InchirieriValidatorException
import unittest


class TestInchirieriValidator(unittest.TestCase):
    def setUp(self):
        self.val=ValInchirieri()
        
    def test_validare(self):
        self.assertRaises(InchirieriValidatorException,self.val.validator, Inchiriere("",1,1))
        self.val.validator(Inchiriere(1,1,1))


if __name__ == '__main__':
 unittest.main()