import requests
import threading

# Define a function to test subdomains
def test_subdomains(domain_name, wordlist):
    for word in wordlist:
        subdomain = f"{word}.{domain_name}"
        url = f"http://{subdomain}"
        try:
            response = requests.get(url)
            if response.status_code < 400:
                print(f"Subdomain found: {subdomain}")
        except:
            pass

# Get the domain name from the user
domain_name = input("Enter a domain name (e.g., example.com): ")

# Open the wordlist file and read the contents
with open("wordlist.txt", "r") as f:
    wordlist = f.read().splitlines()

# Divide the wordlist into chunks based on the number of threads
num_threads = 4
chunk_size = len(wordlist) // num_threads
chunks = [wordlist[i:i + chunk_size] for i in range(0, len(wordlist), chunk_size)]

# Create a list to hold the threads
threads = []

# Create and start a thread for each chunk of the wordlist
for i in range(num_threads):
    thread = threading.Thread(target=test_subdomains, args=(domain_name, chunks[i]))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
