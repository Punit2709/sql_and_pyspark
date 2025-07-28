
---

## 🧾 Monthly Transactions Summary

### 📘 Problem

Given a `Transactions` table, for each **month** and **country**, find:

* total number of transactions
* number of **approved** transactions
* total amount of all transactions
* total amount of **approved** transactions

Return one row per country per month.

---

### 📥 Input

Table: `Transactions`

| id  | country | state    | amount | trans\_date |
| --- | ------- | -------- | ------ | ----------- |
| 121 | US      | approved | 1000   | 2018-12-18  |
| 122 | US      | declined | 2000   | 2018-12-19  |
| 123 | US      | approved | 2000   | 2019-01-01  |
| 124 | DE      | approved | 2000   | 2019-01-07  |

---

### 📤 Output

| month   | country | trans\_count | approved\_count | trans\_total\_amount | approved\_total\_amount |
| ------- | ------- | ------------ | --------------- | -------------------- | ----------------------- |
| 2018-12 | US      | 2            | 1               | 3000                 | 1000                    |
| 2019-01 | US      | 1            | 1               | 2000                 | 2000                    |
| 2019-01 | DE      | 1            | 1               | 2000                 | 2000                    |

---

## 📚 Learning — Date Format Codes

| Format Code | Description                  | Example (`2024-07-26 18:30:45`) | Output   |
| ----------- | ---------------------------- | ------------------------------- | -------- |
| `%Y`        | Year (4 digits)              |                                 | `2024`   |
| `%y`        | Year (2 digits)              |                                 | `24`     |
| `%m`        | Month (2 digits)             |                                 | `07`     |
| `%c`        | Month (1 or 2 digits)        |                                 | `7`      |
| `%b`        | Abbreviated month name       |                                 | `Jul`    |
| `%M`        | Full month name              |                                 | `July`   |
| `%d`        | Day of month (2 digits)      |                                 | `26`     |
| `%e`        | Day of month (1 or 2 digits) |                                 | `26`     |
| `%H`        | Hour (00–23)                 |                                 | `18`     |
| `%h` / `%I` | Hour (01–12)                 |                                 | `06`     |
| `%i`        | Minutes (00–59)              |                                 | `30`     |
| `%s`        | Seconds (00–59)              |                                 | `45`     |
| `%p`        | AM or PM                     |                                 | `PM`     |
| `%W`        | Weekday name                 |                                 | `Friday` |
| `%a`        | Abbreviated weekday name     |                                 | `Fri`    |
| `%w`        | Day of the week (0=Sunday)   |                                 | `5`      |
| `%j`        | Day of the year (001–366)    |                                 | `208`    |

---