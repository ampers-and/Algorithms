#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # print("\n", "\nrecipe: ", recipe, "\ningredients: ", ingredients)
    batch_min = -1
    for k, v in recipe.items():
        val = ingredients.get(k, 0)
        batch = val // v
        if batch_min == -1:
            batch_min = batch
        elif batch < batch_min:
            batch_min = batch
        # print("k: ", k, "     val: ", val,
        #       "     v: ", v, "     batches: ", batch)

    # print("batch_min: ", batch_min)
    return batch_min


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
