def imc(nbr):
    message_IMC=""
    if nbr<16.5:
        message_IMC='denutrition ou famine'
    elif (nbr>=16.5 and nbr<=18.5):
        message_IMC='maigreur'
    elif (nbr>18.5 and nbr<=25):
        message_IMC='corpulence normale'
    elif(nbr>25 and nbr<=30):
        message_IMC='surpoid'
    elif(nbr>30 and nbr<=35):
        message_IMC='obesité moderée'
    elif(nbr>35 and nbr<=40):
        message_IMC='obesité severe'
    else :
        message_IMC='obesité morbide'
    return message_IMC
def test():
    print(imc(20))
    print(imc(33))
    print(imc(40))
    print(imc(45))
    
test()
