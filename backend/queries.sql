-- Useful SQL Queries for CareerPath Database
-- Use with: sqlite3 career_path.db < queries.sql
-- Or in DB Browser for SQLite

-- ========== RESUME QUERIES ==========

-- View all resumes
SELECT id, filename, file_type, top_match_role, top_match_percentage, 
       datetime(upload_date) as uploaded
FROM resumes
ORDER BY upload_date DESC;

-- Get resume count by file type
SELECT file_type, COUNT(*) as count
FROM resumes
GROUP BY file_type
ORDER BY count DESC;

-- Find resumes with highest match percentages
SELECT filename, top_match_role, top_match_percentage, 
       datetime(upload_date) as uploaded
FROM resumes
WHERE top_match_percentage IS NOT NULL
ORDER BY top_match_percentage DESC
LIMIT 10;

-- Get most common career matches
SELECT top_match_role, COUNT(*) as count, 
       ROUND(AVG(top_match_percentage), 2) as avg_match
FROM resumes
WHERE top_match_role IS NOT NULL
GROUP BY top_match_role
ORDER BY count DESC;

-- Find resumes uploaded today
SELECT id, filename, top_match_role, top_match_percentage
FROM resumes
WHERE DATE(upload_date) = DATE('now')
ORDER BY upload_date DESC;

-- Get total storage used
SELECT 
    COUNT(*) as total_resumes,
    ROUND(SUM(file_size) / 1024.0 / 1024.0, 2) as total_mb,
    ROUND(AVG(file_size) / 1024.0, 2) as avg_size_kb
FROM resumes;

-- ========== SKILL QUERIES ==========

-- Extract all unique skills (requires JSON parsing)
-- Note: SQLite JSON support is limited, better done in Python

-- View resumes with specific skill (example: Python)
SELECT id, filename, top_match_role, extracted_skills
FROM resumes
WHERE extracted_skills LIKE '%Python%'
ORDER BY upload_date DESC;

-- ========== SKILL GAP ANALYSIS QUERIES ==========

-- View all analyses
SELECT id, target_role, match_percentage, 
       datetime(analysis_date) as analyzed
FROM skill_gap_analyses
ORDER BY analysis_date DESC;

-- Get average match percentage by target role
SELECT target_role, 
       COUNT(*) as analysis_count,
       ROUND(AVG(match_percentage), 2) as avg_match,
       ROUND(MIN(match_percentage), 2) as min_match,
       ROUND(MAX(match_percentage), 2) as max_match
FROM skill_gap_analyses
GROUP BY target_role
ORDER BY analysis_count DESC;

-- Find analyses with low match percentages (< 50%)
SELECT id, target_role, match_percentage, 
       datetime(analysis_date) as analyzed
FROM skill_gap_analyses
WHERE match_percentage < 50
ORDER BY match_percentage ASC;

-- ========== JOINED QUERIES ==========

-- Get resumes with their analyses
SELECT 
    r.filename,
    r.top_match_role as resume_match,
    r.top_match_percentage as resume_match_pct,
    a.target_role as analysis_role,
    a.match_percentage as analysis_match_pct,
    datetime(a.analysis_date) as analyzed
FROM resumes r
LEFT JOIN skill_gap_analyses a ON r.id = a.resume_id
ORDER BY r.upload_date DESC;

-- ========== MAINTENANCE QUERIES ==========

-- View database statistics
SELECT 
    'Resumes' as table_name,
    COUNT(*) as row_count
FROM resumes
UNION ALL
SELECT 
    'Skill Gap Analyses' as table_name,
    COUNT(*) as row_count
FROM skill_gap_analyses;

-- Find orphaned analyses (no associated resume)
SELECT id, target_role, match_percentage
FROM skill_gap_analyses
WHERE resume_id NOT IN (SELECT id FROM resumes);

-- Find resumes without analyses
SELECT id, filename, top_match_role
FROM resumes
WHERE id NOT IN (SELECT resume_id FROM skill_gap_analyses WHERE resume_id IS NOT NULL);

-- ========== CLEANUP QUERIES ==========

-- Delete old resumes (older than 90 days) - BE CAREFUL!
-- DELETE FROM resumes 
-- WHERE upload_date < DATE('now', '-90 days');

-- Delete resumes with no extracted skills
-- DELETE FROM resumes 
-- WHERE extracted_skills = '[]' OR extracted_skills IS NULL;

-- ========== EXPORT QUERIES ==========

-- Export resume data to CSV format
.mode csv
.output resumes_export.csv
SELECT 
    id,
    filename,
    file_type,
    file_size,
    top_match_role,
    top_match_percentage,
    upload_date
FROM resumes
ORDER BY upload_date DESC;
.output stdout
.mode list

-- Export skill gap analyses to CSV
.mode csv
.output analyses_export.csv
SELECT 
    id,
    resume_id,
    target_role,
    match_percentage,
    analysis_date
FROM skill_gap_analyses
ORDER BY analysis_date DESC;
.output stdout
.mode list
