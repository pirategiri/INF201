# INF201

GitHub repository to upload all exercises related to INF201.

##  Task 1
1. `Hello.py` is the code initially pushed to verify GitHub configurations and ensure Git is set up properly.

##  Task 2
The following files are included in this task:
1. `sensor_reading.py` – Python script that processes the data.
2. `config.yml` – Contains the calibration threshold and output filename.
3. `sensors.xlsx` – Contains sensor location and owner information.
4. `calibrations.csv` – Contains calibration information.
5. `calibration_alerts.json` – Generated output containing overdue sensors.

##  How The Script Works
1. Imports the necessary libraries (e.g., `PyYAML` to read the YAML file).
2. The function `config_data` reads the configuration YAML file and returns it as a dictionary.
3. The function `sensor_reading` performs the main logic:
    - Reads the CSV file.
    - Reads the Excel file (requires `openpyxl`).
    - Merges these two files using a common column (`sensor_id`).
    - Filters out calibration data by comparing the threshold value from the config file with the newly merged data.
    - Converts the filtered data from a Pandas DataFrame into a dictionary.
    - Converts the dictionary into JSON format.
4. Calls the `main` function.
5. Executes the program.

##  Additional Libraries
Before running the script, you must install the required Excel engine for Pandas:

```bash
pip install openpyxl
```
