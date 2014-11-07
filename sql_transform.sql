drop table data2;

create table data2 as select dept, jobtitle, joburl, max(datetime) as lastseen, min(datetime) as firstseen from data group by joburl, jobtitle;
alter table data2 add column seenfor;
alter table data2 add column live;
alter table data2 add column latest;
drop table data;
alter table data2 rename to data;

update data set seenfor=round((strftime('%s',lastseen)-strftime('%s',firstseen))/60/60/12);
update data set live=(lastseen==(select max(lastseen) from data));
update data set latest=(seenfor==0 and live==1);
