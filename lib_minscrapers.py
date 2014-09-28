__author__ = 'petrbouchal'


def open_checksnag(request):
    import urllib2
    request = urllib2.Request(url=request, headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
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


def scrape_old(timestamp, deptabb, url, level1, level2, items={'name': 'a', 'id': None, 'class': None},
           subitems={'name': 'a', 'id': None, 'class': None}, dosubitems=False):
    from bs4 import BeautifulSoup

    print(url)
    # import mechanize
    import urlparse
    import re
    # br = mechanize.Browser()
    # br.set_cookiejar(cjar)
    # br.set_handle_robots(False)
    # br.set_handle_redirect(True)
    # opener = mechanize.build_opener(*br.handlers)
    # request = mechanize.Request(url)
    # request.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
    page = open_checksnag(url)
    page = page.read()
    # print(page)
    page = BeautifulSoup(page)

    level1html = page.find(level1['name'], {'class': level1['class']}, id=level1['id'])
    # print(level1)
    # print(level1['name'])
    # print(level1['id'])
    # print(level1['class'])
    # print('Level1html: ' + str(level1html))
    # print(level2)
    # print(level2['name'])
    # print(level2['id'])
    # print(level2['class'])
    level2html = level1html.find(level2['name'], {'class': level2['class']}, id=level2['id'])
    # print(level2html)
    # print(items)
    jobs = level2html.find_all(items['name'], {'class': items['class']}, id=items['id'])
    # print(jobs)
    if dosubitems:
        # print(subitems)
        newjobs = []
        jobsforlevel4 = jobs
        for job in jobsforlevel4:
            newjob = job.find(subitems['name'], {'class': subitems['class']}, id=subitems['id'])
            newjobs.append(newjob)
        jobs = newjobs


    # print(jobs)
    jobslist = []
    for job in jobs:
        parsed_jobspage = urlparse.urlparse(url)
        parsed_jobpage = urlparse.urlparse(job['href'])
        fulljoburl = urlparse.urlunparse([parsed_jobspage.scheme, parsed_jobspage.netloc,
                                          parsed_jobpage.path, parsed_jobpage.params, parsed_jobpage.query,
                                          parsed_jobpage.fragment])
        if deptabb == 'MSp': fulljoburl = url  # to get around session-dependent MSp pages
        jobtitle = re.sub('([\w])', lambda x: x.groups()[0].upper(), job.contents[0], 1, flags=re.UNICODE)
        jobdict = {'joburl': fulljoburl, 'jobtitle': jobtitle, 'dept': deptabb, 'datetime': timestamp}
        jobslist.append(jobdict)
    # print(jobslist)
    print('Nalezeno ' + str(len(jobslist)) + ' pozic na ' + str(deptabb))
    return jobslist


def scrape(timestamp, bodydata):
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
    for i in jobs: print(i.contents)

    # Add href attribute if URL was collected separately
    if bodydata['separateurl']:
        joburls = page.select(bodydata['joburldata']['itemselect'])
        for count in range(0,len(jobs),1):
            jobs[count].attrs['href'] = joburls[count]['href']

    # Add additional title text if it is to be collected
    if bodydata['jobtitledata']['additionaltitletext']:
        additionaltexts = page.select(bodydata['jobtitledata']['additionaltextselect'])
        for count in range(0,len(jobs),1):
            jobs[count].contents = jobs[count].contents[0] + ', ' + additionaltexts[count].contents[0]
    else:
        for job in jobs: job.contents = job.contents[0]

    for job in jobs:
        parsed_jobsurl = urlparse.urlparse(bodydata['jobsurl'])
        parsed_joburl = urlparse.urlparse(job['href'])
        fulljoburl = urlparse.urlunparse([parsed_jobsurl.scheme, parsed_jobsurl.netloc,
                                          parsed_joburl.path, parsed_joburl.params, parsed_joburl.query,
                                          parsed_joburl.fragment])
        if bodydata['abbrev'] == 'MSp': fulljoburl = bodydata['jobsurl']  # to get around session-dependent MSp pages
        jobtitle = re.sub('([\w])', lambda x: x.groups()[0].upper(), job.contents, 1, flags=re.UNICODE)
        jobdict = {'joburl': fulljoburl, 'jobtitle': jobtitle, 'dept': bodydata['abbrevcz'], 'datetime': timestamp}
        jobslist.append(jobdict)
    # print(jobslist)
    print('Nalezeno ' + str(len(jobslist)) + ' pozic na ' + str(bodydata['abbrevcz']))
    return jobslist