# 📨 Confirmation Rate Calculation

## 📊 Table Schemas

### **Signups**

| Column Name | Type     | Description                       |
|-------------|----------|-----------------------------------|
| user_id     | int      | Unique identifier for the user    |
| time_stamp  | datetime | Signup timestamp of the user      |

- `user_id` is the **primary key** of this table.

---

### **Confirmations**

| Column Name | Type     | Description                                               |
|-------------|----------|-----------------------------------------------------------|
| user_id     | int      | Foreign key referencing `Signups.user_id`                |
| time_stamp  | datetime | Time when confirmation message was requested              |
| action      | ENUM     | One of `'confirmed'` or `'timeout'`                       |

- `(user_id, time_stamp)` is the **primary key** of this table.
- `action` indicates whether the user confirmed or timed out on the confirmation request.

---

## 📌 Problem Statement

Write a query to calculate the **confirmation rate** for each user.

> The confirmation rate is defined as:
>
> \[
> \text{confirmation\_rate} = \frac{\text{# of 'confirmed' messages}}{\text{Total # of confirmation messages}}
> \]

- If a user has not made any confirmation requests, their confirmation rate is `0.00`.
- Round the final confirmation rate to **2 decimal places**.
- Return the result in **any order**.

---

## 📥 Example Input

### `Signups` Table:

| user_id | time_stamp          |
|---------|---------------------|
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |

### `Confirmations` Table:

| user_id | time_stamp          | action    |
|---------|---------------------|-----------|
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |

---

## 📤 Expected Output

| user_id | confirmation_rate |
|---------|-------------------|
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |

---

## ✅ Explanation

- **User 6**: No confirmation requests → `0.00`
- **User 3**: 2 timeouts → `0 / 2 = 0.00`
- **User 7**: 3 confirmed → `3 / 3 = 1.00`
- **User 2**: 1 confirmed, 1 timeout → `1 / 2 = 0.50`

---

## 🛠️ SQL Strategy

1. Start with the `Signups` table.
2. Left join with `Confirmations` to include users with no confirmations.
3. Group by `user_id`.
4. Calculate:
   - total confirmations
   - confirmed confirmations
5. Use `IFNULL()` or `COALESCE()` to handle division by zero.
6. Round the result to two decimal places.

---

> 📌 This is a typical SQL aggregation problem involving `LEFT JOIN`, `GROUP BY`, and conditional aggregation using `CASE`.
