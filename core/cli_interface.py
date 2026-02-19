"""
CLI Interface with hacking-themed design
"""

import time
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

class SingularityCLI:
    def __init__(self):
        self.prompt = f"{Fore.GREEN}[S!NGUL4RITY]{Fore.CYAN} > {Style.RESET_ALL}"
        
    def display_banner(self):
        banner = f"""
{Fore.RED}
 ████████╗██╗  ██╗███████╗    ███████╗██╗███╗   ██╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗ ██╗████████╗██╗   ██╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║████╗  ██║██╔════╝ ██║   ██║██║     ██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
   ██║   ███████║█████╗      ███████╗██║██╔██╗ ██║██║  ███╗██║   ██║██║     ███████║██████╔╝██║   ██║    ╚████╔╝ 
   ██║   ██╔══██║██╔══╝      ╚════██║██║██║╚██╗██║██║   ██║██║   ██║██║     ██╔══██║██╔══██╗██║   ██║     ╚██╔╝  
   ██║   ██║  ██║███████╗    ███████║██║██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║██║   ██║      ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
{Style.RESET_ALL}
{Fore.CYAN}                           AI-Powered Intelligence Framework v1.0{Style.RESET_ALL}
{Fore.YELLOW}                              Criminal Network Analysis System{Style.RESET_ALL}
"""
        print(banner)
        self._animate_loading()
        
    def _animate_loading(self):
        chars = "/-\\|"
        for i in range(20):
            sys.stdout.write(f"\r{Fore.GREEN}[{chars[i % len(chars)]}] Initializing systems...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
        print(f"\n{Fore.GREEN}[✓] All systems operational{Style.RESET_ALL}\n")
        
    def get_input(self):
        return input(self.prompt)
        
    def status(self, message):
        print(f"{Fore.YELLOW}[*] {message}{Style.RESET_ALL}")
        
    def success(self, message):
        print(f"{Fore.GREEN}[✓] {message}{Style.RESET_ALL}")
        
    def error(self, message):
        print(f"{Fore.RED}[✗] {message}{Style.RESET_ALL}")
        
    def warning(self, message):
        print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")
        
    def progress_bar(self, current, total, prefix="Progress"):
        percent = int(100 * (current / float(total)))
        bar = '█' * int(percent / 2) + '-' * (50 - int(percent / 2))
        print(f"\r{Fore.CYAN}{prefix}: |{bar}| {percent}%{Style.RESET_ALL}", end='')
        if current == total:
            print()