# https://www.codewars.com/kata/525c65e51bf619685c000059


def cakes(recipe, available):
    amount = 9999
    tmp_amount = 0

    for kr, vr in recipe.items():
        if vr != 0 and kr not in list(available.keys()):
            return 0
        for ka, va in available.items():
            if kr == ka:
                tmp_amount = va // vr
                if tmp_amount < amount:
                    amount = tmp_amount

    return amount
