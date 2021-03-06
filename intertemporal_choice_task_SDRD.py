 #### Intertemporal Choice Task ####
# Developed by Michael Poon and Dominic Fareri
# Fareri Lab at Adelphi University
# Most recent update: 11/28/2018
### specs ###
# 17 trials
# Two choices: one smaller amount of money given immediately versus a larger amount at a specified delay
### timing ###
# unlimited decision time
# 2000ms of feedback
# 1000ms intertrial interval (ITI)

#import modules
from psychopy import visual, core, event, gui, data, sound, logging
import os
import sys
import csv
import datetime
import random
import numpy

#parameters
useFullScreen = True
DEBUG = False
frame_rate=1
decision_dur= 20
instruct_dur=()
final_fixation_dur = 10
#outcome_dur=2

responseKeys=('1','2','z')

#get subjID
subjDlg=gui.Dlg(title="Intertemporal Choice Task")
subjDlg.addField('Enter Subject ID: ')
subjDlg.addField('Enter Session Number: ')
subjDlg.addField('Enter Age: ')
subjDlg.addField('Enter Sex: ')
subjDlg.show()

if gui.OK:
    subj_id=subjDlg.data[0]
    sess_id=subjDlg.data[1]
    age=subjDlg.data[2]
    sex=subjDlg.data[3]
else:
    sys.exit()
run_data = {
    'Participant ID': subj_id,
    'Date': str(datetime.datetime.now()),
    'Description': 'Intertemporal Choice Task'
    }
#window setup
win = visual.Window([1280,800], monitor="testMonitor", units="deg", fullscr=useFullScreen, allowGUI=False)
win.setColor('black')
#define stimulus
fixation = visual.TextStim(win, text="+", height=2)
ready_screen = visual.TextStim(win, text="Please wait for this round of the game to begin.", height=1.5)
waiting = visual.TextStim(win, text="+", height=1.5)
initial_fixation_dur = 2
ready_screen_dur = 2

#decision screen
pictureStim =  visual.ImageStim(win, pos=(0,6.5))
cardStim_left = visual.Rect(win=win, name='polygon', width=(7.0,7.0)[0], height=(7.0,7.0)[1], ori=0, pos=(-7, 0),lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb',opacity=1, depth=0.0, interpolate=True)
immed_text = visual.TextStim(win,text='',pos=(-7,0),height = 1,alignHoriz="center")
delay_text = visual.TextStim(win,text='',pos=(7,0),height = 1,alignHoriz="center")
cardStim_right = visual.Rect(win=win, name='polygon', width=(7.0,7.0)[0], height=(7.0,7.0)[1], ori=0, pos=(7, 0),lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb',opacity=1, depth=0.0, interpolate=True)
'''
# outcome screen
outcome_stim = visual.TextStim(win, text='')
outcome_map = {
    1: 'You have chosen to receive money now',
    2: 'You have chosen to receive money later',
    }
'''
#instructions
instruct_screen = visual.TextStim(win, text='Welcome to the experiment.\n\nIn this task you will be choosing between an immediate reward or a delayed reward.\n\nIn the following slides: \nPress 1= choose immediate reward \nPress 2= choose delayed reward. \n\nWhen you are ready, press SPACEBAR to continue.', pos = (0,1), wrapWidth=23, height = 1.2)
#exit
exit_screen = visual.TextStim(win, text='Thanks for playing! Please wait for instructions from the researcher.', pos = (0,1), wrapWidth=20, height = 1.2)
#create log file
#log_file = 'logs/{}_run_{}.csv'

expdir = os.getcwd()
subjdir = '%s/logs/%s' % (expdir, subj_id)
if not os.path.exists(subjdir):
    os.makedirs(subjdir)
log_file = os.path.join(subjdir,'sub-{}_task-intertemporalchoice_run{}_raw.csv')

#initialize time clocks
globalClock = core.Clock()
logging.setDefaultClock(globalClock)
timer = core.Clock()

#set up trial handler
trial_data = [r for r in csv.DictReader(open('IntertemporalChoice_17item_test.csv','rU'))]
#trials = data.TrialHandler(trial_data[:], 1, method='sequential')
#print "got here1" #checkpoint

#### TASK ####
#reset globalClock for beginning of task
globalClock.reset()
#print "got here2" #checkpoint

#present instructions
curTime=globalClock.getTime()
startTime=curTime

#if not DEBUG:
instruct_screen.draw()
win.flip()
event.waitKeys(keyList=('space'))


# main task loop
def do_run(run, trials):
    fileName=log_file.format(subj_id,run)
    trials = data.TrialHandler(trial_data, 1, method="sequential")

    #Ready Screen
    ready_screen.draw()
    win.flip()
    core.wait(ready_screen_dur)
    
    print(type(decision_dur))

    globalClock.reset()
    studyStart = globalClock.getTime()

    # Initial Fixation screen
    fixation.draw()
    win.flip()
    core.wait(initial_fixation_dur)

    for trial in trials:
        image = "money.png"
        pictureStim.setImage(image)

        #decision phase
        timer.reset()
        event.clearEvents()
        resp_val=None
        resp_onset=None

        decision_onset = globalClock.getTime()

        #ifresp = 0
        while timer.getTime() < int(decision_dur):
            pictureStim.draw()
            cardStim_left.draw()
            cardStim_right.draw()
            immed_left = trial['Immed']
            delay_right = trial['Delay']
            timeD_right = trial['Time']
            immediate = '$%s today' % immed_left
            delayed = '$%s in %s days' % (delay_right, timeD_right)
            immed_text.setText(immediate)
            delay_text.setText(delayed)
            immed_text.draw()
            delay_text.draw()
            win.flip()
            resp = event.getKeys(keyList = responseKeys)

            if len(resp)>0:
                if resp[0] == 'z':
                    os.chdir(subjdir)
                    trials.saveAsWideText(fileName)
                    os.chdir(expdir)
                    win.close()
                    core.quit()
                resp_val = int(resp[0])
                resp_onset = globalClock.getTime()
                rt = resp_onset - decision_onset

                if resp_val == 1:
                    immed_text.setColor('red')
                if resp_val == 2:
                    delay_text.setColor('red')
                #print "got here3" #checkpoint
                pictureStim.draw()
                cardStim_left.draw()
                cardStim_right.draw()
                immed_text.draw()
                delay_text.draw()
                win.flip()
                core.wait(1)
                decision_offset = globalClock.getTime()
                break
                #print "got here4" #checkpoint

        trials.addData('rt',rt)
        trials.addData('resp', resp_val)
        trials.addData('sub',subj_id)
        trials.addData('session',sess_id)
        trials.addData('Age',age)
        trials.addData('sex',sex)
        trials.addData('decision_onset', decision_onset)
        trials.addData('resp_onset', resp_onset)
        trials.addData('decision_offset', decision_offset)
        #print "got here5" #checkpoint

        #reset rating number color
        immed_text.setColor('#FFFFFF')
        delay_text.setColor('#FFFFFF')
        #print "got here7" #checkpoint

        #ITI
        logging.log(level=logging.DATA, msg='ITI') #send fixation log event
        timer.reset()
        iti_for_trial = float(trial['ITI'])
        while timer.getTime() < iti_for_trial:
            waiting.draw()
            win.flip()
        #print "got here7" #checkpoint

    #trials.saveAsText(fileName=log_file.format(subj_id, run_num)) #, dataOut='all_raw', encoding='utf-8'
    os.chdir(subjdir)
    trials.saveAsWideText(fileName)
    os.chdir(expdir)

for run, trials in enumerate([trial_data]):
    do_run(run, trials)

# Exit
exit_screen.draw()
win.flip()
event.waitKeys()
