# Imagine a software system that needs to send different types of messages (text, email, push notification) but must process them all through a single, standard command: send_notification().
'''class Notification:
    def __init__(self,recipient,message):
        self.recipient = recipient
        self.message = message
    def sendNotification(self):
        print("Notification from Notification class.")

class EmailNotification(Notification):
    def __init__(self,recipient,message,subject):
        super().__init__(recipient,message)
        self.__subject = subject
    
    def sendNotification(self):
        print("------Notification From Email.------")
        print(f"Subject: {self.__subject}")
        print(f"To: {self.recipient}")
        print(f"From: {self.message}")

class SMSNotification(Notification):
    def __init__(self,recipient,message,provider):
        super().__init__(recipient,message)
        self.provider = provider
    
    def sendNotification(self):
        print("------Notification From SMS.------")
        print(f"To: {self.recipient}")
        print(f"Provider: {self.provider}")
        print(f"From: {self.message}")

email_obj = EmailNotification(
    recipient= "gauravyeskar@123.com",
    message="Your order #1212 has Shipped and will arrive tomorrow.",
    subject="Order shipped Confirmation."
)
sms_obj = SMSNotification(
    recipient= 'akash@gmail.com',
    message = 'Your OTP is 8745. Please do not share code. It will be valid for 30 seconds.',
    provider= 'Flipkart'
)
email_obj.sendNotification()
sms_obj.sendNotification()'''

# Scenario: The Processor Mixins
# Imagine you're designing a system to process data, where different operations 
# (logging, validation) can be mixed and matched.
# Question: What is the full order of operations (the printed output) when you call SecureData().process(), and how does the class definition order (class SecureData(Validator, Logger):) directly influence this result?
'''
class Data:
    def process(self):
        print("Data Processing Finished...!!")
class Validator:
    def process(self):
        print("Validation check started...")
        Data.process(self)
class Logger:
    def process(self):
        print("Logging the operation details....")
        super().process()
class secureData(Logger,Validator,Data):
    def process(self):
        print("Starting secure processing...")
        super().process()

obj_SD = secureData()
obj_SD.process()'''

# Scenario: The EmployeePayment System
# Question: What happens if you comment out the generate_report method in the HourlyEmployee class and try to instantiate it? What error does Python raise, and why is this behavior beneficial?
