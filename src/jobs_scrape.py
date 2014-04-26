from __future__ import unicode_literals, print_function, division
# This Python file uses the following encoding: utf-8
import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")



__author__ = 'petrbouchal'

ministerstva = {
    'MPSV' : ['MPSV','Ministerstvo práce a sociálních věcí','http://www.mpsv.cz/cs/70'],
    'MV' : ['MVČR','Ministerstvo vnitra','http://www.mvcr.cz','http://www.mvcr.cz/nabidka-mist.aspx'],
    'UV' : ['ÚV','Úřad vlády','http://www.vlada.cz','http://www.vlada.cz/scripts/detail.php?pgid=445'],
    'MF' : ['MFČR','Ministerstvo financí','http://www.mfcr.cz','http://mfcr.cz/cs/o-ministerstvu/pracovni-mista/volna-mista-mf'],
    'MK' : ['MKČR','Ministerstvo kultury','http://www.mkcr.cz','http://www.mkcr.cz/volna-mista/default.htm'],
    'MSk' : ['MŠMT','Ministerstvo školství','http://www.msmt.cz','http://www.msmt.cz/ministerstvo/volna-mista'],
    'MSp' : ['MSpr','Ministerstvo spravedlnosti','http://www.justice.cz','NA'],
    'MZd' : ['MZd','Ministerstvo zdravotnictví','http://www.mzcr.cz','http://www.mzcr.cz/obsah/pracovni-prilezitosti_838_1.html'],
    'MD' : ['MDČR','Ministerstvo dopravy','http://www.mdcr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
    'MZe' : ['MDČR','Ministerstvo zemědělství','http://www.eagri.cz','http://www.http://eagri.cz/public/web/mze/ministerstvo-zemedelstvi/volna-pracovni-mista/'],
    'MO' : ['MO','Ministerstvo obrany','http://www.mocr.army.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
    'MMR' : ['MMR','Ministerstvo pro místní rozvoj','http://www.mmr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
    'MZP' : ['MŽP','Ministerstvo životního prostředí','http://www.mmr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
    'MZV' : ['MZV','Ministerstvo zahraničních věcí','http://www.mmr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
    'MPO' : ['MPO','Ministerstvo průmyslu a obchodu','http://www.mmr.cz','http://www.mdcr.cz/cs/Nabidka-zamestnani/'],
}

print(ministerstva['MPSV'][2])
