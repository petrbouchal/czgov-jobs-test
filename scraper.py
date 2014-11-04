from __future__ import unicode_literals, print_function, division
# This Python file uses the following encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import sqlite3

db = sqlite3.connect('data.sqlite')
cursor = db.cursor()

selected0 = cursor.execute("""select * from data""")

print(len(selected0.fetchall()))

cursor.execute("""
                create table data2 as select dept, jobtitle, joburl, max(datetime) as lastseen, min(datetime) as firstseen from data group by joburl, jobtitle;
               """)
cursor.execute("""
                alter table data2 add column seenfor;
               """)
cursor.execute("""
                alter table data2 add column live;
               """)
cursor.execute("""
                alter table data2 add column latest;
               """)
cursor.execute("""
                drop table data;
               """)
cursor.execute("""
                alter table data2 rename to data;
               """)
db.commit()

selected = cursor.execute("""select * from data""")

print(len(selected.fetchall()))

for row in selected.fetchall():
    print(row)

cursor.execute("""
                update data set seenfor=round((strftime('%s',lastseen)-strftime('%s',firstseen))/60/60/12);
               """)
cursor.execute("""
                update data set live=(lastseen==(select max(lastseen) from data));
               """)
cursor.execute("""
                update data set latest=(seenfor==0 and live==1);
               """)
db.commit()

selected2 = cursor.execute("""select * from data where live==1""")

print(len(selected2.fetchall()))

for row in selected2.fetchall():
    print(row)

db.close()
