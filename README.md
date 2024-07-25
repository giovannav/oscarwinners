### Instructions on How to Run This App

1. **Setup Directory and Internet Connection**

   Ensure you have unzipped the files, and they are all in the same directory. Navigate to the correct directory using your command-line interface (CMD, PowerShell, Terminal, etc.). An active internet connection is required to run the code.

2. **Install Necessary Modules and Packages**

   First, you need to install the required modules and packages listed in the `requirements.txt` file. This app was developed using Python version 3.9.13, so it is strongly recommended to use a similar or the same Python version (e.g., 3.9.18) to avoid compatibility issues. 

   To install the necessary libraries, run the following command in your command-line interface:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Script**

    The main script to collect the data is main.py. You can run it without customizations using the following command:

    ```bash
    python main.py
    ``` 

    You can also customize the output CSV file by renaming it using arguments. Note: Do not add the extension; the code handles it automatically.

    To rename the output CSV file, use the following command:

    ```bash
    python main.py --csv_file_name 'output_csv_oscars'
    ``` 

    You can also choose the directory where you want the file to be saved. Here's how you can do it:

    ```bash
    python main.py --csv_file_name 'output_csv_oscars' --csv_file_path 'C://Documents/'
    ``` 

    The arguments are optional. If left empty, the file will be named oscar_winners.csv and will be saved in the current folder by default.
    This folder also contains a 'output_example.csv' which is a file showing how the new csv output should look like.