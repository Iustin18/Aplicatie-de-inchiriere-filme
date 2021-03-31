from domain.entities import Client
class ClientiRepositoryException(Exception):
    pass


class RepoClienti:
    def __init__(self):
        self._clienti={}
        
        
    def stocare(self,cl):
        """
        Memoreaza un client
        input: cl-cliemntul de memorat
        """
        if cl.get_id() in self._clienti:
            raise ClientiRepositoryException("Id deja existent")
        else:
            self._clienti[cl.get_id()]=cl
            
    def get_clienti(self):
        """
        returneaza lista cu toti clienti
        """
        return list(self._clienti.values())
    
    def get_client(self,idc):
        """
        returneaza un singur client
        input idc-id client
        """
        try:
            return self._clienti[idc]
        except:
            raise ClientiRepositoryException("Client inexistent")
    
    
    def size(self):
        """
        lungimea listei
        """
        return len(self._clienti)


    def delete_client(self,Id):
        """
        sterge un client
        input: id-id client de sters
        """
        if Id in self._clienti:
            self._clienti.pop(Id)
        else:
            raise ClientiRepositoryException("Id insexistent")
        
    def mod_client(self,cl):
        """
        Modifica un client
        input cl-noul client 
        """
        if cl.get_id() in self._clienti:
            self._clienti[cl.get_id()]=cl
        else:
            raise ClientiRepositoryException("Id inexistent! ")
        
    def get_client_id(self,Id):
        """
        Returneaza un client prin id ul sau
        input: id-id client
        """
        if Id in self._clienti:
            l=[]
            l.append(self._clienti[Id].get_id())
            l.append(self._clienti[Id].get_nume())
            l.append(self._clienti[Id].get_cnp())
            return l
        else:
            raise ClientiRepositoryException("Id inexistent! ")
        
    def contr_inchirieri(self,idc):
        if idc in self._clienti:
            return 
        else:
            raise ClientiRepositoryException("Id client inexistent")
        
    def get_client_nume(self,nume,indx,lista):
        """
        Returneaza un client prin numele sau
        input: nume-nume client
        """
        l=list(self._clienti.values())
        subl=[]
        #Non recursiv
        """
        x=[]
        for i in range (len(self._clienti)):
            if l[i].get_nume()==nume:
                subl=[]
                subl.append(l[i].get_id())
                subl.append(l[i].get_nume())
                subl.append(l[i].get_cnp())
                x.append(subl)
        return x
        """
        #recursiv
        x=lista
        if l[indx].get_nume()==nume:
            subl=[]
            subl.append(l[indx].get_id())
            subl.append(l[indx].get_nume())
            subl.append(l[indx].get_cnp())
            x.append(subl)
        indx=indx+1
        if indx>=len(l):
            return x
        return self.get_client_nume(nume,indx,x)
        
        


class RepoClientiFile(RepoClienti):
    def __init__(self,ClientiFile):
        RepoClienti.__init__(self)
        self.__ClientiFile=ClientiFile
        self.__loadFromFile()
        
    def __loadFromFile(self):
        """
          incarca client din fiser
        """
        try:
            file = open(self.__ClientiFile)
            content = file.read()
            file.close()
        except IOError:
            return
        for line in content.split('\n'):
            if line.strip() == "":
                continue
            fields = line.split(" ")
            cl = Client(fields[0], fields[1], fields[2])
            self._clienti[cl.get_id()] = cl
         
         
    def __clear_all(self):
        """
        sterge tot ce se gaseste in file
        """
        file = open(self.__ClientiFile, "w")
        file.close()
       
    
    def __write_all(self):
        """
        Salveaza toate filmele din memorie in file
        """
        self.__clear_all()
        file = open(self.__ClientiFile, "a")
        for cl in self._clienti.values():
            file.write(cl.get_id() + " ")
            file.write(cl.get_nume() + " ")
            file.write(cl.get_cnp() + "\n")
        file.close()
        
        
    def __createClientFromLine(self, line):
        """
        preia o linie din fisier si o transforma in un film
        """
        fields = line.split(" ")
        cl = Client(fields[0], fields[1], fields[2])
        return cl
    
    def stocare(self,cl):
        RepoClienti.stocare(self,cl)
        self.__write_all()

    def delete_client(self,Id):
        RepoClienti.delete_client(self, Id)
        self.__write_all()

    def mod_client(self,cl):
        RepoClienti.mod_client(self, cl)
        self.__write_all()


    



                  

def testStocare():
    repo=RepoClienti()
    repo.stocare(Client(1,'mihai',12221))
    assert repo.size()==1
    
def testDelete():
    repo=RepoClienti()
    repo.stocare(Client(1,'mihai',12221))
    repo.delete_client(1)
    assert repo.size()==0
    
def testGetClientId():
    repo=RepoClienti()
    repo.stocare(Client(1,'mihai',12221))
    assert repo.size()==1
    assert repo.get_client_id(1)==[1,'mihai',12221]
    
testStocare()
testDelete()
testGetClientId()
        



