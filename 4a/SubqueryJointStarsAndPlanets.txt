select round( avg(p.t_eq) , 1) , min(s.t_eff) , max(s.t_eff)
from Star s
join Planet p using(kepler_id)
where s.t_eff > (
  select avg(t_eff) from star
);