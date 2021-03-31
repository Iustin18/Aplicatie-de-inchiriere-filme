from domain.val_filme import FilmValidatorException
from repository.repo_filme import FilmRepositoryException 

class MeniuFilme:
    def __init__(self,serv_filme):
        self.__serv_filme=serv_filme
    
    def adaugare_film(self):
        """
        adauga film
        """
        Id=input("Introduceti id film: ")
        titlu=input("Introduceti titlu film: ")
        gen=input("Introduceti gen film: ")
        descriere=input("Introduceti descriere film: ")
        try:
            fl=self.__serv_filme.creare_film(Id,titlu,gen,descriere)
            print("Filmul " + fl.get_titlu() + " a fost salvat cu succes")
        except FilmValidatorException as x:
            print(x)
        except FilmRepositoryException as x:
            print(x)
            
    
    def afisare_film(self):
        """
        afiseaza filme
        """
        l=self.__serv_filme.get_filme()
        if len(l)==0:
            print("Nu exista filme de afisat")
        else:
            for i in l:
                print(i)
                
                
    def stergere_client(self):
        """
        sterge un film
        """
        Id=input("Inserati Id filmului care trebuie sters: ")
        try:
            self.__serv_filme.sterg_film(Id)
            print("Sters!")
        except FilmRepositoryException() as x:
            print(x)
            
            
    def modificare_film(self):
        """
        modifica un film
        """
        Id=input("Inserati Id: ")
        titlu=input("Inserati noul titlu: ")
        gen=input('Inserati noul gen: ')
        descriere=input("Inserati o noua descriere: ")
        try:
            fl=self.__serv_filme.modific_film(Id,titlu,gen,descriere)
            print("Modificare cu succes")
        except FilmValidatorException() as x:
            print(x)
        except FilmRepositoryException() as x:
            print(x)
        
        
        
    def cautare_id(self):
        """
        cauta dupa id 
        """
        Id=input("Inserati Id film: ")
        try:
            fl=self.__serv_filme.caut_film_id(Id)
            print(fl[0],' ',fl[1],' ',fl[2],' ',fl[3])
        except FilmRepositoryException as x:
            print(x)
            
    def cautare_titlu(self):
        """
        cauta dupa titlu
        """
        y=[]
        titlu=input("Inserati titlu filmului: ")
        l=self.__serv_filme.caut_film_titlu(titlu,0,y)
        if len(l)==0:
            print("Nume inexistent")
        else:
            for i in l:
                print(i[0],' ',i[1],' ',i[2],' ',i[3])        
            
            
    def show(self):
        while True:
            print("_____Meniu Film_____")
            print("[1]-Adaugare")
            print("[2]-Stergere")
            print("[3]-Afisare")
            print("[4]-Cautare")
            print("[5]-Modificare")
            print("[6]-Exit")
            x=input()
            if x=='1':
                self.adaugare_film()
            elif x=='2':
                self.stergere_client()
            elif x=='3':
                self.afisare_film()
            elif x=='4':
                print("[1]-Cautare dupa Id ")
                print("[2]-Cautare dupa titlu ")
                q=input()
                if q=='1':
                    self.cautare_id()
                elif q=='2':
                    self.cautare_titlu()
            elif x=='5':
                self.modificare_film()
            elif x=='6':
                return False
            else:
                print("Comanda gresita!") 


