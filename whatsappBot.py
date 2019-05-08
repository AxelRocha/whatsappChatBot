from selenium import webdriver
#from bs4 import BeautifulSoup
from time import sleep

#chat imports
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com')


bot_users = {} # A dictionary that stores all the users that sent activate bot 

def bot_chatting():
	while True:
		unread = browser.find_elements_by_class_name("OUeyt") # The green dot tells us that the message is new
		name,message  = '',''
		if len(unread) > 0:
			ele = unread[-1]
			action = webdriver.common.action_chains.ActionChains(browser)
			action.move_to_element_with_offset(ele, 0, -20) # move a bit to the left from the green dot
			
			# Clicking couple of times because sometimes whatsapp web responds after two clicks
			try:
				action.click()
				action.perform()
				action.click()
				action.perform()
			except Exception as e:
				pass
			try:
				#name = browser.find_element_by_class_name("_3TEwt").text  # Contact name
				name = browser.find_element_by_class_name("_1wjpf").text  # Contact name
				#message = browser.find_elements_by_class_name("vW7d1")[-1]  # the message content
				#message = browser.find_elements_by_class_name("Tkt2p")[-1]  # the message content
				message = browser.find_elements_by_class_name("_3zb-j")[-1]  # the message content
				#if 'activate bot' in message.text.lower():
				
				if (message.text.lower().find('ativar bot') != -1):
					if name not in bot_users:
						bot_users[name] = True
						text_box = browser.find_element_by_class_name("_2S1VP")
						response = "Olá, " + name + ". Bot ativado!\n"
						text_box.send_keys(response)

				if name in bot_users:
					text_box = browser.find_element_by_class_name("_2S1VP")
					#response = message.text + "\n"
					#text_box.send_keys(response)

					#bot respondendo no chat
					response = name + " disse: " + message.text
					client_socket.send(bytes(response, "utf8"))
						
					if (message.text.lower().find('desativar') != -1):
						if name in bot_users:
							text_box = browser.find_element_by_class_name("_2S1VP")
							response = "Tchau "+name+".\n"
							text_box.send_keys(response)
							del bot_users[name]

				idle = browser.find_element_by_class_name("_2wP_Y").e
			except Exception as e:
				print(e)
				pass
		#sleep(2) # A 2 second pause so that the program doesn't run too fast

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
	#mandando msg duas vezes ????
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Bot Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbarY = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.

# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=80, yscrollcommand=scrollbarY.set)
scrollbarY.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)


#----Now comes the sockets part----
#HOST = input('Enter host: ')
HOST = "127.0.0.1"
#PORT = input('Enter port: ')
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

#ativar usuario do bot no chat
msg = "Bot"
client_socket.send(bytes(msg, "utf8"))

receive_thread = Thread(target=receive)
receive_thread.start()
whats_thread = Thread(target=bot_chatting)
whats_thread.start()
tkinter.mainloop()  # Starts GUI execution.