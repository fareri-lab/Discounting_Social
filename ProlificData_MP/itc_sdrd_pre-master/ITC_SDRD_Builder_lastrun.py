#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on August 02, 2019, at 08:22
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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'newer wtp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jojo\\Downloads\\Psychopy\\Michael\\ITC_SDRD_Builder_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

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
leftbox = visual.TextStim(win=win, name='leftbox',
    text='default text',
    font='Times New Roman',
    pos=(-0.5, 0.0), height=0.094, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rightbox = visual.TextStim(win=win, name='rightbox',
    text='default text',
    font='Times New Roman',
    pos=(0.5, 0.0), height=0.094, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
money1 = visual.TextStim(win=win, name='money1',
    text='default text',
    font='Arial',
    pos=(0.5, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
money2 = visual.TextStim(win=win, name='money2',
    text='default text',
    font='Arial',
    pos=(-0.5, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='money.png', mask=None,
    ori=0, pos=(0, 0.5), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Immed_Resp = visual.TextStim(win=win, name='Immed_Resp',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Delay_Resp = visual.TextStim(win=win, name='Delay_Resp',
    text=Delay,
    font='Arial',
    pos=(0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
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
spacebar = event.BuilderKeyResponse()
# keep track of which components have finished
IntroductionComponents = [Instructions, spacebar]
for thisComponent in IntroductionComponents:
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
        Instructions.tStart = t
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    
    # *spacebar* updates
    if t >= 0.0 and spacebar.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar.tStart = t
        spacebar.frameNStart = frameN  # exact frame index
        spacebar.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spacebar.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spacebar.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spacebar.keys = theseKeys[-1]  # just the last key pressed
            spacebar.rt = spacebar.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if spacebar.keys in ['', [], None]:  # No response was made
    spacebar.keys=None
thisExp.addData('spacebar.keys',spacebar.keys)
if spacebar.keys != None:  # we had a response
    thisExp.addData('spacebar.rt', spacebar.rt)
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
    leftbox.setText(Immed)
    rightbox.setText(Delay)
    responses = event.BuilderKeyResponse()
    money1.setText(Time)
    money2.setText('Now')
    border_right = visual.Circle(win,radius = 0.4, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (0.5, 0.1), opacity = 1)
    border_left = visual.Circle(win,radius = 0.4, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (-0.5, 0.1), opacity = 1)
    
    blank.setText('')
    Immed_Resp.setColor('red', colorSpace='rgb')
    Immed_Resp.setPos((-0.5, 0))
    Immed_Resp.setText(Immed)
    Immed_Resp.setFont('Arial')
    Immed_Resp.setHeight(0.1)
    # keep track of which components have finished
    ChoiceComponents = [leftbox, rightbox, responses, money1, money2, blank, image, Immed_Resp, Delay_Resp]
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *leftbox* updates
        if t >= 0.0 and leftbox.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftbox.tStart = t
            leftbox.frameNStart = frameN  # exact frame index
            leftbox.setAutoDraw(True)
        
        # *rightbox* updates
        if t >= 0.0 and rightbox.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightbox.tStart = t
            rightbox.frameNStart = frameN  # exact frame index
            rightbox.setAutoDraw(True)
        
        # *responses* updates
        if t >= 0.0 and responses.status == NOT_STARTED:
            # keep track of start time/frame for later
            responses.tStart = t
            responses.frameNStart = frameN  # exact frame index
            responses.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(responses.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if responses.status == STARTED and bool(Immed_Resp.status == finished):
            responses.status = FINISHED
        if responses.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                responses.keys = theseKeys[-1]  # just the last key pressed
                responses.rt = responses.clock.getTime()
        
        # *money1* updates
        if t >= 0.0 and money1.status == NOT_STARTED:
            # keep track of start time/frame for later
            money1.tStart = t
            money1.frameNStart = frameN  # exact frame index
            money1.setAutoDraw(True)
        
        # *money2* updates
        if t >= 0.0 and money2.status == NOT_STARTED:
            # keep track of start time/frame for later
            money2.tStart = t
            money2.frameNStart = frameN  # exact frame index
            money2.setAutoDraw(True)
        if responses.keys == '1':
            border_left.autoDraw=True
        
        if responses.keys =='2':
            border_right.autoDraw=True
        
        if money1.status == FINISHED:
            border_left.autoDraw = False
        
        if money2.status==FINISHED:
            border_right.autoDraw = False
        
        # *blank* updates
        if (border_right. autoDraw==False) and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        if blank.status == STARTED and t >= (blank.tStart + 1.0):
            blank.setAutoDraw(False)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *Immed_Resp* updates
        if (responses.keys == '1') and Immed_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Immed_Resp.tStart = t
            Immed_Resp.frameNStart = frameN  # exact frame index
            Immed_Resp.setAutoDraw(True)
        if Immed_Resp.status == STARTED and t >= (Immed_Resp.tStart + 2):
            Immed_Resp.setAutoDraw(False)
        
        # *Delay_Resp* updates
        if (responses.keys == "2") and Delay_Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Delay_Resp.tStart = t
            Delay_Resp.frameNStart = frameN  # exact frame index
            Delay_Resp.setAutoDraw(True)
        if Delay_Resp.status == STARTED and t >= (Delay_Resp.tStart + 2):
            Delay_Resp.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # check responses
    if responses.keys in ['', [], None]:  # No response was made
        responses.keys=None
    Loop.addData('responses.keys',responses.keys)
    if responses.keys != None:  # we had a response
        Loop.addData('responses.rt', responses.rt)
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [text_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Loop'


# ------Prepare to start Routine "Thank_You"-------
t = 0
Thank_YouClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ThankYou.setText('Thank you for participating!\n\nPlease notify the experimenter before moving on to the final \npart of the task')
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Thank_YouComponents = [ThankYou, key_resp_2]
for thisComponent in Thank_YouComponents:
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
        ThankYou.tStart = t
        ThankYou.frameNStart = frameN  # exact frame index
        ThankYou.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
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
            Question1.tStart = t
            Question1.frameNStart = frameN  # exact frame index
            Question1.setAutoDraw(True)
        
        # *scale_msg1* updates
        if t >= 0.0 and scale_msg1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg1.tStart = t
            scale_msg1.frameNStart = frameN  # exact frame index
            scale_msg1.setAutoDraw(True)
        
        # *scale_msg2* updates
        if t >= 0.0 and scale_msg2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg2.tStart = t
            scale_msg2.frameNStart = frameN  # exact frame index
            scale_msg2.setAutoDraw(True)
        
        # *scale_msg3* updates
        if t >= 0.0 and scale_msg3.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg3.tStart = t
            scale_msg3.frameNStart = frameN  # exact frame index
            scale_msg3.setAutoDraw(True)
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # store data for questions (TrialHandler)
    questions.addData('rating.response', rating.getRating())
    questions.addData('rating.rt', rating.getRT())
    questions.addData('rating.history', rating.getHistory())
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
            Question2.tStart = t
            Question2.frameNStart = frameN  # exact frame index
            Question2.setAutoDraw(True)
        
        # *scale1* updates
        if t >= 0.0 and scale1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale1.tStart = t
            scale1.frameNStart = frameN  # exact frame index
            scale1.setAutoDraw(True)
        
        # *scale2* updates
        if t >= 0.0 and scale2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale2.tStart = t
            scale2.frameNStart = frameN  # exact frame index
            scale2.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        # *rating_2* updates
        if t >= 0.0 and rating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_2.tStart = t
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # store data for questions (TrialHandler)
    questions.addData('rating_2.response', rating_2.getRating())
    questions.addData('rating_2.rt', rating_2.getRT())
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
            Question3.tStart = t
            Question3.frameNStart = frameN  # exact frame index
            Question3.setAutoDraw(True)
        
        # *scalemsg1* updates
        if t >= 0.0 and scalemsg1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scalemsg1.tStart = t
            scalemsg1.frameNStart = frameN  # exact frame index
            scalemsg1.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        # *rating_3* updates
        if t >= 0.0 and rating_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_3.tStart = t
            rating_3.frameNStart = frameN  # exact frame index
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # store data for questions (TrialHandler)
    questions.addData('rating_3.response', rating_3.getRating())
    questions.addData('rating_3.rt', rating_3.getRT())
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
            Question4.tStart = t
            Question4.frameNStart = frameN  # exact frame index
            Question4.setAutoDraw(True)
        
        # *scales1* updates
        if t >= 0.0 and scales1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales1.tStart = t
            scales1.frameNStart = frameN  # exact frame index
            scales1.setAutoDraw(True)
        
        # *scales2* updates
        if t >= 0.0 and scales2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales2.tStart = t
            scales2.frameNStart = frameN  # exact frame index
            scales2.setAutoDraw(True)
        
        # *scales3* updates
        if t >= 0.0 and scales3.status == NOT_STARTED:
            # keep track of start time/frame for later
            scales3.tStart = t
            scales3.frameNStart = frameN  # exact frame index
            scales3.setAutoDraw(True)
        # *rating_4* updates
        if t >= 0.0 and rating_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_4.tStart = t
            rating_4.frameNStart = frameN  # exact frame index
            rating_4.setAutoDraw(True)
        continueRoutine &= rating_4.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # store data for questions (TrialHandler)
    questions.addData('rating_4.response', rating_4.getRating())
    questions.addData('rating_4.rt', rating_4.getRT())
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
            Question5.tStart = t
            Question5.frameNStart = frameN  # exact frame index
            Question5.setAutoDraw(True)
        
        # *scale_1* updates
        if t >= 0.0 and scale_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_1.tStart = t
            scale_1.frameNStart = frameN  # exact frame index
            scale_1.setAutoDraw(True)
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        # *rating_5* updates
        if t >= 0.0 and rating_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_5.tStart = t
            rating_5.frameNStart = frameN  # exact frame index
            rating_5.setAutoDraw(True)
        continueRoutine &= rating_5.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # store data for questions (TrialHandler)
    questions.addData('rating_5.response', rating_5.getRating())
    questions.addData('rating_5.rt', rating_5.getRT())
    # the Routine "Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'questions'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
