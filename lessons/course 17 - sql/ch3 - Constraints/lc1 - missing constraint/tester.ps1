# Define the relative paths to the SQLite database and the SQL script
$dbPath = Join-Path -Path $PSScriptRoot -ChildPath "test.db"
$sqlScriptPath = Join-Path -Path $PSScriptRoot -ChildPath "up.sql"

# Check if the SQLite database file already exists
if (Test-Path $dbPath) {
    Remove-Item $dbPath
}

# Create a new SQLite database
sqlite3 $dbPath ".databases"

# Read the SQL script
$sqlScript = Get-Content -Path $sqlScriptPath -Raw

# Execute the SQL script to create tables and insert data
sqlite3 $dbPath $sqlScript

Write-Output "Database created successfully at $dbPath"

# Define the path to the main SQL script
$mainSqlScriptPath = Join-Path -Path $PSScriptRoot -ChildPath "main.sql"

# Read the main SQL script
$mainSqlScript = Get-Content -Path $mainSqlScriptPath -Raw

# Execute the main SQL script with headers and capture the output
$output = sqlite3 $dbPath -header $mainSqlScript

# Print the output of the query
Write-Output $output

