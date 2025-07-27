from faker import Faker


fk = Faker(locale="pt-br")


def create_fake_db(num:int) -> None:
    if num <= 0:
        return None
    for n in range(1,num+1):
        nome = fk.name()
        cep = fk.postal_code
        cidade = fk.city()
        uf = fk.estado()[0]
        tel = fk.phone_number()
        print(nome,cep,cidade,uf,tel)
       
       

create_fake_db(100) 