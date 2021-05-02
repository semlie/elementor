SELECT department_id, first_name, last_name, sal_diff
FROM
(SELECT
  department_id,first_name, last_name,
  (MAX(salary) - (SELECT
    MAX(salary)
  FROM Employees
  WHERE department_id = yt.department_id
  AND salary <
  MAX(yt.salary))
  ) sal_diff
FROM Employees yt
GROUP BY department_id,first_name, last_name) AS temp
WHERE temp.sal_diff IS NOT NULL

