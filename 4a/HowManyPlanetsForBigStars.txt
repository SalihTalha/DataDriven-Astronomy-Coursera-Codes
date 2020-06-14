select Star.radius, count(Planet.koi_name) 
from Star join Planet using (kepler_id) 
where Star.radius >= 1 
group by Star.kepler_id
having count(Planet.koi_name) > 1
order by Star.radius desc