from domain.val_inchirieri import InchirieriValidatorException
from repository.repo_inchirieri import InchirieriRepositoryException
from repository.repo_filme import FilmRepositoryException
from repository.repo_clienti import ClientiRepositoryException



class MeniuInchirieri:
    def __init__(self,serv_inchirieri):
        self.__serv_inchirieri=serv_inchirieri
        
    def adaugare_inchiriere(self):
        """
        adaugare inchiriere
        """
        idi=input("Inserati Id inchiriere: ")
        idc=input("Inserati Id client: ")
        idf=input("Inserati Id film: ")
        try:
            inc=self.__serv_inchirieri.adaugare_inchirieri(idi,idc,idf)
            print("Inchirierea salvata!")
        except ClientiRepositoryException as x:
            print(x)
        except FilmRepositoryException as x:
            print(x)
        except InchirieriValidatorException as x:
            print(x)
        except InchirieriRepositoryException as x:
            print(x)
            
            
    def returnare_film(self):
        """
        returnare film
        """
        idi=input("Inserare id inchiriere: ")
        try:
            r=self.__serv_inchirieri.return_film(idi)
            print("Film returnat")
        except InchirieriRepositoryException() as x:
            print(x)
        
    def afisare(self):
        """
        afiseaza inchirierile
        """
        l=self.__serv_inchirieri.afisare_inchirieri()
        for i in l:
            print(i)
        
        
    def show(self):
        while True:
            print("_____Meniu Inchirieri_____")
            print("[1]-Adaugare")
            print("[2]-Returnare")
            print("[3]-Afisare")
            print("[4]-Exit")
            x=input()
            if x=='1':
                self.adaugare_inchiriere()
            elif x=='2':
                self.returnare_film()
            elif x=='3':
                self.afisare()
            else:
                return False

