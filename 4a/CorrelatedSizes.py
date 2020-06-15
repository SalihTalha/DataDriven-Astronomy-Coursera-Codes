select p.koi_name , p.radius , s.radius from Star s join Planet p using(kepler_id)
where s.kepler_id in (
  select kepler_id
  from Star
  order by radius desc limit 5
);