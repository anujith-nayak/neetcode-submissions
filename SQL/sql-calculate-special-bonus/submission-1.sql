-- Write your query below
select employee_id,
case
   WHEN employee_id%2=1 and name NOT LIKE 'M%'
   THEN salary 
   else 0 end AS bonus from employees 
   ORDER BY employee_id;