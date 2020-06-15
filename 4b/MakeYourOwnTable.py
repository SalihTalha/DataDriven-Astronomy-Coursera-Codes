create table Planet (
  kepler_id INTEGER not null,
  koi_name VARCHAR(15) unique not null,
  kepler_name VARCHAR(15),
  status VARCHAR(20) not null,
  radius FLOAT not null
);
insert into Planet(kepler_id, koi_name, kepler_name, status, radius) values(6862328,	'K00865.01', null	,	'CANDIDATE',	119.021);
insert into Planet(kepler_id, koi_name, kepler_name, status, radius) values(10187017,	'K00082.05',	'Kepler-102 b',	'CONFIRMED',	5.286); 
insert into Planet(kepler_id, koi_name, kepler_name, status, radius) values(10187017	,'K00082.04'	,'Kepler-102 c'	,'CONFIRMED'	,7.071);