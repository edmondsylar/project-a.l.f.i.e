from rich.console import Console
from rich.spinner import Spinner
import time

def spinner_function():
    console = Console()
    with console.status("[bold green]Loading...") as status:
        for i in range(10):
            time.sleep(1)
            status.update(f"[bold green]Loading... {i+1}0%")

import threading
import time

def download_file(file_url):
    print(f"Starting download of {file_url}")
    time.sleep(5) # simulate a long download
    print(f"Finished download of {file_url}")

def handle_request(request):
    if request['type'] == 'download':
        thread = threading.Thread(target=download_file, args=(request['file_url'],))
        thread.start()
        print("Download started in the background")
        print ("New counter below as the download is in progress")
        input("You can interact with the system while the download is in progress. Press enter to continue...")

# Example usage
handle_request({'type': 'download', 'file_url': 'https://example.com/file.txt'})
print("You can continue entering commands while the download is in progress")