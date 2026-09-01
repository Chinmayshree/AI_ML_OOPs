
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
                pass
                #  self.signUp()
           elif user_input =='2':
                self.signIn()
           elif user_input =='3':
               pass
           elif user_input =='4':
               pass
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
         
                 
             
             
obj = chatbook() 
            