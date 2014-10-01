-- Basic select to get list of jobs with latest date
select dept as title, jobtitle as content, joburl as link, datetime as date
from 'data'
where date = (select max(datetime)
              from data)
order by title

-- select to get all new jobs, useful to generate atom (easy to turn into count of new jobs)
select jobtitle as content, maxdate as date, "http://www.byrokrates.cz/praceprostat" as link, "title" as title
from (select jobtitle, max(datetime) as maxdate, min(datetime) as mindate
      from data
      group by jobtitle)
where maxdate=mindate and maxdate=(select max(datetime)
                                   from data)

-- update to mark all jobs as either new at that date or not
select max(datetime) as maxdate, jobtitle, joburl, "True" as newjob
from data
group by jobtitle, joburl

select * from data i
where not exists(select ii.datetime
			from data ii
			where ii.joburl=i.joburl and
				ii.datetime>i.datetime
		)

select * from data i
where exists(select ii.datetime, ii.joburl
			     from data ii
			     where ii.joburl=i.joburl and ii.datetime>i.datetime)

			     SELECT a.joburl, a.datetime as FirstSeen, a.jobtitle
FROM data as a
INNER JOIN (
   SELECT joburl, min(datetime) as FirstSeen
   FROM data as b
   GROUP BY joburl)
ON b.joburl = a.joburl
AND b.FirstSeen = a.datetime

SELECT A.joburl, A.datetime as FirstViewed, A.jobtitle
FROM data A
LEFT JOIN data B
ON A.joburl = B.joburl
AND A.datetime > B.datetime
WHERE B.datetime is null