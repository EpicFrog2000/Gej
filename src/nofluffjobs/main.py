from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Bot:
    def __init__(self):
        print("\rInitiation", end="")
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
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
        
    def kliknij_przycisk_ciasteczka(self):
        print("\rClicking cookies button", end="")
        try:
            button = WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
            button.click()
        except NoSuchElementException as e:
            print(f"\rError occurred while clicking cookies button: {e}")
            pass
    
    def get_all_sites_nums(self):
        print("\rGetting nums of all sites", end="")
        try:
            ul_element = self.bot.find_element(By.CSS_SELECTOR, 'ul.pagination')
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
            last_item = li_elements[-2]
            link_element = last_item.find_element(By.TAG_NAME, 'a')
            numer_stron_sesji = link_element.get_attribute("innerHTML")
            return int(numer_stron_sesji)
        except:
            print("\r Error getting number of all sites", end="")
            pass

    def get_linki_from_current_site(self):
        print("\r get_linki_from_current_site", end="")
        try:
            self.linki_do_oferty.clear()
            all_div = self.bot.find_element(By.CLASS_NAME, "list-container.ng-star-inserted")
            all_offers = all_div.find_elements(By.CLASS_NAME, "posting-list-item")
            for offer in all_offers:
                self.linki_do_oferty.append(offer.get_attribute("href"))
        except:
            print("\r Error get_linki_from_current_site", end="")
            pass
            
    
    def get_data_from_offers(self):
        self.bot.tymczasowe_dane_jednej_oferty = []
        for link_do_oferty in self.linki_do_oferty:
            try:
                self.bot.get(link_do_oferty)
            except:
                continue
            # company
            try:
                company_div = self.bot.find_element(By.ID, "postingCompanyUrl")
                self.bot.tymczasowe_dane_jednej_oferty.append(company_div.get_attribute("innerHTML"))
            except:
                
                pass
            # category
            try:
                category_div = self.bot.find_element_by_css_selector('a[data-cy="JobOffer_Category"]')
                self.bot.tymczasowe_dane_jednej_oferty.append(category_div.get_attribute("innerHTML"))
            except:
                self.bot.tymczasowe_dane_jednej_oferty.append("")
                pass
            # seniority
            try:
                div = self.bot.find_element(By.ID, "posting-seniority")
                lvl_span = div.find_element(By.TAG_NAME, "span")
                self.bot.tymczasowe_dane_jednej_oferty.append(lvl_span.get_attribute("innerHTML"))
            except:
                self.bot.tymczasowe_dane_jednej_oferty.append("")
                pass
            # must have
            try:
                temp_wymagania = []
                element = self.bot.find_element_by_css_selector('section[commonpostingrequirements][branch="musts"]')
                ul = element.find_element(By.CLASS_NAME, "mb-0.ng-star-inserted")
                li = ul.find_elements(By.TAG_NAME, "li")
                for elem in li:
                    span_element = elem.find_element(By.TAG_NAME, "span")
                    temp_wymagania.append(span_element.get_attribute("innerHTML"))
                self.bot.tymczasowe_dane_jednej_oferty.append(temp_wymagania)
            except:
                self.bot.tymczasowe_dane_jednej_oferty.append([])
                pass
            #Nice to have
            
            #Got tired, ide spać zzz...
        
bot = Bot()
bot.kliknij_przycisk_ciasteczka()
numer_stron_sesji = bot.get_all_sites_nums()
bot.get_linki_from_current_site()
bot.get_data_from_offers()
