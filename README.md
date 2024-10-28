# Prior to Installation

The script  assumes you already have python installed, if you do proceed to the Installation section otherwise see below:

- Download and install python for your operating system here https://www.python.org/downloads/
- Open your command line and type in `py -m pip --version` and ensure that pip is installed as well.
- If pip isn't installed, do so by typing `py -m ensurepip --default-pip`

# Installation

To install the dependencies, run the below command:

```commandline
pip install -r requirements.txt
```

# Usage

1. You can use the sample CSV File named "input.csv" to add the inputs
The CSV File has the following inputs:

- `company_name` - The company name the code is for (just a visual signifier when the script runs so you know what organization is running in the list of codes)
- `contract_number` - The organization code, the website calls these account numbers and the app calls them contract IDs
- `pickup_dt` - Pickup date and time (Enter the time in 24 hours format)
    - Example - 22nd September 2022 4:30 PM = 2022-09-22T16:30
- `dropoff_dt` - Dropoff date and time (Enter the time in 24 hours format)
  - Example - 24th September 2022 9:00 AM = 2022-09-24T09:00
- `location_name` - Airport code of the location you're looking for the prices.

You can enter multiple company_name/contract_number / pickup_dt / dropoff_dt / location_name so that you can research prices at different points of a single trip in different cities or even at different airports for any number of organization codes.

2. After creating the CSV File, run the below command:

```commandline
python main.py
```

3. After fetching and processing all the data, it will create a results.csv file in the same directory.

The results.csv will `company_name` `contract_number` `location_name` `pickup_dt` `dropoff_dt` `car_type` `total_price` using these values you can filter through to see what locations are the cheapest with a given code.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
