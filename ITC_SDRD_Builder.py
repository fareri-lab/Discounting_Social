#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Mon Aug  5 17:29:50 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'ITC_SDRD'  # from the Builder filename that created this script
expInfo = {'MTurk Code': '', 'session': '001', 'Sex': '', 'Race': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['MTurk Code'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/MichaelPoon/Desktop/Psychology/SDRD Project/Intertemporal Choice Task/GitHub Discounting Social/Discounting_Social/ITC_SDRD_Builder.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='In this task you will be choosing between an immediate reward or a delayed reward.\n\nIn the following slides: \nPress 1= choose immediate reward \nPress 2= choose delayed reward\n\nWhen you are ready, press the SPACEBAR to start',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
Immed_Choice_Box = visual.TextStim(win=win, name='Immed_Choice_Box',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Delay_Choice_Box = visual.TextStim(win=win, name='Delay_Choice_Box',
    text='default text',
    font='Arial',
    pos=(0.5, 0.0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='money.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "Immed_Decision"
Immed_DecisionClock = core.Clock()
Immed_Choice_BoxA = visual.TextStim(win=win, name='Immed_Choice_BoxA',
    text='default text',
    font='Arial',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Delay_Choice_BoxA = visual.TextStim(win=win, name='Delay_Choice_BoxA',
    text='default text',
    font='Arial',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Immed_Decision_Stim = visual.ImageStim(
    win=win,
    name='Immed_Decision_Stim', 
    image='money.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Delay_Decision"
Delay_DecisionClock = core.Clock()
Immed_Choice_BoxB = visual.TextStim(win=win, name='Immed_Choice_BoxB',
    text='default text',
    font='Arial',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Delay_Choice_BoxB = visual.TextStim(win=win, name='Delay_Choice_BoxB',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Delay_Decision_Stim = visual.ImageStim(
    win=win,
    name='Delay_Decision_Stim', 
    image='money.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ITI_Stim = visual.TextStim(win=win, name='ITI_Stim',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thank_You"
Thank_YouClock = core.Clock()
ThankYou = visual.TextStim(win=win, name='ThankYou',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Q1"
Q1Clock = core.Clock()
Question1 = visual.TextStim(win=win, name='Question1',
    text='How likely were you to choose a social experience over a non-social experience?',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scale_msg1 = visual.TextStim(win=win, name='scale_msg1',
    text='Very Unlikely (1)',
    font='Arial',
    pos=(-0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
scale_msg2 = visual.TextStim(win=win, name='scale_msg2',
    text='Very Likely (7)',
    font='Arial',
    pos=(0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
scale_msg3 = visual.TextStim(win=win, name='scale_msg3',
    text='Neutral',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# Initialize components for Routine "Q2"
Q2Clock = core.Clock()
Question2 = visual.TextStim(win=win, name='Question2',
    text='How likely were you to choose a non-social experience over a social experience?',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scale1 = visual.TextStim(win=win, name='scale1',
    text='Very Unlikely (1)',
    font='Arial',
    pos=(-0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
scale2 = visual.TextStim(win=win, name='scale2',
    text='Neutral',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text = visual.TextStim(win=win, name='text',
    text='Very Likely (7)',
    font='Arial',
    pos=(0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# Initialize components for Routine "Q3"
Q3Clock = core.Clock()
Question3 = visual.TextStim(win=win, name='Question3',
    text='How likely were you to choose experiences involving friends over experiences involving family?',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scalemsg1 = visual.TextStim(win=win, name='scalemsg1',
    text='Very Unlikely (1)',
    font='Arial',
    pos=(-0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Neutral',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Very Likely (7)',
    font='Arial',
    pos=(0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# Initialize components for Routine "Q4"
Q4Clock = core.Clock()
Question4 = visual.TextStim(win=win, name='Question4',
    text='How likely were you to choose experiences involving family over experiences involving a significant other',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scales1 = visual.TextStim(win=win, name='scales1',
    text='Very Unlikely (1)',
    font='Arial',
    pos=(-0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
scales2 = visual.TextStim(win=win, name='scales2',
    text='Neutral',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
scales3 = visual.TextStim(win=win, name='scales3',
    text='Very Likely (7)',
    font='Arial',
    pos=(0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# Initialize components for Routine "Q5"
Q5Clock = core.Clock()
Question5 = visual.TextStim(win=win, name='Question5',
    text='How much did you enjoy participating?',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scale_1 = visual.TextStim(win=win, name='scale_1',
    text='Not at all (1)',
    font='Arial',
    pos=(-0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Neutral',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='Very Much (7)',
    font='Arial',
    pos=(0.5, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1, high=7, labels=['Very Unlikely', ' Unlikely', ' Somewhat Unlikely', ' Neutral', ' Somewhat Likely', ' Likely', ' Very Likely'], scale='')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction"-------
t = 0
IntroductionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
spacebar = keyboard.Keyboard()
# keep track of which components have finished
IntroductionComponents = [Instructions, spacebar]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t  # not accounting for scr refresh
        Instructions.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *spacebar* updates
    if t >= 0.0 and spacebar.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar.tStart = t  # not accounting for scr refresh
        spacebar.frameNStart = frameN  # exact frame index
        win.timeOnFlip(spacebar, 'tStartRefresh')  # time at next scr refresh
        spacebar.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spacebar.clock.reset)  # t=0 on next screen flip
        spacebar.clearEvents(eventType='keyboard')
    if spacebar.status == STARTED:
        theseKeys = spacebar.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            spacebar.keys = theseKeys.name  # just the last key pressed
            spacebar.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if spacebar.keys in ['', [], None]:  # No response was made
    spacebar.keys = None
thisExp.addData('spacebar.keys',spacebar.keys)
if spacebar.keys != None:  # we had a response
    thisExp.addData('spacebar.rt', spacebar.rt)
thisExp.addData('spacebar.started', spacebar.tStartRefresh)
thisExp.addData('spacebar.stopped', spacebar.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IntertemporalChoice_17item_test.csv'),
    seed=None, name='Loop')
thisExp.addLoop(Loop)  # add the loop to the experiment
thisLoop = Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in Loop:
    currentLoop = Loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Choice"-------
    t = 0
    ChoiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Immed_Choice_Box.setText(Immed_Choice_Text)
    Delay_Choice_Box.setText(Delay_Choice_Text)
    Response = keyboard.Keyboard()
    # keep track of which components have finished
    ChoiceComponents = [Immed_Choice_Box, Delay_Choice_Box, image, Response]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Immed_Choice_Box* updates
        if t >= 0.0 and Immed_Choice_Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Immed_Choice_Box.tStart = t  # not accounting for scr refresh
            Immed_Choice_Box.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Immed_Choice_Box, 'tStartRefresh')  # time at next scr refresh
            Immed_Choice_Box.setAutoDraw(True)
        
        # *Delay_Choice_Box* updates
        if t >= 0.0 and Delay_Choice_Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Delay_Choice_Box.tStart = t  # not accounting for scr refresh
            Delay_Choice_Box.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Delay_Choice_Box, 'tStartRefresh')  # time at next scr refresh
            Delay_Choice_Box.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *Response* updates
        if t >= 0.0 and Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response.tStart = t  # not accounting for scr refresh
            Response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
            Response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
            Response.clearEvents(eventType='keyboard')
        if Response.status == STARTED:
            theseKeys = Response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Response.keys = theseKeys.name  # just the last key pressed
                Response.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice"-------
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop.addData('Immed_Choice_Box.started', Immed_Choice_Box.tStartRefresh)
    Loop.addData('Immed_Choice_Box.stopped', Immed_Choice_Box.tStopRefresh)
    Loop.addData('Delay_Choice_Box.started', Delay_Choice_Box.tStartRefresh)
    Loop.addData('Delay_Choice_Box.stopped', Delay_Choice_Box.tStopRefresh)
    Loop.addData('image.started', image.tStartRefresh)
    Loop.addData('image.stopped', image.tStopRefresh)
    # check responses
    if Response.keys in ['', [], None]:  # No response was made
        Response.keys = None
    Loop.addData('Response.keys',Response.keys)
    if Response.keys != None:  # we had a response
        Loop.addData('Response.rt', Response.rt)
    Loop.addData('Response.started', Response.tStartRefresh)
    Loop.addData('Response.stopped', Response.tStopRefresh)
    if (Response.keys == '1'):
        doImmed_Decision = 1
    else:
        doImmed_Decision = 0
    
    if (Response.keys == '2'):
        doDelay_Decision = 1
    else:
        doDelay_Decision = 0
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Immed_Decision_Loop = data.TrialHandler(nReps=doImmed_Decision, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Immed_Decision_Loop')
    thisExp.addLoop(Immed_Decision_Loop)  # add the loop to the experiment
    thisImmed_Decision_Loop = Immed_Decision_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImmed_Decision_Loop.rgb)
    if thisImmed_Decision_Loop != None:
        for paramName in thisImmed_Decision_Loop:
            exec('{} = thisImmed_Decision_Loop[paramName]'.format(paramName))
    
    for thisImmed_Decision_Loop in Immed_Decision_Loop:
        currentLoop = Immed_Decision_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisImmed_Decision_Loop.rgb)
        if thisImmed_Decision_Loop != None:
            for paramName in thisImmed_Decision_Loop:
                exec('{} = thisImmed_Decision_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Immed_Decision"-------
        t = 0
        Immed_DecisionClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Immed_Choice_BoxA.setText(Immed_Choice_Text)
        Delay_Choice_BoxA.setText(Delay_Choice_Text)
        # keep track of which components have finished
        Immed_DecisionComponents = [Immed_Choice_BoxA, Delay_Choice_BoxA, Immed_Decision_Stim]
        for thisComponent in Immed_DecisionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Immed_Decision"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Immed_DecisionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Immed_Choice_BoxA* updates
            if t >= 0.0 and Immed_Choice_BoxA.status == NOT_STARTED:
                # keep track of start time/frame for later
                Immed_Choice_BoxA.tStart = t  # not accounting for scr refresh
                Immed_Choice_BoxA.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Immed_Choice_BoxA, 'tStartRefresh')  # time at next scr refresh
                Immed_Choice_BoxA.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Immed_Choice_BoxA.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Immed_Choice_BoxA.tStop = t  # not accounting for scr refresh
                Immed_Choice_BoxA.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Immed_Choice_BoxA, 'tStopRefresh')  # time at next scr refresh
                Immed_Choice_BoxA.setAutoDraw(False)
            
            # *Delay_Choice_BoxA* updates
            if t >= 0.0 and Delay_Choice_BoxA.status == NOT_STARTED:
                # keep track of start time/frame for later
                Delay_Choice_BoxA.tStart = t  # not accounting for scr refresh
                Delay_Choice_BoxA.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Delay_Choice_BoxA, 'tStartRefresh')  # time at next scr refresh
                Delay_Choice_BoxA.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Delay_Choice_BoxA.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Delay_Choice_BoxA.tStop = t  # not accounting for scr refresh
                Delay_Choice_BoxA.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Delay_Choice_BoxA, 'tStopRefresh')  # time at next scr refresh
                Delay_Choice_BoxA.setAutoDraw(False)
            
            # *Immed_Decision_Stim* updates
            if t >= 0.0 and Immed_Decision_Stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                Immed_Decision_Stim.tStart = t  # not accounting for scr refresh
                Immed_Decision_Stim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Immed_Decision_Stim, 'tStartRefresh')  # time at next scr refresh
                Immed_Decision_Stim.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Immed_Decision_Stim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Immed_Decision_Stim.tStop = t  # not accounting for scr refresh
                Immed_Decision_Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Immed_Decision_Stim, 'tStopRefresh')  # time at next scr refresh
                Immed_Decision_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Immed_DecisionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Immed_Decision"-------
        for thisComponent in Immed_DecisionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Immed_Decision_Loop.addData('Immed_Choice_BoxA.started', Immed_Choice_BoxA.tStartRefresh)
        Immed_Decision_Loop.addData('Immed_Choice_BoxA.stopped', Immed_Choice_BoxA.tStopRefresh)
        Immed_Decision_Loop.addData('Delay_Choice_BoxA.started', Delay_Choice_BoxA.tStartRefresh)
        Immed_Decision_Loop.addData('Delay_Choice_BoxA.stopped', Delay_Choice_BoxA.tStopRefresh)
        Immed_Decision_Loop.addData('Immed_Decision_Stim.started', Immed_Decision_Stim.tStartRefresh)
        Immed_Decision_Loop.addData('Immed_Decision_Stim.stopped', Immed_Decision_Stim.tStopRefresh)
        
        # ------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [ITI_Stim]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Stim* updates
            if t >= 0.0 and ITI_Stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                ITI_Stim.tStart = t  # not accounting for scr refresh
                ITI_Stim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
                ITI_Stim.setAutoDraw(True)
            frameRemains = 0.0 + ITI- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ITI_Stim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI_Stim, 'tStopRefresh')  # time at next scr refresh
                ITI_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Immed_Decision_Loop.addData('ITI_Stim.started', ITI_Stim.tStartRefresh)
        Immed_Decision_Loop.addData('ITI_Stim.stopped', ITI_Stim.tStopRefresh)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed doImmed_Decision repeats of 'Immed_Decision_Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Delay_Decision_Loop = data.TrialHandler(nReps=doDelay_Decision, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Delay_Decision_Loop')
    thisExp.addLoop(Delay_Decision_Loop)  # add the loop to the experiment
    thisDelay_Decision_Loop = Delay_Decision_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDelay_Decision_Loop.rgb)
    if thisDelay_Decision_Loop != None:
        for paramName in thisDelay_Decision_Loop:
            exec('{} = thisDelay_Decision_Loop[paramName]'.format(paramName))
    
    for thisDelay_Decision_Loop in Delay_Decision_Loop:
        currentLoop = Delay_Decision_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisDelay_Decision_Loop.rgb)
        if thisDelay_Decision_Loop != None:
            for paramName in thisDelay_Decision_Loop:
                exec('{} = thisDelay_Decision_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Delay_Decision"-------
        t = 0
        Delay_DecisionClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Immed_Choice_BoxB.setText(Immed_Choice_Text)
        Delay_Choice_BoxB.setColor('red', colorSpace='rgb')
        Delay_Choice_BoxB.setPos((0.5, 0))
        Delay_Choice_BoxB.setText(Delay_Choice_Text)
        Delay_Choice_BoxB.setFont('Arial')
        Delay_Choice_BoxB.setHeight(0.1)
        # keep track of which components have finished
        Delay_DecisionComponents = [Immed_Choice_BoxB, Delay_Choice_BoxB, Delay_Decision_Stim]
        for thisComponent in Delay_DecisionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Delay_Decision"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Delay_DecisionClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Immed_Choice_BoxB* updates
            if t >= 0.0 and Immed_Choice_BoxB.status == NOT_STARTED:
                # keep track of start time/frame for later
                Immed_Choice_BoxB.tStart = t  # not accounting for scr refresh
                Immed_Choice_BoxB.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Immed_Choice_BoxB, 'tStartRefresh')  # time at next scr refresh
                Immed_Choice_BoxB.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Immed_Choice_BoxB.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Immed_Choice_BoxB.tStop = t  # not accounting for scr refresh
                Immed_Choice_BoxB.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Immed_Choice_BoxB, 'tStopRefresh')  # time at next scr refresh
                Immed_Choice_BoxB.setAutoDraw(False)
            
            # *Delay_Choice_BoxB* updates
            if t >= 0.0 and Delay_Choice_BoxB.status == NOT_STARTED:
                # keep track of start time/frame for later
                Delay_Choice_BoxB.tStart = t  # not accounting for scr refresh
                Delay_Choice_BoxB.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Delay_Choice_BoxB, 'tStartRefresh')  # time at next scr refresh
                Delay_Choice_BoxB.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Delay_Choice_BoxB.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Delay_Choice_BoxB.tStop = t  # not accounting for scr refresh
                Delay_Choice_BoxB.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Delay_Choice_BoxB, 'tStopRefresh')  # time at next scr refresh
                Delay_Choice_BoxB.setAutoDraw(False)
            
            # *Delay_Decision_Stim* updates
            if t >= 0.0 and Delay_Decision_Stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                Delay_Decision_Stim.tStart = t  # not accounting for scr refresh
                Delay_Decision_Stim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Delay_Decision_Stim, 'tStartRefresh')  # time at next scr refresh
                Delay_Decision_Stim.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Delay_Decision_Stim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Delay_Decision_Stim.tStop = t  # not accounting for scr refresh
                Delay_Decision_Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Delay_Decision_Stim, 'tStopRefresh')  # time at next scr refresh
                Delay_Decision_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Delay_DecisionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Delay_Decision"-------
        for thisComponent in Delay_DecisionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Delay_Decision_Loop.addData('Immed_Choice_BoxB.started', Immed_Choice_BoxB.tStartRefresh)
        Delay_Decision_Loop.addData('Immed_Choice_BoxB.stopped', Immed_Choice_BoxB.tStopRefresh)
        Delay_Decision_Loop.addData('Delay_Choice_BoxB.started', Delay_Choice_BoxB.tStartRefresh)
        Delay_Decision_Loop.addData('Delay_Choice_BoxB.stopped', Delay_Choice_BoxB.tStopRefresh)
        Delay_Decision_Loop.addData('Delay_Decision_Stim.started', Delay_Decision_Stim.tStartRefresh)
        Delay_Decision_Loop.addData('Delay_Decision_Stim.stopped', Delay_Decision_Stim.tStopRefresh)
        
        # ------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [ITI_Stim]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Stim* updates
            if t >= 0.0 and ITI_Stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                ITI_Stim.tStart = t  # not accounting for scr refresh
                ITI_Stim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ITI_Stim, 'tStartRefresh')  # time at next scr refresh
                ITI_Stim.setAutoDraw(True)
            frameRemains = 0.0 + ITI- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ITI_Stim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                ITI_Stim.tStop = t  # not accounting for scr refresh
                ITI_Stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI_Stim, 'tStopRefresh')  # time at next scr refresh
                ITI_Stim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Delay_Decision_Loop.addData('ITI_Stim.started', ITI_Stim.tStartRefresh)
        Delay_Decision_Loop.addData('ITI_Stim.stopped', ITI_Stim.tStopRefresh)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed doDelay_Decision repeats of 'Delay_Decision_Loop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Loop'


# ------Prepare to start Routine "Thank_You"-------
t = 0
Thank_YouClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ThankYou.setText('Thank you for participating!\n\nPlease notify the experimenter before moving on to the final \npart of the task')
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
Thank_YouComponents = [ThankYou, key_resp_2]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thank_You"-------
while continueRoutine:
    # get current time
    t = Thank_YouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYou* updates
    if t >= 0.0 and ThankYou.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYou.tStart = t  # not accounting for scr refresh
        ThankYou.frameNStart = frameN  # exact frame index
        win.timeOnFlip(ThankYou, 'tStartRefresh')  # time at next scr refresh
        ThankYou.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_You"-------
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThankYou.started', ThankYou.tStartRefresh)
thisExp.addData('ThankYou.stopped', ThankYou.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Thank_You" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
questions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='questions')
thisExp.addLoop(questions)  # add the loop to the experiment
thisQuestion = questions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
if thisQuestion != None:
    for paramName in thisQuestion:
        exec('{} = thisQuestion[paramName]'.format(paramName))

for thisQuestion in questions:
    currentLoop = questions
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Q1"-------
    t = 0
    Q1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating.reset()
    # keep track of which components have finished
    Q1Components = [Question1, scale_msg1, scale_msg2, scale_msg3, rating]
    for thisComponent in Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Q1"-------
    while continueRoutine:
        # get current time
        t = Q1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question1* updates
        if t >= 0.0 and Question1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question1.tStart = t  # not accounting for scr refresh
            Question1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question1, 'tStartRefresh')  # time at next scr refresh
            Question1.setAutoDraw(True)
        
        # *scale_msg1* updates
        if t >= 0.0 and scale_msg1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg1.tStart = t  # not accounting for scr refresh
            scale_msg1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale_msg1, 'tStartRefresh')  # time at next scr refresh
            scale_msg1.setAutoDraw(True)
        
        # *scale_msg2* updates
        if t >= 0.0 and scale_msg2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg2.tStart = t  # not accounting for scr refresh
            scale_msg2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale_msg2, 'tStartRefresh')  # time at next scr refresh
            scale_msg2.setAutoDraw(True)
        
        # *scale_msg3* updates
        if t >= 0.0 and scale_msg3.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg3.tStart = t  # not accounting for scr refresh
            scale_msg3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale_msg3, 'tStartRefresh')  # time at next scr refresh
            scale_msg3.setAutoDraw(True)
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # not accounting for scr refresh
            rating.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q1"-------
    for thisComponent in Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('Question1.started', Question1.tStartRefresh)
    questions.addData('Question1.stopped', Question1.tStopRefresh)
    questions.addData('scale_msg1.started', scale_msg1.tStartRefresh)
    questions.addData('scale_msg1.stopped', scale_msg1.tStopRefresh)
    questions.addData('scale_msg2.started', scale_msg2.tStartRefresh)
    questions.addData('scale_msg2.stopped', scale_msg2.tStopRefresh)
    questions.addData('scale_msg3.started', scale_msg3.tStartRefresh)
    questions.addData('scale_msg3.stopped', scale_msg3.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('rating.response', rating.getRating())
    questions.addData('rating.rt', rating.getRT())
    questions.addData('rating.history', rating.getHistory())
    questions.addData('rating.started', rating.tStart)
    questions.addData('rating.stopped', rating.tStop)
    # the Routine "Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q2"-------
    t = 0
    Q2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_2.reset()
    # keep track of which components have finished
    Q2Components = [Question2, scale1, scale2, text, rating_2]
    for thisComponent in Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Q2"-------
    while continueRoutine:
        # get current time
        t = Q2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question2* updates
        if t >= 0.0 and Question2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question2.tStart = t  # not accounting for scr refresh
            Question2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question2, 'tStartRefresh')  # time at next scr refresh
            Question2.setAutoDraw(True)
        
        # *scale1* updates
        if t >= 0.0 and scale1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale1.tStart = t  # not accounting for scr refresh
            scale1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale1, 'tStartRefresh')  # time at next scr refresh
            scale1.setAutoDraw(True)
        
        # *scale2* updates
        if t >= 0.0 and scale2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale2.tStart = t  # not accounting for scr refresh
            scale2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale2, 'tStartRefresh')  # time at next scr refresh
            scale2.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # not accounting for scr refresh
            text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        # *rating_2* updates
        if t >= 0.0 and rating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_2.tStart = t  # not accounting for scr refresh
            rating_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q2"-------
    for thisComponent in Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('Question2.started', Question2.tStartRefresh)
    questions.addData('Question2.stopped', Question2.tStopRefresh)
    questions.addData('scale1.started', scale1.tStartRefresh)
    questions.addData('scale1.stopped', scale1.tStopRefresh)
    questions.addData('scale2.started', scale2.tStartRefresh)
    questions.addData('scale2.stopped', scale2.tStopRefresh)
    questions.addData('text.started', text.tStartRefresh)
    questions.addData('text.stopped', text.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('rating_2.response', rating_2.getRating())
    questions.addData('rating_2.rt', rating_2.getRT())
    questions.addData('rating_2.started', rating_2.tStart)
    questions.addData('rating_2.stopped', rating_2.tStop)
    # the Routine "Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q3"-------
    t = 0
    Q3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_3.reset()
    # keep track of which components have finished
    Q3Components = [Question3, scalemsg1, text_2, text_4, rating_3]
    for thisComponent in Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Q3"-------
    while continueRoutine:
        # get current time
        t = Q3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question3* updates
        if t >= 0.0 and Question3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question3.tStart = t  # not accounting for scr refresh
            Question3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question3, 'tStartRefresh')  # time at next scr refresh
            Question3.setAutoDraw(True)
        
        # *scalemsg1* updates
        if t >= 0.0 and scalemsg1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scalemsg1.tStart = t  # not accounting for scr refresh
            scalemsg1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scalemsg1, 'tStartRefresh')  # time at next scr refresh
            scalemsg1.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # not accounting for scr refresh
            text_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # not accounting for scr refresh
            text_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        # *rating_3* updates
        if t >= 0.0 and rating_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_3.tStart = t  # not accounting for scr refresh
            rating_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_3, 'tStartRefresh')  # time at next scr refresh
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q3"-------
    for thisComponent in Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('Question3.started', Question3.tStartRefresh)
    questions.addData('Question3.stopped', Question3.tStopRefresh)
    questions.addData('scalemsg1.started', scalemsg1.tStartRefresh)
    questions.addData('scalemsg1.stopped', scalemsg1.tStopRefresh)
    questions.addData('text_2.started', text_2.tStartRefresh)
    questions.addData('text_2.stopped', text_2.tStopRefresh)
    questions.addData('text_4.started', text_4.tStartRefresh)
    questions.addData('text_4.stopped', text_4.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('rating_3.response', rating_3.getRating())
    questions.addData('rating_3.rt', rating_3.getRT())
    questions.addData('rating_3.started', rating_3.tStart)
    questions.addData('rating_3.stopped', rating_3.tStop)
    # the Routine "Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q4"-------
    t = 0
    Q4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_4.reset()
    # keep track of which components have finished
    Q4Components = [Question4, scales1, scales2, scales3, rating_4]
    for thisComponent in Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Q4"-------
    while continueRoutine:
        # get current time
        t = Q4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question4* updates
        if t >= 0.0 and Question4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question4.tStart = t  # not accounting for scr refresh
            Question4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question4, 'tStartRefresh')  # time at next scr refresh
            Question4.setAutoDraw(True)
        
        # *scales1* updates
        if t >= 0.0 and scales1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales1.tStart = t  # not accounting for scr refresh
            scales1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scales1, 'tStartRefresh')  # time at next scr refresh
            scales1.setAutoDraw(True)
        
        # *scales2* updates
        if t >= 0.0 and scales2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales2.tStart = t  # not accounting for scr refresh
            scales2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scales2, 'tStartRefresh')  # time at next scr refresh
            scales2.setAutoDraw(True)
        
        # *scales3* updates
        if t >= 0.0 and scales3.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales3.tStart = t  # not accounting for scr refresh
            scales3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scales3, 'tStartRefresh')  # time at next scr refresh
            scales3.setAutoDraw(True)
        # *rating_4* updates
        if t >= 0.0 and rating_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_4.tStart = t  # not accounting for scr refresh
            rating_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_4, 'tStartRefresh')  # time at next scr refresh
            rating_4.setAutoDraw(True)
        continueRoutine &= rating_4.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q4"-------
    for thisComponent in Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('Question4.started', Question4.tStartRefresh)
    questions.addData('Question4.stopped', Question4.tStopRefresh)
    questions.addData('scales1.started', scales1.tStartRefresh)
    questions.addData('scales1.stopped', scales1.tStopRefresh)
    questions.addData('scales2.started', scales2.tStartRefresh)
    questions.addData('scales2.stopped', scales2.tStopRefresh)
    questions.addData('scales3.started', scales3.tStartRefresh)
    questions.addData('scales3.stopped', scales3.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('rating_4.response', rating_4.getRating())
    questions.addData('rating_4.rt', rating_4.getRT())
    questions.addData('rating_4.started', rating_4.tStart)
    questions.addData('rating_4.stopped', rating_4.tStop)
    # the Routine "Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Q5"-------
    t = 0
    Q5Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_5.reset()
    # keep track of which components have finished
    Q5Components = [Question5, scale_1, text_5, text_6, rating_5]
    for thisComponent in Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Q5"-------
    while continueRoutine:
        # get current time
        t = Q5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question5* updates
        if t >= 0.0 and Question5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question5.tStart = t  # not accounting for scr refresh
            Question5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question5, 'tStartRefresh')  # time at next scr refresh
            Question5.setAutoDraw(True)
        
        # *scale_1* updates
        if t >= 0.0 and scale_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_1.tStart = t  # not accounting for scr refresh
            scale_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scale_1, 'tStartRefresh')  # time at next scr refresh
            scale_1.setAutoDraw(True)
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # not accounting for scr refresh
            text_5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # not accounting for scr refresh
            text_6.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        # *rating_5* updates
        if t >= 0.0 and rating_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_5.tStart = t  # not accounting for scr refresh
            rating_5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_5, 'tStartRefresh')  # time at next scr refresh
            rating_5.setAutoDraw(True)
        continueRoutine &= rating_5.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Q5"-------
    for thisComponent in Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    questions.addData('Question5.started', Question5.tStartRefresh)
    questions.addData('Question5.stopped', Question5.tStopRefresh)
    questions.addData('scale_1.started', scale_1.tStartRefresh)
    questions.addData('scale_1.stopped', scale_1.tStopRefresh)
    questions.addData('text_5.started', text_5.tStartRefresh)
    questions.addData('text_5.stopped', text_5.tStopRefresh)
    questions.addData('text_6.started', text_6.tStartRefresh)
    questions.addData('text_6.stopped', text_6.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('rating_5.response', rating_5.getRating())
    questions.addData('rating_5.rt', rating_5.getRT())
    questions.addData('rating_5.started', rating_5.tStart)
    questions.addData('rating_5.stopped', rating_5.tStop)
    # the Routine "Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'questions'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
