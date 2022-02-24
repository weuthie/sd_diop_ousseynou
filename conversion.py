
import pathlib
import os
import json
import yaml
import csv
import xmltodict
from dict2xml import dict2xml
import json
import xmltodict


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
    liste = ["csv", "json", "yaml", "xml"]
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
    return document1


def conversion_dict_xml(dictionnaire):
    xml = dict2xml(dictionnaire)
    return xml


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





