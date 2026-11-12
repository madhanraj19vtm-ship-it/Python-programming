# MODULE 4 - File Handling and CSV Practice

This folder contains three Python lab programs, sample data, and sample outputs.

## Folder Contents

### Lab 1 - Log File Reader
**Python file:** `lab1_log_file_reader.py`  
**Sample output:** `sample_output_lab1.txt`  
**Sample data:** `sample_app.log`

Reads a log file, counts its entries, and allows the user to filter messages by INFO, WARNING, ERROR, or ALL. If the sample log file is missing, the program creates it automatically.

### Lab 2 - Student Data Manager using Files
**Python file:** `lab2_student_data_manager.py`  
**Sample output:** `sample_output_lab2.txt`

Uses a text file named `students.txt` to add, display, and search student records. The data file is created automatically when the first student is added.

### Lab 3 - CSV-Based Payroll Management System
**Python file:** `lab3_csv_payroll_management.py`  
**Sample output:** `sample_output_lab3.txt`

Accepts employee salary details, calculates HRA, DA, gross salary, and net salary, and saves the payroll records in `payroll.csv`.

## How to Run

Open a terminal in the MODULE 4 folder and run:

```bash
python lab1_log_file_reader.py
python lab2_student_data_manager.py
python lab3_csv_payroll_management.py
```

Python's built-in `csv` module is used, so no external packages are required.

## Important

The sample output files show example runs. The actual data files (`students.txt` and `payroll.csv`) are generated when you run the respective programs and enter records.

 
### Lab 4 - JSON-Based Log File Analyzer
**Python file:** `lab4_json_log_file_analyzer.py`  
**JSON data:** `logs.json`  
**Sample output:** `sample_output_lab4.txt`

Reads application log records from a JSON file using Python's built-in `json` module. Displays every record, counts INFO, WARNING, and ERROR messages, prints a category summary, and handles missing files, invalid JSON, and incorrectly structured data. If `logs.json` is absent, the program creates a sample file automatically.

Run it using:

```bash
python lab4_json_log_file_analyzer.py
```
