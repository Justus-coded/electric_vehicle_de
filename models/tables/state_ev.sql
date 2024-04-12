select b.state, city,  count(*) as no_of_cars 
from  `electricvehicles-420015.electric_vehicles.ev_us` a,
`electricvehicles-420015.dbt_jilemobayo.states_code` b
where a.state = b.code
group by b.state, city
order by no_of_cars desc