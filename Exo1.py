def message_imc(imc:float)->float:
    if imc<16.5:
        imc="denutrition ou famine"
    elif imc>=16.5 and imc<18.5:
        imc="maigreur"
    elif imc>=18.5 and imc<25:
        imc="corpulence normale"        
    elif imc>=25 and imc<30:
        imc="surpoid"
    elif imc>=30 and imc<35:
        imc="obeisite modere"    
    elif imc>=35 and imc<40:
        imc="obeisite severe"        
    elif imc>=40:
        imc="obeisite morbide"   
    return imc
def test():
    print(message_imc(25))
    print(message_imc(15))
    print(message_imc(45))
    print(message_imc(5))
    print(message_imc(18))
    print(message_imc(32))


test()             