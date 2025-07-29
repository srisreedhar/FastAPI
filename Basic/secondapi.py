from fastapi import FastAPI, Path
from data.superheros import superheroes
from fastapi.params import Body
import json
from pydantic import BaseModel
from typing import Optional


snd = FastAPI()


@snd.get("/")
def index():
    return {
        "/all": "all data",
        "/heros": "list of all superheros",
        "/team": "all teams",
        "/powers": "lists all unique powers",
        "/heros/<heroname>": "get hero-details by <heroname>",
        "/powers/<power_name>": "get all hero-details by <power_name>",
    }


# get all data
@snd.get("/all")
def getalldata():
    return superheroes


# get all teams
@snd.get("/teams")
def getallteams():
    uniq = []
    for value in superheroes.values():
        uniq.append(value.get("team"))
    return {"details": "all unique teams", "teams": set(uniq)}


# get all heroes
@snd.get("/heros")
def getallheros():
    heros_list = list()
    for everyhero in superheroes:
        heros_list.append(everyhero)
    return {"details": "all superhero names", "heroes": heros_list}


# get all details by Power name
@snd.get("/powers")
def getallpowers():
    powers_list = list()
    for power_details in superheroes.values():
        lst = power_details.get("powers", [])
        powers_list.extend(lst)
    return {"all powers": set(powers_list)}


# get details by Hero Name
@snd.get("/heros/{heroname}")
def getherobyname(heroname: str):
    heroname = superheroes.get(heroname, "null")
    if heroname == "null":
        response = "Check the Spelling & Case of the name you are searching"
    else:
        response = heroname
    heroes_list = list(superheroes.keys())
    return response


# get details by team name
@snd.get("/teams/{teamname}")
def getteambyname(teamname: str):
    superhero_list = dict()
    for name, hero_detials in superheroes.items():
        if teamname.lower() == hero_detials["team"].lower():
            superhero_list[name] = hero_detials
    return superhero_list


# get details by power-name
@snd.get("/powers/{power_name}")
def getdatabypowername(power_name: str):
    superhero_powers = {}
    for name, power_info in superheroes.items():
        if any(power.lower() == power_name.lower() for power in power_info["powers"]):
            superhero_powers[name] = power_info
    return superhero_powers


# create a super hero test record
@snd.post("/createnew-test")
def create_hero_test(payload: dict = Body(...)):
    print(payload)
    return {"new hero details":payload}

# create a super hero record
@snd.post("/createnewhero")
def create_hero(payload: dict = Body(...)):
    name = payload['real_name']
    superheroes[name]=payload
    print(superheroes[name])