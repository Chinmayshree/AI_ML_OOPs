
class chatbook:
    
    def __init__(self):
        
        self.userName= ''
        self.passWord= ''
        self.loggedIn= False
        self.menu()
    
    
    def menu(self):
            
           user_input =input('''Welcome to chatbook...How would you like to proceed?
                   
                1.press 1 to signUp
                2.press 2 to signIn
                3.press 3 to write a Post
                4.press 4 to write a message
                5.press any other key to exit''')
           
           if user_input == '1':
               self.signUp()
           elif user_input =='2':
                self.signIn()
           elif user_input =='3':
               self.my_post()
           elif user_input =='4':
               self.my_msg()
           else:
               exit()
               
               
               
    def signUp(self):
        uName = input('enter your email here: ')
        passwd = input("set your password here: ")
        self.userName = uName
        self.passWord = passwd
        print("You have sucessfully Signed-In into the Chatbook")
        print("\n")
        self.menu()
        self.my_msg()
    
    def signIn(self):
         
        
         if self.userName == "" and self.passWord == "":
             print("Press SignUp first by pressing 1 from the Main menu")
         else:
             useName = input('enter your email here:--> ')
             pword = input("enter your password here:--> ")
             
             if self.userName == useName and self.passWord == pword:
                 print("You have sucessfully Logged-In into the Chatbook")
                 self.loggedIn = True
             else:
                 print("incorrect credential please,Please input correct credential")
         print("\n")
         self.menu()
         
    def my_post(self):
        if self.loggedIn == True:
            post = input("Enter the msg to sent as post")
            print(f"below content has been sent as {post}")
        else:
            print("plz signIn first to send a post")    
        print("\n")
        self.menu()
    def my_msg(self):
            if self.loggedIn == True:
                text = input("Enter the msg to sent as to frd")
                frd = input("whom to send a msg")
                print(f"below {text} has been sent as {frd}")
            else:
                print("plz signIn first to send a msg")    
            print("\n")
            self.menu()
                                
             
             
obj = chatbook() 
            