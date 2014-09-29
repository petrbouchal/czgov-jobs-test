from __future__ import unicode_literals, print_function, division
# This Python file uses the following encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from lib_minscrapers import scrapejobs, scrapepages
from datetime import datetime

now = datetime.now()

__author__ = 'petrbouchal'

# Basic infomration: name, proper abbreviation, top url and jobs url
ministerstva = {
    'MF' : ['MFČR','Ministerstvo financí','http://www.mfcr.cz','http://www.mfcr.cz/cs/o-ministerstvu/pracovni-mista/volna-mista-mf'],
    'MK' : ['MKČR','Ministerstvo kultury','http://www.mkcr.cz','http://www.mkcr.cz/volna-mista/default.htm'],
    'MSMT' : ['MŠMT','Ministerstvo školství','http://www.msmt.cz','http://www.msmt.cz/ministerstvo/volna-mista'],
    'MZd' : ['MZd','Ministerstvo zdravotnictví','http://www.mzcr.cz','http://www.mzcr.cz/obsah/pracovni-prilezitosti_838_1.html'],
    'MD' : ['MDČR','Ministerstvo dopravy','http://www.mdcr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/nz.htm'],
    'MO' : ['MO','Ministerstvo obrany','http://www.mocr.army.cz','http://www.mocr.army.cz/ministr-a-ministerstvo/kariera-vzdelavani/pracovni-prilezitosti/default.htm'],
    'MMR' : ['MMR','Ministerstvo pro místní rozvoj','http://www.mmr.cz','http://www.mmr.cz/cs/Pracovni-prilezitosti/'],
    'MZP' : ['MŽP','Ministerstvo životního prostředí','http://www.mzp.cz','http://mzp.cz/cz/volna_mista'],
    'MZV' : ['MZV','Ministerstvo zahraničních věcí','http://www.mzv.cz','http://www.mzv.cz/jnp/cz/o_ministerstvu/zamestnani/aktualni_nabidky_zamestnani/index.html'],
    'MPO' : ['MPO','Ministerstvo průmyslu a obchodu','http://www.mpo.cz','http://www.mpo.cz/dokument61716.html'],
}

# Parameters for scraping job pages of each department
# list of dicts: level1, level2, items, subitems + T/F whether going through subitems is needed
minparameters = {
    'MPO' : [False,
             {'name':'div', 'id':'text','class':None},
             {'name':'ul','id':None,'class':None},
             {'name':'a','id':None,'class':None}],
    'MZd' : [True,
             {'name':'div', 'id':'main','class':None},
             {'name':'div','id':'middle-column-content','class':'clearfix'},
             {'name':'div','id':None,'class':'uvod-clanek'},
             {'name':'a', 'id':True, 'class':None}],
    'MD' : [False,
            {'name':'div', 'id':None,'class':'innermenubottom'},
             {'name':'div','id':None,'class':'postings'},
             {'name': 'a', 'id': None, 'class': None}],
    'MF' : [False,
            {'name':'div', 'id':None,'class':'mainContent'},
             {'name':'div','id':None,'class':'layoutFull'},
             {'name': 'a', 'id': None, 'class': None}],
    'MO' : [False,
            {'name':'div', 'id':None,'class':'item'},
             {'name':'div','id':None,'class':'txt-left'},
             {'name': 'a', 'id': None, 'class': None}],
    'MSMT' : [False,
            {'name':'div', 'id':'article','class':True},
             {'name':'div','id':None,'class':'article-content'},
             {'name': 'a', 'id': None, 'class': None}],
    'MK' : [False,
            {'name':'div', 'id':'main','class':None},
             {'name':'div','id':'content','class':None},
             {'name': 'a', 'id': None, 'class': None}],
    'MZP' : [False,
            {'name':'div', 'id':'content','class':None},  # based on current HTML
             {'name':'div','id':None,'class':'contentMain'},  # based on current HTML
             {'name': 'a', 'id': None, 'class': None}],  # needs updating when info becomes available
    'MZV' : [True,
            {'name':'div', 'id':None,'class':'article_list'},  # based on current HTML
             {'name':'div','id':None,'class':'article_content'},  # based on current HTML
             {'name': 'h2', 'id': None, 'class': 'article_title'},  # needs updating when info becomes available
             {'name': 'a', 'id': None, 'class': None}],  # needs updating when info becomes available
    'MMR' : [True,
            {'name':'div', 'id':None,'class':'rightPanel'},
            {'name':'div','id':'content','class':True},
            {'name':'div','class':'ClanekOdkaz','id':None},
            {'name':'a','id':None,'class':None}],
}

import json
minparameters = json.load(open('./bodiesdata.py'))

# Loop

# activedepts = ['MPO','MPSV','UV','MZd','MSMT','MF','MMR','MV','MZe','MK','MSp','MSp2','MO','MD','MZV','CSSZ']
activedepts = ['UV','CSSZ']

jobsallbodies = []
for dept in activedepts:
    # print(dept)
    jobsallbodies = jobsallbodies + scrapepages(now, minparameters[dept])
print('Celkem nalezeno pozic: ', len(jobsallbodies))
from pprint import pprint
# pprint(jobsall)

import litepiesql
import sqlite3

db = sqlite3.connect('data.sqlite')
cursor = db.cursor()

if len(cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='data';""").fetchall()) == 0:
    cursor.execute("""CREATE TABLE data
                        (jobtitle, joburl, dept, datetime timestamp)
                    """)
db.commit()
db.close()

db = litepiesql.Database('data.sqlite')
for row in jobsallbodies:
    db.insert('data',row)
    print(row)
