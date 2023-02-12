from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Chromedriver/chromedriver.exe')
driver.get("https://app.bluealert.pl/ba/form/formularz-testowy")

first_name = driver.find_element(By.ID, "id_first_name")
first_name.send_keys("Test")

last_name = driver.find_element(By.ID, "id_last_name")
last_name.send_keys("Tester")

email = driver.find_element(By.ID, "id_email")
email.send_keys("test@test.pl")

phone = driver.find_element(By.ID, "id_phone")
phone.send_keys("285190593")

pesel = driver.find_element(By.ID, "id_pesel")
pesel.send_keys("00210199932")

id_number = driver.find_element(By.ID, "id_id_numer")
id_number.send_keys("LAF423036")

birth_date = driver.find_element(By.ID, "id_date")
birth_date.send_keys("2000-01-01")

datepicker = driver.find_element(By.CLASS_NAME, "datepicker")
driver.execute_script("arguments[0].style.visibility='hidden'", datepicker)

next_button = driver.find_element(by="id", value="form_button_next")
next_button.click()

input("Press Enter to quit")