from domain.entities import Inchiriere,Client,Film

class InchirieriRepositoryException(Exception):
    pass

class RepoInchirieri:
    def __init__(self):
        self._inchirieri={}
        
    def stocare(self,inc):
        """
        Memoreaza o inchiriere
        input: inc-inchirierea de memorat
        """
        if inc.get_idi() in self._inchirieri:
            raise InchirieriRepositoryException("Id inchiriere deja existent")
        else:
            self._inchirieri[inc.get_idi()]=inc
            
    def lista(self):
        """
        returneaza o lista de toate inchirierile
        """
        x=[]
        for i in self._inchirieri:
            l=[]
            idi=self._inchirieri[i].get_idi()
            l.append(idi)
            idc=self._inchirieri[i].get_idc()
            l.append(idc)
            idf=self._inchirieri[i].get_idf()  
            l.append(idf)
            x.append(l)
        return x
            
    def size(self):
        """
        lungimea listei
        """
        return len(self._inchirieri)
    
    def retur(self,idi):
        """
        face returul unui inchirieri
        input- idi=id inchiriere
        """
        if idi in self._inchirieri: 
            self._inchirieri.pop(idi)
        else:
            raise InchirieriRepositoryException("Id film incorect")
        
    def ret_inc(self):
        """
        returneaza toate inchirierile
        """
        return list(self._inchirieri.values())
    
    
class RepoInchirieriFile(RepoInchirieri):
    def __init__(self,InchirieriiFile):
        RepoInchirieri.__init__(self)
        self.__InchirieriiFile=InchirieriiFile
        self.__loadFromFile()
        
    def __loadFromFile(self):
        """
          incarca filme din fiser
        """
        try:
            file = open(self.__InchirieriiFile)
            content = file.read()
            file.close()
        except IOError:
            return
        for line in content.split('\n'):
            if line.strip() == "":
                continue
            fields = line.split(":")
            client=fields[1].split(" ")
            cl=Client(client[0],client[1],client[2])
            film=fields[2].split(" ")
            fl=Film(film[0],film[1],film[2],film[3])
            inc = Inchiriere(fields[0],cl,fl)
            self._inchirieri[inc.get_idi()] = inc
         
         
    def __clear_all(self):
        """
        sterge tot ce se gaseste in file
        """
        file = open(self.__InchirieriiFile, "w")
        file.close()
       
    
    def __write_all(self):
        """
        Salveaza toate filmele din memorie in file
        """
        self.__clear_all()
        file = open(self.__InchirieriiFile, "a")
        for inc in self._inchirieri.values():
            file.write(inc.get_idi() + ":")
            cl=inc.get_idc().get_id() + " " + inc.get_idc().get_nume() + " " + inc.get_idc().get_cnp()
            file.write(cl + ":")
            fl=inc.get_idf().get_id() + " " + inc.get_idf().get_titlu() + " " + inc.get_idf().get_gen() + " " + inc.get_idf().get_descriere()
            file.write(fl + "\n")
        file.close()
        
        
    def __createClientFromLine(self, line):
        """
        preia o linie din fisier si o transforma in un film
        """
        fields = line.split(" ")
        inc = Inchiriere(fields[0], fields[1], fields[2])
        return inc
    
    def stocare(self,cl):
        RepoInchirieri.stocare(self,cl)
        self.__write_all()

    def retur(self,Id):
        RepoInchirieri.retur(self, Id)
        self.__write_all()

    
def testInchirieri():
    repo=RepoInchirieri()
    repo.stocare(Inchiriere(1,2,4))
    assert repo.size()==1
    repo.retur(1)
    assert repo.size()==0
    
testInchirieri()



