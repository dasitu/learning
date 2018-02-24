CREATE TABLE VehicleComplain(
reporter TEXT,
reporter_location TEXT,
product_producer TEXT,
brand_name TEXT,
product_model TEXT,
product_year TEXT,
product_name TEXT,
assemble TEXT,
sub_assemble TEXT,
submit_time TIME,
PRIMARY KEY (reporter, product_name, submit_time)
);