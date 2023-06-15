import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import dotenv_values

# Rest of your code here
import requests



# Benutzername und Passwort für die Anmeldung
# Lade die Benutzername und Passwort aus der .env-Datei
config = dotenv_values(".env")
username = config["USERNAME"]
password = config["PASSWORD"]
# URL der Website, auf der du dich einloggen möchtest
login_url = config["LOGIN_URL"]
noti_url = config["NOTI_URL"]


def job(previous_dataa):
    # Initialisierung des Webtreibers (Chrome)
    chrome_options = Options()
    chrome_options.headless = True  # Deaktiviert den Headless Mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.experimental_options["prefs"] = chrome_prefs = {}
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    driver = webdriver.Chrome(options=chrome_options)

    # Öffnen der Login-Seite
    if login_url is not None:
        driver.get(login_url)

    # Eingabe des Benutzernamens und Passworts und Absenden des Formulars
    username_field = driver.find_element(By.ID, "user")
    password_field = driver.find_element(By.ID, "passwort")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    # Warten, bis die Anmeldung abgeschlossen ist und die Daten-Seite geladen wurde
    driver.implicitly_wait(10)  # Warte maximal 10 Sekunden

    link = driver.find_element(By.ID, "menu21311")
    link.click()
    # wait for page to load
    driver.implicitly_wait(10)  # Warte maximal 10 Sekunden

    # get tbody element by tag name
    tbody = driver.find_element(By.TAG_NAME, "tbody")

    # Finde alle Zeilen im tbody-Element die direkt unter dem tbody-Element sind
    rows = tbody.find_elements(By.XPATH, "./tr")
    
    # check if the rows have the style attribute display: none; and remove them
    for row in rows:
        if row.get_attribute("style") == "display: none;":
            rows.remove(row)

    data = []
    # Iteriere über alle Zeilen
    for row in rows:
        # Finde alle Spalten in der aktuellen Zeile
        columns = row.find_elements(By.TAG_NAME, "td")
        # Erstelle eine leere Liste für die Spalten
        row_data = []
        # Iteriere über alle Spalten
        for column in columns:
            # Füge den Text der Spalte zur Liste hinzu
            row_data.append(column.text)

        data.append(row_data)

        # replace /n with space
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = data[i][j].replace("\n", " ")


    # delete all arrays with length 0
    data = [x for x in data if len(x) != 0]
    # delete all arrays with length 1
    data = [x for x in data if len(x) != 1]

    # compare data with previous data
    print(data)
    print(previous_data)

    min_length = min(len(data), len(previous_data))

    if previous_data != "":
        # check wich array is different
        for i in range(min_length):
            if data[i] != previous_data[i]:
                # send request to server with data
                
                
                url = noti_url

                payload = json.dumps(
                    {
                        "value1": data[i][0],
                        "value2": data[i][1],
                    }
                )
                headers = {"Content-Type": "application/json"}

                print(payload)

                if url is not None:
                    response = requests.request("POST", url, headers=headers, data=payload)

                    if response.status_code == 200:
                        print("Webanfrage erfolgreich durchgeführt.")
                    else:
                        print("Fehler bei der Webanfrage:", response.status_code)

        if len(data) > len(previous_data):
            for i in range(min_length, len(data)):
                
                url = noti_url

                payload = json.dumps(
                    {
                        "value1": data[i][0],
                        "value2": data[i][1],
                    }
                )
                headers = {"Content-Type": "application/json"}

                print(payload)
                if url is not None:
                    response = requests.request("POST", url, headers=headers, data=payload)

                    if response.status_code == 200:
                        print("Webanfrage erfolgreich durchgeführt.")
                    else:
                        print("Fehler bei der Webanfrage:", response.status_code)  
    # Schließen des Webtreibers
    driver.quit()
    return data


previous_data = []
# Endlosschleife zum Ausführen des Zeitplans
while True:
    previous_data = job(previous_data)  
    time.sleep(60 * 10)  # Warte 10 Minuten (600 Sekunden)
