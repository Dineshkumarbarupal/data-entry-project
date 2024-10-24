import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import calendar
from time import sleep

driver = webdriver.Chrome()
driver.get("https://fasalrin.gov.in/")
driver.maximize_window()

def fill_form():
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[1]'))).click()
    except Exception as e:
        print(f"Error with clicking dropdown: {e}")
   
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[2]/span/i'))).click()
    except Exception as e:
        print(f"Error with clicking submenu link: {e}")

    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/section/div/div/div/div[2]/div/form/div/input').send_keys("9887784666")
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="slide-pass"]/div[1]/form/div/input').send_keys("9887784666")
    sleep(20)  

    try:
  
        next_page_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div[5]/button'))
        )
        print("Login successful, next page loaded!")
    except Exception as e:
        print(f"Error after login: {e}")
        return False  
    return True

def loan_application(data, skip_first_task=False):
    try:
        if not skip_first_task:
            try:
                WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div[5]/button/span'))).click()
                sleep(1)
            except EC.TimeoutException:
                print("Button not found, skipping the task...")

        driver.find_element(By.XPATH, '//*[@id="menu"]/li[2]/a').click()
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/a/span').click()
        sleep(1)

        fin_year = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[1]/form/div/select')
        fin_year.click()
        sleep(1)
        
        fin_year.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        fin_year.send_keys(Keys.ENTER)
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/input').send_keys(data['aadhaar_no'])
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[3]/div/div[2]/button').click()
        sleep(1)

        beneficiary_details = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[1]/form/div/select')
        sleep(2)
        beneficiary_details.click()
        sleep(2)
        beneficiary_details.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        beneficiary_details.send_keys(Keys.ENTER)
        sleep(2)

        ok_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[3]/button[2]')))
        ok_button.click()
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="applicantDetails"]/div[3]/div/button').click()
        sleep(3)

        driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div/div/button[2]').click()
        sleep(1)

        date_input = driver.find_element(By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[1]/div/input')
        date_input.click()
        sleep(2) 

        kcc_loan_sanctioned_date = data['kcc_loan_sanctioned_date'] 
        d, m, y = kcc_loan_sanctioned_date.split('.')

        month_number = int(m) 
        day = str(int(d))
        year = int(y)

        month_name = calendar.month_name[month_number] 
        try:
            year_picker = driver.find_element(By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[1]/div/div/span[2]')
            year_picker.click()
            sleep(2)

            year_picker_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='rmdp-ym']//span[text()='{year}']")))
            year_picker_click.click()
            sleep(3)
       
            month_pic = driver.find_element(By.XPATH, '//*[@id="finance"]/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[1]/div/div/span[1]')
            month_pic.click()
            sleep(1)

            month_picker_option = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='rmdp-ym']//span[text()='{month_name}']")))
            month_picker_option.click()
            sleep(5)
            day_picker_option = driver.find_element(By.XPATH, f"//span[text()='{day}']")
            day_picker_option.click()
            sleep(4)
        except Exception as e:
            print(f"day selection failed: {e}")

        driver.find_element(By.XPATH, '//*[@id="finance"]/div[1]/div[2]/form/div/input').send_keys(data['kcc_loan_sanctioned_amt'])
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="finance"]/div[1]/div[3]/form/div/input').send_keys(data['kcc_loan_drawing_limit_curr_fy'])
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="finance"]/div[2]/div/div/button[2]').click()
        sleep(2)

        agri_crop = driver.find_element(By.XPATH, '//*[@id="activity"]/div/div[1]/div/div/button[1]')
        agri_crop.click()

        driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[1]/div[1]/form/div/input').send_keys(data['activity_loan_sanction_amt'])
        sleep(2)

        crop = driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/form/div/select')
        crop.send_keys('w')
        crop.send_keys(Keys.ENTER)
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[3]/form/div/input').send_keys(data['activity_survey_no'])
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[4]/form/div/input').send_keys(data['activity_khata_no'])
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[5]/form/div/input').send_keys(data['activity_land_area'])
        sleep(2)

        land_type = driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[6]/form/div/select')
        land_type.send_keys(data['activity_land_type'])
        sleep(1)
        land_type.send_keys(Keys.ENTER)
        sleep(2)

        season = driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[7]/form/div/select')
        season.send_keys(data['activity_season'])
        season.send_keys(Keys.ENTER)
        sleep(5)

        select_address = driver.find_element(By.XPATH, '//*[@id="cropHusbandry"]/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/a')
        select_address.click()
        sleep(3)

        sub_district = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[1]/div[3]/div/form/div/select')
        sub_district.click()
        sub_district.send_keys(data['resSubDistrictId'])
        sub_district.send_keys(Keys.ENTER)
        sleep(3)

        village = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[1]/div[4]/div/form/div/select')
        village.click()
        village.send_keys(data['resVillageId'])
        village.send_keys(Keys.ENTER)
        sleep(2)

        proceed_button = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div[2]/div/button')
        proceed_button.click()
        sleep(2)

        submit_button = driver.find_element(By.XPATH, '//*[@id="activity"]/div/div[3]/div/button[3]')
        submit_button.click()
        sleep(2)

        preview_button = driver.find_element(By.XPATH, '//*[@id="formTabs-tabpane-5"]/div/div[2]/div/div/button')
        preview_button.click()
        sleep(2)

        submit_button2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/button')
        submit_button2.click()
        sleep(2)

        cunfirm_button = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/button[2]')
        cunfirm_button.click()
        sleep(2)

        ok_button = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/button')
        ok_button.click()
    except Exception as e:
        print(f"Error in loan application form: {e}")

def extract_and_append_data(csv_file):
    try:
        # Wait for the success message after submission
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h4.pt-4"))  # Update the CSS selector as per the actual success message element
        ).text
        print(f"Success Message: {success_message}")  # For debugging purposes

        # Extract the loan application ID from the success message
        loan_application_id = success_message.split()[2]  # Assuming the ID is the third word in the message
        print(f"Loan Application ID: {loan_application_id}")  # For debugging purposes

        # Prepare the data to append in the CSV
        new_data = {'status_detail': 'submitted successfully', 'loan_application_id': loan_application_id}

        # Append the data to the CSV file
        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['status_detail', 'loan_application_id'])

            # If the CSV is empty, write the header first
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(new_data)

        print("Data successfully written to CSV")

    except Exception as e:
        print(f"Error extracting application ID or writing to CSV: {e}")



def process_csv(file):
    with open(file, newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        skip_first_task = False
        for row in data:
            if fill_form():
                loan_application(row, skip_first_task)
                extract_and_append_data(file)
                skip_first_task = True

# Main Execution
file = 'data.csv'
process_csv(file)
