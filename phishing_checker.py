
import re
from urllib.parse import urlparse


def check_url(url):

    warnings = []

    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or ""
    except ValueError:
        print("Invalid URL format.")
        return

    # Check 1: HTTP
    if parsed_url.scheme.lower() == "http":
        warnings.append((
            "Uses HTTP instead of HTTPS",
            "HTTP does not provide the same transport encryption as HTTPS.",
            "Use an independently verified official website."
        ))

    # Check 2: @ symbol
    if "@" in url:
        warnings.append((
            "Contains the @ symbol",
            "It can make a misleading URL appear to contain a trusted name.",
            "Check the actual hostname carefully."
        ))

    # Check 3: URL length
    if len(url) > 100:
        warnings.append((
            "URL is longer than 100 characters",
            "Long URLs can hide confusing or unnecessary information.",
            "Read the hostname and path carefully."
        ))

    # Check 4: IP-like hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        warnings.append((
            "Uses an IP-like hostname",
            "An IP address instead of a familiar domain deserves review.",
            "Verify the organisation's official domain independently."
        ))

    # Check 5: Five or more hostname labels
    labels = hostname.split(".")
    if len(labels) >= 5:
        warnings.append((
            "Contains five or more hostname labels",
            "Many hostname parts can make the address harder to read.",
            "Check which organisation controls the actual domain."
        ))

    # Check 6: Punycode marker
    if "xn--" in hostname:
        warnings.append((
            "Contains a punycode-style hostname",
            "International characters may be represented in encoded form.",
            "Verify the domain carefully before trusting it."
        ))

    # Display results
    print("\n----- CHECKING RESULT -----")

    if warnings:
        for number, warning in enumerate(warnings, start=1):
            print(f"\nWarning {number}: {warning[0]}")
            print("Why it matters:", warning[1])
            print("Advice:", warning[2])

        print("\nTotal warnings:", len(warnings))

    else:
        print("No listed warning signs found.")
        print("This does not prove the URL is safe.")


# Main program
print("EWB PHISHING URL AWARENESS CHECKER")

while True:

    url = input("\nEnter a URL to check: ").strip()

    if not url:
        print("Please enter a URL.")
        continue

    check_url(url)

    choice = input(
        "\nCheck another URL? (yes/no): "
    ).strip().lower()

    if choice != "yes":
        print("\nThank you for using the checker!")
        break
