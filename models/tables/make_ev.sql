select  make, count(*) as no_of_cars
from `electricvehicles-420015.electric_vehicles.ev_us`
group by make
order by no_of_cars desc