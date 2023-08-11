from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import html
import re

key_words_doswiadczenie = {
"doświadczenia",
"doświadczenie",
"experience",
}

def extract_number(input_string):
    pattern = r'\d+'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None

def extract_numeric_value(text):
    # Remove any non-numeric characters and spaces from the text
    numeric_text = ''.join(filter(str.isdigit, text))
    return int(numeric_text)

class Bot:
    def __init__(self):
        print("\rInitiation", end="")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920x1080')
        options.add_argument("--incognito")
        #options.add_argument("pageLoadStrategy=eager")
        self.bot = webdriver.Chrome(options=options)
        self.current_site = 1
        url = 'https://it.pracuj.pl/?pn=' + str(self.current_site)
        self.bot.get(url)
        self.bot.execute_script("return document.readyState")
        self.linki_do_oferty = []
        self.dane_oferty = []
        self.retry = False
           
    def click_button_acc(self):
        print("\rClicking cookies button", end="")
        try:
            button = WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='size-medium variant-primary cookies_b1fqykql']")))
            button.click()
        except NoSuchElementException as e:
            print(f"\rError occurred while clicking cookies button: {e}")
            pass
        
    # Pobiera ile jest stron z ofertami
    def get_all_sites_nums(self):
        print("\rGetting nums of all sites", end="")
        try:
            div = WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Paginatorstyles__Wrapper-sc-1ur9l1s-0.dDposH')))
            ul_element = div.find_element(By.CSS_SELECTOR, 'ul.pagination')
            li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
            last_item = li_elements[-2]
            link_element = last_item.find_element(By.TAG_NAME, 'a')
            numer_stron_sesji = link_element.get_attribute("innerHTML")
            return int(numer_stron_sesji)
        except Exception as e:
            print("\rError occurred while getting the number of pages")
            pass
    
    # Pobieranie danych na temat ofert
    def get_data(self,numer_stron_sesji):
        print("\rGetting data", end="")
        self.dane_oferty.clear()
        oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div.ContentBoxstyles__Wrapper-sc-11jmnka-0.jevXWE.JobOfferstyles__ContentBoxWrapper-sc-1rq6ue2-0')
        self.id_oferty = 0
        self.linki_do_oferty = [''] * len(oferty)
        print("\rGetting offer links", end="")
        for oferta in oferty:
            # Pobierz linki ofert
            unique_links = set()
            try:
                button = oferta.find_element(By.CLASS_NAME, 'JobOfferstyles__TitleButton-sc-1rq6ue2-5.HPWqN')
                button.click()
                href_element = oferta.find_element(By.CLASS_NAME, 'OfferLocationsListstyles__LocationsItemLink-sc-b1eixg-2.ZUWyH')
                href = href_element.get_attribute("href")
                if href not in unique_links:
                    self.linki_do_oferty[self.id_oferty] = href
                    unique_links.add(href)
            except NoSuchElementException:
                offer_link_element = oferta.find_element(By.CSS_SELECTOR, 'a[data-test="offer-link"]')
                link_text = offer_link_element.get_attribute("href")
                if link_text and link_text not in unique_links:
                    self.linki_do_oferty[self.id_oferty] = link_text
                    unique_links.add(link_text)
            self.id_oferty += 1
        self.id_oferty = 0

        # Pobierz dane z linków do ofert
        print("\rStart gathering data from offers", end="")
        total_offers = len(self.linki_do_oferty)

        for index, oferta in enumerate(self.linki_do_oferty, start=1):
            progress_msg = f"Getting data {index} / {total_offers}               "
            print(f"\r{progress_msg}", end="")
            if oferta != '':
                try:
                    self.bot.get(str(oferta))
                    WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.ID, "kansas-offerview")))
                except:
                    continue
                inner_data = [''] * 14
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
                    parts = location.get_attribute("innerHTML").split(", ")
                    if len(parts) > 1:
                        inner_data[2] = parts[0]
                    else:
                        inner_data[2] = location.get_attribute("innerHTML")
                except NoSuchElementException:
                    location = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewUIYWmu[data-test="text-benefit"]')
                    parts = location.get_attribute("innerHTML").split(", ")
                    if len(parts) > 1:
                        inner_data[2] = parts[0]
                    else:
                        inner_data[2] = location.get_attribute("innerHTML")
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
                    #inner_data[5] = salary_to
                except NoSuchElementException:
                    inner_data[4] = 0
                    pass 
                # tryb_pracy?
                try:
                    tryb_pracy = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-modes-text"]')
                    inner_data[5] = tryb_pracy.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # etat?
                try:
                    etat = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-schedule-text"]')
                    inner_data[6] = etat.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # kontrakt?
                try:
                    kontrakt = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-contracts-text"]')
                    inner_data[7] = kontrakt.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # specjalizacja?
                try:
                    specjalizacja = self.bot.find_element(By.CSS_SELECTOR, 'span.offer-viewPFKc0t')
                    inner_data[8] = specjalizacja.get_attribute("innerHTML")
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
                    inner_data[9] = self.wymagane
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
                    inner_data[10] = self.mile_widziane
                except NoSuchElementException:
                    pass
                # doswiadczenie? sucks but kinda works
                # studia/wykrztalcenie? :C
                try:
                    div_doswiadczenie = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="requirements-expected-1"][data-test="section-requirements-expected"]')
                    lista = div_doswiadczenie.find_element(By.CSS_SELECTOR, '[class^="offer-view6lWuAT"]')
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    doswiadczenie = False
                    for paragraf in li_elements:
                        text = paragraf.find_element(By.TAG_NAME, 'p')
                        inner_html = text.get_attribute("innerHTML")
                        if doswiadczenie == False:
                            for keyword in key_words_doswiadczenie:
                                if keyword in str(inner_html):
                                    result = extract_number(inner_html)
                                    if result is not None and int(result) < 16:
                                        inner_data[11] = result # THIS SUCKS
                                        doswiadczenie = True
                                        break
                except NoSuchElementException:
                    pass
                #
                #
                # PAIN
                self.dane_oferty.append(inner_data)
        self.linki_do_oferty.clear()
        
    def go_to_next_site(self):
        try:
            self.retry = False
            print("\rGoint to next site", end="")
            self.current_site += 1
            self.bot.get("https://it.pracuj.pl/?pn=" + str(self.current_site))
            WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Paginatorstyles__Wrapper-sc-1ur9l1s-0.dDposH')))
            self.bot.execute_script("return document.readyState")
        except:
            if(self.retry == False):
                self.retry = True
                self.current_site -= 1
            self.go_to_next_site()
    

    
    