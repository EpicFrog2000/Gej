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
        self.currentSite = 1
        self.LinkiDoOferty = []
        self.DaneOferty = []
        
    def ClickButtonAcc(self):
        WebDriverWait(self.bot, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql"))
        )
        button = self.bot.find_element(By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql")
        button.click() 
          
    def GetSiteReady(self):
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
        ul_element = self.bot.find_element(By.CSS_SELECTOR, "[class^='Paginatorstyles__Wrapper-sc-1ur9l1s-0 dDposH']")
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        last_item = li_elements[-2]
        link_element = last_item.find_element(By.TAG_NAME, 'a')
        numer_stron_sesji = link_element.get_attribute("innerHTML")
        return numer_stron_sesji
    
    #Pobierania danych an temat ofert
    def GetOffersFromCurrentSite(self):
        oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div[class^="ContentBoxstyles__Wrapper-"]')
        self.IdOferty = 0
        self.LinkiDoOferty = [None] * len(oferty)
        
        #Pobierz dane z ofert na głównej
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
            Pdate = date.text if date else ''
            Pdate = Pdate.replace("opublikowana: ", "")
            dane = [tytul,company,location,management_level,Pdate,None,None,self.IdOferty]
            if soup.find('span', attrs={'data-test': 'offer-salary'}):
                salary = soup.find('span', attrs={'data-test': 'offer-salary'})
                dane[6] = salary.text
                
            #Pobierz tagi
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
            #Pobierz linki do ofert
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
            
        self.IdOferty = 0
        #wejdz w każdy self.LinkiDoOferty i pobierz z niego dane i wpierdol do bot.DaneOferty, chce sie zajebać
        #Pobierz dane ze strony oferty
        for oferta in self.LinkiDoOferty:
            self.bot.get(str(oferta))
            #geting data
            #PAIN

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
    for dane in bot.DaneOferty:
        print(dane)
    bot.GoToNextSite()
input(" ")