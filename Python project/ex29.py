# 1. funkcio: adatbazis feltoltes, betoltes, modositas
import pandas as pd
import os


def fajlbairas():
    autok_write = open("autok.txt", "a")
    while True:

        marka = input("Milyen marka? ")
        tipus = input("Milyen tipus? ")
        evjarat = input("Milyen evjarat? ")
        loero = input("Hany loeros? ")
        tomeg = input("Hany kg a tomege? ")
        vegsebesseg = input("Hany km/h a vegsebessege? ")
        print(marka + "," + tipus + "," + evjarat + "," + loero + "," + tomeg + "," + vegsebesseg, file=autok_write)
        kerdes = input("szeretnel meg adatot betolteni?(i/n) ")
        if kerdes == "n":
            break
    autok_write.close()


def kiiras():
    autok_read = data = pd.read_csv("autok.txt", delimiter=",")
    print(autok_read)





def modositas():
    data = pd.read_csv("autok.txt", delimiter=",")
    print(data)
    while True:
        hanyadik = int(input("Hanyadik sorban szeretnel modositani? "))
        mit = input("Mit szeretnel modositani? ")
        mire = input("Mire szeretned a(z) "+ mit + " parametert modositani? ")
        data.at[int(hanyadik), mit] = mire
        print(data)
        tovabb = input("szeretnel meg valamit modositani?(i/n) ")
        if tovabb == "n":
            break
        break
    open("autok.txt", "w").close()  ## Fajl torles
    write_file = open("autok.txt", "w")
    print("marka" + "," + "tipus" + "," + "evjarat" + "," + "loero" + "," + "tomeg" + "," + "vegsebesseg", file=write_file)
    write_file.close()
    data.to_csv('autok.txt', header=None, index=None, sep=',', mode='a')





#
# print(len(osszegzo))
def ajanlo(osszegzo):
    data = pd.read_csv("autok.txt", delimiter=",")
    out_data = {"marka":[],"tipus": [], "evjarat": [], "loero":[], "tomeg":[], "vegsebesseg":[]}
    out_dataframe = pd.DataFrame(out_data)

    print(data)
    # Elso hely az index masodik a pont
    szamok= [] # Azok a sz'mok ahanyadik indexeket vizsgalni kell
    for i in range(len(osszegzo)):
        szamok.append(osszegzo[i][0])

    for i in data.itertuples():
        ossz = 0
        for j in szamok:
            for z in range(len(osszegzo)):
                if osszegzo[z][0] > 2:
                    if i[j] in range(int(osszegzo[z][1][0]), int(osszegzo[z][1][1])+1):
                        ossz += 1
                        if ossz == len(osszegzo):
                            new_row = {"marka": i[1], "tipus": i[2], "evjarat": i[3], "loero": i[4], "tomeg": i[5],
                                       "vegsebesseg": i[6]}
                            out_dataframe = out_dataframe.append(new_row, ignore_index=True)
                else:

                    if i[j] in osszegzo[z][1]:
                        ossz += 1
                        if ossz == len(osszegzo):
                            # print(data.loc[[i]])
                            new_row = {"marka":i[1],"tipus": i[2], "evjarat": i[3], "loero":i[4], "tomeg":i[5],
                                       "vegsebesseg":int(i[6])}
                            out_dataframe = out_dataframe.append(new_row, ignore_index=True)
    pd.options.display.float_format = '{:.0f}'.format
    print(out_dataframe)


if os.stat("autok.txt").st_size == 0:
    write_file = open("autok.txt", "w")
    print("marka" + "," + "tipus" + "," + "evjarat" + "," + "loero" + "," + "tomeg" + "," + "vegsebesseg",
          file=write_file)
    write_file.close()
intent = input("Akarsz valamit csinalni?(i/n) ")
if not intent == "n":

    while True:
        mitcsi = input("Mit akarsz csinalni(adatfel,adatmod,kereses)")
        if mitcsi == "adatfel":
            kiiras()
            fajlbairas()
        elif mitcsi == "adatmod":
            modositas()
        elif mitcsi == "kereses":
            szempontok = input("Mik a szempontjaid? (vesszovel valaszd el): ")
            szempont_lista = list(szempontok.split(","))
            print(szempont_lista)
            osszegzo = []
            for szempont in range(len(szempont_lista)):
                if szempont_lista[szempont] == "marka":
                    bemenet = input("Milyen markakat keresel?(vesszovel elvalasztva pls): ")
                    bemenet = list(bemenet.split(","))
                    print(bemenet)
                    osszegzo.append((1, bemenet))
                elif szempont_lista[szempont] == "tipus":
                    bemenet = input("Milyen tipust keresel?(vesszovel elvalasztva pls): ")
                    bemenet = list(bemenet.split(","))
                    print(bemenet)
                    osszegzo.append((2,bemenet))
                elif szempont_lista[szempont] == "evjarat":
                    bemenet = input("Milyen evjaratot keresel?(kotojellel elvalasztva, ha intervallum: ")
                    bemenet = list(bemenet.split("-"))
                    print(bemenet)
                    osszegzo.append((3,bemenet))
                elif szempont_lista[szempont] == "loero":
                    bemenet = input("Milyen loerot keresel?(kotojellel elvalasztva, ha intervallum): ")
                    bemenet = list(bemenet.split("-"))
                    print(bemenet)
                    osszegzo.append((4,bemenet))
                elif szempont_lista[szempont] == "tomeg":
                    bemenet = input("Milyen tomegut keresel?(kotojellel elvalasztva, ha intervallum): ")
                    bemenet = list(bemenet.split("-"))
                    print(bemenet)
                    osszegzo.append((5,bemenet))
                elif szempont_lista[szempont] == "vegsebesseg":
                    bemenet = input("Milyen tipust keresel?(kotojellel elvalasztva, ha intervallum): ")
                    bemenet = list(bemenet.split("-"))
                    print(bemenet)
                    osszegzo.append((6,bemenet))
            ajanlo(osszegzo)
        mitcsi = input("Szeretnel meg valamit csinalni?(i/n) ")
        if mitcsi == 'n':
            break










