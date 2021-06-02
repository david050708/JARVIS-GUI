from tkinter import *
import pyttsx3
import speech_recognition as sr
from PIL import ImageTk
import webbrowser  
import datetime  
import wikipedia 
import pyjokes

root = Tk()
root.title("JARVIS")
root.geometry("300x300")
root.iconbitmap("D:\\8th Notes\\Visual Studio Code\\JARVIS\\Icon.ico")


C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "D:\\8th Notes\\Visual Studio Code\\JARVIS\\Jarvis.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

def AI():
	def takeCommand():
  
		r = sr.Recognizer()
	
		# from the speech_Recognition module 
		# we will use the Microphone module
		# for listening the command
		with sr.Microphone() as source:
			print('Listening...')
			
			# seconds of non-speaking audio before 
			# a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)
			
			# Now we will be using the try and catch
			# method so that if sound is recognized 
			# it is good else we will have exception 
			# handling
			try:
				print("Analysing...")
				
				Query = r.recognize_google(audio, language='en-in')
				print(Query)
				
			except Exception as e:
				print(e)
				print("Say that again sir")
				return "None"
			
			return Query
	
	def speak(audio):
		
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[0].id)
		
		
		engine.say(audio)  
		
		engine.runAndWait()
	
	def tellDay():
		
		# This function is for telling the
		# day of the week
		day = datetime.datetime.today().weekday() + 1
		
		#this line tells us about the number 
		# that will help us in telling the day
		Day_dict = {1: 'Monday', 2: 'Tuesday', 
					3: 'Wednesday', 4: 'Thursday', 
					5: 'Friday', 6: 'Saturday',
					7: 'Sunday'}
		
		if day in Day_dict.keys():
			day_of_the_week = Day_dict[day]
			print(day_of_the_week)
			speak("The day is " + day_of_the_week)
	
	
	def tellTime():
		
		# This method will give the time
		time = str(datetime.datetime.now())
		
		# the time will be displayed like 
		# this "2020-06-05 17:50:14.582630"
		#nd then after slicing we can get time
		print(time)
		hour = time[11:13]
		min = time[14:16]
		speak("The time is sir" + hour + "Hours and" + min + "Minutes")    
	
	def Hello():
		
		# This function is for when the assistant 
		# is called it will say hello and then 
		# take query
		speak("Hello sir, I am JAVRIS your virtual assistant.")
			
	def Take_query():
	
		# calling the Hello function for 
		# making it more interactive
		Hello()
		
		# This loop is infinite as it will take
		# our queries continuously until and unless
		# we do not say bye to exit or terminate 
		# the program
		while(True):
			
			# taking the query and making it into
			# lower case so that most of the times 
			# query matches and we get the perfect 
			# output
			query = takeCommand().lower()
			if "open geeksforgeeks" in query:
				speak("Opening GeeksforGeeks ")
				
				# in the open method we just to give the link
				# of the website and it automatically open 
				# it in your default browser
				webbrowser.open("www.geeksforgeeks.com")
				continue
			
			elif "open google" in query:
				print("Opening Google Chrome")
				speak("Opening Google Chrome")
				webbrowser.open("www.google.com")
				continue

			elif "open notes" in query:
				print("Opening 8th Notes")
				speak("Opening 8th Notes")
				webbrowser.open("D:\8th Notes")
				continue

			elif "open zoom" in query:
				print("Opening Zoom")
				speak("Opening Zoom")
				webbrowser.open("www.zoom.com")
				continue

			elif "open word" in query:
				print("Opening Microsoft Word")
				speak("Opening Microsoft Word")
				webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word")
				continue

			elif "open powerpoint" in query:
				print("Opening Microsoft Powerpoint")
				speak("Opening Microsoft Powerpoint")
				webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint")
				continue

			elif "open amazon" in query:
				print("Opening Amazon")
				speak("Opening Amazon")
				webbrowser.open("www.amazon.com")
				continue

			elif "open flipkart" in query:
				print("Opening Flipkart")
				speak("Opening Flipkart")
				webbrowser.open("www.flipkart.com")
				continue

			elif "open youtube" in query:
				print("Opening Youtube")
				speak("Opening Youtube")
				webbrowser.open("www.youtube.com")
				continue

			elif "open python" in query:
				print("Opening Python")
				speak("Opening Python")
				webbrowser.open("www.python.org")
				continue

			elif "jokes" in query:
				speak(pyjokes.get_joke())
				
			elif "open ndtv" in query:
				print("Opening NDTV")
				speak("Opening NDTV")
				webbrowser.open("www.ndtv.com")
				continue

			elif "open cnn" in query:
				print("Opening CNN")
				speak("Opening CNN")
				webbrowser.open("www.cnn.com")
				continue

			elif "open gmail" in query:
				print("Opening Gmail")
				speak("Opening Gmail")
				webbrowser.open("www.gmail.com")
				continue
				
			elif "what day is it today" in query:
				tellDay()
				continue
			
			elif "tell me the time" in query:
				tellTime()
				continue

			elif "open meet" in query:
				print("Opening Google Meet")
				speak("Opening Google Meet")
				webbrowser.open("meet.google.com")
			
			# this will exit and terminate the program
			elif "bye" in query:
				print("Bye. See you later sir!")
				speak("Bye. See you later sir!")
				exit()
			
			elif "wikipedia" in query:
				
				# if any one wants to have a information
				# from wikipedia
				speak("Analysing your query using Wikipedia ")
				query = query.replace("wikipedia", "")
				
				# it will give the summary of 4 lines from 
				# wikipedia we can increase and decrease 
				# it also.
				result = wikipedia.summary(query, sentences=4)
				speak("According to wikipedia")
				print(result)
				speak(result)
			
			elif "tell me your name" in query:
				speak("I am Javris your Virtual Assistant")
	
	if __name__ == '__main__':
		
		# main method for executing
		# the functions
		Take_query()

photo = PhotoImage(file = r"D:\\8th Notes\\Visual Studio Code\\JARVIS\\Microphone2.png")

CommandBtn = Button(root,image = photo,command = AI,width = 50,height = 50).pack()

root.mainloop()
