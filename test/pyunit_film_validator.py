from domain.entities import Film
from domain.val_filme import ValFilme,FilmValidatorException
import unittest


class TestFilmeValidator(unittest.TestCase):
    def setUp(self):
        self.val=ValFilme()
        
    def test_validare(self):
        self.assertRaises(FilmValidatorException, self.val.validator, Film("","titanic","drama","barca"))
        self.assertRaises(FilmValidatorException, self.val.validator, Film(1,"","drama","barca"))
        self.assertRaises(FilmValidatorException, self.val.validator, Film(1,"titanic","","barca"))
        self.assertRaises(FilmValidatorException, self.val.validator, Film(1,"titanic","drama",""))
        self.val.validator(Film(1,"titanic","drama","barca"))


if __name__ == '__main__':
 unittest.main()