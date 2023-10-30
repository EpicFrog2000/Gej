from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def extract_numeric_value(text):
    # Remove any non-numeric characters and spaces from the text
    numeric_text = ''.join(filter(str.isdigit, text))
    return int(numeric_text)

class Bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new') just does not work on this site maybe make it diffrent way someday
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('log-level=3')
        options.add_argument("--incognito")
        options.add_argument("--pageLoadStrategy=eager")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-features=NetworkService")
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-default-apps')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-remote-fonts')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-renderer-backgrounding')
        options.add_argument('--disable-component-extensions-with-background-pages')
        options.add_argument("--disable-javascript")

        self.bot = webdriver.Chrome(options=options)
        url = 'https://pl.indeed.com/q-it-oferty-pracy.html?l=Polska'
        self.bot.get(url)
        self.bot.maximize_window()
        self.data = ["0"] * 18

    def get_data(self):
        #tryb
        trybButton = self.bot.find_element(By.ID, 'filter-remotejob')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-remotejob-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            if "Hybrydowo" in inner_html:
                self.data[0] = extract_numeric_value(inner_html)
            else:
                self.data[1] = extract_numeric_value(inner_html)                
        #wynagrodzenie
        trybButton = self.bot.find_element(By.ID, 'filter-salary-estimate')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-salary-estimate-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        wynagrodzenie = []
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            
            parts = inner_html.split(".")
            kwota = re.sub(r'\D', '', parts[0])
            ilosc = re.sub(r'\D', '', parts[1])
            wynagrodzenie.append([kwota, ilosc])
        self.data[2] = wynagrodzenie
        #wymiar pracy
        trybButton = self.bot.find_element(By.ID, 'filter-jobtype')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-jobtype-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            if "Pełny etat" in inner_html:
                parts = inner_html.split("(")
                self.data[3] = extract_numeric_value(parts[1])
            elif "Stała" in inner_html:
                parts = inner_html.split("(")
                self.data[4] = extract_numeric_value(parts[1])
            elif "Podwykonawstwo" in inner_html:
                parts = inner_html.split("(")
                self.data[5] = extract_numeric_value(parts[1])  
            elif "Staż/Praktyka" in inner_html:
                parts = inner_html.split("(")
                self.data[6] = extract_numeric_value(parts[1])  
            elif "Tymczasowa" in inner_html:
                parts = inner_html.split("(")
                self.data[7] = extract_numeric_value(parts[1])
            elif "Część etatu" in inner_html:
                parts = inner_html.split("(")
                self.data[8] = extract_numeric_value(parts[1])
            elif "Wolontariat" in inner_html:
                parts = inner_html.split("(")
                self.data[9] = extract_numeric_value(parts[1]) 
        #wykrztałcenie
        trybButton = self.bot.find_element(By.ID, 'filter-taxo1')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-taxo1-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            if "Średnie techniczne/branżowe" in inner_html:
                parts = inner_html.split("(")
                self.data[10] = extract_numeric_value(parts[1])
            elif "Magister" in inner_html:
                parts = inner_html.split("(")
                self.data[11] = extract_numeric_value(parts[1])
            elif "Inżynier" in inner_html:
                parts = inner_html.split("(")
                self.data[12] = extract_numeric_value(parts[1])  
            elif "Średnie" in inner_html:
                parts = inner_html.split("(")
                self.data[13] = extract_numeric_value(parts[1])  
            elif  "Licencjat" in inner_html:
                parts = inner_html.split("(")
                self.data[14] = extract_numeric_value(parts[1])
            elif "Doktor" in inner_html:
                parts = inner_html.split("(")
                self.data[15] = extract_numeric_value(parts[1])
            elif "Zasadnicze zawodowe/branżowe" in inner_html:
                parts = inner_html.split("(")
                self.data[16] = extract_numeric_value(parts[1])
            elif "Podstawowe" in inner_html:
                parts = inner_html.split("(")
                self.data[17] = extract_numeric_value(parts[1])
        #Lokalizacja
        trybButton = self.bot.find_element(By.ID, 'filter-loc')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-loc-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        list_temp = []
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            parts = inner_html.split("(")
            data_temp = ['', '0']  # Create a new data_temp list for each iteration
            data_temp[1] = extract_numeric_value(parts[1])
            partssecondary = parts[0].split(",")
            if len(partssecondary) > 1:
                data_temp[0] = partssecondary[0]
            else:
                data_temp[0] = parts[0]
            list_temp.append(data_temp)
        self.data.append(list_temp)
        #firma
        trybButton = self.bot.find_element(By.ID, 'filter-fcckey')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-fcckey-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        list_temp = []
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            parts = inner_html.split("(")
            data_temp = ['', '0']
            data_temp[1] = extract_numeric_value(parts[1])
            partssecondary = parts[0].split(",")
            if len(partssecondary) > 1:
                data_temp[0] = partssecondary[0]
            else:
                data_temp[0] = parts[0]
            list_temp.append(data_temp)
        self.data.append(list_temp)
        #język oferty
        trybButton = self.bot.find_element(By.ID, 'filter-lang')
        trybButton.click()
        ul_element = self.bot.find_element(By.ID, "filter-lang-menu")
        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        for li in li_elements:
            a_element = li.find_element(By.TAG_NAME, "a")
            inner_html = a_element.get_attribute("innerHTML")
            if "English" in inner_html:
                parts = inner_html.split("(")
                self.data.append(extract_numeric_value(parts[1]))
            elif "Polski" in inner_html:
                parts = inner_html.split("(")
                self.data.append(extract_numeric_value(parts[1]))
            #maybe add other someday
        #ilosc ofert
        count_element = self.bot.find_element(By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount')
        span = count_element.find_element(By.TAG_NAME, 'span')
        span_innerhtml = span.get_attribute("innerHTML")
        self.data.append(extract_numeric_value(span_innerhtml))
        
        # add management lvl someday
