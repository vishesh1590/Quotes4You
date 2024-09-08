from tkinter import *
from PIL import Image
import os

root = Tk()

#root.iconbitmap("C:\Users\seung\Hackathon\Quotes4You\quotes4you_icon (1).ico")
            
gifImage = 'wavesGif.gif'

if not os.path.exists(gifImage):
    print("GIF file not found! Exiting...")
    root.destroy()  # Exit the program if the GIF is not found
else:
    # Open the image
    openImage = Image.open(gifImage)
    frames = openImage.n_frames

imageObject = [PhotoImage(file = gifImage, format = f"gif -index {i}") for i in range(frames)]
count = 0
showAnimation = None
def animation(count):
    global showAnimation
    newImage = imageObject[count]
    gif_Label.configure(image=newImage)
    count +=1
    if count == frames:
        count = 0
    showAnimation = root.after(50, lambda: animation(count))

gif_Label = Label(root, image = "")
gif_Label.place(x=0,y=-200, width = 540, height = 600)
animation(count)

root.title("Welcome to Quotes4u")
# Set geometry(widthxheight)
root.geometry('500x250')

#lbl = Label(root, text = "How are you Feeling Today?")
#lbl.grid()
#pos_button = Button(root, text = "I am feeling postive", padx = 10, command= positive_btn_clicked(), fg = "green")
#pos_button.grid()
#neg_button = Button(root, text = "I am feeling negative", padx = 7, command= negative_btn_clicked(), fg = "red")
#neg_button.grid()


def positive_btn_clicked():
    # Clear previous widgets and display the next question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text="How are you feeling at this current moment?")
    lbl.grid()
    
    happy_button = Button(root, text="Happy", padx=10, command=happy_btn_clicked)
    happy_button.grid()
    
    proud_button = Button(root, text="Proud", padx=10, command=proud_btn_clicked)
    proud_button.grid()
    
    at_ease_button = Button(root, text="At Ease", padx=10, command=at_ease_btn_clicked)
    at_ease_button.grid()
    
    
    gif_Label.place(x=0,y=-200, width = 540, height = 600)
    animation(count)
def happy_btn_clicked():
    # Clear previous widgets and ask why happy
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text="What is the cause of your happiness?")
    lbl.grid()
    
    accomplishment_button = Button(root, text="Accomplishment", padx=10, command=accomplishment_btn_clicked)
    accomplishment_button.grid()
    
    relationships_button = Button(root, text="Relationships", padx=10, command=relationships_btn_clicked)
    relationships_button.grid()
    
    good_day_button = Button(root, text="The day is going well!", padx=10, command=good_day_btn_clicked)
    good_day_button.grid()
def accomplishment_btn_clicked():
    #display quotes #1
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"The greatest achievement is to outperform yourself" - Denis Waitley \n"All great achievements have one thing in common - people with a passion to succeed" - Pat Cash')
    lbl.grid()
def relationships_btn_clicked():
                #display quotes #2
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"Family is not an important thing, it’s everything" - Michael J. Fox \n"The best relationship is not the one being shared in good times, but rather the one who has the staying power through rough times" - Anonymous')
    lbl.grid()
def good_day_btn_clicked():
                #display quotes #3
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“Every day may not be good, but there’s something good in every day” - Alice Morse Earle \n“Every day is a good day. There is something to learn, care, and celebrate” - Amit Ray')
    lbl.grid()
def proud_btn_clicked():
        #why proud question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text="What made you proud?")
    lbl.grid()
    
    own_accomplishment_button = Button(root, text = "Own Accomplishment", padx = 10, command= own_accomplishment_btn_clicked)
    own_accomplishment_button.grid()
    
    other_accomplishment_button = Button(root, text = "Others' Accomplishment", padx = 10, command= other_accomplishment_btn_clicked)
    other_accomplishment_button.grid()
    
    helped_button = Button(root, text = "Helped someone in need", padx = 10, command= helped_btn_clicked)
    helped_button.grid()

def own_accomplishment_btn_clicked():
                #display quotes #4
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“The greatest achievement is to outperform yourself” - Denis Waitley\n “All great achievements have one thing in common - people with a passion to succeed” - Pat Cash')
    lbl.grid()

def other_accomplishment_btn_clicked():
                #display quotes #5
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “There’s nothing to be proud of in being able to put others down.” - Anonymous\n “Proud souls in the true sense are never humbled by adversity” - Henry S. Haskins')
    lbl.grid()
def helped_btn_clicked():
                #display quotes #6
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“A good way to overcome stress is to help others out of theirs” Dada J. P. Vaswani\n “If you want to achieve your goals, help others achieve theirs” - Zig Ziglar')
    lbl.grid()
def at_ease_btn_clicked():
        #why at ease question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "Why are you at ease?")
    lbl.grid()
    
    finished_event_button = Button(root, text = "Finished big event", padx = 10, command= finished_event_btn_clicked)
    finished_event_button.grid()
    
    resolved_problem_button = Button(root, text = "Resolved Problem", padx = 10, command= fixed_problem_btn_clicked)
    resolved_problem_button.grid()
    
    restful_day_button = Button(root, text = "Had a restful day", padx = 10, command= restful_day_btn_clicked)
    restful_day_button.grid()
    

def finished_event_btn_clicked():
                #display quotes #7
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“The greatest achievement is to outperform yourself” - Denis Waitley\n“All great achievements have one thing in common - people with a passion to succeed” - Pat Cash')
    lbl.grid()
def fixed_problem_btn_clicked():
                #display quotes #8
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“A problem defined, is a problem half solved” - Albert Einstein\n“Life is problems. Living is solving problems.” - Raymond E. Feist')
    lbl.grid()
def restful_day_btn_clicked():
                #display quotes #9
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '“Rest when you need to, but never quit” - John Wooden\n“If you get tired, learn to rest, not quit” - Anonymous')
    lbl.grid()
def negative_btn_clicked():
    #negative moods question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "How are you feeling as this current moment?")
    lbl.grid()
    
    sad_button = Button(root, text = "Sad", padx = 10, command= sad_btn_clicked)
    sad_button.grid()
    
    angry_button = Button(root, text = "Angry", padx = 10, command= angry_btn_clicked)
    angry_button.grid()
    
    tired_button = Button(root, text = "Tired", padx = 10, command= tired_btn_clicked)
    tired_button.grid()
    
    stressed_button = Button(root, text = "Stressed", padx = 10, command= stressed_btn_clicked)
    stressed_button.grid()
def sad_btn_clicked():
    #why sad question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "What is the main root of your sadness?")
    lbl.grid()
    
    personal_problem_button = Button(root, text = "Personal/family problem", padx = 10, command= personal_problem_btn_clicked)
    personal_problem_button.grid()
    
    work_problem_button = Button(root, text = "Work/school problem", padx = 10, command= work_problem_btn_clicked)
    work_problem_button.grid()
    
    regret_button = Button(root, text = "Disappointment/Regret", padx = 10, command= regret_btn_clicked)
    regret_button.grid()   
    
    
    
def personal_problem_btn_clicked():
    #display quotes #10
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"Problems in a relationship occur because each person is concentrating on what is missing in the other person" - Wayne Dyer \n"Everyone has problems, but don’t lose your happiness just because you’re focused on them" - Anonymous')
    lbl.grid()
def work_problem_btn_clicked():
    #display quotes #11
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"The pain you feel today will be the strength you feel tomorrow" - Anonymous \n"Work hard at work worth doing" - Theodore Roosevelt')
    lbl.grid()
def regret_btn_clicked():
    #display quotes #12
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"I have no regrets. Regrets are meaningless. You can’t change yesterday or tomorrow. You can change only this present moment" - Richey Edwards \n"Never regret a day in your life: good days give happiness, bad days give experience, worst days give lessons, and best days give memories" - Anonymous')
    lbl.grid()
def angry_btn_clicked():
    #why angry question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "What is the main root of your sadness?")
    lbl.grid()
    
    others_actions_button = Button(root, text = "Someone else’s actions", padx = 10, command= others_actions_btn_clicked)
    others_actions_button.grid()
    
    own_actions_button = Button(root, text = "Your own actions", padx = 10, command= own_actions_btn_clicked)
    own_actions_button.grid()
    
    unexpected_event_button = Button(root, text = "Unexpected event", padx = 10, command= unexpected_event_btn_clicked)
    unexpected_event_button.grid()  

def others_actions_btn_clicked():
    #display quotes #13
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"Whatever is begun in anger ends in shame" - Benjamin Franklin" \n"Anger, resentment, and jealousy doesn’t change the heart of others - it only changes yours" - Shannon L. Alder')
    lbl.grid()
def own_actions_btn_clicked():
    #display quotes #14
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"Anger comes when you aren’t getting the results you want. The key is to use the anger to drive yourself to improve" - Larry Weidel \n"Anger doesn’t solve anything. It builds nothing, but it can destroy everything" - Lawrence Douglas Wilder')
    lbl.grid()
def unexpected_event_btn_clicked():
    #display quotes #15
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"Anger is never without a reason, but seldom with a good one" - Benjamin Franklin \n"Anger is an acid that can do more harm to the vessel in which it’s stored than to anything on which it is poured" - Mark Twain')
    lbl.grid()
def tired_btn_clicked():
    #why tired question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "What is causing your tiredness?")
    lbl.grid()
    
    sleep_button = Button(root, text = "Lack of sleep", padx = 10, command= sleep_btn_clicked)
    sleep_button.grid()
    
    burnout_button = Button(root, text = "Overworked/Burnout", padx = 10, command= burnout_btn_clicked)
    burnout_button.grid()
    
    emotional_exhaustion_button = Button(root, text = "Emotional Exhaustion", padx = 10, command= emotional_exhaustion_btn_clicked)
    emotional_exhaustion_button.grid()  
    
    
def sleep_btn_clicked():
    #display quotes #16
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “Sleep is an investment in the energy you need to be effective tomorrow” - Tom Roth \n“Your future depends on your dreams, so go to sleep” - Mesut Barazany - Wayne W. Dyer')
    lbl.grid()
def burnout_btn_clicked():
    #display quotes #17
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = '"If you get tired, learn to rest, not  quit" - Anonymous \n"I advise all the young kids to not overwork. You can not be out there blowing hard. You have to pace yourself" - Freddie Hubbard')
    lbl.grid()
def emotional_exhaustion_btn_clicked():
    #display quotes #18
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “I know you are tired, I know you are physically and emotionally drained. But you have to keep going” - Anonymous \n“Keep believing. You may be tired, discouraged, but don’t give up on your future” - Joel Osteen')
    lbl.grid()
def stressed_btn_clicked():
    #why stressed question
    for widget in root.winfo_children():
        widget.destroy()

    lbl = Label(root, text = "What is the primary root of your stress?")
    lbl.grid()
    
    upcoming_event_button = Button(root, text = "Upcoming event", padx = 10, command= upcoming_event_btn_clicked)
    upcoming_event_button.grid()
    
    personal_stress_button = Button(root, text = "Health/personal", padx = 10, command= personal_stress_btn_clicked)
    personal_stress_button.grid()
    
    work_stress_button = Button(root, text = "Work/School", padx = 10, command= work_stress_btn_clicked)
    work_stress_button.grid()  
    

def upcoming_event_btn_clicked():
    #display quotes #19
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “Anxiety happens when you think you have to figure out everything all at once. Breathe. You are strong. You got this. Take it day by day” - Anonymous \n“My key to dealing with stress is simple: just stay cool and stay focused” - Ashton Eaton')
    lbl.grid()
def personal_stress_btn_clicked():
    #display quotes #20
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “Health is not valued till sickness comes” - Thomas Fuller \n“The preservation of health is easier than the cure of the disease” - Anonymous')
    lbl.grid()
def work_stress_btn_clicked():
                #display quotes #21
    for widget in root.winfo_children():
        widget.destroy()
    lbl = Label(root, text = ' “Anxiety happens when you think you have to figure out everything all at once. Breathe. You are strong. You got this. Take it day by day” - Anonymous \n“There is no stress in the world, only people thinking stressful thoughts” - Wayne W. Dyer')
    lbl.grid()

lbl = Label(root, text = "How are you Feeling Today?")
lbl.grid()
pos_button = Button(root, text = "I am feeling postive", padx = 10, command= positive_btn_clicked, fg = "green")
pos_button.grid()
neg_button = Button(root, text = "I am feeling negative", padx = 7, command= negative_btn_clicked, fg = "red")
neg_button.grid()

root.mainloop()