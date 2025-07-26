
---

### **Table: Employee**

| Column Name | Type    |
| ----------- | ------- |
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |

`id` is the primary key column for this table.
Each row represents an employee, their department, and the `id` of their manager.
If `managerId` is `null`, that employee has no manager.
No employee is their own manager.

---

### **Write a SQL query to find the names of managers who have at least 5 direct reports.**
---

### **Example Input:**

**Employee table:**

| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |

---

### **Example Output:**

| name |
| ---- |
| John |

---

### **Explanation:**

* John (id = 101) is the manager of 5 employees.
* So, we return `'John'`.
