from domain.entities import Client
class ClientiValidatorException (Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors

class ValClienti:
    def validare(self,cl):
        """
        Valideaza un client si verifica daca nu are campuri goale
        """
        errors=[]
        if (cl.get_id()==""): errors.append("Id Client gol")
        if (cl.get_nume()==""): errors.append("Nume Client gol")
        if (cl.get_cnp()==""): errors.append("CNP Client gol")
        if len(errors)>0:
            raise ClientiValidatorException(errors)


def testValClienti():
    """
    testare la validare
    """
    val=ValClienti()
    
    cl=Client("","","")
    try:
        val.validare(cl)
        assert False
    except ClientiValidatorException as x:
        assert len(x.getErrors())==3
    cl=Client(1,"","")
    try:
        val.validare(cl)
        assert False
    except ClientiValidatorException as x:
        assert len(x.getErrors())==2
    cl=Client(1,'mihai',1234)
    try:
        val.validare(cl)
        assert True
    except ClientiValidatorException as x:
        assert False
        
testValClienti()