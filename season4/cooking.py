from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound

app = Sanic("RecipeAPI")

# Database (In Memory)
recipes = []
next_id = 1


# POST /recipes
@app.post("/recipes")
async def create_recipe(request):
    global next_id

    data = request.json

    recipe = {
        "id": next_id,
        "title": data.get("title"),
        "category": data.get("category"),
        "description": data.get("description"),
        "estimated_time": data.get("estimated_time"),
        "difficulty": data.get("difficulty"),
        "ingredients": data.get("ingredients", [])
    }

    recipes.append(recipe)
    next_id += 1

    return json(recipe, status=201)


# GET /recipes
@app.get("/recipes")
async def get_recipes(request):
    return json(recipes)


# GET /recipes/<id:int>
@app.get("/recipes/<id:int>")
async def get_recipe(request, id):

    for recipe in recipes:
        if recipe["id"] == id:
            return json(recipe)

    raise NotFound("Recipe not found")


# PUT /recipes/<id:int>
@app.put("/recipes/<id:int>")
async def update_recipe(request, id):

    data = request.json

    for recipe in recipes:

        if recipe["id"] == id:

            recipe["title"] = data.get("title", recipe["title"])
            recipe["category"] = data.get("category", recipe["category"])
            recipe["description"] = data.get("description", recipe["description"])
            recipe["estimated_time"] = data.get(
                "estimated_time",
                recipe["estimated_time"]
            )
            recipe["difficulty"] = data.get(
                "difficulty",
                recipe["difficulty"]
            )
            recipe["ingredients"] = data.get(
                "ingredients",
                recipe["ingredients"]
            )

            return json(recipe)

    raise NotFound("Recipe not found")


# DELETE /recipes/<id:int>
@app.delete("/recipes/<id:int>")
async def delete_recipe(request, id):

    for recipe in recipes:

        if recipe["id"] == id:
            recipes.remove(recipe)

            return json(
                {"message": "Recipe deleted successfully"},
                status=200
            )

    raise NotFound("Recipe not found")


# GET /recipes/export
@app.get("/recipes/export")
async def export_recipes(request):

    return json({
        "count": len(recipes),
        "recipes": recipes
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)