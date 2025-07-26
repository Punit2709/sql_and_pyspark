-- Solution 1
select e2.name from Employee as e1
join Employee as e2 
on e1.managerId = e2.id
group by e1.managerId
having count(*) >= 5


-- solution 2
select name from Employee
where Employee.id in (
    select Employee.managerId
    from Employee
    where Employee.managerId is not null
    group by Employee.managerId
    having count(*) >= 5
)


-- Solution 3
with cte as (
    select 
        *, 
        count(*) over (partition by managerId) as cnt 
    from Employee
),
cte2 as (
    select 
        distinct managerId 
    from cte 
    where cnt >= 5
)
select
    name 
from Employee 
where id in (select managerId from cte2)