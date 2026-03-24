DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT,
    score REAL
);

INSERT INTO students(name,age,major,score)
VALUES
('张三',20,'计算机科学',88.5),
('李四',21,'软件工程',92.0),
('王五',19,'网络安全',76.0),
('赵六',22,'人工智能',95.5);
