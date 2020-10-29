#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import os
import sys


if len(sys.argv) < 3 or len(sys.argv[1]) < 1 or len(sys.argv[2]) < 1:
    print('Please provide path to contacts2.db and output filename')
    print('e.g. ./contacts.py contacts2.db contacts.csv')
    sys.exit()

db_file = sys.argv[1]
csv_file = sys.argv[2]

# create connection and get data
con = sqlite3.connect(db_file)
db = con.cursor()
"""
mimetype_id explanation:
    1 email
    3 nickname
    4 organization
    5 phone_number
    7 name
    8 address
    13 birthday
"""
data = db.execute(
    'select raw_contact_id ,mimetype_id, data1 from data where mimetype_id in (1,3,4,5,7,8,13) and LENGTH(data1) > 1 order by raw_contact_id').fetchall()

contacts = {}
# format data
for d in data:
    id, type, value = d
    if id not in contacts:
        contacts[id] = []
    contacts[id].append(value)

# create csv string
csv = ''
for c in contacts:
    for i in contacts[c]:
        csv += '"'+i+'",'
    csv += "\n"

# remove file if it already exists
if os.path.exists(csv_file):
    os.remove(csv_file)

# write csv string to file
csvfile = open(csv_file, 'w')
csvfile.write(csv)
csvfile.close()
