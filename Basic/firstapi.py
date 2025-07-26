from fastapi import FastAPI
from data.superheros import superheroes
import json

bsc = FastAPI()

@bsc.get('/')
def index():
    return {
        '/all': 'all data',
        '/heros':'list of all superheros',
        '/team':'all teams',
        '/heros/heroname':'get hero-details by name'
    }


@bsc.get("/all")
def getalldata():
    return superheroes

@bsc.get("/teams")
def getallteams():
    uniq = []
    for value in superheroes.values():
        uniq.append(value.get("team"))
    return {
        'details':'all unique teams',
        'teams':set(uniq)
    }

@bsc.get("/heros")
def getallheros():
    heros_list=list()
    for everyhero in superheroes:
        heros_list.append(everyhero)
    return {
        'details':"all superhero names",
        'heroes':heros_list
    }

@bsc.get("/heros/{heroname}")
def getherobyname(heroname: str):
    heroname=superheroes.get(heroname,"null")
    if heroname == 'null':
        response = 'Check the Spelling & Case of the name you are searching'
    else:
        response = heroname
    heroes_list = list(superheroes.keys())
    return response


# '''{'info':'heroname is Case-Sensitive',
#             'details':%s,
#             'heores-list':%s
#             }'''%(heroname,heroes_list)