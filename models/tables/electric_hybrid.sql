select electric_vehicle_type, count(*) as no_of_cars
from `electricvehicles-420015.electric_vehicles.ev_us`
group by electric_vehicle_type
order by no_of_cars desc