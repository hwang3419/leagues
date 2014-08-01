use test;
SELECT distinct Hometeam,count(Hometeam) as tcount FROM rest_resource_e0 group by hometeam order by tcount Desc;