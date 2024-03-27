# API Speed Test

This Python script tests the speed of API requests to multiple URLs and presents the results in a visually appealing table.

## Features

- Prompts the user to enter API URLs and the number of requests to send
- Sends the specified number of requests to each URL
- Measures the response time for each request
- Calculates the average, minimum, and maximum response times for each URL
- Presents the results in a tabular format with the TLD/subdomain, average response time, minimum response time, and maximum response time

## Requirements

- Python 3.x
- `requests` library
- `tabulate` library

You can install the required libraries using pip:
```
pip install requests tabulate
```

## Usage

1. Run the script in your terminal or command prompt.
2. When prompted, enter the API URLs you want to test (or type 'n' to stop adding URLs).
3. Enter the number of API requests to send to each URL.
4. The script will start sending requests to each URL and display the progress.
5. After completing all requests, the script will print a table with the response time summary for each URL.

## Example Output
```
Enter an API URL (or 'n' to stop): https://example.com/api/endpoint
Add another URL? (y/n): y
Enter an API URL (or 'n' to stop): https://another.example.com/api/endpoint
Add another URL? (y/n): n
Enter the number of API requests: 100
Sending 100 requests to each URL...
Request 1/100 to https://example.com/api/endpoint completed.
Request 1/100 to https://another.example.com/api/endpoint completed.
...
Request 100/100 to https://example.com/api/endpoint completed.
Request 100/100 to https://another.example.com/api/endpoint completed.

Response Time Summary:
+-------------------+---------------+---------------+---------------+
| TLD/Subdomain     | Average Response Time (s) | Minimum Response Time (s) | Maximum Response Time (s) |
+===================+===============+===============+===============+
| example.com       |   0.123456   |   0.012345   |   0.456789   |
+-------------------+---------------+---------------+---------------+
| another.example.com |   0.234567   |   0.054321   |   0.987654   |
+-------------------+---------------+---------------+---------------+
```
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the GNU License.
