from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import key_words_for_indeed

def extract_number(input_string):
    pattern = r'\s(\d+)\s'
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
        url = 'https://pl.indeed.com/q-it-oferty-pracy.html?l=Polska'
        self.bot.get(url)
        self.bot.maximize_window()
        
    def close_powiadomienie(self):
        try:
            button = self.bot.find_element_by_css_selector('button[aria-label="zamknij"].css-yi9ndv.e8ju0x51')
            button.click()
        except:
            print("closePowiadomienieButton not found")
            pass
        
    def get_next_site_button(self):
            self.next_page_element = self.bot.find_element_by_css_selector('[data-testid="pagination-page-next"]')
            self.next_page_element = self.next_page_element.get_attribute("href")

    def go_next_site(self):
        self.bot.get(self.next_page_element)

    def getLinks(self):
        ul_with_links = self.bot.find_element(By.CLASS_NAME, 'css-zu9cdh')
        oferty = ul_with_links.find_elements(By.CLASS_NAME, 'css-5lfssm')
        
        self.id_oferty = 0
        self.linki_do_oferty = [''] * len(oferty)
        unique_links = set()
        
        for oferta in oferty:
            try:
                href_element = oferta.find_element(By.CLASS_NAME, 'jcs-JobTitle.css-jspxzf.eu4oa1w0')
                href = href_element.get_attribute("href")
                if href not in unique_links:
                    self.linki_do_oferty[self.id_oferty] = href
                    unique_links.add(href)
                self.id_oferty += 1
            except:
                pass
        self.id_oferty = 0
        
    def get_data_from_offers(self):
        for oferta in self.linki_do_oferty:
            try:
                self.bot.get(oferta)
            except:
                print("blad w getting oferta site")
                continue
            inner_data = [''] * 14
            #get data

            try: #inner_list[0],#title
                title_element = oferta.find_element(By.CLASS_NAME, 'jobsearch-JobInfoHeader-title')
                title_span = title_element.find_element_by_tag_name('span')
                inner_data[0] = title_span.get_attribute("innerHTML")
            except:
                pass
            try: #inner_list[1],#company
                company_element = oferta.find_element_by_css_selector('div[data-company-name="true"][data-testid="inlineHeader-companyName"]')
                a_element = company_element.find_element_by_css_selector('a')
                inner_data[1] = a_element.get_attribute("innerHTML")
            except:
                pass
            
            try: #inner_list[2],#location
                location_element = oferta.find_element_by_css_selector('div[data-testid="inlineHeader-companyLocation"]')
                div_element = location_element.find_element_by_css_selector('div')
                parts = div_element.get_attribute("innerHTML").split(", ")
                if len(parts) > 1:
                    inner_data[2] = parts[0]
                else:
                    inner_data[2] = div_element.get_attribute("innerHTML")
            except:
                pass
            
            try:#inner_list[4],#salary
                salary_element = oferta.find_element(By.CLASS_NAME, 'css-tvvxwd.ecydgvn1')
                parts = salary_element.get_attribute("innerHTML").split("-")
                if len(parts) > 1:
                    inner_data[4] = extract_numeric_value(parts[0]) # this is from and extract_numeric_value(parts[1]) would be to
                else:
                    inner_data[4] = salary_element.get_attribute("innerHTML")
            except:
                pass
            
            try:#inner_list[5],#tryb_pracy
                all_text = oferta.get_attribute("innerHTML")
                found = False
                for phrase in key_words_for_indeed.key_words_work_type:
                    if phrase in all_text:
                        found = True
                        inner_data[5] = phrase
                        break
                found = False
            except:
                pass
            
            try:#inner_list[6],#etat
                if oferta.find_element_by_id("salaryInfoAndJobType"):
                    element = oferta.find_element_by_id("salaryInfoAndJobType")
                    all_text = element.get_attribute("innerHTML")
                    found = False
                    for phrase in key_words_for_indeed.key_words_etat:
                        if phrase in all_text:
                            found = True
                            inner_data[6] = phrase
                            break
                    found = False
                elif oferta.find_element_by_id("jobDetailsSection"):
                    element = oferta.find_element_by_id("jobDetailsSection")
                    all_text = element.get_attribute("innerHTML")
                    found = False
                    for phrase in key_words_for_indeed.key_words_etat:
                        if phrase in all_text:
                            found = True
                            inner_data[6] = phrase
                            break
                    found = False
                else:
                    all_text = oferta.get_attribute("innerHTML")
                    found = False
                    for phrase in key_words_for_indeed.key_words_etat:
                        if phrase in all_text:
                            found = True
                            inner_data[6] = phrase
                            break
                    found = False
                    
            except:
                pass
            
            #try: # inner_list[7],#kontrakt
            #                               # NOT ENOUGH INFO ON WEBSITE
            #except:
            #    pass
            
            try: #inner_list[3],#management_level - Mid	systent	Junior	Senior	ekspert	team manager	menedżer	praktykant / stażysta	dyrektor ITP
                # chceck if wherever of inner_list is any of above phrases or something
                
                
            except:
                pass
            
            #HOWWWWWWWWWWWWWWWWWW DO THE REST ITS SO BADDDDDDDDD
            # INDEED SUCKS DICK AND BALLS 
            # KYS 
            
                #maybe these:
            
            
            
            
            
            #inner_list[8],#specjalizacja
            #tuple(inner_list[9]),# technologie_wymagane (converted to a tuple)
            #tuple(inner_list[10]),# technologie_mile_widziane (converted to a tuple)
            #inner_list[11],#doswiadczenie

bot = Bot()
bot.getLinks()
input(' ')