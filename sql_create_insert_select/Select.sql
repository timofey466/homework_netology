select title, years from albom where years ='2018';
select title, times from song where times >= '3.30';
select title, times from song where times = (select max(times)from song);
select title, year_old from playlist where year_old >='2018' and year_old <='2020';
select title from song where title like '%%my%%';
select title from songer where title not like  '%% %%'
