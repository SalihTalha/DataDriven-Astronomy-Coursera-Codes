delete from Planet where radius < 0;
update Planet set kepler_name = NULL where UPPER(status) != 'CONFIRMED';