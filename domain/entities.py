class Client:
    def __init__(self,Id,nume,cnp):
        """
        Crearea unui nou client
        iput: Id- id client, nume- nume client, cnp-cnp clien
        """
        self.__Id=Id
        self.__nume=nume
        self.__cnp=cnp
    
    def get_id(self):
        return self.__Id
    
    def get_nume(self):
        return self.__nume
    
    def get_cnp(self):
        return self.__cnp
    

    def __str__(self):
        """
        scimba obiectul in un tip string
        output: string (customer id, name, cnp)
        """
        return str(self.get_id()) + " " + str(self.get_nume()) + " " + str(self.get_cnp())


class Film:
    def __init__(self,Id,titlu,gen,descriere):
        """
        Crearea unui nou film
        iput: Id- id film, titlu- titlu film, gen- gen film, descriere- descrierea filmului
        """
        self.__Id=Id
        self.__titlu=titlu
        self.__gen=gen
        self.__descriere=descriere
    
    def get_id(self):
        return self.__Id
    
    def get_titlu(self):
        return self.__titlu
    
    def get_gen(self):
        return self.__gen
    
    def get_descriere(self):
        return self.__descriere
    
    def __str__(self):
        """
        scimba obiectul in un tip string
        output: string (customer id, name, cnp)
        """
        return str(self.get_id()) + " " + str(self.get_titlu()) + " " + str(self.get_gen()) + " " + str(self.get_descriere())


class Inchiriere:
    def __init__(self,idi,idc,idf):
        """
        Crearea unei noi inchirieri
        input: idi-id inchirieri, idc-id client, idf- id film
        """
        self.__idi=idi
        self.__idc=idc
        self.__idf=idf
        
    def get_idi(self):
        return self.__idi
    
    def get_idc(self):
        return self.__idc
    
    def get_idf(self):
        return self.__idf
    
    def __str__(self):
        return str(self.get_idi()) + " " + str(self.get_idc()) + " " + str(self.get_idf())

def test_creare_client():
    """
    testarea crearea unui nou client
    """
    cl=Client(1,"matei",12221341221)
    assert cl.get_id()==1
    assert cl.get_nume()=='matei'
    assert cl.get_cnp()==12221341221
    
    
def test_creare_film():
    """
    testarea crearea unui nou film
    """
    fl=Film(1,"titanic","drama","barca")
    assert fl.get_id()==1
    assert fl.get_titlu()=='titanic'
    assert fl.get_gen()=="drama"
    assert fl.get_descriere()=="barca"
    
    
def test_creare_inchiriere():
    """
    testarea crearea unei noi inchirieri
    """
    inc=Inchiriere(1,2,2)
    assert inc.get_idi()==1
    assert inc.get_idc()==2
    assert inc.get_idf()==2
    
    
test_creare_client()
test_creare_film()
test_creare_inchiriere()
    
