select kepler_id, count(kepler_id) from Planet group by kepler_id having count(kepler_id) > 1 order by count(kepler_id) desc