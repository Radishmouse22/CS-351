# CS 351 Project
Sam Dunlap, Isaac Hutchinson, Katherine Cho

Make sure to cd into the project file first
```powershell
cd "django-project"
```

# Run Webserver
While cd-ed into the project folder, run this command to run the webserver on port 80:
```powershell
py manage.py runserver 80
```
You may have to run python3 or python instead of py

Then visit `127.0.0.1` or `localhost` on a web browser on the same computer

# Admin Login
admin login is `admin` password `changeme123`

# Employee Function Tests

### Mechanic Tests
Mechanics can access service data, worked on, and vehicle

Sample mechanic login: `rcruz` password `changeme123`
1. Service a vehicle and update service records
    1. select service data relation
    2. update/add entries (billing can be null)

### Salesperson Tests
Salespeople can access inventory vehicle, vehicle, sales, and customer

Sample salesperson login: `tbell` password `changeme123`
1. Sell a vehicle and update inventory
    1. select sales relation
    2. add new sale (vehicle updates automatically to be 'sold')
2. Insert new vehicle records
    1. select vehicle relation
    2. add entries
3. Insert new customer records
    1. select customer relation
    2. add entries

### Billing Staff Tests
Billing staff can access billing, vehicle, and customer

Sample billing staff login: `mshaw` password `changeme123`
1. Query the database for customer, vehicle, and billing information
    1. select customer/vehicle/billing relation
    2. use djangoql to search through the entries (automatically suggests what to type next for non-technical users)


# SQL Tests (In Shell)
You must have SQLite3 installed and added to your PATH.

To run these test prompts in the sqlite3 shell, first cd into the folder and run the shell on the database file.
```powershell
sqlite3 db.sqlite3
```
Then run any of these prompts.

These prompts also have equivalents in the more user-friendly admin panel and djangoql.
### Prompt 1
Get all vehicles that have been serviced, along with the customer who brought them in
```sql
SELECT 
    v.year, v.make, v.model, c.name AS customer
FROM models_servicedata sd
JOIN models_vehicle v ON sd.vehicle_id = v.id
JOIN models_customer c ON sd.customer_id = c.id;
```
### Prompt 2
Get all employees who worked on a specific service job, with their hours
```sql
SELECT 
    sd.id AS service_id, v.make, v.model, u.first_name, u.last_name, u.email, w.hours
FROM models_workedon w
JOIN models_servicedata sd ON w.serviceData_id = sd.id
JOIN models_vehicle v ON sd.vehicle_id = v.id
JOIN models_employee e ON w.employee_id = e.id
JOIN auth_user u ON e.user_id = u.id
ORDER BY sd.id;
```
### Prompt 3
Get total hours worked per employee across all service jobs
```sql
SELECT 
    u.first_name, u.last_name, u.email, SUM(w.hours) AS total_hours
FROM models_workedon w
JOIN models_employee e ON w.employee_id = e.id
JOIN auth_user u ON e.user_id = u.id
GROUP BY u.first_name, u.last_name, u.email
ORDER BY total_hours DESC;
```
### Prompt 4
Get all sales with the vehicle, buyer, and payment method
```sql
SELECT 
    v.year, v.make, v.model, c.name AS customer, s.dateSold, b.paymentMethod
FROM models_sales s
JOIN models_vehicle v ON s.vehicle_id = v.id
JOIN models_customer c ON s.customer_id = c.id
JOIN models_billing b ON s.billing_id = b.id;
```
### Prompt 5
Get all customers who have both bought a vehicle AND had a service done
```sql
SELECT c.name
FROM models_customer c
WHERE c.id IN (SELECT customer_id FROM models_sales)
  AND c.id IN (SELECT customer_id FROM models_servicedata);
```
### Prompt 6
Get the total estimated cost per customer across all their service visits
```sql
SELECT 
    c.name AS customer, SUM(sd.estimate) AS total_estimate
FROM models_servicedata sd
JOIN models_customer c ON sd.customer_id = c.id
GROUP BY c.name
ORDER BY total_estimate DESC;
```
### Prompt 7
Get all inventory vehicles and their current location
```sql
SELECT 
    v.year, v.make, v.model, iv.location, iv.note
FROM models_inventoryvehicle iv
JOIN models_vehicle v ON iv.vehicle_id = v.id;
```
### Prompt 8
Get average mileage at arrival for service visits per vehicle make
```sql
SELECT 
    v.make, AVG(sd.arrivalMileage) AS avg_arrival_mileage
FROM models_servicedata sd
JOIN models_vehicle v ON sd.vehicle_id = v.id
GROUP BY v.make
ORDER BY v.make;
```
### Prompt 9
Get each service job with the total hours worked and compare to the estimate
```sql
SELECT 
    sd.id AS service_id, v.make, v.model, sd.estimate, SUM(w.hours) AS total_hours
FROM models_servicedata sd
JOIN models_vehicle v ON sd.vehicle_id = v.id
LEFT JOIN models_workedon w ON w.serviceData_id = sd.id
GROUP BY sd.id, v.make, v.model, sd.estimate;
```
### Prompt 10
Get all vehicles and their current status, with related sale or service info if applicable
```sql
SELECT 
    v.year, v.make, v.model, v.status,
    c_sale.name AS sold_to,
    s.dateSold,
    c_svc.name AS serviced_for,
    sd.estimate AS service_estimate
FROM models_vehicle v
LEFT JOIN models_sales s ON s.vehicle_id = v.id
LEFT JOIN models_customer c_sale ON s.customer_id = c_sale.id
LEFT JOIN models_servicedata sd ON sd.vehicle_id = v.id
LEFT JOIN models_customer c_svc ON sd.customer_id = c_svc.id;
```

# Report Generation
To generate a report for reach relation, go to the admin panel of that model and press the export button in the top-right corner, which will allow you to download all of the data for those entries in a human readable format.