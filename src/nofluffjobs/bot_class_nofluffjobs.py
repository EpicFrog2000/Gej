from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

key_words_doswiadczenie = {
"Doświadczenie",
"doświadczenia",
"doświadczenie",
"experience",
"Experience",
}

def extract_numeric_value(text):
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    if result:
        return int(result)
    else:
        return None

def extract_number(input_string):
    pattern = r'[-+]?\s*\d+(?:[-+]\d*)?'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None

class Bot:
    def __init__(self):
        ##print("\rInitiation", end="")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
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
        self.obecna_strona = 1
        url = 'https://nofluffjobs.com/?criteria=country%3Dpolska&page=' + str(self.obecna_strona)
        self.bot.get(url)
        self.bot.maximize_window()
        self.linki_do_oferty = []
        self.tymczasowe_dane_jednej_oferty = []
        self.dane_z_ofert_stron = []
        
        self.bot.wszystkie_dane_ofert = []
        
    def kliknij_przycisk_ciasteczka(self):
        ##print("\rClicking cookies button", end="")
        try:
            button = WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
            button.click()
        except:
            ##print("Error occurred while clicking cookies button")
            pass
    
    def get_all_sites_nums(self):
        ##print("\rGetting nums of all sites", end="")
        try:
            ul_element = self.bot.find_element(By.CSS_SELECTOR, 'ul.pagination')
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
            last_item = li_elements[-2]
            link_element = last_item.find_element(By.TAG_NAME, 'a')
            numer_stron_sesji = link_element.get_attribute("innerHTML")
            return int(numer_stron_sesji)
        except:
            ##print("\rError getting number of all sites", end="")
            pass

    def get_linki_from_current_site(self):
        self.dane_z_ofert_stron = []
        ##print("\rGet_linki_from_current_site", end="")
        try:
            self.linki_do_oferty.clear()
            all_div = self.bot.find_element(By.CLASS_NAME, "list-container.ng-star-inserted")
            all_offers = all_div.find_elements(By.CLASS_NAME, "posting-list-item")
            for offer in all_offers:
                self.linki_do_oferty.append(offer.get_attribute("href"))
        except:
            ##print("\r Error get_linki_from_current_site", end="")
            pass
            
    
    def get_data_from_offers(self):
        iterator = 1
        count = len(self.linki_do_oferty)
        ##print("r\get_data_from_offers", end="")
        self.tymczasowe_dane_jednej_oferty = [""] * 8
        for link_do_oferty in self.linki_do_oferty:
            #print('\r' + ' ' * 150 + '\r', end='', flush=True)
            msg = f"\r" + "Obecnie zbiera dane z:" + str(iterator) + " / " + str(count) + " " + str(link_do_oferty)
            #print(msg, end ="", flush=True)
            iterator +=1
            try:
                ##print("r\going to offer site", link_do_oferty, end="")
                self.bot.get(link_do_oferty)
            except:
                continue
            # company
            try:
                ##print("r\getting title", end="")
                company_div = self.bot.find_element(By.ID, "postingCompanyUrl")
                company_pre_format = company_div.get_attribute("innerHTML")
                company = company_pre_format.split("<")
                if len(company) > 1:
                    self.tymczasowe_dane_jednej_oferty[0] = company[0].strip()
                else:
                    self.tymczasowe_dane_jednej_oferty[0] = company_pre_format.strip()
            except:
                pass
            # category
            try:
                ##print("r\getting category", end="")
                category_div = self.bot.find_element(By.CSS_SELECTOR, 'a[data-cy="JobOffer_Category"]')
                self.tymczasowe_dane_jednej_oferty[1] = category_div.get_attribute("innerHTML").strip()
            except:
                pass
            # seniority
            try:
                ##print("r\getting seniority", end="")
                div = self.bot.find_element(By.ID, "posting-seniority")
                lvl_span = div.find_element(By.TAG_NAME, "span")
                self.tymczasowe_dane_jednej_oferty[2] = lvl_span.get_attribute("innerHTML").strip()
            except:
                pass
            # must have
            try:
                ##print("r\getting must have", end="")
                temp_wymagania = []
                element = self.bot.find_element(By.XPATH, '//section[@branch="musts" and @class="d-block"]')
                ul = element.find_element(By.TAG_NAME, "ul")
                li = ul.find_elements(By.TAG_NAME, "li")
                for elem in li:
                    try:
                        span_element = elem.find_element(By.TAG_NAME, "span")
                        temp_wymagania.append(span_element.text.strip())
                    except:
                        continue
                self.tymczasowe_dane_jednej_oferty[3] = temp_wymagania
            except:
                self.tymczasowe_dane_jednej_oferty[3] = []
                pass
            #Nice to have
            try:
                ##print("r\getting Nice to have", end="")
                temp_wymagania = []
                element = self.bot.find_element(By.XPATH, '//section[@branch="nices" and @class="d-block mt-3 ng-star-inserted"]')
                ul = element.find_element(By.TAG_NAME, "ul")
                li = ul.find_elements(By.TAG_NAME, "li")
                for elem in li:
                    try:
                        span_element = elem.find_element(By.TAG_NAME, "span")
                        temp_wymagania.append(span_element.text.strip())
                    except:
                        continue
                self.tymczasowe_dane_jednej_oferty[4] = temp_wymagania
            except:
                self.tymczasowe_dane_jednej_oferty[4] = []
                pass
            #Got tired, ide spać zzz...
            #salary
            try:
                ##print("r\getting salary", end="")
                elem = self.bot.find_element(By.CLASS_NAME, "salary.ng-star-inserted")
                salary_elem = elem.find_element(By.TAG_NAME, "h4")
                parts = salary_elem.get_attribute("innerHTML").split("–")
                if len(parts) > 1:
                    self.tymczasowe_dane_jednej_oferty[5] = extract_numeric_value(parts[0])
                else:
                    self.tymczasowe_dane_jednej_oferty[5] = extract_numeric_value(salary_elem.get_attribute("innerHTML"))
            except:
                pass
            # lokacje
            try:
                ##print("r\getting lokacje", end="")
                temp_locations = []
                ul = self.bot.find_element(By.CLASS_NAME, "locations-compact")
                li_elements = ul.find_elements(By.TAG_NAME, "li")
                for elem in li_elements:
                    if(elem.text != ""):
                        result_string = elem.text.split('+')[0].split(',')[0].strip()
                        temp_locations.append(result_string)
                self.tymczasowe_dane_jednej_oferty[6] = temp_locations
            except:
                self.tymczasowe_dane_jednej_oferty[6] = []
                pass
            
            self.bot.wszystkie_dane_ofert.append(self.tymczasowe_dane_jednej_oferty.copy())
            # experience
            try:
                ##print("r\getting experience", end="")
                found = False 
                element = self.bot.find_element(By.CLASS_NAME, "d-block.border-top.ng-star-inserted")
                inner_elem = element.find_element(By.CLASS_NAME, "p-20")
                inner_elem = inner_elem.find_element(By.CLASS_NAME, "font-weight-normal.ng-star-inserted")
                inner_elem = inner_elem.find_element(By.CLASS_NAME, "tw-overflow-hidden.ng-star-inserted")
                uls = inner_elem.find_elements(By.TAG_NAME, "ul")
                for ul in uls:
                    if found:
                        break
                    li_elements = ul.find_elements(By.TAG_NAME, "li")
                    for li in li_elements:
                        if found:
                            break
                        for keyword in key_words_doswiadczenie:
                            if found:
                                break
                            if keyword in li.text:
                                if found:
                                    break
                                match = re.search(r'[-+]?\s*\d+(?:[-+]\d*)|\b\d+\b', li.text)
                                if match:
                                    if found:
                                        break
                                    result = match.group()
                                    result = int(result.replace(' ', '').replace('+', '').replace('-', ''))
                                    if result is not None and result < 16:
                                        if found:
                                            break
                                        found = True
                                        self.tymczasowe_dane_jednej_oferty[7] = result
                                        break
            except:
                self.tymczasowe_dane_jednej_oferty[7] = ""
                pass
            self.dane_z_ofert_stron.append(self.tymczasowe_dane_jednej_oferty.copy())
            ###print("dane_z_ofert_stron: ",self.dane_z_ofert_stron)# company
            #input("")
            ###print("company: ", self.tymczasowe_dane_jednej_oferty[0])# company
            ###print("category: ", self.tymczasowe_dane_jednej_oferty[1])# category
            ###print("seniority: ", self.tymczasowe_dane_jednej_oferty[2])# seniority
            ###print("must have: ", self.tymczasowe_dane_jednej_oferty[3])# must have
            ###print("Nice to have: ", self.tymczasowe_dane_jednej_oferty[4])# Nice to have
            ###print("salary: ", self.tymczasowe_dane_jednej_oferty[5])# salary
            ###print("lokacje: ", self.tymczasowe_dane_jednej_oferty[6])# lokacje
            ###print("doswiadczenie: ", self.tymczasowe_dane_jednej_oferty[7])# doswiadczenie
    def go_next_site(self):
        ##print("r\going to next sites", end="")
        self.obecna_strona += 1
        url = 'https://nofluffjobs.com/?criteria=country%3Dpolska&page=' + str(self.obecna_strona)
        self.bot.get(url)
        