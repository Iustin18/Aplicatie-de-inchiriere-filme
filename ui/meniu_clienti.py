from domain.val_clienti import ClientiValidatorException
from repository.repo_clienti import ClientiRepositoryException

class MeniuClienti:
    def __init__(self,serv_clienti):
        self.__serv_clienti=serv_clienti
        
    def adaugare_client(self):
        """
        adauga un client
        """
        Id=input("Inserati id client ")
        nume=input("Inserati nume client ")
        cnp=input("Inserati CNP client ")
        try:
            cl=self.__serv_clienti.creare_client(Id,nume,cnp)
            print("Clientul " + cl.get_nume() + " a fost salvat!")
        except ClientiValidatorException as x:
            print(x)
        except ClientiRepositoryException as x:
            print(x)
            
    
    def afisare_client(self):
        """
        afiseaza clienti
        """
        l=self.__serv_clienti.get_clienti()
        if len(l)==0:
            print("Nu exista clienti de afisat")
        else:
            for i in l:
                print(i)
                
                
    def stergere_client(self):
        """
        sterge client
        """
        Id=input("Inserati Id clientului care trebuie sters: ")
        try:
            self.__serv_clienti.sterg_client(Id)
            print("Sters!")
        except ClientiRepositoryException() as x:
            print(x)        
    
    def modificare_client(self):
        """
        modifica client
        """
        Id=input("Inserati Id: ")
        nume=input("Inserati noul nume: ")
        cnp=input("Inserati noul cnp: ")
        try:
            cl=self.__serv_clienti.modific_client(Id,nume,cnp)
            print("Modificare cu succes")
        except ClientiValidatorException() as x:
            print(x)
        except ClientiRepositoryException() as x:
            print(x)
        
        
    def cautare_id(self):
        """
        cauta client duapa id
        """
        Id=input("Inserati id client: ")
        try:
            cl=self.__serv_clienti.caut_client_id(Id)
            print(cl[0],' ',cl[1],' ',cl[2])
        except ClientiRepositoryException() as x:
            print(x)
            
    def cautare_nume(self):
        """
        cauta clienti dupa nume
        """
        nume=input("inserati nume client: ")
        y=[]
        l=self.__serv_clienti.caut_client_nume(nume,0,y)
        if len(l)==0:
            print("Nume inxistetn")
        else:
            for i in l:
                print(i[0],' ',i[1],' ',i[2])
                
        
    def show(self):
        while True:
            print("______Meniu Cilent_____")
            print("[1]-Adaugare")
            print("[2]-Stergere")
            print("[3]-Afisare")
            print("[4]-Cautare")
            print("[5]-Modificare")
            print("[6]-Exit")
            x=input()
            if x=='1':
                self.adaugare_client()
            elif x=='2':
                self.stergere_client()
            elif x=='3':
                self.afisare_client()
            elif x=='4':
                print("[1]-Cautare dupa id")
                print("[2]-Cautare dupa nume")
                q=input()
                if q=='1':
                    self.cautare_id()
                elif q=='2':
                    self.cautare_nume()
            elif x=='5':
                self.modificare_client()
            elif x=='6':
                return False
            else:
                print("Comanda gresita")
                
            


