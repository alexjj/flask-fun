from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://alexjj:MY2egZ9YCf7b%23mVBhu22@atlas-g6yq2.mongodb.net/test?retryWrites=true&w=majority")

recipes = client['twilio']['recipes']

def search_recipe(search_word):
    cursor = recipes.find({'$text': {'$search': search_word}})
    result = []
    for data in cursor:
        result.append(data)
    return result