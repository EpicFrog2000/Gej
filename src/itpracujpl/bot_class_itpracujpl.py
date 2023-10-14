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


# Obie poniższe funkcje były napisane jakiś czas temu, nie wiem dlaczego obie egzystują pomimo tego samogo przeznaczenia, nie ruszam :P (komentarz z 07.10.2023)
def extract_number(input_string):
    pattern = r'\s(\d+)\s'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None

def extract_numeric_value(text):
    numeric_text = ''.join(filter(str.isdigit, text))
    return int(numeric_text)

class Bot:
    def __init__(self):
        print("\rInitiation", end="")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
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
        url = 'https://it.pracuj.pl/?pn=' + str(self.obecna_strona)
        self.bot.get(url)
        self.bot.maximize_window()
        self.linki_do_oferty = []
        self.dane_oferty = []
        self.retry = False
        # czasem ładuje się jedna domena a czasem druga więc są 2 skrypty na 2 różne domeny
        self.mode = 0 # 0 is it.pracuj.pl and 1 is it.pracuj.pl/praca, it is decided in get_all_sites_nums()

    # Kilka przycisk z akceptacją ciasteczek jeśli się pojawi
    def kliknij_przycisk_ciasteczka(self):
        print("\rClicking cookies button", end="")
        try:
            button = WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='size-medium variant-primary cookies_b1fqykql']")))
            button.click()
        except NoSuchElementException as e:
            print(f"\rError occurred while clicking cookies button: {e}")
            pass

    # Pobiera ile jest stron z ofertami
    # Szuka i wyczytuje numer z elementu który posiada ilość stron z ofertami
    def get_all_sites_nums(self):
        print("\rGetting nums of all sites", end="")
        try:
            try:
                div = WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Paginatorstyles__Wrapper-sc-1ur9l1s-0.dDposH')))
                ul_element = div.find_element(By.CSS_SELECTOR, 'ul.pagination')
                li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
                last_item = li_elements[-2]
                link_element = last_item.find_element(By.TAG_NAME, 'a')
                numer_stron_sesji = link_element.get_attribute("innerHTML")
                return int(numer_stron_sesji)
            except Exception as e:
                div = WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='job-offers-bottom-pagination']")))
                second_last_button = div.find_element(By.CSS_SELECTOR, "button[data-test^='bottom-pagination-button-page-']:nth-last-child(2)")
                numer_stron_sesji = second_last_button.text
                self.mode = 1
                return int(numer_stron_sesji)
        except:
            print("\r Error getting number of all sites", end="")

    # Pobieranie danych na temat ofert
    def get_data(self,numer_stron_sesji):
        print("\rGetting data", end="")
        self.dane_oferty.clear()
        # Szuka elementy zawierające linki do stron z detalami oferty oraz magazynuje te linki w tablicy linki_do_oferty
        if(self.mode == 0):
            oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div.ContentBoxstyles__Wrapper-sc-11jmnka-0.jevXWE.JobOfferstyles__ContentBoxWrapper-sc-1rq6ue2-0')
            self.id_oferty = 0
            self.linki_do_oferty = [''] * len(oferty)
            print("\rGetting offer links", end="")
            for oferta in oferty:
                #unikalne_linki pomaga w tym aby zduplikowane oferty nie powtarzały się 
                unikalne_linki = set()
                try:
                    button = oferta.find_element(By.CLASS_NAME, 'JobOfferstyles__TitleButton-sc-1rq6ue2-5.HPWqN')
                    button.click()
                    href_element = oferta.find_element(By.CLASS_NAME, 'OfferLocationsListstyles__LocationsItemLink-sc-b1eixg-2.ZUWyH')
                    href = href_element.get_attribute("href")
                    if href not in unikalne_linki:
                        self.linki_do_oferty[self.id_oferty] = href
                        unikalne_linki.add(href)
                except NoSuchElementException:
                    offer_link_element = oferta.find_element(By.CSS_SELECTOR, 'a[data-test="offer-link"]')
                    link_text = offer_link_element.get_attribute("href")
                    if link_text and link_text not in unikalne_linki:
                        self.linki_do_oferty[self.id_oferty] = link_text
                        unikalne_linki.add(link_text)
                self.id_oferty += 1
            self.id_oferty = 0
        else:
            oferty = self.bot.find_elements(By.CSS_SELECTOR, "div.listing-it_bp811tr.listing-it_po9665q[data-test='default-offer']")
            self.id_oferty = 0
            self.linki_do_oferty = [''] * len(oferty)
            print("\rGetting offer links", end="")
            for oferta in oferty:
                unikalne_linki = set()
                try:
                    location = oferta.get_attribute("data-test-location")
                    # Jesli oferta ma wiele lokalizacji, rozwiń i kliknij pierwszą lokalizację od góry
                    if location == "multiple":
                        oferta.click()
                    offer_link_element = oferta.find_element(By.CSS_SELECTOR, "a[data-test='link-offer']")
                    link_text = offer_link_element.get_attribute("href")
                    if link_text and link_text not in unikalne_linki:
                        self.linki_do_oferty[self.id_oferty] = link_text
                        unikalne_linki.add(link_text)
                    self.id_oferty += 1
                except:
                    print("\rError getting or clicking offer", end="")
                    pass
            self.id_oferty = 0

        # Pobierz dane z linków do ofert
        print("\rStart gathering data from offers", end="")
        wszystkie_oferty = len(self.linki_do_oferty)
        # Odwiedza każdy link z ofertami i pobiera z niego dane
        for index, oferta in enumerate(self.linki_do_oferty, start=1):
            print("\r\033[K", end='', flush=True)
            msg = f"\rGetting data {index} / {wszystkie_oferty}, {str(oferta)}"
            print(msg, end='')
            if oferta != '':
                try:
                    self.bot.get(str(oferta))
                    WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.ID, "kansas-offerview")))
                    print("\r\033[K", end='')
                    print(f"\rGetting offer site   ", end="")
                except:
                    continue
                tymczasowe_dane_jednej_oferty = [''] * 14
                # getting data
                # title
                try:
                    print("\rGetting offer title", end="")
                    title = self.bot.find_element(By.CSS_SELECTOR, 'h1.offer-viewkHIhn3[data-test="text-positionName"][data-scroll-id="job-title"]')
                    tymczasowe_dane_jednej_oferty[0] = title.get_attribute("innerHTML")
                except NoSuchElementException:
                    continue
                # company
                try:
                    print("\rGetting offer company", end="")
                    company = self.bot.find_element(By.CSS_SELECTOR, 'h2.offer-viewwtdXJ4[data-test="text-employerName"]')
                    company = company.get_attribute("innerHTML")
                    index_of_first_less_than = company.find("<")
                    company = company[:index_of_first_less_than].strip()
                    tymczasowe_dane_jednej_oferty[1] = company
                except NoSuchElementException:
                    pass
                # location
                try:
                    print("\rGetting offer location", end="")
                    location = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewqtkGPu[data-test="text-benefit"]')
                    parts = location.get_attribute("innerHTML").split(", ")
                    if len(parts) > 1:
                        tymczasowe_dane_jednej_oferty[2] = parts[0]
                    else:
                        tymczasowe_dane_jednej_oferty[2] = location.get_attribute("innerHTML")
                except NoSuchElementException:
                    print("\rGetting offer location after exeption", end="")
                    location = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewUIYWmu[data-test="text-benefit"]')
                    parts = location.get_attribute("innerHTML").split(", ")
                    if len(parts) > 1:
                        tymczasowe_dane_jednej_oferty[2] = parts[0]
                    else:
                        tymczasowe_dane_jednej_oferty[2] = location.get_attribute("innerHTML")
                    pass
                # management_level
                try:
                    print("\rGetting offer management_level", end="")
                    management_level = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-employment-type-name-text"]')
                    tymczasowe_dane_jednej_oferty[3] = management_level.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # salary
                try:
                    print("\rGetting offer salary", end="")
                    salary = self.bot.find_element(By.CSS_SELECTOR, "strong[data-test='text-earningAmount']")
                    salary_from = salary.find_element(By.CSS_SELECTOR, 'span[data-test="text-earningAmountValueFrom"]')
                    salary_to = salary.find_element(By.CSS_SELECTOR, 'span[data-test="text-earningAmountValueTo"]')
                    salary_from = extract_numeric_value(html.unescape(salary_from.get_attribute("innerHTML")))
                    salary_to = extract_numeric_value(html.unescape(salary_to.get_attribute("innerHTML")))
                    tymczasowe_dane_jednej_oferty[4] = salary_from
                    #tymczasowe_dane_jednej_oferty[5] = salary_to
                except NoSuchElementException:
                    tymczasowe_dane_jednej_oferty[4] = 0
                    pass 
                # tryb_pracy
                try:
                    print("\rGetting offer tryb_pracy", end="")
                    tryb_pracy = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-modes-text"]')
                    tymczasowe_dane_jednej_oferty[5] = tryb_pracy.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # etat
                try:
                    print("\rGetting offer etat", end="")
                    etat = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-work-schedule-text"]')
                    tymczasowe_dane_jednej_oferty[6] = etat.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # kontrakt
                try:
                    print("\rGetting offer kontrakt", end="")
                    kontrakt = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewXo2dpV[data-test="sections-benefit-contracts-text"]')
                    tymczasowe_dane_jednej_oferty[7] = kontrakt.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # specjalizacja
                try:
                    print("\rGetting offer specjalizacja", end="")
                    specjalizacja = self.bot.find_element(By.CSS_SELECTOR, 'span.offer-viewPFKc0t')
                    tymczasowe_dane_jednej_oferty[8] = specjalizacja.get_attribute("innerHTML")
                except NoSuchElementException:
                    pass
                # technologie_wymagane
                try:
                    print("\rGetting offer technologie_wymagane", end="")
                    div_wymagane = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="technologies-expected-1"][data-test="section-technologies-expected"]')
                    lista = div_wymagane.find_element(By.CSS_SELECTOR, "[class^='offer-viewEX0Eq-']")
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    self.wymagane = [] * len(li_elements)
                    for element in li_elements:
                        link_element = element.find_element(By.TAG_NAME, 'p')
                        inner_html = link_element.get_attribute("innerHTML")
                        self.wymagane.append(inner_html)
                    tymczasowe_dane_jednej_oferty[9] = self.wymagane
                except NoSuchElementException:
                    pass
                # technologie mile widziane
                try:
                    print("\rGetting offer technologie mile widziane", end="")
                    div_optional = self.bot.find_element(By.CSS_SELECTOR, 'div.offer-viewfjH4z3[data-scroll-id="technologies-optional-1"][data-test="section-technologies-optional"]')
                    lista = div_optional.find_element(By.CSS_SELECTOR, "[class^='offer-viewEX0Eq-']")
                    li_elements = lista.find_elements(By.TAG_NAME, 'li')
                    self.mile_widziane = [] * len(li_elements)
                    for element in li_elements:
                        link_element = element.find_element(By.TAG_NAME, 'p')
                        inner_html = link_element.get_attribute("innerHTML")
                        self.mile_widziane.append(inner_html)
                    tymczasowe_dane_jednej_oferty[10] = self.mile_widziane
                except NoSuchElementException:
                    pass
                # doswiadczenie? Działa okropnie i czasem są błędy ale lepiej bez AI ciężko
                try:
                    print("\rGetting offer doswiadczenie", end="")
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
                                        tymczasowe_dane_jednej_oferty[11] = result # THIS SUCKS
                                        doswiadczenie = True
                                        break
                except NoSuchElementException:
                    pass
                # studia/wykrztalcenie? Raczej ciężko dodać bez AI(nie chce mi się)
                #
                self.dane_oferty.append(tymczasowe_dane_jednej_oferty)
        self.linki_do_oferty.clear()

    # Ładuje następną stronę z ofertami
    def go_to_next_site(self):
        try:
            self.retry = False
            print("\rGoing to next site", end="")
            self.obecna_strona += 1
            if(self.mode ==0):
                self.bot.get("https://it.pracuj.pl/?pn=" + str(self.obecna_strona))
            else:
                self.bot.get("https://it.pracuj.pl/praca?pn=" + str(self.obecna_strona))
        except:
            print("\rGoing to next site exeption", end="")
            if(self.retry == False):
                self.retry = True
                self.obecna_strona -= 1
            self.go_to_next_site()