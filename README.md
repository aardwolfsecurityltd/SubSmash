# SubSmash

This Python script searches for subdomains of a given domain name. It does this by testing all possible subdomains using a wordlist of common subdomains. The script uses multi-processing to speed up the process.

## Installation

1. Install Python 3.x
2. Install `requests` module: `pip install requests`
3. Install `tqdm` module: `pip install tqdm`
4. Clone this repository: `git clone https://github.com/username/repo.git`

## Usage

1. Navigate to the directory where the script is located.
2. Run the script: `python subdomain_enumerator.py`
3. Enter the domain name when prompted (e.g., example.com).
4. Optionally, enter the path to a custom wordlist file or leave it blank to use the default wordlist.
5. Wait for the script to finish running.

## Acknowledgments

This script was inspired by a similar script created by Daniel Miessler. The default wordlist used in this script is also from his repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
