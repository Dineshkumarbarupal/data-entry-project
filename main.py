import logging
import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import calendar
from time import sleep

logging.basicConfig(filename='automation.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.get("https://fasalrin.gov.in/")
driver.maximize_window()
driver.implicitly_wait(100)

logging.info("वेबसाइट खुली - URL: https://example.com")

def fill_form():

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[1]'))).click()
    except Exception as e:
        print(f"Error with clicking dropdown: {e}")
   
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[2]/span/i'))).click()
    except Exception as e:
        print(f"Error with clicking submenu link: {e}")

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/section/div/div/div/div[2]/div/form/div/input'))).send_keys("9887784666")
    sleep(1)

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="slide-pass"]/div[1]/form/div/input'))).send_keys("9887784666")
    sleep(1)  

    logging.info("लॉगिन बटन क्लिक किया गया")
    try:
        next_page_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div[5]/button'))
        )
        print("Login successful, next page loaded!")
    except Exception as e:
        print(f"Error after login: {e}")
        return False  
    return True

logging.info("लॉगिन फॉर्म में डेटा भरा गया")

def loan_application(data, skip_first_task=False):
    try:
        if not skip_first_task:
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div[5]/button/span'))).click()
                sleep(1)

                application_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/li[3]/a/span')))
                application_button.click()

            except EC.TimeoutException:
                print("Button not found, skipping the task...")

        # dasbord_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/li[2]/a')))
        # dasbord_button.click()
      
        fin_year = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[1]/form/div/select')))
        fin_year.click()
        
        fin_year.send_keys(Keys.ARROW_DOWN)
        
        fin_year.send_keys(Keys.ENTER)
        
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/input'))).send_keys(data['aadhaar_no'])
        
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[3]/div/div[2]/button'))).click()
        
        beneficiary_details = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[1]/form/div/select')))
        beneficiary_details.click()
        beneficiary_details.send_keys(Keys.ARROW_DOWN)
        beneficiary_details.send_keys(Keys.ENTER)

        ok_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[3]/button[2]')))
        ok_button.click() 

        select_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applicantDetails"]/div[1]/div/div/form/div/select')))
        select_button.click()
        select_button.send_keys(Keys.ARROW_DOWN)
        select_button.send_keys(Keys.ENTER)

        button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applicantDetails"]/div[4]/div/button')))
        button.click()
    
        button2 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="account"]/div[2]/div/div/button[2]')))
        button2.click() 

        date_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[1]/div/input')))
        date_input.click()
       
        kcc_loan_sanctioned_date = data['kcc_loan_sanctioned_date'] 
        d, m, y = kcc_loan_sanctioned_date.split('.')

        month_number = int(m) 
        day = str(int(d))
        year = int(y)

        month_name = calendar.month_name[month_number] 
        try:
            year_picker = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[1]/div/div/span[2]')))
            year_picker.click()  

            year_picker_click = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='rmdp-ym']//span[text()='{year}']")))
            year_picker_click.click()
          
            month_pic = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[1]/div/div/span[1]')))
            month_pic.click()   

            month_picker_option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='rmdp-ym']//span[text()='{month_name}']")))
            month_picker_option.click()
          
            day_picker_option = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{day}']")))
            day_picker_option.click()
           
        except Exception as e:
            print(f"day selection failed: {e}")

        loan_sanctioned_amt = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[1]/div[2]/form/div/input')))
        loan_sanctioned_amt.send_keys(data['kcc_loan_sanctioned_amt'])
        
        # loan_drawing_limit = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[1]/div[3]/form/div/input')))
        # loan_drawing_limit.send_keys(data['kcc_loan_drawing_limit_curr_fy'])
       
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finance"]/div[2]/div/div/button[2]'))).click()
       
        # agri_crop = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activity"]/div/div[1]/div/div/button[1]')))
        # agri_crop.click()
    

        # activity_loan_amount = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[1]/div[1]/form/div/input')))
        # activity_loan_amount.send_keys(data['activity_loan_sanction_amt'])
     
        crop = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/form/div/select')))
        crop.send_keys('w')
        crop.send_keys(Keys.ENTER)
        
        survey_no = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[3]/form/div/input')))
        survey_no.send_keys(data['activity_survey_no'])

        khata_no = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[4]/form/div/input')))
        khata_no.send_keys(data['activity_khata_no'])
       
        land_area = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[5]/form/div/input')))
        land_area.send_keys(data['activity_land_area'])
        
        land_type = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[6]/form/div/select')))
        land_type.send_keys(data['activity_land_type'])
       
        land_type.send_keys(Keys.ENTER)
        
        season = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[7]/form/div/select')))
        season.send_keys(data['activity_season'])
        season.send_keys(Keys.ENTER)
        
        select_address = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/a')))
        select_address.click()

        sub_district = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[1]/div[3]/div/form/div/select')))
        sub_district.click()
        sub_district.send_keys(data['resSubDistrictId'])
        sub_district.send_keys(Keys.ENTER)
      
        village =WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[1]/div[4]/div/form/div/select')))
        village.click()
        village.send_keys(data['resVillageId'])
        village.send_keys(Keys.ENTER)

        proceed_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[2]/div/button')))
        proceed_button.click()
       
        submit_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activity"]/div/div[3]/div/button[3]')))
        submit_button.click()
        
        preview_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formTabs-tabpane-5"]/div/div[2]/div/div/button')))
        preview_button.click()
   
        submit_button2 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/button')))
        submit_button2.click()

        cunfirm_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/button[2]')))
        cunfirm_button.click()
        sleep(1)
        print("Clicking ok button...")
    
        return True
    except Exception as e:
        print(f"Error in loan application form: {e}")

def next_task():
        ok_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/button')))
        ok_button.click()

        # return False

def extract_and_update_data(csv_file, current_row_data):
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'pt-4'))
        ).text

        print(f"Success Message: {success_message}")

        message_parts = success_message.split()

        try:
            loan_application_id = message_parts[2]  
            status_detail = message_parts[4]  
            
        except IndexError:
            print("Error extracting Loan Application ID or Status Detail, check success message format...")
            return

        print(f"Loan Application ID: {loan_application_id}")
        print(f"Status Detail: {status_detail}")

        updated_rows = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row['sno'] == current_row_data['sno']: 
                    row['loan_application_id'] = loan_application_id
                    row['status_detail'] = status_detail
                updated_rows.append(row)

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        print("Data successfully updated in CSV...")

    except Exception as e:
        print(f"Error extracting application ID or updating CSV: {e}")

def process_csv(file):
    with open(file, newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        skip_first_task = False
        for row in data:
            print("Processing row...")

            if skip_first_task or fill_form():
                print("Form filing start...")
                success = loan_application(row, skip_first_task)
                print(f"Loan application for row {row}: {success}")
            
                if success:
                    print("Loan application successful, extracting and appending data...")
                    extract_and_update_data(file, row)
                    next_task()
                else:
                    print("Loan application failed, skipping data extraction...")
                
                skip_first_task = True
            else:
                print("An error occurred...")

file = 'data.csv'
process_csv(file)