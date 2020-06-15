create table Star (
  kepler_id integer primary key,
  t_eff integer not null,
  radius float not null
  );
create table Planet (
  kepler_id integer references Star(kepler_id),
  koi_name varchar(20) primary key,
  kepler_name varchar(20),
  status varchar(20) not null,
  period float,
  radius float,
  t_eq integer
  );

copy Star (kepler_id, t_eff, radius) from 'stars.csv' CSV;
copy Planet (kepler_id, koi_name, kepler_name, status, period, radius, t_eq) from 'planets.csv' CSV;
  
  