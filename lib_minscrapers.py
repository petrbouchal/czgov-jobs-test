__author__ = 'petrbouchal'


def open_checksnag(request):
    import urllib2
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        # print(e)
        if e.getcode() == 302 and e.headers.get('Location') is not None:
            opener = urllib2.build_opener()
            cookie = e.headers.get('Set-Cookie')
            # print(cookie)
            opener.addheaders.append(('Cookie',cookie))
            opener.addheaders.append(('User-agent','Mozilla/5.0 (Linux i686)'))
            newurl = e.headers.get('Location')
            # print(newurl)
            response = opener.open(newurl)
            return response
        else:
            print('Error opening page')
            raise
    return response


def scrape(timestamp, deptabb, url, level1, level2, items = {'name': 'a', 'id': None, 'class': None},
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

    level1html = page.find(level1['name'],{'class':level1['class']}, id=level1['id'])
    # print(level1)
    # print(level1['name'])
    # print(level1['id'])
    # print(level1['class'])
    # print('Level1html: ' + str(level1html))
    # print(level2)
    # print(level2['name'])
    # print(level2['id'])
    # print(level2['class'])
    level2html = level1html.find(level2['name'], {'class':level2['class']}, id=level2['id'])
    # print(level2html)
    # print(items)
    jobs = level2html.find_all(items['name'],{'class':items['class']},id=items['id'])
    # print(jobs)
    if dosubitems:
        # print(subitems)
        newjobs = []
        jobsforlevel4 = jobs
        for job in jobsforlevel4:
            newjob = job.find(subitems['name'], {'class':subitems['class']},id = subitems['id'])
            newjobs.append(newjob)
        jobs = newjobs


    # print(jobs)
    jobslist = []
    for job in jobs:
        parsed_jobspage = urlparse.urlparse(url)
        parsed_jobpage = urlparse.urlparse(job['href'])
        fulljoburl = urlparse.urlunparse([parsed_jobspage.scheme, parsed_jobspage.netloc,
                     parsed_jobpage.path,parsed_jobpage.params,parsed_jobpage.query, parsed_jobpage.fragment])
        if deptabb=='MSp': fulljoburl = url # to get around session-dependent MSp pages
        jobtitle = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), job.contents[0], 1)
        jobdict = {'joburl':fulljoburl, 'jobtitle':jobtitle,'dept':deptabb,'datetime':timestamp}
        jobslist.append(jobdict)
    # print(jobslist)
    print('Nalezeno ' + str(len(jobslist)) + ' pozic na ' + str(deptabb))
    return jobslist
