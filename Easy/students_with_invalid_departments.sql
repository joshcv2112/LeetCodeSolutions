-- https://leetcode.com/problems/students-with-invalid-departments/
-- SOLVED

SELECT id, name
FROM Students
where department_id NOT IN
    (SELECT id
FROM Departments)