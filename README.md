# Password Manager

A Python GUI application to generate, save, and retrieve passwords for different websites. Users can generate strong random passwords, save them along with their email/username, and search for stored credentials.

## Key Features / Concepts
- GUI development with `tkinter`
- Random password generation with letters, numbers, and symbols
- Copy passwords to clipboard with `pyperclip`
- Save and read credentials using JSON
- Error handling and input validation
- Search functionality to quickly retrieve saved passwords

## Example Usage
1. Open the app:
`python main.py`
2. Enter the website, email/username, and either generate a password or type one in.
3. Click **Add** to save credentials.
4. Click **Search** to retrieve saved passwords for a website.
5. Click **Generate Password** to generate a random password instead of creating your own. 

## Files
- `main.py` – main Python program
- `logo.png` – application logo
- `data.json` – stores saved credentials (automatically created when adding your first password)

## Notes / Learning Points
- Learned to integrate GUI with backend data storage
- Practiced JSON file handling for storing structured data
- Implemented error handling and input validation for robust application

## How to Run
1. Clone this repository:  
`git clone <your-repo-url>`
2. Make sure you have the required modules installed:  
`pip install pyperclip`
3. Navigate to the project folder and run:  
`python main.py`
## License
This project is licensed under the MIT License.
