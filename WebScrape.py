from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class Bot:
    DaneOferty = []
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
        self.currentSite = 1
        
    def ClickButtonAcc(self):
        # Wait until the "Akceptuj" button is present
        WebDriverWait(self.bot, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql"))
        )
        # Find and click the "Akceptuj" button
        button = self.bot.find_element(By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql")
        button.click() 
          
    def GetSiteReady(self):
        # Wait for the content box and paginator to be present
        WebDriverWait(self.bot, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='ContentBoxstyles__Wrapper-']"))
        )
        WebDriverWait(self.bot, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']"))
        )
    #Pobiera ile jest stron z ofertami
    def GetAllSitesNums(self):
        WebDriverWait(self.bot, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']"))
        )
        # Find the <ul> element with class "pagination"
        ul_element = self.bot.find_element(By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']")
        # Find all the <li> elements within the <ul> element
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        last_item = li_elements[-2]
        # Find the <a> element within the second-to-last <li> element
        link_element = last_item.find_element(By.TAG_NAME, 'a')
        # Get the inner HTML content of the <a> element
        numer_stron_sesji = link_element.get_attribute("innerHTML")
        # Print the inner HTML content
        #print("Ilosc stron: " + numer_stron_sesji)
        return numer_stron_sesji
            
    # Pobierz divy z ofertami
    def GetOffersFromCurrentSite(self):
        oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div[class^="ContentBoxstyles__Wrapper-"]')
        self.IdOferty = 0
        self.LinkiDoOferty = [None] * len(oferty)
        for oferta in oferty:
            inner_html = oferta.get_attribute("innerHTML")
            soup = BeautifulSoup(inner_html, 'html.parser')
            dane = []

            # Get the text of the element, checking if it exists
            tytul_element = soup.find('h3', attrs={'data-test': 'offer-title'})
            company_name_element = soup.find('span', attrs={'data-test': 'company-name'})
            offer_location_element = soup.find('span', attrs={'data-test': 'offer-location'})
            offer_management_level_element = soup.find('span', attrs={'data-test': 'offer-management-level'})
            date = soup.find('div', class_='JobOfferstyles__FooterText-sc-1rq6ue2-22')
            
            tytul = tytul_element.text if tytul_element else ''
            company = company_name_element.text if company_name_element else ''
            location = offer_location_element.text if offer_location_element else ''
            management_level = offer_management_level_element.text if offer_management_level_element else ''
            Pdate = date.text if date else ''
            Pdate = Pdate.replace("opublikowana: ", "")
            # Print the details only if the title is not empty
            dane = [tytul,company,location,management_level,Pdate,None,None,self.IdOferty]
            if soup.find('span', attrs={'data-test': 'offer-salary'}):
                salary = soup.find('span', attrs={'data-test': 'offer-salary'})
                dane[6] = salary.text
                
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
                
             # Find the desired element by tag, class, or other attributes
            try:
                button = oferta.find_element(By.CLASS_NAME, 'JobOfferstyles__TitleButton-sc-1rq6ue2-5.HPWqN')
                button.click()
                href_element = oferta.find_element(By.CLASS_NAME, 'OfferLocationsListstyles__LocationsItemLink-sc-b1eixg-2.ZUWyH')
                href = href_element.get_attribute("href")
                self.LinkiDoOferty[self.IdOferty] = href
            except NoSuchElementException:
                offer_link = soup.find('a', attrs={'data-test': 'offer-link'})
                if offer_link is not None:
                    href = offer_link['href']
                    self.LinkiDoOferty[self.IdOferty] = href
                
            self.DaneOferty.append(dane)
            self.IdOferty+=1
            #w jakim formacie to zapisywać? baza danych? json? po prostu txt?
            #wpierdolic to wszystko do jakiegoś excela i analiza
            
            
            #wejście w oferte
            #self.bot.get(href_link)
                #Dodać
                #Technologie, których używamy "Mile widziane"
                #Czy wymagają i ile lat doświadczenia
                #Specjalizacje
                #Bachelor's/Master's/PhD in STEM albo bycie studentem(debilem)
                #Jeśli na ogłoszeniu są juz napisane technologie to git jak nie to trzeba będzie wejść w ogłoszenie i je wziąć OOF :ccccc
                    # TODO: wejść w każdą ofertę i wyciągnąć: Mile widziane technologie, doświadczenie, wymagania, specjalizacja costam cośtam
                    #prawdopodobnie trzeba będzie uzyc AI do czytania i skracania teksów do jednego słowa na kategorie czy coś
                    #ale openAI jest płatne, jebać to pisze własne AI
            #wyjście z oferty
            #self.bot.get("https://it.pracuj.pl/?pn=" + str(self.currentSite))
        self.IdOferty = 0
        del self.LinkiDoOferty[:]
    def GoToNextSite(self):
        self.currentSite+=1
        self.bot.get("https://it.pracuj.pl/?pn=" + str(self.currentSite))
        self.GetSiteReady()
        
bot = Bot()
bot.GetSiteReady()
bot.ClickButtonAcc()
numer_stron_sesji = bot.GetAllSitesNums()

while int(bot.currentSite) < int(numer_stron_sesji):
    bot.GetOffersFromCurrentSite()
    #wejdz w każdy self.LinkiDoOferty i pobierz z niego dane i wpierdol do bot.DaneOferty, chce sie zajebać
    for dane in bot.DaneOferty:
        print(dane)
        #input("\n")
    bot.GoToNextSite()
    
#    input(" ")
input(" ")