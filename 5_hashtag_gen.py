# https://www.codewars.com/kata/52449b062fb80683ec000024


def generate_hashtag(s):
    s = "#" + "".join(s.title().split()) if s != "" else ""
    return False if (s == "" or len(s) > 140) else s
