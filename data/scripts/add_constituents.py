from src.constituent.constituent_actions import ConstituentActions


constituents = [
    ["Paul Revere", "32 Battle Road", "Lexington", "02476", "(111) 415-1775"],
    ["Bugs Bunny", "32 Looney Tune Road", "Cwazy Rabbit", "02174", "(WHA) TSU-PDOC"],
    ["Kamala Harris", "1 Whitehouse", "Pleasantville", "41923", "(111) 347-0000"],
    ["Sirius Black", "12 Grimmauld Place", "Magic", "12345", "(123) 321-1234"],
    ["Mrs Addams", "001 Cemetery Lane", "Death Hollow", "34521", "(617) 862-7731"],
    ["Harriet Tubman", "000 Secret Street", "Hiddenville", "00000", ""],
]

# mock person data for proof of concept demo
# in production, person data would come from external system
def add_mock_constituents():
    print("Adding constituents")
    x = 0
    for constituent in constituents:
        person = constituents[x]
        name = person[0]
        address = person[1]
        town = person[2] + ", <state> " + person[3]
        phone = person[4]
        ConstituentActions.create(
            name=name, address=address, town=town, phone=phone, uuid_param=str(x)
        )
        x = x + 1
