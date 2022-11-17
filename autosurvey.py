from SurveyClass import Survey
from colorama import Fore, init
import sys
import threading
from string import ascii_lowercase, digits
from random import choice
from os import system


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117",
                "origin": "https://survey.alchemer.eu",
                "referer": "https://survey.alchemer.eu/s3/90491875/c13926a7cd5f"}

completed_surveys = 0

def create_payload():
    session_id = generateSessionId()
    return [{
        "sg_navchoice": "",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_currentpageid": "12",
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "2",
        "sgd7bedb5b6ae56e4a57a0fb385acab70d": "2094434569",
        "sgE-90491875-12-4-meta": "hidden=false&required=true",
        "sgE-90491875-12-4-time": "0.013",
        "sgE-90491875-12-4-10427": "10427",
        "sgE-90491875-12-4-10429": "10429",
        "sgE-90491875-12-4-10685": "10685",
        "sgE-90491875-12-4-10569": "10569",
        "sgE-90491875-12-4-10434-other": ""
    },
            
    {
        "sg_navchoice": "",
        "sg_currentpageid": "17",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "3",
        "sge897da870e33a032ebb9305d0f0395d3": "2094434569",
        "sgE-90491875-17-74-meta": "hidden=true&required=true",
        "sgE-90491875-17-74-time": "0.033",
        "sgE-90491875-17-74-10736-other": "",
        "sgE-90491875-17-5-meta": "hidden=true&required=true",
        "sgE-90491875-17-5-time": "0.052",
        "sgE-90491875-17-5-10450-other": "",
        "sgE-90491875-17-76-meta": "hidden=false&required=true",
        "sgE-90491875-17-76-time": "0.022",
        "sgE-90491875-17-76-10761": "10761",
        "sgE-90491875-17-76-10763": "10763",
        "sgE-90491875-17-76-10762": "10762",
        "sgE-90491875-17-76-10771": "10771",
        "sgE-90491875-17-76-10759": "10759",
        "sgE-90491875-17-76-10767": "10767",
        "sgE-90491875-17-76-10768": "10768",
        "sgE-90491875-17-76-10777-other": "",
        "sgE-90491875-17-75-meta": "hidden=true&required=true",
        "sgE-90491875-17-75-time": "0.043",
        "sgE-90491875-17-75-10757-other": "",
        "sGizmoNextButton": "Next",
    },
    {
        "sg_navchoice": "",
        "sg_currentpageid": "20",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "4",
        "sg2df080d9d4659deac0dbde30f92edb66": "2094434569",
        "sgE-90491875-20-104-meta": "hidden=false&required=true",
        "sgE-90491875-20-104-time": "645.623",
        "sgE-90491875-20-107-meta": "hidden=false&required=false",
        "sgE-90491875-20-106-meta": "hidden=false&required=false",
        "sgE-90491875-20-108-meta": "hidden=false&required=false",
        "sgE-90491875-20-105-meta": "hidden=false&required=false",
        "sgE-90491875-20-107": "10943",
        "sgE-90491875-20-106": "10943",
        "sgE-90491875-20-108": "10943",
        "sgE-90491875-20-105": "10943",
        "sGizmoNextButton": "Next",
    },
    {
        "sg_navchoice": "",
        "sg_currentpageid": "18",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "7",
        "sgabbbe0014ba75266f3305800e9686e10": "2094434569",
        "sgE-90491875-18-68-meta": "hidden=false&required=true",
        "sgE-90491875-18-68-time": "0.029",
        "sgE-90491875-18-68-10699": "10699",
        "sgE-90491875-18-68-10697": "10697",
        "sGizmoNextButton": "Next"
    },
    {
        "sg_navchoice": "",
        "sg_currentpageid": "4",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "8",
        "sg6a8b790ac0b7a320174bd3f7654026bc": "2094434569",
        "sgE-90491875-4-18-meta": "hidden=false&required=true",
        "sgE-90491875-4-18-time": "0.059",
        "sgE-90491875-4-18-10485": "10485",
        "sgE-90491875-4-18-10491-other": "",
        "sGizmoNextButton": "Next"
    },
    
    {
        "sg_navchoice": "",
        "sg_currentpageid": "6",
        "sg_surveyident": "90491875",
        "sg_sessionid": session_id,
        "sg_high_contrast": "false",
        "sg_cint_panelist": "",
        "sg_interactionlevel": "9",
        "sg6d5e3ed6f80b20dcb80e49329cad56c5": "2094434569",
        "sgE-90491875-6-66-meta": "hidden=false&required=true",
        "sgE-90491875-6-66-time": "164.984",
        "sgE-90491875-6-66": "10677",
        "sgE-90491875-6-66-10682-other": "",
        "sgE-90491875-6-73-meta": "hidden=false&required=true",
        "sgE-90491875-6-73-time": "2.046",
        "sgE-90491875-6-73": "10710",
        "sgE-90491875-6-20-meta": "hidden=false&required=true",
        "sgE-90491875-6-20-time": "13.672",
        "sgE-90491875-6-20": "10262",
        "sgE-90491875-6-12-meta": "hidden=false&required=true",
        "sgE-90491875-6-12-time": "0.044",
        "sgE-90491875-6-12-10146": "10146",
        "sgE-90491875-6-12-10151": "10151",
        "sgE-90491875-6-12-10150": "10150",
        "sGizmoSubmitButton": "Submit",
    }
]


    
def generateSessionId() -> str:
    return "1665323" + "".join(choice(str(digits)) for i in range(3)) + "_6342d" + "".join(choice(digits)) \
        + "".join(choice(digits + ascii_lowercase) for i in range(8)) + "." + "".join(choice(digits) for i in range(8))

        

def CompleteSurvey(repeat, output, sleep) -> None:
    if not output:
        class Values:
            PERCENTAGE_1 = repeat / 100 * 25 
            PERCENTAGE_2 = repeat / 100 * 50 
            PERCENTAGE_3 = repeat/ 100 * 75
            PERCENTAGE_4 = repeat
    global completed_surveys
    payloads = create_payload()
    s = Survey("https://geeklab.app/store/redirect/?storeurl=https://survey.alchemer.eu/s3/90491875/c13926a7cd5f?llc=on", sleep=sleep, output=output)
    s._send_requests(headers, "https://survey.alchemer.eu/s3/90491875/c13926a7cd5f", payloads, repeat=repeat)
    completed_surveys +=1
    if output:   
        sys.stdout.write(f"{Fore.LIGHTGREEN_EX}{completed_surveys} Surveys Completed!" + "\n")
        
    if not output:
        match completed_surveys:
            case Values.PERCENTAGE_1:
                sys.stdout.write(f"\r{Fore.YELLOW}[██______] {completed_surveys}/{surveys} Surveys completed...\r")
                
            case Values.PERCENTAGE_2:
                sys.stdout.write(f"\r{Fore.YELLOW}[████____] {completed_surveys}/{surveys} Surveys completed...\r")
                
            case Values.PERCENTAGE_3:
                sys.stdout.write(f"\r{Fore.YELLOW}[██████__] {completed_surveys}/{surveys} Surveys completed...\r")
                
            case Values.PERCENTAGE_4:
                sys.stdout.write(f"\r{Fore.YELLOW}[████████] {completed_surveys}/{surveys} Surveys completed...\r\n")
                
            case _:
                sys.stdout.write(f"\r{Fore.YELLOW}[________] {completed_surveys}/{surveys} Surveys completed...\r")

def main():
    global surveys
    try:  
        try:  
            surveys = int(input(f"{Fore.CYAN}How many surveys do you want to bot: "))
            sleep = int(input(f"{Fore.CYAN}How many seconds do you want to sleep after every question answered: "))
        except ValueError:
            surveys = 2
            sleep = 2
        output = input(f"{Fore.CYAN}Do you want request output (y/n): ").lower()
        match output:
            case "y":
                output=True
            case "n":
                output=False
            case "_":
                pass
        if not output:
            sys.stdout.write(f"\r{Fore.YELLOW}[________] 0/{surveys} Surveys completed...\r")
        
        
        for thread in (threads := [threading.Thread(target=CompleteSurvey, args=(surveys, output, sleep,)) for _ in range(surveys)]):
            thread.start()
            
        threads = [thread.join() for thread in threads]
    except KeyboardInterrupt:
        init(autoreset=True)
        raise KeyboardInterrupt
    main()
                
if __name__ == "__main__":
    system('cls')
    main()     