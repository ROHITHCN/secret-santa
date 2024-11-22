# Secret Santa Assignment Automation

This project automates the process of assigning Secret Santa participants, adhering to specified constraints such as avoiding self-assignment and preventing repetitions from the previous year's assignments.

## Features

- **Automatic Assignment**: Ensures each participant is assigned a unique Secret Santa child.
- **Conflict Avoidance**: Avoids self-assignment and repetition of assignments from the previous year.
- **Extensibility**: Built using modular and object-oriented principles for easy maintenance and extension.
- **Error Handling**: Incorporates mechanisms to handle invalid inputs and file-related errors.

---

## Prerequisites

- **Python 3.7+**
- Required Python packages:
  - `openpyxl`
  - `pandas`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Input Files

  Employee List: A spreadsheet (employee.xlsx) containing employee information.
        Columns:
            Employee_Name
            Employee_EmailID

   Previous Year Assignments: A spreadsheet (previous_assignments.xlsx) containing last year's Secret Santa data.
        Columns:
            Employee_Name
            Employee_EmailID
            Secret_Child_Name
            Secret_Child_EmailID

## Output

The program generates a output.csv file containing the Secret Santa assignments with the following columns:

  Employee_Name
  Employee_EmailID
  Secret_Child_Name
  Secret_Child_EmailID

## Usage

  Prepare Input Files: Ensure the employee.xlsx and previous_assignments.xlsx files are in the data/ directory with the correct format.

  Run the Program: Execute the following command:

  ```bash
  python main.py
  ```

  View Results: The assignments will be saved as output.csv in the data/ directory.

## Tests
  
  All test cases have been given in the tests folder

## Project Structure
  
    ├── data/
    │   ├── employee.xlsx
    │   ├── previous_assignments.xlsx
    │   ├── output.csv
    ├── tests/
    |   ├── test_convert_to_csv.py
    |   ├── test_file_operations.py
    |   ├── test_secret_santa.py
    ├── main.py
    ├── requirements.txt
    └── README.md



## Component Descriptions

### `data/`
This folder contains all the input and output data files:
- **`employee.xlsx`**: Input file listing employees and their email IDs.
- **`previous_assignments.xlsx`**: Input file with the previous year's Secret Santa assignments to avoid repetition.
- **`output.csv`**: Output file generated after assigning Secret Santas, containing employee and secret child details.

### `tests/`
This folder contains unit tests for the project:
- **`test_convert_to_csv.py`**: Tests for ensuring correct conversion and formatting of CSV files.
- **`test_file_operations.py`**: Tests to validate file reading and writing processes.
- **`test_secret_santa.py`**: Tests for the logic behind the Secret Santa assignment, ensuring constraints are met.

### `main.py`
The primary script to execute the Secret Santa assignment process:
- Reads the input data from the `data/` folder.
- Handles Secret Santa assignment logic.
- Writes the output data to the `output.csv` file in the `data/` folder.

### `requirements.txt`
Lists the dependencies required for the project. Install them using:

```bash
pip install -r requirements.txt

