# SuperHeroes FastAPI

A funny API interface to JSON data, 
saving the world one endpoint at a time! This script unleashes the power of FastAPI to wrangle superhero data faster than a speeding bullet.

## Requirements
- **FastAPI** 

To launch this heroic API into action:
```bash
uvicorn api:bsc --reload
```

## Index View
Check out the superhero headquarters, where all endpoints assemble in glorious formation:
```
http://localhost:8000/
```

## Created Views (Endpoints)
| Endpoint | Description |
|----------|-------------|
| `/all` | Unleashes the entire data vault—every hero, team, and power in one epic swoop! |
| `/heros` | Lists all superheroes, from caped crusaders to masked marvels. |
| `/team` | Reveals the squads that save the day, because teamwork makes the dream work! |
| `/powers` | Showcases every unique superpower, from laser eyes to talking to fish. |
| `/heros/<heroname>` | Zooms in on a hero’s secret identity by `<heroname>`. No cape required! |
| `/powers/<power_name>` | Rounds up all heroes wielding the mighty `<power_name>`. Great power, great responsibility! |