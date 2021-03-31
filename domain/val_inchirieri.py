from domain.entities import Inchiriere
class InchirieriValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors


class ValInchirieri:
    def validator(self,inc):
        """
        Valideaza o inchirieri si verifica daca nu are campuri goale
        """
        errors=[]
        if (inc.get_idi()==""): errors.append("Id Inchiriere gol")
        if len(errors)>0: raise InchirieriValidatorException(errors)


def TestValInchirieri():
    """
    testare la validare
    """
    val=ValInchirieri()
    inc=Inchiriere("","","")
    try:
        val.validator(inc)
        assert False
    except InchirieriValidatorException as x:
        assert len(x.getErrors())==1

    inc=Inchiriere(1,2,4)
    try:
        val.validator(inc)
        assert True
    except InchirieriValidatorException as x:
        assert False

TestValInchirieri()


