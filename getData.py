import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
    "locale": "en",
    "X-City": "Mumbai",
    "Accept": "application/json",
    "X-Platform": "mobileweb-0.0.1",
    "X-Access-Key": "1mg_client_access_key"
}

def get_list(drug_query: str) -> list:
    """Get the list of drugs from 1mg.com and return the search results as a list of dictionaries.

    Args:
        drug_query (str): Drug name to search for.

    Returns:
        list: drug details as a list of dictionaries.

    Example:
        >>> get_list("Ciplox")
        [{'id': '159603', 'name': 'Cipcal Cipcal 500 Tablet from Cipla | Source of Calcium & Vitamin D | For Bone, Joint and Muscle Care', 'type': 'otc', 'pack_size': '15 tablets', 'actual_price': '₹104.66', 'image': 'https://onemg.gumlet.io/a_ignore,w_380,h_380,c_fit,q_auto,f_auto/a8730d167e7d4b0cb8bc769936d3151c.jpg', 'prescription_required': False, 'url': 'https://www.1mg.com//otc/cipcal-cipcal-500-tablet-from-cipla-source-of-calcium-vitamin-d-for-bone-joint-and-muscle-care-otc159603'}]
    """
    data = {}
    search_results = []
    filter_results = {}
    result_details = {}
    session = requests.Session()
    session.headers.update(HEADERS)
    url = (f"https://www.1mg.com/pwa-api/api/v4/search/all?q={drug_query}&filter=&per_page=20&types=all&sort=relevance")
    response = session.get(url)
    if response.json()['is_success'] == True:
        if response.json()['data']['result_found'] == True:
            # gets the search results
            for i in response.json()['data']['search_results']:
                search_data = {}
                search_data['id'] = i['id']
                search_data['name'] = i['name']
                search_data['type'] = i['type']
                search_data['pack_size'] = i['label']
                search_data['actual_price'] = i['prices']['mrp']
                search_data['image'] = i['image']
                search_data['prescription_required'] = i['rx_required']
                search_data['url'] = f"https://www.1mg.com/{i['url']}"
                print(search_data['id'])
                search_results.append(search_data)
            # gets the filters types & data
            for type in response.json()['data']['filter']['values']:
                filter_name = type['name']
                filter_values = []
                for k in type['values']:
                    _filter_values = {}
                    _filter_values['key'] = k['key']
                    _filter_values['name'] = k['name']
                    _filter_values['count'] = k['count']
                    filter_values.append(_filter_values)
                filter_results[filter_name]=filter_values
            # gets the general data
            mix_panel_data = response.json()['data']['mix_panel_data']
            result_details['number_of_results'] = mix_panel_data['number_of_results']
            result_details['autocorrected_search'] = mix_panel_data['autocorrected_search']
            result_details['corrected_query'] = mix_panel_data['corrected_query']
            result_details['did_you_mean_suggestions_count'] = mix_panel_data['did_you_mean_suggestions_count']
            data['search_results'] = search_results
            data['filter_results'] = filter_results
            data['result_details'] = result_details
            return data
