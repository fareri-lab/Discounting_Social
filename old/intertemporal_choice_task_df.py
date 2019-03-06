#### Intertemporal Choice Task ####



# Developed by Michael Poon
# Fareri Lab at Adelphi University
# Most recent update: 9/4/2018



### specs ###
# 51 trials
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

decision_dur=3

instruct_dur=()

#outcome_dur=2



responseKeys=('1','2')



#get subjID

subjDlg=gui.Dlg(title="Intertemporal Choice Task")

subjDlg.addField('Enter Subject ID: ')

subjDlg.show()



if gui.OK:

    subj_id=subjDlg.data[0]

else:

    sys.exit()



run_data = {

    'Participant ID': subj_id,

    'Date': str(datetime.datetime.now()),

    'Description': 'Intertemporal Choice Task'

    }



#window setup

win = visual.Window([1280,800], monitor="testMonitor", units="deg", fullscr=useFullScreen, allowGUI=False)



#define stimulus

fixation = visual.TextStim(win, text="+", height=2)

ready_screen = visual.TextStim(win, text="Please wait for this round of the game to begin.", height=1.5)

waiting = visual.TextStim(win, text="+", height=1.5)

initial_fixation_dur = 4



#decision screen

pictureStim =  visual.ImageStim(win, pos=(0,6.5))

cardStim_left = visual.Rect(win=win, name='polygon', width=(5.0,5.0)[0], height=(7.0,7.0)[1], ori=0, pos=(-7, 0),lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb',opacity=1, depth=0.0, interpolate=True)

immed_text = visual.TextStim(win,text='',pos=(-7,0),height = 1,alignHoriz="center")

delay_text = visual.TextStim(win,text='',pos=(7,0),height = 1,alignHoriz="center")

cardStim_right = visual.Rect(win=win, name='polygon', width=(5.0,5.0)[0], height=(7.0,7.0)[1], ori=0, pos=(7, 0),lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',fillColor=[0,0,0], fillColorSpace='rgb',opacity=1, depth=0.0, interpolate=True)



'''

# outcome screen

outcome_stim = visual.TextStim(win, text='')

outcome_map = {

    1: 'You have chosen to receive money now',

    2: 'You have chosen to receive money later',

    }

'''



#instructions

instruct_screen = visual.TextStim(win, text='Welcome to the experiment.\n\nIn this task you will be choosing between an immediate reward or a delayed reward.\n\nIn the following slides: \nPress 1= choose immediate reward \nPress 2= choose delayed reward. \n\nWhen you are ready press SPACEBAR to continue.', pos = (0,1), wrapWidth=23, height = 1.2)



#exit

exit_screen = visual.TextStim(win, text='Thanks for playing! Please wait for instructions from the researcher.', pos = (0,1), wrapWidth=20, height = 1.2)



#create log file

log_file = 'logs/{}_run_{}.csv'



'''

expdir = os.getcwd()

subjdir = '%s/logs/%s' % (expdir, subj_id)

if not os.path.exists(subjdir):

    os.makedirs(subjdir)

log_file = os.path.join(subjdir,'sub-{}_task-trust_run-{}_raw.csv')

'''



#initialize time clocks

globalClock = core.Clock()

logging.setDefaultClock(globalClock)



timer = core.Clock()



#set up trial handler

trial_data = [r for r in csv.DictReader(open('IntertemporalChoice_design_test.csv','rU'))]

trials = data.TrialHandler(trial_data[:], 1, method='sequential')



print "got here"



#### TASK ####



# Instructions

instruct_screen.draw()

win.flip()

event.waitKeys()



#reset globalClock for beginning of task

globalClock.reset()



#present instructions

curTime=globalClock.getTime()

startTime=curTime

if not DEBUG:

    instruct_screen.draw()

    win.flip()

    event.waitKeys(keyList=('space'))



# main task loop



def do_run(trials, run):

    print "got here2" #checkpoint

    trials = data.TrialHandler(trial_data, 1, method="random")



    ready_screen.draw()

    win.flip()

    event.waitKeys(keyList=('equal'))



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

        ifresp = 0

        while timer.getTime() < decision_dur:

            pictureStim.draw()

            #cardStim_left.draw()

            #cardStim_right.draw()

            immed_left = trial['immed']

            delay_right = trial['delay']

            timeD_right = trial['time']

            immediate = '$%s today' % immed_left

            delayed = '$%s in %s days' % (delay_right, timeD_right)

            immed_text.setText(immediate)

            delay_text.setText(delayed)

            immed_text.draw()

            delay_text.draw()



            win.flip()



            resp = event.getKeys(keyList = responseKeys)





            if len(resp)>0:

                resp_val = int(resp[0])

                resp_onset = globalClock.getTime()

                if resp_val == 1:

                    immed_text.setColor('red')

                if resp_val == 2:

                    delay_text.setColor('red')



        trials.addData('resp', resp_val)

        trials.addData('rt', resp_onset)



        #reset rating number color

        immed_text.setColor('#FFFFFF')

        delay_text.setColor('#FFFFFF')



        #ISI

        logging.log(level=logging.DATA, msg='ISI') #send fixation log event

        timer.reset()

        isi_for_trial = float(trial['ITI'])

        while timer.getTime() < isi_for_trial:

            waiting.draw()

            win.flip()

    trials.saveAsText(fileName=log_file.format(subj_id, run_num)) #, dataOut='all_raw', encoding='utf-8'





for trials, run in enumerate(trial_data):

    do_run(trials, run)

