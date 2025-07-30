from fastapi import FastAPI, Path
from data.superheros import superheroes
from fastapi.params import Body
import json
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime,UTC
from os import environ

# initiating FastAPI app
snd = FastAPI()


class Superhero(BaseModel):
    real_name: str
    powers: List[str]
    team: str
    home: str

# Sample Payload
# payload = {
#     "real_name": "Sri Sreedhar",
#     "powers": [
#         "Flight","Super Strength","X-Ray Vision","Telepathy",
#         "Heat Vision","Chi Energy","Magic","Kinetic Energy","Combat Skills",	"Wall-Crawling","Size Manipulation"],
#     "team": "Justice League",
#     "home": "Hyderabad"
# }


# get all the urls
@snd.get("/")
def index():
    return {
        "/all": "all data",
        "/heros": "list of all superheros",
        "/team": "all teams",
        "/powers": "lists all unique powers",
        "/heros/<heroname>": "get hero-details by <heroname>",
        "/powers/<power_name>": "get all hero-details by <power_name>",
        "/createnewhero":"post request to create a new hero details, the data would directly appear in superheros"
    }


# get all data
@snd.get("/all")
def getalldata():
    """
    Args : 
         No args needed
    Returns :
            JSON Response with all the data
    """
    return superheroes


# get all teams
@snd.get("/teams")
def getallteams():
    """
    Args : 
        No args needed
    Returns :
            JSON Response with all the teams data
    """
    uniq = []
    for value in superheroes.values():
        uniq.append(value.get("team"))
    return {"details": "all unique teams", "teams": set(uniq)}


# get all heroes
@snd.get("/heros")
def getallheros():
    """
    Args : 
         No args needed
    Returns :
            JSON Response with all the heroes data
    """
    heros_list = list()
    for everyhero in superheroes:
        heros_list.append(everyhero)
    return {"details": "all superhero names", "heroes": heros_list}


# get all details by Power name
@snd.get("/powers")
def getallpowers():
    """
    Args : 
         No args needed
    Returns :
            JSON Response with all the powers data
    """
    powers_list = list()
    for power_details in superheroes.values():
        lst = power_details.get("powers", [])
        powers_list.extend(lst)
    return {"all powers": set(powers_list)}


# get details by Hero Name
@snd.get("/heros/{heroname}")
def getherobyname(heroname: str):
    """
    Args : 
         heroname : string
    Returns :
            JSON Response with the data relevant to argument
    """
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
    """
    Args : 
        teamname : string
    Returns :
            JSON Response with the all the superhero data which has <teamname>
    """
    superhero_list = dict()
    for name, hero_detials in superheroes.items():
        if teamname.lower() == hero_detials["team"].lower():
            superhero_list[name] = hero_detials
    return superhero_list


# get details by power-name
@snd.get("/powers/{power_name}")
def getdatabypowername(power_name: str):
    """
    Args : 
        power_name : string
    Returns :
            JSON Response with the all the superhero data which has <power_name>
    """
    superhero_powers = {}
    for name, power_info in superheroes.items():
        if any(power.lower() == power_name.lower() for power in power_info["powers"]):
            superhero_powers[name] = power_info
    return superhero_powers


# create a super hero test record
@snd.post("/createnew-test")
def create_hero_test(payload: dict = Body(...)):
    """
    Test POST request endpoint
    """
    print(payload)
    return {"new hero details":payload}

# create a super hero record
@snd.post("/createnewhero")
def create_hero(payload: dict = Body(...)):
    name = payload['real_name']
    superheroes[name]=payload
    print(superheroes[name])


# diagnostics
@snd.get("/info")
def getuserinfo():
    return {
        "api_version":"1.0",
        "time":datetime.now(tz=UTC),
        "os": environ["OS"],
        "user":environ[ "USERNAME"],
        "intel-arch":environ["PROCESSOR_ARCHITECTURE"]
    }
