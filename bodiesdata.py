#!/usr/bin/python
# -*- coding: utf-8 -*-
paramsjson = {
    "MZe" :
        {
            "fullname": "Ministerstvo zemědělství",
            "abbrev" : "MZe",
            "abbrevcz": "MZe",
            "jobsurl": "http://eagri.cz/public/web/mze/ministerstvo-zemedelstvi/volna-pracovni-mista/?pageSize=50",
            "jobtitledata" : {
                "itemselect": "div#article h2.h a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MPO" :
        {
            "fullname": "Ministerstvo průmyslu a obchodu",
            "abbrev" : "MPO",
            "abbrevcz": "MPO",
            "jobsurl": "http://www.mpo.cz/dokument61716.html",
            "jobtitledata" : {
                "itemselect": "div#text ul a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MV" :
        {
            "fullname": "Ministerstvo vnitra",
            "abbrev" : "MV",
            "abbrevcz": "MV",
            "jobsurl": "http://www.mvcr.cz/nabidka-mist.aspx",
            "jobtitledata" : {
                "itemselect": "div#main div#content div#articleList div.article h3 a",
                "additionaltitletext" : True,
                "additionaltextselect" : "div#main div#content div#articleList div.article p"
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "UV" :
        {
            "fullname": "Úřad vlády",
            "abbrev" : "UV",
            "abbrevcz": "ÚV",
            "jobsurl": "http://www.vlada.cz/scripts/detail.php?pgid=445",
            "jobtitledata" : {
                "itemselect": "div#content div.content-main a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MD" :
        {
            "fullname": "Ministerstvo dopravy",
            "abbrev" : "MD",
            "abbrevcz": "MD",
            "jobsurl": "http://www.mdcr.cz/cs/Nabidka-zamestnani/nz.htm",
            "jobtitledata" : {
                "itemselect": "div.innermenubottom div.postings a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MF" :
        {
            "fullname": "Ministerstvo financí",
            "abbrev" : "MF",
            "abbrevcz": "MF",
            "jobsurl": "http://www.mfcr.cz/cs/o-ministerstvu/pracovni-mista/volna-mista-mf",
            "jobtitledata" : {
                "itemselect": "div.mainContent div.layoutFull a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MK" :
        {
            "fullname": "Ministerstvo kultury",
            "abbrev" : "MK",
            "abbrevcz": "MK",
            "jobsurl": "http://www.mkcr.cz/volna-mista/default.htm",
            "jobtitledata" : {
                "itemselect": "div#main div#content a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MO" :
        {
            "fullname": "Ministerstvo obrany",
            "abbrev" : "MO",
            "abbrevcz": "MO",
            "jobsurl": "http://www.mocr.army.cz/ministr-a-ministerstvo/kariera-vzdelavani/pracovni-prilezitosti/default.htm",
            "jobtitledata" : {
                "itemselect": "div.item div.txt-left div.info h2 a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MMR" :
        {
            "fullname": "Ministerstvo pro místní rozvoj",
            "abbrev" : "MMR",
            "abbrevcz": "MMR",
            "jobsurl": "http://www.mmr.cz/cs/Pracovni-prilezitosti/",
            "jobtitledata" : {
                "itemselect": "div.rightPanel div.content div.VypisClanku div.Clanek div.ClanekOdkaz a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MSMT" :
        {
            "fullname": "Ministerstvo školství",
            "abbrev" : "MSMT",
            "abbrevcz": "MŠMT",
            "jobsurl": "http://www.msmt.cz/ministerstvo/volna-mista",
            "jobtitledata" : {
                "itemselect": "div#article div.article-content h3 a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MZV" :
        {
            "fullname": "Ministerstvo zahraničních věcí",
            "abbrev" : "MZV",
            "abbrevcz": "MZV",
            "jobsurl": "http://www.mzv.cz/jnp/cz/o_ministerstvu/zamestnani/aktualni_nabidky_zamestnani/index.html",
            "jobtitledata" : {
                "itemselect": "div.article_list div.article_content h2.article_title a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False
        },
    "MZP":
        {
            "fullname": "Ministerstvo životního prostředí",
            "abbrev": "MZP",
            "abbrevcz": "MŽP",
            "jobsurl": "http://mzp.cz/cz/volna_mista",
            "jobtitledata": {
                "itemselect": "div#content div.contentMain h2 a",
                "additionaltitletext": False
            },
            "separateurl": False,
            "joburldata": {
                "itemselect": ""
            },
            "paginate": False
        },

    "MPSV" :
        {
            "fullname": "Ministerstvo práce a sociálních věcí",
            "abbrev" : "MPSV",
            "abbrevcz": "MPSV",
            "jobsurl": "http://www.mpsv.cz/cs/70",
            "jobtitledata" : {
                "itemselect": "div#articlebody div#toc ul li a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False,
            "paginatelinkselect" : ""
        },
    "CSSZ" :
        {
            "fullname": "Česká správa sociálního zabezpečení",
            "abbrev" : "CSSZ",
            "abbrevcz": "ČSSZ",
            "jobsurl": "http://www.cssz.cz/cz/o-cssz/volna-mista/",
            "jobtitledata" : {
                "itemselect": "div#main-content div.article ul li a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False,
            "paginatelinkselect" : ""
        },
    "MZd" :
        {
            "fullname": "Ministerstvo zdravotnictví",
            "abbrev" : "MZd",
            "abbrevcz": "MZd",
            "jobsurl": "http://www.mzcr.cz/obsah/pracovni-prilezitosti_838_1.html",
            "jobtitledata" : {
                "itemselect": "div#main div#middle-column-content div.uvod-clanek h3 a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : False,
            "paginatelinkselect" : ""
        },
    "MSp" :
        {
            "fullname": "Ministerstvo spravedlnosti",
            "abbrev" : "MSp",
            "abbrevcz": "MSp",
            "jobsurl": "http://portal.justice.cz/Justice2/MS/ms.aspx?j=33&o=23&k=5956",
            "jobtitledata" : {
                "itemselect": "div.news-list.clearfix div.item.main div.item.full h2.heading a",
                "additionaltitletext" : False
            },
            "separateurl": False,
            "joburldata" : {
                "itemselect":""
            },
            "paginate" : True,
            "paginatelinkselect" : "div.pages a.next"
        },
    "UP" :
        {
            "fullname" : "Úřad práce",
            "abbrev" : "UP",
            "abbrevcz" : "ÚP",
            "jobsurl" : "http://portal.mpsv.cz/upcr/vmnaup",
            "jobtitledata" : {
                "itemselect" : "div.region h4.nadpisRad",
                "additionaltitletext" : False
            },
            "separateurl" : True,
            "joburldata" : {
                "itemselect" : "div.region table + a"
            },
            "paginate" : False
        },
    "FS" :
        {
            "fullname" : "Finanční správa",
            "abbrev" : "FS",
            "abbrevcz" : "FS",
            "jobsurl" : "http://www.financnisprava.cz/cs/financni-sprava/volna-pracovni-mista",
            "jobtitledata" : {
                "itemselect" : "div.attachments article header h3 a",
                "additionaltitletext" : True,
                "additionaltextselect" : "div.attachments article header p.subtitle"
            },
            "separateurl" : False,
            "joburldata" : {
                "itemselect" : ""
            },
            "paginate" : True,
            "paginatelinkselect" : "div.nabidkaPrace div.pagination a[rel=next]"
        }
}


