from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import html

def extract_numeric_value(text):
    # Remove any non-numeric characters and spaces from the text
    numeric_text = ''.join(filter(str.isdigit, text))
    return int(numeric_text)

class Bot:
    def __init__(self):
        # WebDriver setup to avoid detection
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--incognito")
        desired_version = "114.0.5735.90"  # Replace with the desired version, or wait for chromedriver to update
        self.bot = webdriver.Chrome(service=Service(ChromeDriverManager(version=desired_version).install()), options=options)
        self.bot.get("https://it.pracuj.pl/")
        self.bot.maximize_window()
        self.current_site = 1
        self.linki_do_oferty = []
        self.dane_oferty = []

    def click_button_acc(self):
        WebDriverWait(self.bot, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql"))
        )
        button = self.bot.find_element(By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql")
        button.click() 
          
    def get_site_ready(self):
        WebDriverWait(self.bot, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='ContentBoxstyles__Wrapper-']"))
        )
        WebDriverWait(self.bot, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']"))
        )
        
    # Pobiera ile jest stron z ofertami
    def get_all_sites_nums(self):
        WebDriverWait(self.bot, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']"))
        )
        ul_element = self.bot.find_element(By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']")
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        last_item = li_elements[-2]
        link_element = last_item.find_element(By.TAG_NAME, 'a')
        numer_stron_sesji = link_element.get_attribute("innerHTML")
        return numer_stron_sesji
    
    # Pobieranie danych na temat ofert
    def get_data(self):
        oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div.ContentBoxstyles__Wrapper-sc-11jmnka-0.jevXWE.JobOfferstyles__ContentBoxWrapper-sc-1rq6ue2-0')
        self.id_oferty = 0
        self.linki_do_oferty = [None] * len(oferty)

        # Pobierz linki ofert
        for oferta in oferty:
            try:
                button = oferta.find_element(By.CLASS_NAME, 'JobOfferstyles__TitleButton-sc-1rq6ue2-5.HPWqN')
                button.click()
                href_element = oferta.find_element(By.CLASS_NAME, 'OfferLocationsListstyles__LocationsItemLink-sc-b1eixg-2.ZUWyH')
                href = href_element.get_attribute("href")
                self.linki_do_oferty[self.id_oferty] = href
            except NoSuchElementException:
                offer_link_element = oferta.find_element(By.CSS_SELECTOR, 'a[data-test="offer-link"]')
                link_text = offer_link_element.get_attribute("href")
                if link_text is not None:
                    self.linki_do_oferty[self.id_oferty] = link_text
            self.id_oferty += 1
        self.id_oferty = 0
        
        # Pobierz dane z linków do ofert
        for oferta in self.linki_do_oferty:
            if oferta is not None:
                self.bot.get(str(oferta))
                inner_data = [None] * 12
                # getting data
                # title?
                try:
                    title = self.bot.find_element(By.CSS_SELECTOR, 'h1.offer-viewkHIhn3[data-test="text-positionName"][data-scroll-id="job-title"]')
                    inner_data[0] = title.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # company?
                try:
                    company = self.bot.find_element(By.CSS_SELECTOR, 'h2.offer-viewwtdXJ4[data-test="text-employerName"]')
                    company = company.get_attribute("innerHTML")
                    index_of_first_less_than = company.find("<")
                    company = company[:index_of_first_less_than].strip()
                    inner_data[1] = company
                except NoSuchElementException:
                    pass
                # location?
                try:
                    location = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewqtkGPu[data-test="text-benefit"]')
                    inner_data[2] = location.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # management_level?
                try:
                    management_level = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-employment-type-name-text"]')
                    inner_data[3] = management_level.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # salary?
                try:
                    salary = self.bot.find_element(By.CSS_SELECTOR, "strong[data-test='text-earningAmount']")
                    salary_from = salary.find_element(By.CSS_SELECTOR, 'span[data-test="text-earningAmountValueFrom"]')
                    salary_to = salary.find_element(By.CSS_SELECTOR, 'span[data-test="text-earningAmountValueTo"]')
                    salary_from = extract_numeric_value(html.unescape(salary_from.get_attribute("innerHTML")))
                    salary_to = extract_numeric_value(html.unescape(salary_to.get_attribute("innerHTML")))
                    inner_data[4] = salary_from
                    inner_data[5] = salary_from
                except NoSuchElementException:
                    pass 
                # tryb_pracy?
                try:
                    tryb_pracy = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-modes-text"]')
                    inner_data[6] = tryb_pracy.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # etat?
                try:
                    etat = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-schedule-text"]')
                    inner_data[7] = etat.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # kontrakt?
                try:
                    kontrakt = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-contracts-text"]')
                    inner_data[8] = kontrakt.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # specjalizacja?
                try:
                    specjalizacja = self.bot.find_element(By.CSS_SELECTOR, 'span.offer-viewPFKc0t')
                    inner_data[9] = specjalizacja.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # technologie_wymagane?
                try:
                    div_wymagane = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="technologies-expected-1"][data-test="section-technologies-expected"]')
                    lista = div_wymagane.find_element(By.CSS_SELECTOR, "[class^='offer-viewEX0Eq-']")
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    self.wymagane = [] * len(li_elements)
                    for element in li_elements:
                        link_element = element.find_element(By.TAG_NAME, 'p')
                        inner_html = link_element.get_attribute("innerHTML")
                        self.wymagane.append(inner_html)
                    inner_data[10] = self.wymagane
                except NoSuchElementException:
                    pass
                # technologie mile widziane?
                try:
                    div_optional = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="technologies-optional-1"][data-test="section-technologies-optional"]')
                    lista = div_optional.find_element(By.CSS_SELECTOR, "[class^='offer-viewEX0Eq-']")
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    self.mile_widziane = [] * len(li_elements)
                    for element in li_elements:
                        link_element = element.find_element(By.TAG_NAME, 'p')
                        inner_html = link_element.get_attribute("innerHTML")
                        self.mile_widziane.append(inner_html)
                    inner_data[11] = self.mile_widziane
                except NoSuchElementException:
                    pass
                # doswiadczenie?
                # studia/wykrztalcenie?
                try:
                    div_doswiadczenie = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="requirements-expected-1"][data-test="section-requirements-expected"]')
                    lista = div_doswiadczenie.find_element(By.CSS_SELECTOR, '[class^="offer-view6lWuAT"]')
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    for paragraf in li_elements:
                        text = paragraf.find_element(By.TAG_NAME, 'p')
                        inner_html = text.get_attribute("innerHTML")
                        # Prawdopodobnie trzeba przędzie patrzeć czy w jakimś paragrawfie jest x słowo/a z naszego zbioru i jesli jest to pobrac i jakos to zformatowac do jednego słowa lub cyfry na paragraf
                        #TODO: FINISH THIS SHIT
                except NoSuchElementException:
                    pass
                #
                #
                # PAIN
                self.dane_oferty.append(inner_data)
        del self.linki_do_oferty[:]

    def go_to_next_site(self):
        self.current_site += 1
        self.bot.get("https://it.pracuj.pl/?pn=" + str(self.current_site))
        self.get_site_ready()

bot = Bot()
bot.get_site_ready()
bot.click_button_acc()
numer_stron_sesji = bot.get_all_sites_nums()
print("title, company, location, management_level, salary, tryb_pracy, etat, kontrakt, specjalizacja, technologie_wymagane[LISTA], technologie_mile_widziane[LISTA],") #Will be more data later
while int(bot.current_site) < int(numer_stron_sesji):
    bot.get_data()
    
    #print data every like 19 offers
    for inner_list in bot.dane_oferty:
        for item in inner_list:
            print(item, end=' ')
        print()

    bot.go_to_next_site()
#input(" ")
