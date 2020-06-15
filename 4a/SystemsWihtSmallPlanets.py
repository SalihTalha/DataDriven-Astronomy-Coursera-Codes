select s.radius as sun_radius, p.radius as planet_radius
from Star as s, planet as p
where s.kepler_id = p.kepler_id and s.radius > p.radius
order by s.radius desc