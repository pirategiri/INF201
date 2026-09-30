import json
import yaml
import pandas as pd

#reading config data
def config_data(filename: str):
    """Function to read the orgininal config file"""

    #opening file
    with open(filename, "r") as file:
        config=yaml.safe_load(file)

    return config

print(config_data('config.yml'))


#OPERATIONS WITH EXCEL AND CSV FILE

def read_sensors():
    """Function to Manage and check all the operations specified for the assignment """

    #Reading the config file data
    config= config_data('config.yml')
    max_days_since_calibration= config['max_days_since_calibration']
    output_file=config["output_file"]

    #Using pandas to read excel and csv file

    sensor_data=pd.read_excel('sensors.xlsx')
    calibration_data=pd.read_csv('calibrations.csv')

    #merging two files in a single file using a common value

    merged_data=pd.merge(
        sensor_data, calibration_data ,on="sensor_id")

    overdue_sensors= merged_data[merged_data["days_since_calibration"]>max_days_since_calibration]
    print(overdue_sensors)

    #keeping only the required columns from the merged dataset

    overdue_sensors=overdue_sensors[[
        "sensor_id",
        "lab_room",
        "owner",
        "days_since_calibration"
    ]]

    #Since python cannot convert a pandas df directly into json, converting the data into a dictionary

    organized_data= overdue_sensors.to_dict(orient="records")

    with open(output_file ,"w") as file:

        #Wrting into JSON file, indent organizes the data into a structure
        print(json.dump(organized_data,file, indent=2))

    print(f"Overdue Sensors count {len(overdue_sensors)}")
    print(f"Results saved to {output_file}")

if __name__== "__main__":
    read_sensors()
    print("Done")
    




        


    
