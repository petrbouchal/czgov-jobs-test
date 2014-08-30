__author__ = 'petrbouchal'

def scrape(deptabb, url, level1, level2, items = {'name': 'a', 'id': None, 'class': None},
           subitems={'name': 'a', 'id': None, 'class': None}, dosubitems=False):
    from bs4 import BeautifulSoup
    print(url)
    from datetime import datetime
    import mechanize
    import urlparse
    br = mechanize.Browser()
    br.set_handle_redirect(False)
    br.set_handle_robots(False)
    try:
        page0 = br.open(url)
    except mechanize.HTTPError as e:
        print(e.reason)
        print(e.code)
        print(e.info())
        print(e.geturl())
        page0 = 'blah'
    page = page0.read()
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
    datetimestring = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S%Z')
    for job in jobs:
        fulljoburl = urlparse.urlparse(url).scheme + '://' + str(urlparse.urlparse(url).netloc) + '/' \
                     + str(urlparse.urlparse(job['href']).path)
        jobdict = {'joburl':fulljoburl, 'jobtitle':job.contents[0], 'dept':deptabb,'datetime':datetimestring}
        jobslist.append(jobdict)
    # print(jobslist)
    return jobslist