
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
           elif user_input =='2':
                pass
           elif user_input =='3':
               pass
           elif user_input =='4':
               pass
           else:
               exit()
obj = chatbook() 
            