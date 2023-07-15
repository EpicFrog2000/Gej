from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

class Bot:
    def __init__(self):
        # WebDriver setup to avoid detection
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("--incognito")
        
        self.bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.bot.maximize_window()
        self.bot.get("https://it.pracuj.pl/")
        try:
            # Wait until the "Akceptuj" button is present
            WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql"))
            )
            # Find and click the "Akceptuj" button
            button = self.bot.find_element(By.CLASS_NAME, "size-medium.variant-primary.cookies_b1fqykql")
            button.click()
            
            # Poczekaj na załadowanie
            element = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='ContentBoxstyles__Wrapper-']"))
            )
            # Pobierz divy z ofertami
            oferty = self.bot.find_elements(By.CSS_SELECTOR, 'div[class^="ContentBoxstyles__Wrapper-"]')
            for oferta in oferty:
                inner_html = oferta.get_attribute("innerHTML")
                # TODO podziel na czesci:
                # tytul, pracodawca, lokalizacja i tam takie detale, data publikacji, technologie, czasem nie dawają wszystkich to ifa sie jebnie
                #Get tytul oferty
                # Parse the HTML content
                soup = BeautifulSoup(inner_html, 'html.parser')

                # Find the desired element by tag, class, or other attributes
                tytul_element = soup.find('h3', attrs={'data-test': 'offer-title'})

                # Get the text of the element
                tytul = tytul_element.text if tytul_element else ''
                
                print(tytul)
                print("\n")
            
        except Exception as e:
            print("Error:", e)

bot = Bot()
input(" ")