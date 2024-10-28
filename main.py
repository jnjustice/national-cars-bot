import csv
from lib import get_data
from locations import get_location


def init():
    results = []
    csv_header = ['company_name','contract_number', 'location_name', 'pickup_dt', 'dropoff_dt', 'car_type', 'total_price']
    locations_fetched = {}
    with open('input.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            company_name = row['company_name']
            contract_number = row['contract_number']
            location_name = row['location_name']
            pickup_dt = row['pickup_dt']
            dropoff_dt = row['dropoff_dt']

            print("Fetching - "+company_name+" at "+location_name+" from "+pickup_dt+
                  " - "+dropoff_dt)

            if location_name in locations_fetched:
                print("Getting location data from cache")
                location = locations_fetched[location_name]
            else:
                print("Getting location data from API")
                location = get_location(location_name)
                locations_fetched[location_name] = location

            if len(location['airports']) == 0:
                print("Failed fetching location data")
            else:
                data = get_data(row, location['airports'][0])

                if 'gbo' in data and \
                    'reservation' in data['gbo'] and \
                    'car_classes' in data['gbo']['reservation']:

                    print("Processing data for "+company_name)

                    car_classes = data['gbo']['reservation']['car_classes']

                    for cls in car_classes:
                        results.append([
                            company_name,
                            contract_number,
                            location_name,
                            pickup_dt,
                            dropoff_dt,
                            cls['name'],
                            cls['charges']['PAYLATER']['total_price_payment']['amount']
                        ])
                else:
                    print("Fetching failed for "+company_name)

        with open('results.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(csv_header)

            # write multiple rows
            writer.writerows(results)


if __name__ == '__main__':
    init()
