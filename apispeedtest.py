import requests
import time
from tabulate import tabulate

# Function to prompt for URLs
def get_urls():
    urls = []
    more = True
    while more:
        url = input("Enter an API URL (or 'n' to stop): ")
        if url.lower() == 'n':
            break
        urls.append(url)
        more_input = input("Add another URL? (y/n): ")
        if more_input.lower() != 'y':
            more = False
    return urls

# Function to prompt for the number of requests
def get_num_requests():
    while True:
        try:
            num_requests = int(input("Enter the number of API requests: "))
            if num_requests > 0:
                return num_requests
            else:
                print("Number of requests must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Prompt for URLs
urls = get_urls()
if not urls:
    print("No URLs provided. Exiting...")
    exit()

# Prompt for the number of requests
num_requests = get_num_requests()

# Lists to store response times
url_times = {url: [] for url in urls}

# Send requests and measure response times
print(f"Sending {num_requests} requests to each URL...")
for i in range(num_requests):
    for url in urls:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        url_times[url].append(end_time - start_time)
        print(f"Request {i+1}/{num_requests} to {url} completed.")

# Calculate summary statistics
results = []
for url in urls:
    times = url_times[url]
    avg_time = sum(times) / num_requests
    min_time = min(times)
    max_time = max(times)
    tld_subdomain = url.replace("https://", "").split("/")[0]
    results.append([tld_subdomain, f"{avg_time:.6f}", f"{min_time:.6f}", f"{max_time:.6f}"])

# Create a table with the results
table = [["TLD/Subdomain", "Average Response Time (s)", "Minimum Response Time (s)", "Maximum Response Time (s)"]]
table.extend(results)

# Print the table
print("\nResponse Time Summary:")
print(tabulate(table, headers="firstrow", tablefmt="grid"))
