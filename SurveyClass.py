from typing import Optional
import requests
from time import sleep
from colorama import Fore
import sys

class Survey:
    def __init__(self,
                 start_url: Optional[str]=None,
                 proxy: Optional[str]=None,
                 *,
                 sleep: Optional[int]=0, 
                 timeout: Optional[int]=False,
                 output: Optional[bool]=False
        ):
        """_summary_

        Args:
            site_url (list): The sites you're sending requests to
            proxy (Optional[str], optional): The proxy you're using. Defaults to None.
            sleep (Optional[int], optional): sleeps for specified amount of seconds. Defaults to 0.
            timeout (Optional[int], optional): timer before ending connection. Defaults to False.
        """
        
        self.proxy = proxy
        self.sleep = sleep
        self.timeout = timeout
        self.start_url = start_url
        self.output = output
        self.sent_requests = 0
        
    def __repr__(self) -> object:
        return f"Survey(sleep={self.sleep}, timeout={self.timeout}"
    
    def _send_requests(self, headers, _url, _payloads=None, *, repeat=1):
        with requests.Session() as session:
            if isinstance(self.start_url, str):
                session.get(self.start_url, allow_redirects=True)
                if self.output:  
                    sys.stdout.write(f"{Fore.LIGHTCYAN_EX}Wrote Starting request...\n")
            for _ in range(len(_payloads)):
                for i in range(repeat):
                    try:
                        a=session.post(_url, headers=headers, data=_payloads[self.sent_requests], allow_redirects=True)
                    except IndexError:
                        break
                    self.sent_requests +=1
                    if self.output:    
                        sys.stdout.write(f"{Fore.MAGENTA}[{Fore.LIGHTGREEN_EX}{a.status_code}{Fore.MAGENTA}]~ Sent {self.sent_requests} requests!" +"\n")
                    sleep(self.sleep)
        return