-- SQL script that creates an index idx_name_first on the table names and the first letter of name.
-- Requirements:
-- 1. Import this table dump: names.sql.zip.
-- 2. Only the first letter of name must be indexed.

CREATE INDEX idx_name_first ON names (LEFT(name, 1));
