import json
import yaml
import pandas as pd

#reading config data
def config_data(filename: str):
    """Function to read the orgininal config file and saving into standard python dictionary"""

    #opening file
    with open(filename, "r") as file:
        config=yaml.safe_load(file)

    return config

print(config_data('config.yml'))


#OPERATIONS WITH EXCEL AND CSV FILE

def read_sensors():
    """Function to Manage and check all the operations specified for the assignment i.e; check overdue and create a json file """

    #Reading the config file
    config= config_data('config.yml')
    max_days_since_calibration= config['max_days_since_calibration']
    output_file=config["output_file"]

    #Reading sensor data from excel file

    sensor_data=pd.read_excel('sensors.xlsx')

    #reading calibration data from csv file

    calibration_data=pd.read_csv('calibrations.csv')

    #merging two files in a single file using a common value

    merged_data=pd.merge(
        sensor_data, calibration_data ,on="sensor_id")

    #Filtering  overdue sensors,

    overdue_sensors= merged_data[merged_data["days_since_calibration"]>max_days_since_calibration]
    print(overdue_sensors)

    #keeping only the required columns from the merged dataset required for the output

    overdue_sensors=overdue_sensors[[
        "sensor_id",
        "lab_room",
        "owner",
        "days_since_calibration"
    ]]

    #Since python cannot convert a pandas df directly into json, converting the data into a dictionary
    #orient=records converts every row into dictionary and that dictionary into list

    organized_data= overdue_sensors.to_dict(orient="records")

    
    with open(output_file ,"w") as file:

        #Writing into JSON file, indent organizes the data into a structure
        print(json.dump(organized_data,file, indent=2))

    print(f"Overdue Sensors count {len(overdue_sensors)}")
    print(f"Results saved to {output_file}")


#Executing the main function
if __name__== "__main__":
    read_sensors()
    print("Done")
    




        


    
