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
decision_dur=()
instruct_dur=()
outcome_dur=2

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
waiting = visual.TextStim(win, text="Calculating...", height=1.5)

#decision screen
pictureStim =  visual.ImageStim(win, pos=(0,1.5))
resp_text_left = visual.TextStim(win,text='', pos =(-7,-4.8), height=1, alignHoriz="center")
resp_text_right = visual.TextStim(win,text='', pos =(7,-4.8), height=1, alignHoriz="center")

# outcome screen
outcome_stim = visual.TextStim(win, text='')

outcome_map = {
    1: 'You have chosen to receive money now',
    2: 'You have chosen to receive money later',
    }

#instructions
instruct_screen = visual.TextStim(win, text='Welcome to the experiment.\n\nIn this task you will be choosing between an immediate reward or a delayed reward.\n\nIn the following slides: \nPress 1= choose immediate reward \nPress 2= choose delayed reward. \n\nWhen you are ready press SPACEBAR to continue.', pos = (0,1), wrapWidth=23, height = 1.2)

#exit
exit_screen = visual.TextStim(win, text='Thanks for playing! Please wait for instructions from the researcher.', pos = (0,1), wrapWidth=20, height = 1.2)

#logging
#log_file = logging.LogFile("logs/%s.log" % (subj_id), level=logging.DATA, filemode='w')
log_file = 'logs/{}_run_{}.csv'

'''
expdir = os.getcwd()
subjdir = '%s/logs/%s' % (expdir, subj_id)
if not os.path.exists(subjdir):
    os.makedirs(subjdir)
log_file = os.path.join(subjdir,'sub-{}_task-trust_run-{}_raw.csv')
'''

#timing
globalClock = core.Clock()
logging.setDefaultClock(globalClock)

timer = core.Clock()

#trial handler
trial_data = [r for r in csv.DictReader(open('IntertemporalChoice_design_test.csv','rU'))]

trials = data.TrialHandler(trial_data[:5], 1, extraInfo=run_data, dataTypes=['stim_onset', 'resp_onset', 'rt', 'resp'], method='sequential')

stim_map = {
  '3': 'friend',
  '2': 'stranger',
  '1': 'computer',
  }

#parsing out file data

runs=[]
'''
for run in range(6):
    run_data = []
    for t in range(12):
        sample = random.sample(range(len(trial_data)),1)[0]
        run_data.append(trial_data.pop(sample))
    runs.append(run_data)
'''

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

def do_run(trial_data, run_num):
    
    trials = data.TrialHandler(trial_data, 1, method="sequential")
    
    ready_screen.draw()
    win.flip()
    event.waitKeys(keyList=('equal'))

    globalClock.reset()
    studyStart = globalClock.getTime()

    # Initial Fixation screen
    fixation.draw()
    win.flip()
    core.wait(initial_fixation_dur)

    print "got to checkpoint 1"
    
    for trial in trials:
        
        print "got to checkpoint 2"
        
        # add trial logic
        # i.e. show stimuli
        # get resp
        # add data to 'trial'
        
        #condition_label = stim_map[trial['Condition']]
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
            resp_text_left.draw()
            resp_text_right.draw()
            
            win.flip()
            if ifresp:
                core.wait(.5)
                break
            
            resp = event.getKeys(keyList = responseKeys)
            
            
            if len(resp)>0:
                resp_val = int(resp[0])
                resp_onset = globalClock.getTime()
                if resp_val == 1:
                    resp_text_keep.setColor('red')
                    ifresp = 1
                if resp_val == 2:
                    resp_text_share.setColor('red')
                    ifresp=1
                
                
        trials.addData('resp', resp_val)
        trials.addData('rt', resp_onset)
        
        #reset rating number color
        resp_text_left.setColor('#FFFFFF')
        resp_text_right.setColor('#FFFFFF')
        
        #ISI
        logging.log(level=logging.DATA, msg='ISI') #send fixation log event
        timer.reset()
        isi_for_trial = float(trial['ISI'])
        while timer.getTime() < isi_for_trial:
            waiting.draw()
            win.flip()
            
        #outcome phase
        if resp_val == 2:
            #partner_resp=random.randint(0,1)
            outcome_txt = outcome_map[2]
            #trials.addData('outcome', partner_resp)
        else:
            outcome_txt = outcome_map[resp_val]
        outcome_stim.setText(outcome_txt)
        outcome_stim.draw()
        trials.addData('outcome_txt', outcome_txt)
        win.flip()
        core.wait(2)
        
    trials.saveAsText(fileName=log_file.format(subj_id, run_num)) #, dataOut='all_raw', encoding='utf-8')


for ridx, run_trials in enumerate(runs):
    do_run(run_trials[:3], ridx+1)