import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.get("https://fasalrin.gov.in/")
driver.maximize_window()

def fill_form():
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[1]'))).click()
    except Exception as e:
        print(f"Error with clicking dropdown:{e}")
   
    try :
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/section/div/div/div/div[1]/div/div[1]/div[2]/span/i'))).click()
    except Exception as e:
        print(f"Error with clicking submenu link:{e}")

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/section/div/div/div/div[2]/div/form/div/input').send_keys("9887784666")
    sleep(2)

    driver.find_element(By.XPATH,'//*[@id="slide-pass"]/div[1]/form/div/input').send_keys("9887784666")
    sleep(20)
 
fill_form()
def loan_application(data, skip_first_task=False):

    try:
        if not skip_first_task:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div[2]/div[5]/button/span'))).click()
                sleep(1)
            except TimeoutExeption: # type: ignore
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

        driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/input').send_keys(data['Adhar *'])
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div[2]/div/div/div/div[3]/div/div[2]/button').click()
        sleep(1)

        beneficiary_details = driver.find_element(By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[1]/form/div/select')
        sleep(1)

        beneficiary_details.click()
        sleep(1)
        beneficiary_details.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        beneficiary_details.send_keys(Keys.ENTER)
        sleep(4)

        ok_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="iss-wrapper"]/div[3]/div/div/div/div/div/div[3]/button[2]')))
        ok_button.click()
        sleep(2)

    except Exception as e:
        print(f"An error occurred in filling form {e}")

row_count = 0
skip_first_task = False 

while True:
    try:
        with open("data.csv", newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            print("Csv file found and open successfully... ")

            for row in csv_reader:
                loan_application(row, skip_first_task)
                sleep(12)
    
                row_count += 1
                if row_count == 4:
                    print("4 rows processed, stopping the process")
                    break
                skip_first_task = True
            if row_count == 4:
                break

    except FileNotFoundError:
        print("File not found, Please check the file path...")
        break
    except Exception as e:
        print(f"An error occurred {e}")


# driver.quit()
