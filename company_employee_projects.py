CREATE DATABASE company; 

CREATE TABLE projects (
    project_id varchar(50) primary key, 
    project_name varchar(50), 
    start_date date, 
    end_date date, 
    budget float
);

CREATE TABLE employees (
    employee_id varchar(50) primary key, 
    employee_name varchar(50),
    telephone_number varchar(50),
    email_address varchar(50),
    job_title varchar(50),
    salary float, 
    hire_date date 
);

CREATE TABLE departments (
    department_id varchar(50) primary key, 
    manager_employee_id varchar(50),
    department_name varchar(50), 
    location varchar(50),
    FOREIGN KEY (manager_employee_id) 
    REFERENCES company.public.employees(employee_id)
);


CREATE TABLE employee_projects (
    employee_id varchar(50),
    project_id varchar(50),
    role varchar(50),
    hours_worked float, 
    FOREIGN KEY (employee_id) 
    REFERENCES company.public.employees(employee_id),
    FOREIGN KEY (project_id)
    REFERENCES  company.public.projects(project_id)
);

INSERT INTO company.public.projects 
(project_id,project_name, start_date, end_date, budget) 
VALUES
('PID 001', 'Pigs in blanket', '2022-05-01', '2026-12-25', 56000)
; 

INSERT INTO company.public.projects 
(project_id,project_name, start_date, end_date, budget) 
VALUES
('PID 000', 'Let''s get this party started', '2000-01-01', '2050-01-01', 10000000)
; #double quote after 'let' to avoid error

INSERT INTO company.public.employees 
(employee_id, employee_name,telephone_number,email_address,job_title,salary,hire_date) 
VALUES 
('EID 001', 'Mariah Carey', '+4489765678', 'mariah.carey@aol.com', 'Principal Engineer', 1000000, '2018-09-18');
;

INSERT INTO company.public.employees 
(employee_id, employee_name,telephone_number,email_address,job_title,salary,hire_date) 
VALUES 
('EID 002', 'David Tennant', '+4432435678', 't_slayer.com', 'Assistant Regional Director', 300000, '2015-01-01');
;


INSERT INTO company.public.departments 
(department_id, manager_employee_id, department_name,location)
VALUES 
('DID 001', 'EID 001', 'Department of Christmas', 'North Pole');

INSERT INTO company.public.departments 
(department_id, manager_employee_id, department_name,location)
VALUES 
('DID 002', 'EID 002', 'Department of Apocalypse', 'Atlantis');

INSERT INTO company.public.employee_projects 
(employee_id,project_id,role,hours_worked) 
VALUES 
('EID 001', 'PID 001', 'Project lead', 4000.25),
('EID 002', 'PID 000', 'Project assistant', 15000)
;

#join statements
SELECT e.employee_name, e.job_title, e.salary, ep.role AS project_role, ep.hours_worked 
FROM employees AS e
INNER JOIN employee_projects AS ep
ON e.employee_id = ep.employee_id;

ALTER TABLE employees
RENAME salary to salary_USD;

