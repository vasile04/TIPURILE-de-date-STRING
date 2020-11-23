# sa se scrie un program  care intreaba numele utilizatorului apoi il saluta
a=str(input('Introdu intrebarea: '))
print(a)
nume=str(input('Introdu numele: '))
if type(nume)==str:
    print('Salut', nume)