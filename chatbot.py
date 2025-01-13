import random
def load_txt(filename):
    #to read the contents of responses.txt and put the keyword as dictionary and random reponse as list 
    config={"keywords":{},"random_responses":[]}
    try:
        with open(filename,"r") as file:
            section=None
            for line in file:
                line=line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.endswith(":"):
                    section=line[:-1].strip().lower()
                elif section=="keywords":
                    key,value=map(str.strip,line.split(":",1))
                    config["keywords"][key.lower()]=value
                elif section=="random_responses":
                    config["random_responses"].append(line)
    except FileNotFoundError:
        print(f"file '{filename}' not found.")
    return config

def signup_login():
    # set up ui for login and signup 
    print("If you are an old user, please log in. If new, sign up first.")
    action=input("enter 'login' or 'signup':").strip().lower()
    
    if action=="signup":
        username=input("enter username:")
        password=input("enter password:")
        with open("project2/user.txt","a") as file:
            file.write(f"{username},{password}\n")
        print(f"sign up successful! please log in {username}.")
        return None
    elif action=="login":
         username=input("username=")
         password=input("password=")
         try:
             with open("project2/user.txt","r") as file:
                for line in file:
                    saved_username,saved_password=line.strip().split(",")
                    if username==saved_username and password==saved_password:
                        print(f"login Successfull! welcome {username}")
                        return username
         except FileNotFoundError:
            print("user not found. please sign in!")
         print("invalid username or password.")
    else:
        print("invalid input. please try again.")
    return None

def chatbot(username, config):
    #set up dialogue ui between user and chatbot
    print(f"Hello, {username}! Type 'bye' to exit.")
    while True:
        user_input=input(f"{username}:").strip().lower()
        if user_input in {"bye","exit","quit"}:
            print(f"chatbot: goodbye, {username}!")
            break
        responded=False
        for keyword,response in config["keywords"].items():
            if keyword in user_input:
                print(f"chatbot:{response}")
                responded=True
                break
        if not responded:
            random_response=random.choice(config["random_responses"]) if config["random_responses"] else print("I do not understand, what you want.")
            print(f"chatbot:{random_response}")
            
def ai_page():
    #main page where all function are called and put together
    username=signup_login()
    if username:
        config=load_txt("project2/responses.txt")
        if config["keywords"] or config["random_responses"]:
            chatbot(username,config)
        else:
            print("chatbot response file is empty.")
    else:
        print("please log in to use chatbot.")  

# Call the function
ai_page()

