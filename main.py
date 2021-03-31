from service.serv_clienti import ServClienti
from service.serv_filme import ServFilme
from service.serv_inchirieri import ServInchirieri
from service.serv_rapoarte import ServRapoarte
from repository.repo_clienti import RepoClienti,RepoClientiFile
from repository.repo_filme import RepoFilme,RepoFilmeFile
from repository.repo_inchirieri import RepoInchirieri,RepoInchirieriFile
from domain.val_clienti import ValClienti
from domain.val_filme import ValFilme
from domain.val_inchirieri import ValInchirieri
from ui.ui_meniu import Console
from sortare.sort import sortare

val_clienti=ValClienti()
val_filme=ValFilme()
val_inchirie=ValInchirieri()

repo_clienti=RepoClienti()
repo_filme=RepoFilme()
repo_inchirieri=RepoInchirieri()

repo_clienti_file=RepoClientiFile("ClientiFile.txt")
repo_filme_file=RepoFilmeFile("FilmeFile.txt")
repo_inchirieri_file=RepoInchirieriFile("InchirieriFile.txt")

sort=sortare(repo_inchirieri_file,repo_clienti_file)

serv_clienti=ServClienti(repo_clienti_file,val_clienti)
serv_filme=ServFilme(repo_filme_file,val_filme)
serv_inchirieri=ServInchirieri(repo_clienti_file,repo_filme_file,repo_inchirieri_file,val_inchirie)
serv_rapoarte=ServRapoarte(repo_inchirieri_file,sort)



ui=Console(serv_clienti,serv_filme,serv_inchirieri,serv_rapoarte)

ui.show()