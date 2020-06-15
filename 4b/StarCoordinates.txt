delete from Star;

alter table Star add column ra float, add column decl float;

copy Star (kepler_id, t_eff, radius, ra, decl) from 'stars_full.csv' CSV