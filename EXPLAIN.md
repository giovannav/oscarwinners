### ETL Process Overview - Oscar Winners (ypitData)
For this ETL process, I decided to use an object-based approach with Pydantic. This is because the API output is a JSON file that can be easily interpreted by a Pydantic class, saving on initial cleaning and processing time before the actual data transformation.

Additionally, this model approach can be extended to other types of objects. For example, if we were collecting data about Grammy winners, we could add an Album class to the models file and still use the class_utils functions, like the budget cleaning, as well as the CSV function to process the data into a CSV file.

I chose not to use pandas for data cleaning because visualizing the data in tables was not necessary during the cleaning and processing phase. Considering pandas can be slightly slow, using dictionaries speeds up the processing time (which is quite fast—the slowest part is accessing the budget endpoint because each needs to be accessed individually).

If the task was only to read the data, I would have used named tuples. They are quicker than dictionaries but not a good option in this case because they are immutable.

**File Breakdown**
```
models.py
```
Contains a `Film` class which represents a film with various attributes. It initializes the budget, cleans the budget, and cleans the year format.

--- 

```
class_utils.py
```

Contains the functions necessary to gather and clean the film data. Functions include:

```
pounds_to_dollars(pounds: int) -> int: Converts pounds to dollars using a currency converter.
```

```
filter_oscar_winners(result: dict) -> list: Filters out the Oscar-winning films from the result dictionary.
```

```
retrieve_data(endpoint: str = 'http://oscars.yipitdata.com/') -> list: Retrieves data from the specified endpoint and filters Oscar winners.
```

```
get_budget_from_api(detail_url: str): Gets the budget of a film from its detail URL.
```

```
to_million(cleaned: str): Converts a string representing millions to an integer.
```

```bash
process_budget_data(film): Processes the budget data for a film, handling different formats and converting currencies.
```
---
```
main_utils.py
```
Contains the function to create and save the final CSV file. Its only function is described below:

```
to_csv(winners: list, file_name: str = 'oscar_winners', file_path: str = ''): Converts the list of winners to a CSV file and saves it to the specified path.
```
---
Finally:
```
main.py
```
The main script parses command-line arguments, retrieves data, and converts it to a CSV file using the specified file name and path.