# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

# CODE:
class Elem:
    def __init__(self, sign="+", value=0, power=1, letter="x"):
        self.sign = sign
        if self.sign == "+":
            self.value = value
        else:
            self.value = value * (-1)
        self.power = power
        self.letter = letter

    def __str__(self):
        if self.value == 0:
            return ""
        elif self.value == 1:
            if self.power == 0:
                return "+1"
            elif self.power == 1:
                return f"+{self.letter}"
            else:
                return f"+{self.letter}^{self.power}"
        elif self.value == -1:
            if self.power == 0:
                return "-1"
            elif self.power == 1:
                return f"-{self.letter}"
            else:
                return f"-{self.letter}^{self.power}"
        elif self.value > 0:
            if self.power == 0:
                return f"{self.sign}{self.value}"
            elif self.power == 1:
                return f"{self.sign}{self.value}{self.letter}"
            else:
                return f"{self.sign}{self.value}{self.letter}^{self.power}"
        else:
            if self.power == 0:
                return f"{self.value}"
            elif self.power == 1:
                return f"{self.value}{self.letter}"
            else:
                return f"{self.value}{self.letter}^{self.power}"


def multiply_elems(elem1, elem2):
    """
    elem - Elem obj
    output -> Elem obj
    """
    result_elem = Elem(letter=elem1.letter)
    result_elem.power = elem1.power + elem2.power
    result_elem.value = elem1.value * elem2.value
    if result_elem.value >= 0:
        result_elem.sign = "+"
    else:
        result_elem.sign = "-"

    return result_elem


def multiply_elems_lists(elems1, elems2):
    """
    elems = array of Elem obj
    output -> array of Elem obj
    """
    result = []
    for i in elems1:
        for j in elems2:
            result.append(multiply_elems(i, j))
    return result


def add_elems(elem1, elem2):
    if elem1.power != elem2.power:
        print("Cant add elem with different powers!")
        return None

    result_elem = Elem(letter=elem1.letter)
    result_elem.power = elem1.power
    result_elem.value = elem1.value + elem2.value
    result_elem.sign = "+" if result_elem.value >= 0 else "-"
    return result_elem


def scale_elem_list(elems):
    """
    add elems with same power
    output -> list of Elem obj
    """
    powers = []
    for i in elems:
        powers.append(i.power)
    max_power = max(powers)

    result = []
    for i in range(max_power, -1, -1):
        elems_to_sum = filter(lambda elem: elem.power == i, elems)
        if not elems_to_sum:
            continue
        else:
            tmp_elem = Elem(power=i, value=0, letter=elems[0].letter, sign="+")
            for j in elems_to_sum:
                tmp_elem = add_elems(tmp_elem, j)
            result.append(tmp_elem)
    return result


def expand(expr):
    base = expr[1:-3]
    power = expr[-1]

    print(f"({base})^{power}")

    # to the 0/1 power
    if power == "0":
        return "1"
    elif power == "1":
        return expr[1:-3]

    # prepare data [elem1, elem2]
    if base[0] == "-":
        first_sign = "-"
        base = base[1:]
    else:
        first_sign = "+"

    tmp_parts = []
    second_sign = "-"
    if "-" in base:
        tmp_parts = base.split("-")
    else:
        tmp_parts = base.split("+")
        second_sign = "+"

    letter = tmp_parts[0][-1]

    # elem1
    tmp_val = ""
    for i in tmp_parts[0]:
        if i.isdigit():
            tmp_val += i

    if tmp_val == "":
        tmp_val = "1"
    elem1 = Elem(sign=first_sign, letter=letter, value=int(tmp_val))

    # elem2
    elem2 = Elem(sign=second_sign, letter=letter, power=0, value=int(tmp_parts[1]))

    elems = [elem1, elem2]

    for i in elems:
        print(i)
        print(i.sign)
        print(i.value)
        print("\n")

    # calculate
    ans = elems.copy()
    for i in range(int(power) - 1):
        ans = multiply_elems_lists(ans, [elem1, elem2])
        ans = scale_elem_list(ans)

    # change to string
    ans_str = ""
    for i in ans:
        ans_str += str(i)

    return ans_str if ans_str[0] == "-" else ans_str[1:]
