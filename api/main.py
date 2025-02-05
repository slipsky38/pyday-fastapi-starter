import random
import fastapi

app = fastapi.FastAPI()

@app.get("/generate_name")
async def generate_name(starts_with:str = 'n', ends_with: str='a'):
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if starts_with is not None:
        filtered_names = [name for name in names if name.lower().startswith(starts_with.lower()) and name.lower().endswith(ends_with.lower)]
        if len(filtered_names) == 0:
            raise fastapi.HTTPException(status_code=404, detail="No name found.")
        random_name = random.choice(filtered_names)
    else:
        random_name = random.choice(names)
    return {"name": random_name} 