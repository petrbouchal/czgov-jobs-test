__author__ = 'petrbouchal'


def open_checksnag(request):
    import urllib2

    request = urllib2.Request(url=request, headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        # print(e)
        if e.getcode() == 302 and e.headers.get('Location') is not None:
            opener = urllib2.build_opener()
            cookie = e.headers.get('Set-Cookie')
            # print(cookie)
            opener.addheaders.append(('Cookie', cookie))
            opener.addheaders.append(('User-agent', 'Mozilla/5.0 (Linux i686)'))
            newurl = e.headers.get('Location')
            # print(newurl)
            response = opener.open(newurl)
            return response
        else:
            print('Error opening page')
            raise
    return response

def completeurl(fullurl, partialurl):
    from urllib2 import urlparse
    parsed_jobsurl = urlparse.urlparse(fullurl)
    parsed_joburl = urlparse.urlparse(partialurl)
    fulljoburl = urlparse.urlunparse([parsed_jobsurl.scheme, parsed_jobsurl.netloc,
                                      parsed_joburl.path, parsed_joburl.params, parsed_joburl.query,
                                      parsed_joburl.fragment])
    return fulljoburl


def scrapejobs(timestamp, bodydata):
    from bs4 import BeautifulSoup

    print(bodydata['jobsurl'])
    import urlparse
    import re

    page = open_checksnag(bodydata['jobsurl'])
    page = page.read()
    # print(page)
    page = BeautifulSoup(page)
    jobslist = []

    jobs = page.select(bodydata['jobtitledata']['itemselect'])
    # for i in jobs: print(i.contents)

    # Add href attribute if URL was collected separately
    if bodydata['separateurl']:
        joburls = page.select(bodydata['joburldata']['itemselect'])
        for count in range(0, len(jobs), 1):
            jobs[count].attrs['href'] = joburls[count]['href']

    # Add additional title text if it is to be collected
    if bodydata['jobtitledata']['additionaltitletext']:
        additionaltexts = page.select(bodydata['jobtitledata']['additionaltextselect'])
        for count in range(0, len(jobs), 1):
            jobs[count].contents = jobs[count].contents[0] + ', ' + additionaltexts[count].contents[0]
    else:
        for job in jobs: job.contents = job.contents[0]

    for job in jobs:
        fulljoburl = completeurl(bodydata['jobsurl'], job['href'])
        if bodydata['abbrev'] == 'MSp': fulljoburl = bodydata['jobsurl']  # to get around session-dependent MSp pages
        jobtitle = re.sub('([\w])', lambda x: x.groups()[0].upper(), job.contents, 1, flags=re.UNICODE)
        jobdict = {'joburl': fulljoburl, 'jobtitle': jobtitle, 'dept': bodydata['abbrevcz'], 'datetime': timestamp}
        jobslist.append(jobdict)
    # print(jobslist)
    return jobslist


def scrapepages(timestamp, bodydata):
    from bs4 import BeautifulSoup

    jobsurlslist = [bodydata['jobsurl']]
    jobspageurl_iter = bodydata['jobsurl']

    def getnextlink(bodydata, iterfirsturl):
        if(bodydata['paginate'] == False):
            return False
        else:
            iterpage = open_checksnag(iterfirsturl)
            iterpage = iterpage.read()
            itersoup = BeautifulSoup(iterpage)
            nextlink = itersoup.select(bodydata['paginatelinkselect'])
            if len(nextlink) == 0:
                return False
            else:
                nextlink_final = completeurl(bodydata['jobsurl'],nextlink[0]['href'])
                return nextlink_final

    while (getnextlink(bodydata, jobspageurl_iter)):
        jobsurlslist.append(getnextlink(bodydata, jobspageurl_iter))
        jobspageurl_iter = getnextlink(bodydata, jobspageurl_iter)

    alljobslist = []
    for jobspageurl in jobsurlslist:
        newbodydata = bodydata
        newbodydata['jobsurl'] = jobspageurl
        thispagejoblist = scrapejobs(timestamp, newbodydata)
        alljobslist = alljobslist + thispagejoblist

    print('Nalezeno ' + str(len(alljobslist)) + ' pozic na ' + str(bodydata['abbrevcz']))

    return alljobslist
