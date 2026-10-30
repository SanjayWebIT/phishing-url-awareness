
# EWB Phishing URL Awareness Checker

## Project Description
This is a beginner-level Python project that checks a URL for selected warning signs that may be associated with phishing.

## Features
The program checks for:

1. HTTP instead of HTTPS
2. The @ symbol in a URL
3. URLs longer than 100 characters
4. IP-like hostnames
5. Five or more hostname labels
6. Punycode-style hostnames

## Technology Used
- Python
- Visual Studio Code
- Python re module
- Python urllib.parse module

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run this command:

   python phishing_checker.py

4. Enter a URL when the program asks.
5. Follow the instructions to check another URL or exit.

## Testing
Six test cases were reported as passing.
See `tests/test_results.md` for the test record.

## Important Safety Note
This tool only checks selected URL warning signs.
It does not visit websites or guarantee that a URL is safe.
A URL with no detected warning signs may still be malicious.

## Author
Name: Sanjay Kushwaha
Batch: [Enter your batch]
