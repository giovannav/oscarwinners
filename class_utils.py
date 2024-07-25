from currency_converter import CurrencyConverter
import requests

def pounds_to_dollars(pounds: int) -> int:
    c = CurrencyConverter()
    conv = c.convert(pounds, 'GBP', 'USD')
    
    return int(conv)

def filter_oscar_winners(result: dict) -> list:
    winners = []
    for data in result['results']:
        year = data['year']
        for film in data['films']:
            if film['Winner']:
                film['Year'] = year
                winners.append(film)
                break
    
    return winners

def retrieve_data(endpoint: str = 'http://oscars.yipitdata.com/') -> list:
    result = requests.get(f'{endpoint}').json()
    
    filtered_data = filter_oscar_winners(result)
    
    return filtered_data

def get_budget_from_api(detail_url: str):
    try:
        response = requests.get(f'{detail_url}')
        if 'Budget' in response.json(): 
            budget = response.json()['Budget']
        else: 
            budget = '0'
    except: 
        budget = '0'
    
    return budget

def to_million(cleaned: str):
    return int(float(cleaned) * 1000000)

def process_budget_data(film):
    
    if '–' in film.Budget or '-' in film.Budget:
        film.OriginalBudget, film.USDBudget = 0, 0
        
    elif film.Budget.startswith("US$ "):
        cleaned = film.Budget.split(' ')[1]
        if 'million' in film.Budget:
            film.OriginalBudget, film.USDBudget = to_million(cleaned), to_million(cleaned)
        else: film.OriginalBudget, film.USDBudget = int(cleaned), int(cleaned)
        
    elif film.Budget.startswith("US$"):
        cleaned = film.Budget.split(' ')[0].replace("US$", "")
        if 'million' in film.Budget:
            film.OriginalBudget, film.USDBudget = to_million(cleaned), to_million(cleaned)
        else: film.OriginalBudget, film.USDBudget = int(cleaned), int(cleaned)
        
    elif film.Budget.startswith("$"):
        cleaned = film.Budget.split(' ')[0].replace("$", "")
        if 'million' in film.Budget:
            film.OriginalBudget, film.USDBudget = to_million(cleaned), to_million(cleaned)
        else: 
            film.OriginalBudget, film.USDBudget = int(cleaned), int(cleaned)
            
    elif film.Budget.startswith("£") or film.Budget.startswith("₤"):
        cleaned = film.Budget.split(' ')[0].replace("£", "").replace("₤", "")
        if 'million' in film.Budget:
            film.OriginalBudget = to_million(cleaned)
            film.USDBudget = pounds_to_dollars(to_million(cleaned))
        else: 
            film.OriginalBudget = int(cleaned)
            film.USDBudget = pounds_to_dollars(int(cleaned))
            
    else: film.OriginalBudget, film.USDBudget = 0, 0