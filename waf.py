import re

class SimpleWAF:
    def __init__(self):
        self.rules = [
            re.compile(r'(union.*select.*from.*information_schema.tables)', re.IGNORECASE),  # SQL Injection
            re.compile(r'<script.*>.*</script>', re.IGNORECASE),                          # XSS
        ]
    
    def is_request_safe(self, request):
        for rule in self.rules:
            if rule.search(request):
                return False
        return True

def main():
    waf = SimpleWAF()
    
    while True:
        request = input("Enter HTTP request: ")
        if waf.is_request_safe(request):
            print("Request is safe.")
        else:
            print("Malicious request detected!")

if __name__ == "__main__":
    main()
