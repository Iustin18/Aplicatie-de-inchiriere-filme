from domain.entities import Film

class FilmRepositoryException(Exception):
    pass

class RepoFilme:
    def __init__(self):
        self._filme={}
        
    def stocare(self,fl):
        """
        Memoreaza un film
        input: fl-filmul de memorat
        """
        if fl.get_id() in self._filme:
            raise FilmRepositoryException("Id deja existent")
        else:
            self._filme[fl.get_id()]=fl
            
    def get_filme(self):
        """
        returneaza lista cu tote filmele
        """
        return list(self._filme.values())
    
    def get_film(self,idf):
        """
        returneaza un singur film
        input idf-id film
        """
        try:
            return self._filme[idf]
        except:
            raise FilmRepositoryException("Film inexistent")

    def size(self):
        """
        lungimea listei
        """
        return len(self._filme)
    
    def contr_inchirieri(self,idf):
        if idf in self._filme:
            return
        else:
            raise FilmRepositoryException("Id film inexistent")
    
    def delete_film(self,Id):
        """
        sterge un film
        input: id-id film de sters
        """
        if Id in self._filme:
            self._filme.pop(Id)
        else:
            raise FilmRepositoryException("Id inexistent! ")
        
        
    def mod_film(self,fl):
        """
        Modifica un film
        input fl-noul film 
        """
        if fl.get_id() in self._filme:
            self._filme[fl.get_id()]=fl
        else:
            raise FilmRepositoryException("Id inexistent! ")
        
    def get_film_id(self,Id):
        """
        Returneaza un film prin id ul sau
        input: fl-id film
        """
        if Id in self._filme:
            l=[]
            l.append(self._filme[Id].get_id())
            l.append(self._filme[Id].get_titlu())
            l.append(self._filme[Id].get_gen())
            l.append(self._filme[Id].get_descriere())
            return l
        else:
            raise FilmRepositoryException("Id inexistent! ")
        
    def get_film_titlu(self,titlu,indx,lista):
        """
        Returneaza un film prin titlul sau
        input: titlu-titlu film
        """
        l=list(self._filme.values())
        """
        #Non recursiv
        x=[]
        for i in range (len(self._filme)):
            if l[i].get_titlu()==titlu:
                subl=[]
                subl.append(l[i].get_id())
                subl.append(l[i].get_titlu())
                subl.append(l[i].get_gen())
                subl.append(l[i].get_descriere())
                x.append(subl)
        return x
        """
        #recursiv
        x=lista
        if l[indx].get_titlu()==titlu:
            subl=[]
            subl.append(l[indx].get_id())
            subl.append(l[indx].get_titlu())
            subl.append(l[indx].get_gen())
            subl.append(l[indx].get_descriere())
            x.append(subl)
        indx=indx+1
        if indx>=len(l):
            return x
        return self.get_film_titlu(titlu, indx, x)
            
        
    


class RepoFilmeFile(RepoFilme):
    def __init__(self,FilmeFile):
        RepoFilme.__init__(self)
        self.__FilmeFile=FilmeFile
        self.__loadFromFile()
        
    def __loadFromFile(self):
        """
          incarca studenti din fiser
        """
        try:
            file = open(self.__FilmeFile)
            content = file.read()
            file.close()
        except IOError:
            return
        for line in content.split('\n'):
            if line.strip() == "":
                continue
            fields = line.split(" ")
            fl = Film(fields[0], fields[1], fields[2], fields[3])
            self._filme[fl.get_id()] = fl
         
         
    def __clear_all(self):
        """
        sterge tot ce se gaseste in file
        """
        file = open(self.__FilmeFile, "w")
        file.close()
       
    
    def __write_all(self):
        """
        Salveaza toti studenti din memorie in file
        """
        self.__clear_all()
        file = open(self.__FilmeFile, "a")
        for fl in self._filme.values():
            file.write(fl.get_id() + " ")
            file.write(fl.get_titlu() + " ")
            file.write(fl.get_gen() + " ")
            file.write(fl.get_descriere() + "\n")
        file.close()
        
        
    def __createFilmFromLine(self, line):
        """
        preia o linie din fisier si o transforma in un client
        """
        fields = line.split(" ")
        fl = Film(fields[0], fields[1], fields[2], fields[3])
        return fl
    
    def stocare(self,cl):
        RepoFilme.stocare(self,cl)
        self.__write_all()

    def delete_film(self,Id):
        RepoFilme.delete_film(self, Id)
        self.__write_all()

    def mod_film(self,cl):
        RepoFilme.mod_film(self, cl)
        self.__write_all()


def testStocare():
    repo=RepoFilme()
    repo.stocare(Film(1,'mihai',"ciao","cmv"))
    assert repo.size()==1
    
def testDelete():
    repo=RepoFilme()
    repo.stocare(Film(1,'mihai',"ciao","cmv"))
    repo.delete_film(1)
    assert repo.size()==0
    
def testGetClientId():
    repo=RepoFilme()
    repo.stocare(Film(1,'mihai',"ciao","cmv"))
    assert repo.size()==1
    assert repo.get_film_id(1)==[1,'mihai',"ciao","cmv"]
    
testStocare()
testDelete()
testGetClientId()

