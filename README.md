# IP Locator

IP Locator is a Python application that fetches the geographical location of a given IP address and displays it on an interactive map. The application uses Tkinter for the user interface and Folium for map generation. The map is displayed in a new window using `pywebview`.

## Features

- Fetches geographical information for a given IP address.
- Displays the location on an interactive map.
- Shows the state and country of the IP address.
- User-friendly interface with Tkinter.
- Displays a loading message while fetching data.

## Prerequisites

- Python 3.x
- `requests` library
- `folium` library
- `pywebview` library
- `tkinter` library (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/James7688/IP-Locator.git
    cd IP-Locator
    ```

2. Install the required libraries:

    ```bash
    pip install requests folium pywebview
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Enter the IP address in the input field and click the "Find Location" button.

3. The application will display the state and country of the IP address and open a new window with an interactive map showing the location.

## Code Explanation

- **get_ip_location(ip)**: Fetches the geographical location of the given IP address using the IP-API service.
- **create_interactive_map(ip)**: Creates an interactive map centered around the location of the IP address and updates the Tkinter UI.
- **open_map_window(map_file)**: Opens the generated HTML map in a new window using `pywebview`.
- **on_submit()**: Handles the submission of the IP address, displays a loading message, and calls the function to create the map.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or feature requests.

## Acknowledgements

- [IP-API](http://ip-api.com) for providing the IP location service.
- [Folium](https://python-visualization.github.io/folium/) for the interactive map generation.
- [Pywebview](https://pywebview.flowrl.com) for displaying the map in a new window.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the user interface.

## CREDIT:
Quy Anh Nguyen - Developer
