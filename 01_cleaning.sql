-- ============================================================
-- 01_cleaning.sql
-- Cleans ab_data_raw and creates ab_data_clean
-- Removes: (1) mismatched group/landing_page rows
--          (2) duplicate user_id rows (keep first occurrence)
-- ============================================================

-- Sanity check #1: how many rows have a mismatched group/landing_page?
SELECT
    group_landing_check,
    COUNT(*) AS row_count
FROM (
    SELECT
        CASE
            WHEN "group" = 'control'   AND landing_page = 'old_page' THEN 'match'
            WHEN "group" = 'treatment' AND landing_page = 'new_page' THEN 'match'
            ELSE 'mismatch'
        END AS group_landing_check
    FROM ab_data_raw
)
GROUP BY group_landing_check;

-- Sanity check #2: how many duplicate user_ids exist?
SELECT
    user_id,
    COUNT(*) AS occurrences
FROM ab_data_raw
GROUP BY user_id
HAVING COUNT(*) > 1
LIMIT 10;

-- ============================================================
-- Build the clean table
-- ============================================================
DROP TABLE IF EXISTS ab_data_clean;

CREATE TABLE ab_data_clean AS
WITH matched_only AS (
    SELECT *
    FROM ab_data_raw
    WHERE
        ("group" = 'control'   AND landing_page = 'old_page')
        OR ("group" = 'treatment' AND landing_page = 'new_page')
),
deduped AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY timestamp
        ) AS rn
    FROM matched_only
)
SELECT
    user_id,
    timestamp,
    "group",
    landing_page,
    converted
FROM deduped
WHERE rn = 1;

-- Final check: row count and CVR per group in the clean table
SELECT
    "group",
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(1.0 * SUM(converted) / COUNT(*), 4) AS conversion_rate
FROM ab_data_clean
GROUP BY "group";