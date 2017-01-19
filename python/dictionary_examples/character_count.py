import pprint

string = raw_input("write your string here:")
count = {}

for character in string:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)
