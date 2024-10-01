import os
import sys
import time
import json
import random
import requests
import subprocess
from colorama import Fore, Style, init
from fake_useragent import UserAgent

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m-------------[MoonBix Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def install_npm_if_needed():
    current_directory = os.getcwd()
    node_modules_path = os.path.join(current_directory, 'node_modules')
    
    if not os.path.exists(node_modules_path):
        command = ["npm", "install"]

        try:
            subprocess.run(command, cwd=current_directory, check=True)
            main()
        except subprocess.CalledProcessError as e:
            print(f"Error during npm install: {e}")


def load_queries(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def load_proxies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(query):
    ua = UserAgent()
    return {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://www.binance.com",
        "Referer": "https://www.binance.com/en/game/tg/moon-bix?tgWebAppStartParam=ref_5496274031",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "User-Agent": ua.random
    }

def get_token(query, proxy=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/third-party/access/accessToken"
    headers = get_headers(query)
    body = {"queryString": query, "socialType": "telegram"}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
        data = response.json()
        access_token = data.get("data", {}).get("accessToken")
        if access_token is None:
            print(f"{Fore.RED + Style.BRIGHT}Failed to retrieve access token.")
            return None
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")
        return None

def re(access_token, query, proxy=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/referral"
    headers = get_headers(query)
    headers["X-Growth-Token"] = access_token
    body = {"resourceId": 2056, "agentId": "5496274031"}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def user_data(access_token, query, proxy=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/user/user-info"
    headers = get_headers(query)
    headers["X-Growth-Token"] = access_token
    body = {"resourceId": 2056}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
        data = response.json()

        total_grade = data.get("data", {}).get("metaInfo", {}).get("totalGrade", 0) or 0
        referral_total_grade = data.get("data", {}).get("metaInfo", {}).get("referralTotalGrade", 0) or 0
        total_attempts = data.get("data", {}).get("metaInfo", {}).get("totalAttempts", 0) or 0
        consumed_attempts = data.get("data", {}).get("metaInfo", {}).get("consumedAttempts", 0) or 0

        balance = int(total_grade) + int(referral_total_grade)
        play_pass = max(0, int(total_attempts) - int(consumed_attempts))

        print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance} | {Fore.MAGENTA + Style.BRIGHT}Play Pass: {Fore.WHITE + Style.BRIGHT}{play_pass}/6")
        return {'balance': balance, 'play_pass': play_pass}  # Return as a dict
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def task_complete(access_token, query, proxy=None):
    task_list_url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/task/list"
    task_comp_url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/task/complete"
    headers = get_headers(query)
    headers["X-Growth-Token"] = access_token
    body = {"resourceId": 2056}

    try:
        response = requests.post(task_list_url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data and 'data' in data['data']:
            for task in data['data']['data']:
                for sub_task in task.get('taskList', {}).get('data', []):
                    sub_resource_id = sub_task['resourceId']
                    task_status = sub_task['status']
                    code = sub_task['rewardList'][0].get('code')
                    amount = sub_task['rewardList'][0].get('amount')
                    
                    if task_status == 'COMPLETED':
                        print(f"{Fore.YELLOW + Style.BRIGHT}Task {Fore.WHITE + Style.BRIGHT}'{code}' {Fore.YELLOW + Style.BRIGHT}Already Completed")
                    else:
                        complete_body = {"resourceIdList": [sub_resource_id], "referralCode": None}
                        complete_response = requests.post(task_comp_url, headers=headers, json=complete_body, proxies=proxy)
                        if complete_response.status_code == 200:
                            print(f"{Fore.GREEN + Style.BRIGHT}Task WHITE'{code}' {Fore.GREEN + Style.BRIGHT}Complete")
                            print(f"{Fore.CYAN + Style.BRIGHT}Task Reward: {Fore.WHITE + Style.BRIGHT}{amount}")
                        else:
                            print(f"{Fore.RED + Style.BRIGHT}Failed to complete task with Resource ID '{code}'")
        else:
            print("No tasks found in the response.")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def start_game(access_token, query, proxy=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/game/start"
    headers = get_headers(query)
    headers["X-Growth-Token"] = access_token
    body = {"resourceId": 2056}

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
        data = response.json()
        code = data.get("code")
        
        if code == "000000":
            start_time = time.time()
            while time.time() - start_time < 45:
                for i in range(4):
                    sys.stdout.write(f"\r{Fore.YELLOW}{Style.BRIGHT}Playing{Fore.WHITE}{Style.BRIGHT}{'.' * i} {Style.RESET_ALL}")
                    sys.stdout.flush()
                    time.sleep(0.5)
                sys.stdout.write(f"\r{Fore.YELLOW}{Style.BRIGHT}Playing{Style.RESET_ALL} " + " " * 4)
                sys.stdout.flush()
                time.sleep(0.5)
                
            sys.stdout.flush()
            sys.stdout.write('\r' + ' ' * len(f"{Fore.YELLOW}{Style.BRIGHT}Playing{Style.RESET_ALL} " + " " * 4))
            sys.stdout.write('\r')
            
            return data
        else:
            print(data)
            print(response.status_code)
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def get_game_data(data):
    try:
        start_time = time.time()
        end_time = int(start_time + 45000)
        game_tag = data['data']['gameTag']
        item_settings = data['data']['cryptoMinerConfig']['itemSettingList']

        current_time = int(start_time)
        score = 100
        game_events = []

        while current_time < end_time:
            time_increment = random.randint(1500, 2500)
            current_time += time_increment

            if current_time >= end_time:
                break

            hook_pos_x = round(random.uniform(75, 275), 3)
            hook_pos_y = round(random.uniform(199, 251), 3)
            hook_shot_angle = round(random.uniform(-1, 1), 3)
            hook_hit_x = round(random.uniform(100, 400), 3)
            hook_hit_y = round(random.uniform(250, 700), 3)

            item_type, item_size, points = 0, 0, 0
            random_value = random.random()

            if random_value < 0.6:
                reward_items = [item for item in item_settings if item['type'] == 'REWARD']
                selected_reward = random.choice(reward_items)
                item_type = 1
                item_size = selected_reward['size']
                points = min(selected_reward['rewardValueList'][0], 10)
                score = min(score + points, 200)
            elif random_value < 0.8:
                trap_items = [item for item in item_settings if item['type'] == 'TRAP']
                selected_trap = random.choice(trap_items)
                item_type = 1
                item_size = selected_trap['size']
                points = min(abs(selected_trap['rewardValueList'][0]), 20)
                score = max(100, score - points)
            else:
                bonus_item = next((item for item in item_settings if item['type'] == 'BONUS'), None)
                if bonus_item:
                    item_type = 2
                    item_size = bonus_item['size']
                    points = min(bonus_item['rewardValueList'][0], 15)
                    score = min(score + points, 200)

            event_data = f"{current_time}|{hook_pos_x}|{hook_pos_y}|{hook_shot_angle}|{hook_hit_x}|{hook_hit_y}|{item_type}|{item_size}|{points}"
            game_events.append(event_data)

        payload = ';'.join(game_events)
        
        with open('.pg.txt', 'w') as file:
        	file.write(f"{payload}\n{game_tag}")
        
        
        subprocess.run(['node', '.encrypt.js'])
        
        time.sleep(5)
        
        with open('.ep.txt', 'r') as file:
        	encrypted_payload = file.read().strip()

        game = {
            'payload': encrypted_payload,
            'log': score
        }
        return game

    except Exception as error:
        print(f"{Fore.RED + Style.BRIGHT}Error in get_game_data: {error}", 'error')
        return None

            
def complete_game(game, access_token, query, proxy=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/mini-app-activity/third-party/game/complete"
    headers = get_headers(query)
    headers["X-Growth-Token"] = access_token
    
    string_payload = game["payload"]
    body = {
        "resourceId": 2056,
        "payload": string_payload,
        "log": game["log"]
    }
    
    score = game["log"]

    try:
        response = requests.post(url, headers=headers, json=body, proxies=proxy)
        response.raise_for_status()
        data = response.json()
        print(f"{Fore.GREEN + Style.BRIGHT}Playing Reward: {Fore.WHITE + Style.BRIGHT}{score}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def main():
    queries = load_queries('data.txt')
    proxies = load_proxies('proxy.txt') if os.path.exists('proxy.txt') else None
    total_accounts = len(queries)
    
    clear_terminal()
    art()
    use_proxy = input(f"{Fore.CYAN}Do you want to use a proxy? (y/n): ").strip().lower()
    clear_terminal()
    art()
    
    while True:
        print(f"{Fore.MAGENTA + Style.BRIGHT}Total Accounts: {Fore.WHITE + Style.BRIGHT}{total_accounts}{Style.RESET_ALL}\n")
        
        for i, query in enumerate(queries, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{i}------{Style.RESET_ALL}")
            proxy = None
            
            if use_proxy == 'y' and proxies:
                proxy = {
                    "http": f"http://{proxies[i % len(proxies)]}",
                    "https": f"http://{proxies[i % len(proxies)]}"
                }
                formatted_proxy = f"{proxy['http'].split('@')[-1].split(':')[0][:4]}.....{proxy['http'].split('@')[-1].split(':')[1]}"
                print(f"{Fore.YELLOW + Style.BRIGHT}Using Proxy: {formatted_proxy}{Style.RESET_ALL}")
    
            try:
                install_npm_if_needed()
                access_token = get_token(query, proxy)
                
                if access_token:
                    user_info = user_data(access_token, query, proxy)
                    re(access_token, query, proxy)
                    task_complete(access_token, query, proxy)

                    while True:
                        user_info = user_data(access_token, query, proxy)
                        play_pass = user_info['play_pass']
                        
                        if play_pass <= 0:
                            print(f"{Fore.RED + Style.BRIGHT}Play Pass is 0{Style.RESET_ALL}")
                            break
                            
                        data = start_game(access_token, query, proxy)
                        game = get_game_data(data)
                        complete_game(game, access_token, query, proxy)

                else:
                    print(f"{Fore.RED + Style.BRIGHT}Failed to retrieve access token for Account No.{i}. Skipping account.")

            except Exception as e:
                print(f"Error processing account {i}: {e}")
                continue
            countdown_timer(5)
              
        countdown_timer(1 * 5 * 60)

if __name__ == "__main__":
    init()
    main()