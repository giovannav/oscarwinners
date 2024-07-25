from pydantic import BaseModel, Field
from typing import Optional
from class_utils import *

class Film(BaseModel):
    DetailUrl: str = Field(alias='Detail URL')
    Film: str
    Producer: str = Field(alias='Producer(s)')
    ProductionCompany: str = Field(alias='Production Company(s)')
    WikiURL: str = Field(alias='Wiki URL')
    Winner: bool
    Year: str
    Budget: Optional[str] = ''
    OriginalBudget: Optional[int] = 0
    USDBudget: Optional[int] = 0
    
    def set_budget(self):
        self.Budget = get_budget_from_api(self.DetailUrl)
        if '\xa0' in self.Budget:
            self.Budget = self.Budget.replace('\xa0', ' ')
        elif ',' in self.Budget:
            self.Budget = self.Budget.replace(',', '')
        
    def clean_budget(self):
        process_budget_data(self)
            
    def clean_year(self):
        year = self.Year.strip().split(" ")[0]
        self.Year = year
        
    def __init__(self, **data):
        super().__init__(**data)
        self.set_budget()
        self.clean_budget()
        self.clean_year()