from __future__ import unicode_literals, print_function, division
# This Python file uses the following encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from lib_minscrapers import scrape
from datetime import datetime

now = datetime.now()

__author__ = 'petrbouchal'

# Basic infomration: name, proper abbreviation, top url and jobs url
ministerstva = {
    'MPSV' : ['MPSV','Ministerstvo práce a sociálních věcí','http://www.mpsv.cz','http://www.mpsv.cz/cs/70'],
    'MV' : ['MVČR','Ministerstvo vnitra','http://www.mvcr.cz','http://www.mvcr.cz/nabidka-mist.aspx'],
    'UV' : ['ÚV','Úřad vlády','http://www.vlada.cz','http://www.vlada.cz/scripts/detail.php?pgid=445'],
    'MF' : ['MFČR','Ministerstvo financí','http://www.mfcr.cz','http://www.mfcr.cz/cs/o-ministerstvu/pracovni-mista/volna-mista-mf'],
    'MK' : ['MKČR','Ministerstvo kultury','http://www.mkcr.cz','http://www.mkcr.cz/volna-mista/default.htm'],
    'MSMT' : ['MŠMT','Ministerstvo školství','http://www.msmt.cz','http://www.msmt.cz/ministerstvo/volna-mista'],
    'MSp' : ['MSp','Ministerstvo spravedlnosti','http://www.justice.cz','http://portal.justice.cz/Justice2/MS/ms.aspx?j=33&o=23&k=5956'],
    'MSp2' : ['MSp','Ministerstvo spravedlnosti','http://www.justice.cz','http://portal.justice.cz/Justice2/MS/ms.aspx?j=33&o=23&k=5956&page=2'],
    'MZd' : ['MZd','Ministerstvo zdravotnictví','http://www.mzcr.cz','http://www.mzcr.cz/obsah/pracovni-prilezitosti_838_1.html'],
    'MD' : ['MDČR','Ministerstvo dopravy','http://www.mdcr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/nz.htm'],
    'MZe' : ['MZe','Ministerstvo zemědělství','http://www.eagri.cz','http://eagri.cz/public/web/mze/ministerstvo-zemedelstvi/volna-pracovni-mista/'],
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
    'UV' : [False,
             {'name':'div', 'id':'content','class':None},
             {'name':'div','id':None,'class':'content-main'},
             {'name': 'a', 'id': None, 'class': None}],
    'MPSV' : [False,
              {'name':'div', 'id':'articlebody','class':None},
             {'name':'ul','id':None,'class':None},
             {'name': 'a', 'id': None, 'class': None}],
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
    'MSp' : [False,
            {'name':'div', 'id':None,'class':'news-list clearfix'},
             {'name':'div','id':None,'class':'item main'},
            {'name':'a','id':True,'class':None}],
    'MK' : [False,
            {'name':'div', 'id':'main','class':None},
             {'name':'div','id':'content','class':None},
             {'name': 'a', 'id': None, 'class': None}],
    'MZe' : [False,
            {'name':'div', 'id':'content','class':None},
             {'name':'div','id':'article','class':None},
             {'name': 'a', 'id': None, 'class': None}],
    'MV' : [True,
            {'name':'div', 'id':'content','class':None},
             {'name':'div','id':'articleList','class':None},
             {'name': 'h3', 'class': None, 'id': None},
             {'name': 'a', 'id': None, 'class': None}],
    'MMR' : [True,
            {'name':'div', 'id':None,'class':'rightPanel'},
            {'name':'div','id':'content','class':True},
            {'name':'div','class':'ClanekOdkaz','id':None},
            {'name':'a','id':None,'class':None}]
}

# Individual function calls to test things
# scrape(ministerstva['MPO'][3],minparameters['MPO'][1],minparameters['MPO'][2])
# scrape(ministerstva['UV'][3],minparameters['UV'][1],minparameters['UV'][2])
# scrape(ministerstva['MPSV'][3],minparameters['MPSV'][1],minparameters['MPSV'][2])
# scrape(url=ministerstva['MZd'][3],
#        level1=minparameters['MZd'][1],level2=minparameters['MZd'][2],
#        items=minparameters['MZd'][3],subitems=minparameters['MZd'][4],dosubitems=True)
# scrape(ministerstva['MD'][3],minparameters['MD'][1],minparameters['MD'][2])
# print(scrape(ministerstva['MSp'][0],ministerstva['MSp'][3],minparameters['MSp'][1],minparameters['MSp'][2],
#              minparameters['MSp'][3]))
# scrape(ministerstva['MV'][3],minparameters['MV'][1],minparameters['MV'][2],items=minparameters['MV'][3],
#        subitems=minparameters['MV'][4],dosubitems=True)

# Loop

activedepts = ['MPO','MPSV','UV','MZd','MSMT','MF','MMR','MV','MZe','MK','MSp','MO','MD']
# activedepts = ['MD']

jobsall = []
for dept in activedepts:
    # print(dept)
    depturl = ministerstva[dept][3]
    deptpars = minparameters[dept]
    if deptpars[0]==False:
        jobsall = jobsall + scrape(now, ministerstva[dept][0],depturl,deptpars[1], deptpars[2], deptpars[3])
    else:
        jobsall = jobsall + scrape(now, ministerstva[dept][0],depturl,deptpars[1], deptpars[2],
               deptpars[3],deptpars[4],dosubitems=True)
print('Celkem nalezeno pozic: ', len(jobsall))
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
for row in jobsall:
    # db.insert('data',row)
    print(row)