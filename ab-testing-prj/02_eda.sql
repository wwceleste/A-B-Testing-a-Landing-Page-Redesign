-- ============================================================
-- 02_eda.sql
-- Exploratory checks on ab_data_clean before trusting the results

-- Check 1: is the control/treatment split roughly 50/50?
SELECT
    "group",
    COUNT(*) AS total_users,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM ab_data_clean), 2) AS pct_of_total
FROM ab_data_clean
GROUP BY "group";

-- Check 2: consistent date range?
SELECT
    "group",
    MIN(timestamp) AS earliest,
    MAX(timestamp) AS latest
FROM ab_data_clean
GROUP BY "group";