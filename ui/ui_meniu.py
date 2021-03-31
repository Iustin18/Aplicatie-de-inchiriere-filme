from ui.meniu_clienti import MeniuClienti
from ui.meniu_filme import MeniuFilme
from ui.meniu_inchirieri import MeniuInchirieri
from ui.meniu_rapoarte import MeniuRapoarte

class Console:
    def __init__(self,serv_clienti,serv_filme,serv_inchirieri,serv_rapoarte):
        self.__serv_filme=serv_filme
        self.__serv_clienti=serv_clienti
        self.__serv_inchirieri=serv_inchirieri
        self.__serv_rapoarte=serv_rapoarte
        
    def show(self):
        while True:
            print("~~~~~Meniu General~~~~~")
            print("[1]-Clienti ")
            print("[2]-Filme")
            print("[3]-Inchirieri")
            print("[4]-Rapoarte")
            print("[5]-Exit")
            x=input()
            if x=='1':
                MeniuClienti(self.__serv_clienti).show()
            elif x=='2':
                MeniuFilme(self.__serv_filme).show()
            elif x=='3':
                MeniuInchirieri(self.__serv_inchirieri).show()
            elif x=='4':
                MeniuRapoarte(self.__serv_rapoarte).show()
            elif x=='5':
                print("Sfarsit")
                return False
            else:
                print("Comanda gresita")
                