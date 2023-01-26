from downloadAttachaments import makeDownload #downloadAttachaments --> Dont have return
from getAttchaments import getAttachamentsCard #getAttachemnts --> Return: Key Value and ListNames
from time import sleep
import os

def executeAll(cardNumber, dirName):
    chaveValor = {}
    listaNomes = []

    chaveValor, listaNomes = getAttachamentsCard(cardNumber)

    #Aguardar 2 segundos
    sleep(2)

    for item in chaveValor:
        urlDownload = chaveValor[item]
        if urlDownload != []:
            for link in urlDownload:
                for value in listaNomes:
                    if value in link:
                        path = os.path.join(dirName, value)
                        makeDownload(link, path)

#Teste
numeroCard = 627681545
pathA = r'C:\Users\Mathe\Documents\Git\Pontte\Pipefy\Arquivos Gerados'
executeAll(numeroCard, pathA)