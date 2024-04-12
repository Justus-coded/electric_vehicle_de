select make, model, model_year, count(*) as no_of_cars
from  `electricvehicles-420015.electric_vehicles.ev_us`
group by make, model, model_year
order by no_of_cars desc