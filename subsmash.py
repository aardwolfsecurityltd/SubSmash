import requests
import threading
import os
from tqdm import tqdm

# Define a function to test subdomains
def test_subdomains(domain_name, wordlist, progress, results):
    for word in wordlist:
        subdomain = f"{word}.{domain_name}"
        url = f"http://{subdomain}"
        try:
            response = requests.get(url)
            if response.status_code < 400:
                results.append(subdomain)
        except:
            pass
        progress.update(1)

# Define a function to get the wordlist file path
def get_wordlist_path():
    wordlist_path = input("Enter the path to your wordlist file (or leave blank to use default): ")
    if wordlist_path == "":
        wordlist_path = "subdomains-top1million-5000.txt"
    return wordlist_path

# Get the domain name from the user
domain_name = input("Enter a domain name (e.g., example.com): ")

# Get the wordlist file path from the user
wordlist_path = get_wordlist_path()

# Check if the wordlist file exists
if not os.path.exists(wordlist_path):
    print(f"Wordlist not found: {wordlist_path}")
    download = input("Do you want to download the default wordlist? (y/n): ")
    if download.lower() == "y":
        # Download the default wordlist
        wordlist_url = "https://github.com/danielmiessler/SecLists/raw/master/Discovery/DNS/subdomains-top1million-5000.txt"
        response = requests.get(wordlist_url)
        with open("subdomains-top1million-5000.txt", "wb") as f:
            f.write(response.content)
        wordlist_path = "subdomains-top1million-5000.txt"
        print(f"Wordlist downloaded: {wordlist_path}")
    else:
        print("Exiting script.")
        exit()

# Open the wordlist file and read the contents
with open(wordlist_path, "r") as f:
    wordlist = f.read().splitlines()

# Divide the wordlist into chunks based on the number of threads
num_threads = 50
chunk_size = len(wordlist) // num_threads
chunks = [wordlist[i:i + chunk_size] for i in range(0, len(wordlist), chunk_size)]

# Create a list to hold the threads
threads = []

# Create a progress bar for the total number of subdomains to test
total_subdomains = len(wordlist)
progress = tqdm(total=total_subdomains, desc="Testing subdomains")

# Create a list to hold the subdomains discovered
results = []

# Create and start a thread for each chunk of the wordlist
for i in range(num_threads):
    thread = threading.Thread(target=test_subdomains, args=(domain_name, chunks[i], progress, results))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close the progress bar
progress.close()

# Print the results
if len(results) > 0:
    print("Subdomains found:")
    for result in results:
        print(result)
else:
    print("No subdomains found.")
