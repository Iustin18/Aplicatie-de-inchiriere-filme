from domain.entities import Film

class FilmValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors

class ValFilme:
    def validator(self,fl):
        """
        Valideaza un film si verifica daca nu are campuri goale
        """
        errors=[]
        if (fl.get_id()==""): errors.append("Id film gol")
        if (fl.get_titlu()==""): errors.append("Titlu film gol")
        if (fl.get_gen()==""): errors.append("Gen film gol")
        if (fl.get_descriere()==""): errors.append("Descriere film goala")
        if len(errors)>0:
            raise FilmValidatorException(errors)
        
        
def testValFilme():
    """
    testare la validare
    """
    val=ValFilme()
    fl=Film("","","","")
    try:
        val.validator(fl)
        assert False
    except FilmValidatorException as ex:
        assert len(ex.getErrors())==4
    fl=Film(1,"","","")
    try:
        val.validator(fl)
        assert False
    except FilmValidatorException as ex:
        assert len(ex.getErrors())==3
    fl=Film(1,"as","asdasd","asdasda")
    try:
        val.validator(fl)
        assert True
    except FilmValidatorException as ex:
        assert False
    

testValFilme()
