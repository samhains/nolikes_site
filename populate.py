import json
import sqlite3

db = sqlite3.connect('fluxos.sqlite')
traffic = json.load(open('xxx.json'))

someitem = traffic.itervalues().next()
columns = list(someitem.keys())
columns.remove('medicoes')
columns.remove('regime')

query = "insert into images (timestamp,{0}) values (?{1})"
query = query.format(",".join(columns), ",?" * len(columns))
print query

for timestamp, data in traffic.iteritems():
    keys = (timestamp,) + tuple(data[c] for c in columns)
    c = db.cursor()
    c.execute(query)
    c.close()
