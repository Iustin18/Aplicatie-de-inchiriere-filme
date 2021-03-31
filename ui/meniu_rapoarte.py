class MeniuRapoarte:
    def __init__(self,serv_rapoarte):
        self.__serv_rapoarte=serv_rapoarte
        
        
    def lista_nume(self):
        """
        sorteaza lista de inchirieri dupa numele clientului
        """
        l=self.__serv_rapoarte.lista_nume()
        for i in l:
            print(i)
    
    def lista_numar(self):
        """
        sorteaza lista de inchirieri dupa numarul de inchirieri a fiecarui client
        """
        l=self.__serv_rapoarte.lista_numar()
        for i in l:
            print(i[0],' ',i[1])
            
    def top_inc(self):
        """
        sorteaza lista de inchirieri dupa cele mai inchiriate filme
        """
        x=input("numar filme: ")
        l=self.__serv_rapoarte.top()
        x=int(x)
        for i in range (0,int(len(l)/2)):
            l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
        if x>len(l):
            x=len(l)
        for i in range (0,x):
            print(l[i][0],' ',l[i][1])
            
    def top_30(self):
        """
        primi 30% clienti ce au inchiriat cele mai multe filme
        """
        l=self.__serv_rapoarte.lista_numar()
        y=len(l)
        y=y*30
        y=y/100
        y=int(y)
        for i in range(int(len(l)/2)):
            l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
        for i in range (y):
            print(l[i][0],' ',l[i][1])
    
    def top_gen(self):
        """
        sorteaza lista de inchirieri dupa genul filmului
        """
        l=self.__serv_rapoarte.lista_gen()
        nr=0
        for i in l:
            nr=nr+i[0]
        for i in l:
            y=100/nr
            y=y*i[0]
            print(i[1]," ",y,"%")
        
    def show(self):
        while True:
            print("______Meniu Rapoarte_____")
            print("[1]-Lista clienti ordonata dupa:")
            print("[2]-cele mai inchiriate filme")
            print("[3]-primi 30% clienti ce au inchiriat cele mai multe filme")
            print("[4]-statistica dupa genul filmului")
            print("[5]-exit")
            x=input()
            if x=='1':
                print("[1]-lista dupa nume")
                print("[2]-lista dupa numarul de filme inchiriate")
                q=input()
                if q=='1':
                    self.lista_nume()
                elif q=='2':
                    self.lista_numar()
            elif x=='2':
                self.top_inc()
            elif x=='3':
                self.top_30()
            elif x=='4':
                self.top_gen()
            elif x=='5':
                return False
            else:
                print("comanda gresita")


