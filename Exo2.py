def est_bisextile(nbr:int)->bool:
    annee=''
    if nbr%4==0 and nbr%100!=0 or nbr%400==0:
        anne_bisextile="annee est bisextile"
    else:
        anne_bisextile="annee nest pas bisextile"
    return anne_bisextile
def test():
    print(est_bisextile(400))
    print(est_bisextile(1900))
    print(est_bisextile(1991))
    print(est_bisextile(100))
    print(est_bisextile(2000))
    print(est_bisextile(2028))





test()                
