SELECT tpep_pickup_datetime,
tpep_dropoff_datetime,
total_amount,
CONCAT(zpu."Borough", ' / ', zpu."Zone") as "pick_up_loc",
CONCAT(zdo."Borough",' / ', zdo."Zone") as "dropoff_loc"

FROM 

yellow_taxi_data ytd,
zone_trip_data zpu,
zone_trip_data zdo

WHERE ytd."PULocationID" = zpu."LocationID" AND
	  ytd."DOLocationID" = zdo."LocationID"
	  
LIMIT 100