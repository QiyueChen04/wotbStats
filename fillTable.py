import sqlite3
import json

conn = sqlite3.connect('database.db')

f = open ('./responsecopy.json', "r")
data = json.loads(f.read())

keys = data.keys()
values = data.values()

keysli = list(keys)
valuesli = list(values)

def idFill():
    cur = conn.cursor()
    with conn:
        for key in keys:
            insertid = ("INSERT INTO test (tank_id) VALUES (%s)" % int(key))
            cur.execute(insertid)

    cur.close()


def nameFill():
    cur = conn.cursor()
    with conn:
        for value in values:
            insertName = ("INSERT INTO test (name) VALUES (?)")
            name = (value['name'], )
            cur.execute(insertName, name)

    cur.close()

def Fill():
    cur = conn.cursor()
    with conn:
        insertstr = "INSERT INTO test (tank_id, name, nation, is_premium, tier, type, image_preview, image_normal) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        for i in range(535):
            insertTuple = (keysli[i], valuesli[i]['name'], valuesli[i]['nation'], 
                           valuesli[i]['is_premium'], valuesli[i]['tier'], valuesli[i]['type'], 
                           valuesli[i]['images']['preview'], valuesli[i]['images']['normal'])
            cur.execute(insertstr, insertTuple)
    cur.close()

Fill()

conn.commit()
conn.close()
f.close()

# conn = sqlite3.connect('tankStats.db')
# conn.execute("CREATE TABLE IF NOT EXISTS test (description text, nation text);")

# with open('./responsecopy.json', 'r') as json_file:
#     data = json.load(json_file)
#     for tank in data:
#         print(type(tank))


# # with open('/Users/jackchen/Documents/Winter 2024/WOTB website/data/responsecopy.json', 'r') as json_file:
# #     data = json.load(json_file)
# #     for tank in data:
# #         conn.execute("INSERT INTO test (description, nation) (VALUES (?, ?)", (tank["description"], tank["nation"]))

# #conn.commit()
# conn.close()