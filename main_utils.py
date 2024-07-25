from models import Film
import json
import pandas as pd

def to_csv(winners: list, file_name: str = 'oscar_winners', file_path: str = ''):
    out = []
    for winner in winners:
        obj = Film(**winner)
        obj = obj.model_dump_json()
        input_dict = json.loads(obj)
        out.append(input_dict)
    
    dfItem = pd.DataFrame.from_records(out)
    df = dfItem[['Film', 'Year', 'Winner', 'OriginalBudget', 'USDBudget']]
    df.to_csv(f'{file_path}{file_name}.csv', index=False, encoding='utf-8')