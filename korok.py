def kor():
    lista=[]
    def elso_idos(lista):
        index=0
        idos=1
        while index < len(lista) and lista[index] <70:

            index+=1
        idos+=index
        return idos

    def konzolra_ir():
        valami=elso_idos(lista)
        print(f"Első idős ember korának helye a listában : {valami}.")

    def falj_ir():
        valami = elso_idos(lista)
        f=open("oreg.txt","w",encoding="utf-8")
        f.write(f"Első idős ember korának helye a listában : {valami}.")
        f.close()

    for i in range(5):
        evszam=int(input("Kérem adja meg a korát: "))
        lista.append(evszam)


    i=0
    while i < len(lista)-1:
        print(lista[i],end=":")
        i+=1
    print(lista[i])


    konzolra_ir()
    falj_ir()
