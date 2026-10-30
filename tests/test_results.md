
# EWB Phishing URL Awareness Checker
## Test Results

| Test No. | Feature Tested | Result |
|---|---|---|
| 1 | HTTP instead of HTTPS | PASS |
| 2 | @ symbol | PASS |
| 3 | URL longer than 100 characters | PASS |
| 4 | IP-like hostname | PASS |
| 5 | Five or more hostname labels | PASS |
| 6 | Punycode marker | PASS |

## Final Result

All six reported tests passed successfully.

The program detects selected URL warning signs.
No warning signs found does not guarantee that a URL is safe.
