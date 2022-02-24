
import pathlib
import os
import json
import yaml
import csv
import xmltodict
from dict2xml import dict2xml
import json
import xmltodict
def MENU_CSV():
    print("             MENU                 ")
    print("1: permet convertire le fichier en xml")
    print("2:permet convertire le fichier en yaml ou yml")
    print("3:permet convertire le fichier en json ")
    print("0:pour quitter")

def MENU_XML():
    print("             MENU                 ")
    print("1: permet convertire le fichier en csv ")
    print("2:permet convertire le fichier en json ")
    print("3:permet convertire le fichier yaml ou yml ")
    print("0:pour quitter")

def MENU_JSON():
    print("             MENU                 ")
    print("1: permet convertire le fichier en csv ")
    print("2:permet convertire le fichier  en yaml ou yml")
    print("3:permet convertire le fichier  en xml")
    print("0:pour quitter")

def MENU_YAML():
    print("             MENU                 ")
    print("1: permet convertire le fichier en csv")
    print("2:permet convertire le fichier en json ")
    print("3:permet convertire le fichier en xml")
    print("0:pour quitter")



def conversion_nom_fichier(chaine, counter):
    original_path = pathlib.Path(chaine)
    v = chaine.split(".")[-1]
    mon_fichier = "mon_fichier" + str(counter) + "." + v
    new_path = original_path.rename(mon_fichier)
    cheminabs = os.path.abspath(new_path)
    return new_path


def extension(chaine):
    extension = chaine.split(".")[-1]
    return extension


def verification(chaine):
    liste = ["csv", "json", "yaml", "xml", "yml"]
    if chaine in liste:
        return True
    else:
        return False


def ymal_to_dic(chaine):
    with open(chaine) as f:
        dic = yaml.safe_load(f)
    return dic


def json_to_dict(chaine):
    with open(chaine) as f:
        dic = json.load(f)
    return dic


def csv_to_dict(chaine):
    document = open(chaine)
    document1 = csv.DictReader(document)
    for d in document1:
        dictt= json.dumps(d)
    return dictt


def conversion_dict_xml(dictionnaire):
    xml = dict2xml(dictionnaire)
    data3=open("data3.xml","w")
    data3.write(xml)
    data3.close()



def xml_vers_dic(monfichier):
    fichier = open(monfichier)
    dic = xmltodict.parse(fichier.read())
    dic = json.loads(json.dumps(dic))
    return dic


def dict_vers_json(dictionnaire):
    with open('data.json', 'w') as fichier:
        json.dump(dictionnaire, fichier)
    with open('data.json', 'r') as fichier:
        monfichier = json.load(fichier)
    return monfichier


def dictionnaire_vers_yaml(dictionnaire):
    with open("data.yaml", 'w') as f:
        yaml.dump(dictionnaire, f, default_flow_style=False, sort_keys=False)


def dictionnaie_vers_csv(dictionnaire):
    liste = []
    for i in dictionnaire.keys():
        liste.append(i)
    with open('data.csv', 'w') as f:
        v = csv.DictWriter(f, fieldnames=liste)
        v.writeheader()
        v.writerow(dictionnaire)


counter = 1
text = input("veillez saisir le nom de votre fichier:")
# formatage nom du fichier
extension(text)
if verification(extension(text)):
    print("le format choisie est valide ")
else:
    print("le format n'est pas valide veillez changer de format")
if extension(text) == "csv":
    fichier = csv_to_dict(text)
    while True:
        MENU_CSV()
        try:
            a = int(input("donne un nombre entre 0 et 3:"))
            if a in range(0,4):
                if(a==0):
                    print("BYEBYE")
                    break
                if(a==1):
                    conversion_dict_xml(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break

                elif(a==2):
                    dictionnaire_vers_yaml(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==3):
                    dict_vers_json(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
            else:
                print("erreur")
        except Exception as e:
            print("VOUS AVEZ UNE ERREUR")
elif extension(text) == "json":
    fichier = json_to_dict(text)
    while True:
        MENU_JSON()
        try:
            a = int(input("donne un nombre entre 0 et 3:"))
            if a in range(0,4):
                if(a==0):
                    print("BYEBYE")
                    break
                if(a==1):
                    dictionnaie_vers_csv(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==2):
                    dictionnaire_vers_yaml(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==3):
                    conversion_dict_xml(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
            else:
                print("erreur")
        except Exception as e:
            print("VOUS AVEZ UNE ERREUR")
elif extension(text) == "yaml" or extension(text) == "yml":
    fichier = ymal_to_dic(text)
    while True:
        MENU_YAML()
        try:
            a = int(input("donne un nombre entre 0 et 3:"))
            if a in range(0,4):
                if(a==0):
                    print("BYEBYE")
                    break
                if(a==1):
                    dictionnaie_vers_csv(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==2):
                    dict_vers_json(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==3):
                    conversion_dict_xml(fichier)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
            else:
                print("erreur")
        except Exception as e:
            print("VOUS AVEZ UNE ERREUR")
elif extension(text) == "xml":
    ficher=xml_vers_dic(text)
    while True:
        MENU_XML()
        try:
            a = int(input("donne un nombre entre 0 et 3:"))
            if a in range(0,4):
                if(a==0):
                    print("BYEBYE")
                    break
                if(a==1):
                    dictionnaie_vers_csv(ficher)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==2):
                    dict_vers_json(ficher)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
                elif(a==3):
                    dictionnaire_vers_yaml(ficher)
                    print("transformation fait vas dans le repertoire ou se trouve le fichier")
                    break
            else:
                print("erreur")
        except Exception as e:
            print("VOUS AVEZ UNE ERREUR")







