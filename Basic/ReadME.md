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
All endpoints are listed here:
```
http://localhost:8000/
```

## Created Views (Endpoints)
| Endpoint | Description |
|----------|-------------|
| `/all` |  the entire data view — every hero, team, and power in one epic swoop! |
| `/heros` | Lists all superheroes. |
| `/team` | Lists all the Teams |
| `/powers` | Lists all the powers. |
| `/heros/<heroname>` | Get hero’s identity by `<heroname>`. |
| `/powers/<power_name>` | Get Hero details by Power `<power_name>`. Great power, great responsibility! |


## File Details

[Firstapi](https://github.com/srisreedhar/FastAPI/blob/main/Basic/firstapi.py) has basic api interface with get/post paths/methods
[Secondapi](https://github.com/srisreedhar/FastAPI/blob/main/Basic/secondapi.py) has schema and pydantic implementations
[Superheroes Data.py](https://github.com/srisreedhar/FastAPI/blob/main/Basic/data/superheros.py) JSON file which has Superheroes data