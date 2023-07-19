from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class Bot:
    def __init__(self):
        # WebDriver setup to avoid detection
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--incognito")
        self.bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
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
    # WILL CHANGE LATER BC LOOKS LIKE SHIT
    def get_data(self):
        oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div[class^="ContentBoxstyles__Wrapper-"]')
        self.id_oferty = 0
        self.linki_do_oferty = [None] * len(oferty)
        
        # Pobierz dane z ofert na głównej
        for oferta in oferty:
            inner_html = oferta.get_attribute("innerHTML")
            soup = BeautifulSoup(inner_html, 'html.parser')
            dane = []

            tytul_element = soup.find('h3', attrs={'data-test': 'offer-title'})
            company_name_element = soup.find('span', attrs={'data-test': 'company-name'})
            offer_location_element = soup.find('span', attrs={'data-test': 'offer-location'})
            offer_management_level_element = soup.find('span', attrs={'data-test': 'offer-management-level'})
            date = soup.find('div', class_='JobOfferstyles__FooterText-sc-1rq6ue2-22')
            
            tytul = tytul_element.text if tytul_element else ''
            company = company_name_element.text if company_name_element else ''
            location = offer_location_element.text if offer_location_element else ''
            management_level = offer_management_level_element.text if offer_management_level_element else ''
            p_date = date.text if date else ''
            p_date = p_date.replace("opublikowana: ", "")
            
            if tytul:
                dane = [tytul, company, location, management_level, p_date, None, None, self.id_oferty]
                if soup.find('span', attrs={'data-test': 'offer-salary'}):
                    salary = soup.find('span', attrs={'data-test': 'offer-salary'})
                    dane[6] = salary.text

                # Pobierz tagi
                tagarray = []
                if soup.find('div', attrs={'data-test': 'offer-tags'}):
                    tagi = soup.find('div', attrs={'data-test': 'offer-tags'})
                    inner_html = str(tagi)
                    tag_div = BeautifulSoup(inner_html, 'html.parser')
                    tags = tag_div.find_all(class_="Chipsstyles__Wrapper-sc-17yerqz-0 cShFq JobOfferstyles__ChipsStyled-sc-1rq6ue2-19 dDTkNx")
                    for tag in tags:
                        inner_text = tag.get_text(strip=True)
                        tagarray.append(inner_text)
                    dane[5] = tagarray

                # Pobierz linki do ofert
                try:
                    button = oferta.find_element(By.CLASS_NAME, 'JobOfferstyles__TitleButton-sc-1rq6ue2-5.HPWqN')
                    button.click()
                    href_element = oferta.find_element(By.CLASS_NAME, 'OfferLocationsListstyles__LocationsItemLink-sc-b1eixg-2.ZUWyH')
                    href = href_element.get_attribute("href")
                    self.linki_do_oferty[self.id_oferty] = href
                except NoSuchElementException:
                    offer_link = soup.find('a', attrs={'data-test': 'offer-link'})
                    if offer_link is not None:
                        href = offer_link['href']
                        self.linki_do_oferty[self.id_oferty] = href
                self.dane_oferty.append(dane)
                self.id_oferty += 1
            
        self.id_oferty = 0
        # wejdz w każdy self.linki_do_oferty i pobierz z niego dane i wpierdol do bot.dane_oferty, chce sie zajebać
        # Pobierz dane ze strony oferty
        for oferta in self.linki_do_oferty:
            if oferta is not None:
                self.bot.get(str(oferta))
                inner_data = [None, None, None, None, None, None, None, None]
                # getting data
                # tryb pracy?
                try:
                    tryb_pracy = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-modes-text"]')
                    inner_data[0] = tryb_pracy.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # etat?
                try:
                    etat = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-schedule-text"]')
                    inner_data[1] = etat.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # kontrakt?
                try:
                    kontrakt = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-contracts-text"]')
                    inner_data[2] = kontrakt.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # specjalizacja?
                try:
                    specjalizacja = self.bot.find_element(By.CSS_SELECTOR, 'span.offer-viewPFKc0t')
                    inner_data[3] = specjalizacja.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # technologie wymagane?
                try:
                    div_wymagane = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="technologies-expected-1"][data-test="section-technologies-expected"]')
                    lista = div_wymagane.find_element(By.CSS_SELECTOR, "[class^='offer-viewEX0Eq-']")
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    self.wymagane = [] * len(li_elements)
                    for element in li_elements:
                        link_element = element.find_element(By.TAG_NAME, 'p')
                        inner_html = link_element.get_attribute("innerHTML")
                        self.wymagane.append(inner_html)
                    inner_data[4] = self.wymagane
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
                    inner_data[5] = self.mile_widziane
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
                except NoSuchElementException:
                    pass
                #
                #
                # PAIN
                
        del self.linki_do_oferty[:]

    def go_to_next_site(self):
        self.current_site += 1
        self.bot.get("https://it.pracuj.pl/?pn=" + str(self.current_site))
        self.get_site_ready()
            
bot = Bot()
bot.get_site_ready()
bot.click_button_acc()
numer_stron_sesji = bot.get_all_sites_nums()
print("tytul,company,location,management_level,Pdate,tagi[tablica],salary,self.id_oferty")
while int(bot.current_site) < int(numer_stron_sesji):
    bot.get_data()
    for dane in bot.dane_oferty:
        print(dane)
    bot.go_to_next_site()
input(" ")
