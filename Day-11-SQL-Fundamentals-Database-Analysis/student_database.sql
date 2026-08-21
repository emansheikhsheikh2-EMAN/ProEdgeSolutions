-- Day 11: SQL Fundamentals & Database Analysis
-- Student Database Analysis System

-- Create Departments table
CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create Students table
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    department_id INTEGER,
    semester INTEGER,
    age INTEGER,
    marks REAL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
-- Insert sample departments
INSERT INTO Departments (department_id, department_name) VALUES
(1, 'Computer Science'),
(2, 'Data Science'),
(3, 'Software Engineering'),
(4, 'Information Technology');

-- Insert sample courses
INSERT INTO Courses (course_id, course_name, department_id) VALUES
(101, 'Database Systems', 1),
(102, 'Machine Learning', 2),
(103, 'Web Engineering', 3),
(104, 'Data Analytics', 2),
(105, 'Information Security', 4);

-- Insert sample students
INSERT INTO Students
(student_id, student_name, department_id, semester, age, marks)
VALUES
(1, 'Ali Khan', 1, 4, 21, 85),
(2, 'Sara Ahmed', 2, 6, 22, 92),
(3, 'Hamza Malik', 3, 3, 20, 78),
(4, 'Ayesha Noor', 2, 5, 21, 88),
(5, 'Usman Tariq', 4, 2, 19, 74),
(6, 'Hira Shah', 1, 4, 21, 95),
(7, 'Bilal Khan', 3, 6, 23, 81),
(8, 'Maham Ali', 2, 6, 22, 96),
(9, 'Zain Abbas', 4, 3, 20, 69),
(10, 'Iqra Faisal', 1, 5, 22, 89);
-- ============================================
-- BASIC SQL QUERIES
-- ============================================

-- 1. Display all student records
SELECT * FROM Students;

-- 2. Filter students based on marks
-- Display students who scored 85 or more
SELECT *
FROM Students
WHERE marks >= 85;

-- 3. Sort students by marks
-- Highest marks first
SELECT *
FROM Students
ORDER BY marks DESC;

-- 4. Count total students
SELECT COUNT(*) AS total_students
FROM Students;

-- 5. Calculate average marks
SELECT AVG(marks) AS average_marks
FROM Students;

-- 6. Find highest and lowest marks
SELECT
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM Students;
-- ============================================
-- DEPARTMENT-WISE ANALYSIS
-- ============================================

-- 7. Display department-wise student count
SELECT
    department_id,
    COUNT(*) AS total_students
FROM Students
GROUP BY department_id;

-- 8. Display department-wise average marks
SELECT
    department_id,
    AVG(marks) AS average_marks
FROM Students
GROUP BY department_id;

-- 9. INNER JOIN: Display students with department names
SELECT
    Students.student_id,
    Students.student_name,
    Departments.department_name,
    Students.semester,
    Students.marks
FROM Students
INNER JOIN Departments
    ON Students.department_id = Departments.department_id;

-- 10. LEFT JOIN: Display all departments and their students
SELECT
    Departments.department_name,
    Students.student_name,
    Students.marks
FROM Departments
LEFT JOIN Students
    ON Departments.department_id = Students.department_id;

-- Display departments having average marks above 80
-- Demonstrates GROUP BY and HAVING
SELECT
    department_id,
    AVG(marks) AS average_marks
FROM Students
GROUP BY department_id
HAVING AVG(marks) > 80;
-- ============================================
-- ADVANCED SQL QUERIES
-- ============================================

-- 11. Subquery: Display students scoring above average
SELECT
    student_id,
    student_name,
    marks
FROM Students
WHERE marks > (
    SELECT AVG(marks)
    FROM Students
);

-- 12. ROW_NUMBER(): Rank students by marks
-- Each student gets a unique row number
SELECT
    student_id,
    student_name,
    marks,
    ROW_NUMBER() OVER (ORDER BY marks DESC) AS row_number
FROM Students;

-- 13. RANK(): Rank students by marks
-- Students with equal marks receive the same rank
SELECT
    student_id,
    student_name,
    marks,
    RANK() OVER (ORDER BY marks DESC) AS student_rank
FROM Students;

-- 14. Top-performing students
-- Display students with marks of 90 or above
SELECT
    student_id,
    student_name,
    marks
FROM Students
WHERE marks >= 90
ORDER BY marks DESC;
-- ============================================
-- COMMON TABLE EXPRESSION (CTE)
-- ============================================

-- 15. CTE: Find students whose marks are above
-- the overall class average
WITH AverageMarks AS (
    SELECT AVG(marks) AS class_average
    FROM Students
)
SELECT
    Students.student_id,
    Students.student_name,
    Students.marks,
    AverageMarks.class_average
FROM Students
CROSS JOIN AverageMarks
WHERE Students.marks > AverageMarks.class_average
ORDER BY Students.marks DESC;