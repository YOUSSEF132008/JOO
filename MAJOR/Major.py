import sys 
import time
#I am the developer, my name is Youssef 💙🤍
import os
from os import system as ss
ll = 'pip install'
try:
	from cfonts import render
except ModuleNotFoundError:
	ss(ll+' python-cfonts')
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

sys.dont_write_bytecode = True

from smart_airdrop_claimer import base
from core.token import get_token
from core.info import get_balance
from core.task import process_check_in, process_do_task
from core.reward import (
    process_hold_coin,
    process_spin,
    process_swipe_coin,
    process_puzzle_durov,
)

d = "YOUSEF"

sif = render(f'{d}', colors=['red', 'yellow'], align='center')
print(sif)

print("""\033[1;37m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                    
║\33[0;41m        [ ENTER THE TOOL'S PASSWORD ✅ ]    \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝              """)
password = 'YOUSSEFELJOO'
one = str(input('''❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 :  ''') )
if one == password:
    print(f"""
𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐥𝐨𝐠𝐠𝐞𝐝 𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥 ⚡ """)
    time.sleep(1)
else:
    exit("""
𝚃𝚑𝚎 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝚒𝚜 𝚒𝚗𝚌𝚘𝚛𝚛𝚎𝚌𝚝 ❌ 
𝙿𝚕𝚎𝚊𝚜𝚎 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚝𝚑𝚎 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚝𝚘 𝚏𝚒𝚗𝚍 𝚘𝚞𝚝 @𝚈𝙾𝚄𝚂𝚂𝙴𝙵𝚂𝙾𝙱𝙷𝚈𝟷𝟹 ✅""")
os.system('clear')


class Major:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="JOO.txt")
        self.config_file = base.file_path(file_name="config.json")
        self.durov_file = base.file_path(file_name="durov.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="Major")

        # Get config
        self.auto_check_in = base.get_config(
            config_file=self.config_file, config_name="auto-check-in"
        )

        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_play_hold_coin = base.get_config(
            config_file=self.config_file, config_name="auto-play-hold-coin"
        )

        self.auto_spin = base.get_config(
            config_file=self.config_file, config_name="auto-spin"
        )

        self.auto_play_swipe_coin = base.get_config(
            config_file=self.config_file, config_name="auto-play-swipe-coin"
        )

        self.auto_play_puzzle_durov = base.get_config(
            config_file=self.config_file, config_name="auto-play-puzzle-durov"
        )

    def main(self):
        while True:
            base.clear_terminal()
            d = "YOUSEF"
            JOONY = render(f'{d}', colors=['green', 'yellow'], align='center')
            print(JOONY)
            print('''\n \x1b[38;5;196m\n███████████████████████████\n███████▀▀▀░░░░░░░▀▀▀███████\n████▀░░░░░░░░░░░░░░░░░▀████\n███│░░░░░░░░░░░░░░░░░░░│███\n██▌│░░░░░░░░░░░░░░░░░░░│▐██\n██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░│██████▌░░░▐██████│░▐██\n███░│▐███▀▀░░▄░░▀▀███▌│░███\n██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n████▄─┘██▌░░░░░░░▐██└─▄████\n█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n███████▄░░░░░░░░░░░▄███████\n██████████▄▄▄▄▄▄▄██████████\n███████████████████████████⠀\n''')
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Numer of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    token = get_token(data=data)

                    if token:

                        get_balance(token=token)

                        # Check in
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                        # Do task
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                        # Hold Coin
                        if self.auto_play_hold_coin:
                            base.log(
                                f"{base.yellow}Auto Play Hold Coin: {base.green}ON"
                            )
                            process_hold_coin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Play Hold Coin: {base.red}OFF")

                        # Spin
                        if self.auto_spin:
                            base.log(f"{base.yellow}Auto Spin: {base.green}ON")
                            process_spin(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Spin: {base.red}OFF")

                        # Swipe Coin
                        if self.auto_play_swipe_coin:
                            base.log(
                                f"{base.yellow}Auto Play Swipe Coin: {base.green}ON"
                            )
                            process_swipe_coin(token=token)
                        else:
                            base.log(
                                f"{base.yellow}Auto Play Swipe Coin: {base.red}OFF"
                            )

                        # Puzzle Durov
                        if self.auto_play_puzzle_durov:
                            base.log(
                                f"{base.yellow}Auto Play Puzzle Durov: {base.green}ON"
                            )
                            process_puzzle_durov(
                                token=token, durov_file=self.durov_file
                            )
                        else:
                            base.log(
                                f"{base.yellow}Auto Play Puzzle Durov: {base.red}OFF"
                            )

                        get_balance(token=token)

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 60 * 60
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        major = Major()
        major.main()
    except KeyboardInterrupt:
        sys.exit()
