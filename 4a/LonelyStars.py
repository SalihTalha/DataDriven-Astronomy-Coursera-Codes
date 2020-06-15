select s.kepler_id, s.t_eff, s.radius from Star as s left outer join Planet as p
using (kepler_id) where p.koi_name is null order by t_eff desc 