import requests
import time

print("\r\nWebpage tester \r\n\r\n")

def get_page_loading_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            loading_time = (end_time - start_time) * 1000  # Convert to milliseconds
            return loading_time
        else:
            print(f"Error: Unable to fetch the web page. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    urls_to_test = {
        'https://www.google.co.uk': 'Google',
        'https://albert.racelogic.co.uk/': 'Albert',
        'https://en.racelogic.support/': 'Support',
        'https://en.racelogic.support/VBOX_Automotive': 'Automotive',
        'https://en.racelogic.support/VBOX_Motorsport': 'Motorsport', 
        'https://en.racelogic.support/VBOX_Automotive/Product_Info/VBOX_Data_Loggers/VBOX_II/VBOX_IISL_20_Hz_GPS_Data_Logger_%E2%80%93_Dual_Antenna': 'VBOX2SL',
        'https://en.racelogic.support/VBOX_Automotive/Knowledge_Base/VBOX_and_RL_Input_Module_Communication': 'Input Module', 
        'https://en.racelogic.support/VBOX_Motorsport/Product_Info/Video_Data_Loggers/Video_VBOX_Range/Quick_Start_Guide/Video_VBOX_-_Quick_start_guide': 'VVB Quick Start', 
        'https://en.racelogic.support/VBOX_Motorsport/Product_Info/Video_Data_Loggers/Video_VBOX_Range/Knowledge_Base/How_to_change_a_VBO_file_into_a_CIR_file': 'VBO File to CIR', 
        'https://en.racelogic.support/LabSat_GNSS_Simulators/Product_Info/LabSat/LabSat_User_Guide/01_-_LabSat_Introduction': 'LabSat intro', 
        'https://en.racelogic.support/LabSat_GNSS_Simulators/Software_Info/SatGen_v3_Software/Quick_Start_Guide/SatGen_v3_Quick_Start_Guide': 'SatGen V3 Quick Start',
        'https://en.racelogic.support/VBOX_Automotive/Product_Info/VBOX_Data_Loggers/VBOX_Sigma/VBOX_Sigma_User_Guide/04_-_VBOX_Sigma_Configuration': 'VBOX Sigma', 
        'https://en.racelogic.support/VBOX_Positioning/VBOX_Precision_Ranging_System_(VPRS)/VPRS_User_Guide/05_-_VPRS_VBOX_Touch_App': 'VPRS Touch App', 
        'https://en.racelogic.support/VBOX_Mining/Hardware_Info/VBOX_Camera_Kits/Ruggedised_580TVL_Camera_Kit/User_Guide/Ruggedised_580TVL_Camera_Kit_Inventory': '580 Mining CAM', 
        'https://en.racelogic.support/VBOX_Mining/FAQ/VBOX_Mining_Software_FAQ/How_do_I_analyse_TKPH_on_a_Water_Truck%3F': 'TKPH Mining', 
        'https://en.racelogic.support/Knowledge_Base/Product_Life_Cycle': 'Product Life Cycle' 
        # Add more URLs and friendly names here
    }

    for url, friendly_name in urls_to_test.items():
        loading_time = get_page_loading_time(url)

        if loading_time is not None:
            print(f"Page loading time for {friendly_name}: {loading_time:.2f} milliseconds")
        else:
            print(f"Failed to get the page loading time for {friendly_name}")