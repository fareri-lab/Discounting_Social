/************************* 
 * Itc_Sdrd_Builder Test *
 *************************/

import { PsychoJS } from './lib/core-3.0.7.js';
import * as core from './lib/core-3.0.7.js';
import { TrialHandler } from './lib/data-3.0.7.js';
import { Scheduler } from './lib/util-3.0.7.js';
import * as util from './lib/util-3.0.7.js';
import * as visual from './lib/visual-3.0.7.js';
import { Sound } from './lib/sound-3.0.7.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([-1.0, -1.0, -1.0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'ITC_SDRD_Builder';  // from the Builder filename that created this script
let expInfo = {'Prolific ID *': '', 'Race (1=White 2=Black 3=Asian 4=Hispanic/Latino 5=Other) *': '', 'Sex (1=Male 2=Female 3=Other) *': '', 'Age *': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(IntroductionRoutineBegin);
flowScheduler.add(IntroductionRoutineEachFrame);
flowScheduler.add(IntroductionRoutineEnd);
flowScheduler.add(Introduction2RoutineBegin);
flowScheduler.add(Introduction2RoutineEachFrame);
flowScheduler.add(Introduction2RoutineEnd);
const LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LoopLoopBegin, LoopLoopScheduler);
flowScheduler.add(LoopLoopScheduler);
flowScheduler.add(LoopLoopEnd);
flowScheduler.add(Thank_YouRoutineBegin);
flowScheduler.add(Thank_YouRoutineEachFrame);
flowScheduler.add(Thank_YouRoutineEnd);
const questionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(questionsLoopBegin, questionsLoopScheduler);
flowScheduler.add(questionsLoopScheduler);
flowScheduler.add(questionsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.0.7';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls("https://adelphiderner.co1.qualtrics.com/jfe/form/SV_40Z0dWo03o54Fhz","google.com")
  return Scheduler.Event.NEXT;
}

var IntroductionClock;
var Instructions;
var ChoiceClock;
var responseClock;
var LeftMoney;
var RightMoney;
//var TimeText;
//var NowText;
var conditionalBlank;
var image;
var ISIClock;
var ISI;
var Thank_YouClock;
var ThankYou;
var responseTimer;
var Q1Clock;
var Question1;
var scale_msg1;
var scale_msg2;
//var scale_msg3;
var Q2Clock;
var Question2;
var scale2_msg2;
var scale2_msg1;
var scale2_msg3;
var Q3Clock;
var Question3;
var scale3_msg3;
var scale3_msg2;
var scale3_msg1;
var Q4Clock;
var Question4;
var scale4_msg1;
var scale4_msg2;
var scale4_msg3;
var Q5Clock;
var Question5;
var scale5_msg1;
var scale5_msg2;
var scale5_msg3;
var globalClock;
var routineTimer;
var slider1;
var slider2;
var slider1Clock;
var slider2Clock; 
var slideKeys;
var slideKeys2;
var slider3Clock; 
var slideKeys3;
var slider3;
var slider4Clock; 
var slideKeys4;
var slider4;
var slider5Clock; 
var slideKeys5;
var slider5;
var Introduction2Clock;
var Instructions2;


function experimentInit() {
  // Initialize components for Routine "Introduction"
  IntroductionClock = new util.Clock();
  Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'For this next part of the study, we want to understand how you make choices about money.\n\nImagine that you have the choice of getting some money now (today) or in the future.\n\nFor each of the following questions, you will be asked to make a choice between two monetary options, one available today, and one available in the future. \n\nPress 1 if you want the option on the left.\nPress 2 if you want the option on the right.\n Please use the numbers at the top of your keyboard and NOT on the number pad. \n You will have 5 seconds to make your choice. \n\nPress the SPACEBAR to continue.',
    font: 'Arial',
    pos: [0, 0], height: 0.045,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Introduction2Clock = new util.Clock();
  Instructions2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'Once you make your response, the text of the option you chose will turn red, indicating your response was recorded.\n\nThe choices you will be making are hypothetical, but please treat them as if they are real. \n\nThere are no right or wrong answers in this task, just answer naturally.\n\n When you are ready, press the SPACEBAR to start!',
    font: 'Arial',
    pos: [0, 0], height: 0.045,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Choice"
  ChoiceClock = new util.Clock();
  LeftMoney = new visual.TextStim({
    win: psychoJS.window,
    name: 'LeftMoney',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), 0.0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  RightMoney = new visual.TextStim({
    win: psychoJS.window,
    name: 'RightMoney',
    text: 'default text',
    font: 'Arial',
    pos: [0.49, 0.0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
//   TimeText = new visual.TextStim({
//     win: psychoJS.window,
//     name: 'TimeText',
//     text: 'default text',
//     font: 'Arial',
//     pos: [0.5, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0,
//     color: new util.Color('white'),  opacity: 1,
//     depth: -3.0 
//   });
  
//   NowText = new visual.TextStim({
//     win: psychoJS.window,
//     name: 'NowText',
//     text: 'default text',
//     font: 'Arial',
//     pos: [(- 0.5), (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0,
//     color: new util.Color('white'),  opacity: 1,
//     depth: -4.0 
//   });
  
  conditionalBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'conditionalconditionalBlank',
    text: '',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'money.png', mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });

  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISI = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI',
    text: '+',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Thank_You"
  Thank_YouClock = new util.Clock();
  ThankYou = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankYou',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0], height: 0.065,  wrapWidth: 1.3, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Q1"
  Q1Clock = new util.Clock();
  Question1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question1',
    text: 'How likely were you to choose an immediate reward over a delayed reward?',
    font: 'Arial',
    pos: [0, 0.2], height: 0.08,  wrapWidth: 1.2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slideKeys = new core.BuilderKeyResponse(psychoJS);
  slider1Clock = new util.Clock();
  slider1 = new visual.Slider({
    win: psychoJS.window, name: 'slider1',
    size: [1.0, 0.03], pos: [0, (- 0.15)],
    labels: ['1', '2', '3', '4', '5', '6', '7'], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.TRIANGLE_MARKER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  scale_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg2',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
 /* 
  scale_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg3',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Q2"
  Q2Clock = new util.Clock();
  Question2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question2',
    text: 'How likely were you to choose a non-social experience over a social experience?',
    font: 'Arial',
    pos: [0, 0.2], height: 0.08,  wrapWidth: 1.2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slideKeys2 = new core.BuilderKeyResponse(psychoJS);
  slider2Clock = new util.Clock();
  slider2 = new visual.Slider({
    win: psychoJS.window, name: 'slider2',
    size: [1.0, 0.03], pos: [0, (- 0.15)],
    labels: ['1', '2', '3', '4', '5', '6', '7'], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.TRIANGLE_MARKER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  

  scale2_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale2_msg1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });

  scale2_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  scale2_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale2_msg3',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Q3"
  Q3Clock = new util.Clock();
  Question3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question3',
    text: 'How likely were you to choose experiences involving friends over experiences involving family?',
    font: 'Arial',
    pos: [0, 0.2], height: 0.08,  wrapWidth: 1.2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slideKeys3 = new core.BuilderKeyResponse(psychoJS);
  slider3Clock = new util.Clock();
  slider3 = new visual.Slider({
    win: psychoJS.window, name: 'slider3',
    size: [1.0, 0.03], pos: [0, (- 0.15)],
    labels: ['1', '2', '3', '4', '5', '6', '7'], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.TRIANGLE_MARKER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  
  scale3_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale3_msg3',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale3_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale3_msg2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scale3_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale3_msg1',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Q4"
  Q4Clock = new util.Clock();
  Question4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question4',
    text: 'How likely were you to choose experiences involving family over experiences involving a significant other?',
    font: 'Arial',
    pos: [0, 0.2], height: 0.08,  wrapWidth: 1.2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slideKeys4 = new core.BuilderKeyResponse(psychoJS);
  slider4Clock = new util.Clock();
  slider4 = new visual.Slider({
    win: psychoJS.window, name: 'slider4',
    size: [1.0, 0.03], pos: [0, (- 0.15)],
    labels: ['1', '2', '3', '4', '5', '6', '7'], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.TRIANGLE_MARKER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  
  scale4_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale4_msg1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale4_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale4_msg2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scale4_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale4_msg3',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Q5"
  Q5Clock = new util.Clock();
  Question5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question5',
    text: 'How much did you enjoy participating?',
    font: 'Arial',
    pos: [0, 0.2], height: 0.08,  wrapWidth: 1.2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slideKeys5 = new core.BuilderKeyResponse(psychoJS);
  slider5Clock = new util.Clock();
  slider5 = new visual.Slider({
    win: psychoJS.window, name: 'slider5',
    size: [1.0, 0.03], pos: [0, (- 0.15)],
    labels: ['1', '2', '3', '4', '5', '6', '7'], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1, style: [visual.Slider.Style.RATING, visual.Slider.Style.TRIANGLE_MARKER],
    color: new util.Color('LightGray'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, 
    flip: false,
  });
  
  
  scale5_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale5_msg1',
    text: 'Not at all (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale5_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale5_msg2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scale5_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale5_msg3',
    text: 'Very Much (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  */
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer(); // to track time remaining of each (non-slip) routine
  responseTimer = new util.CountdownTimer();
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var spacebar;
var IntroductionComponents;
function IntroductionRoutineBegin() {
  //------Prepare to start Routine 'Introduction'-------
  t = 0;
  IntroductionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  spacebar = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  IntroductionComponents = [];
  IntroductionComponents.push(Instructions);
  IntroductionComponents.push(spacebar);
  
  for (const thisComponent of IntroductionComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function IntroductionRoutineEachFrame() {
  //------Loop for each frame of Routine 'Introduction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = IntroductionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Instructions* updates
  if (t >= 0.0 && Instructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Instructions.tStart = t;  // (not accounting for frame time here)
    Instructions.frameNStart = frameN;  // exact frame index
    Instructions.setAutoDraw(true);
  }

  
  // *spacebar* updates
  if (t >= 0.0 && spacebar.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    spacebar.tStart = t;  // (not accounting for frame time here)
    spacebar.frameNStart = frameN;  // exact frame index
    spacebar.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { spacebar.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (spacebar.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      spacebar.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      spacebar.rt = spacebar.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of IntroductionComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function IntroductionRoutineEnd() {
  //------Ending Routine 'Introduction'-------
  for (const thisComponent of IntroductionComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (spacebar.keys === undefined || spacebar.keys.length === 0) {    // No response was made
      spacebar.keys = undefined;
  }
  
  psychoJS.experiment.addData('spacebar.keys', spacebar.keys);
  if (typeof spacebar.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('spacebar.rt', spacebar.rt);
      routineTimer.reset();
      }
  
  // the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var spacebar2;
var Introduction2Components;
function Introduction2RoutineBegin() {
  //------Prepare to start Routine 'Introduction2'-------
  t = 0;
  Introduction2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  spacebar2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Introduction2Components = [];
  Introduction2Components.push(Instructions2);
  Introduction2Components.push(spacebar2);
  
  for (const thisComponent of Introduction2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function Introduction2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Introduction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Introduction2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Instructions* updates
  if (t >= 0.0 && Instructions2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Instructions2.tStart = t;  // (not accounting for frame time here)
    Instructions2.frameNStart = frameN;  // exact frame index
    Instructions2.setAutoDraw(true);
  }

  
  // *spacebar* updates
  if (t >= 0.0 && spacebar2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    spacebar2.tStart = t;  // (not accounting for frame time here)
    spacebar2.frameNStart = frameN;  // exact frame index
    spacebar2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { spacebar.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (spacebar.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      spacebar2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      spacebar2.rt = spacebar.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Introduction2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Introduction2RoutineEnd() {
  //------Ending Routine 'Introduction'-------
  for (const thisComponent of Introduction2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (spacebar2.keys === undefined || spacebar2.keys.length === 0) {    // No response was made
      spacebar2.keys = undefined;
  }
  
  psychoJS.experiment.addData('spacebar2.keys', spacebar2.keys);
  if (typeof spacebar2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('spacebar2.rt', spacebar2.rt);
      routineTimer.reset();
      }
  
  // the Routine "Introduction2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Loop;
function LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Loop = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'IntertemporalChoice_17item_test_v2_gitlab.csv',
    seed: undefined, name: 'Loop'});
  psychoJS.experiment.addLoop(Loop); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisLoop of Loop) {
    thisScheduler.add(importConditions(Loop));
    thisScheduler.add(ChoiceRoutineBegin);
    thisScheduler.add(ChoiceRoutineEachFrame);
    thisScheduler.add(ChoiceRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisLoop));
  }

  return Scheduler.Event.NEXT;
}


function LoopLoopEnd() {
  psychoJS.experiment.removeLoop(Loop);

  return Scheduler.Event.NEXT;
}

var questions;
function questionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  questions = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'questions'});
  psychoJS.experiment.addLoop(questions); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisQuestion of questions) {
    thisScheduler.add(importConditions(questions));
    thisScheduler.add(Q1RoutineBegin);
    thisScheduler.add(Q1RoutineEachFrame);
    thisScheduler.add(Q1RoutineEnd);
/*    thisScheduler.add(Q2RoutineBegin);
    thisScheduler.add(Q2RoutineEachFrame);
    thisScheduler.add(Q2RoutineEnd);
    thisScheduler.add(Q3RoutineBegin);
    thisScheduler.add(Q3RoutineEachFrame);
    thisScheduler.add(Q3RoutineEnd);
    thisScheduler.add(Q4RoutineBegin);
    thisScheduler.add(Q4RoutineEachFrame);
    thisScheduler.add(Q4RoutineEnd);
    thisScheduler.add(Q5RoutineBegin);
    thisScheduler.add(Q5RoutineEachFrame);
    thisScheduler.add(Q5RoutineEnd); */
    thisScheduler.add(endLoopIteration(thisQuestion));
  }

  return Scheduler.Event.NEXT;
}


function questionsLoopEnd() {
  psychoJS.experiment.removeLoop(questions);

  return Scheduler.Event.NEXT;
}

var responses;
var ChoiceComponents;
function ChoiceRoutineBegin() {
  //------Prepare to start Routine 'Choice'-------
  t = 0;
  ChoiceClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  LeftMoney.setText(Left_Choice_Text);
  RightMoney.setText(Right_Choice_Text);
  responses = new core.BuilderKeyResponse(psychoJS);
  responseClock = new util.Clock();
//  TimeText.setText(Time);
  //NowText.setText('Now');
  conditionalBlank.setText('');
  
  // keep track of which components have finished
  ChoiceComponents = [];
  ChoiceComponents.push(LeftMoney);
  ChoiceComponents.push(RightMoney);
  ChoiceComponents.push(responses);
  ChoiceComponents.push(responseClock);  
  //ChoiceComponents.push(TimeText);
  //ChoiceComponents.push(NowText);
  ChoiceComponents.push(conditionalBlank);
  ChoiceComponents.push(image);

  
  for (const thisComponent of ChoiceComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}
var t1;
var frameRemains;
function ChoiceRoutineEachFrame() {
  //------Loop for each frame of Routine 'Choice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ChoiceClock.getTime();
 // responseTimer.reset();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame

  // *LeftMoney* updates
  if (t >= 0.0 && LeftMoney.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LeftMoney.tStart = t;  // (not accounting for frame time here)
    LeftMoney.frameNStart = frameN;  // exact frame index
    LeftMoney.setAutoDraw(true);
  }

// set time limit of 5 seconds for choice
  frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (LeftMoney.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    LeftMoney.setAutoDraw(false);
  }


  // *RightMoney* updates
  if (t >= 0.0 && RightMoney.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    RightMoney.tStart = t;  // (not accounting for frame time here)
    RightMoney.frameNStart = frameN;  // exact frame index
    RightMoney.setAutoDraw(true);
  }

// set time limit of 5 seconds for choice
  frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (RightMoney.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    RightMoney.setAutoDraw(false);
  }
  
  // *responses* updates
  if (t >= 0.0 && responses.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    responses.tStart = t;  // (not accounting for frame time here)
    responses.frameNStart = frameN;  // exact frame index
    responses.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { responses.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

//time limit
  frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (responses.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    responses.status = PsychoJS.Status.FINISHED;
  }


// I commented this out because the variable exResponses isn't defined anywhere, but I replaced it with the lines right below it using the variable 'responses'
//   if (exResponses.keys.length > 0) {
//     exResponses.status = PsychoJS.Status.FINISHED;
//   }

//   when they make a response, don't let them make a second response
  if (responses.keys.length > 0) {
    responses.status = PsychoJS.Status.FINISHED;
  }

  if (responses.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['1', '2']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      responses.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      responses.rt = responses.clock.getTime();
    }
  }
  
  
  // *TimeText* updates
//   if (t >= 0.0 && TimeText.status === PsychoJS.Status.NOT_STARTED) {
//     // keep track of start time/frame for later
//     TimeText.tStart = t;  // (not accounting for frame time here)
//     TimeText.frameNStart = frameN;  // exact frame index
//     TimeText.setAutoDraw(true);
//   }

  
  // *NowText* updates
//   if (t >= 0.0 && NowText.status === PsychoJS.Status.NOT_STARTED) {
//     // keep track of start time/frame for later
//     NowText.tStart = t;  // (not accounting for frame time here)
//     NowText.frameNStart = frameN;  // exact frame index
//     NowText.setAutoDraw(true);
//   }

  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  
  if (responses.keys.length > 0){
      responses.status = PsychoJS.Status.FINISHED; //don't allow more than one response 
      //responseClock.reset();
    //   t1 = responseClock.getTime();
    //   responseTimer.reset();
    //   responseTimer.add(2.000000);
  }

  if (responses.keys == '1') {
      LeftMoney.setColor(new util.Color(DecisionColor));
//      NowText.setColor(new util.Color(DecisionColor));
  }
  
  if (responses.keys == '2') {
      RightMoney.setColor(new util.Color(DecisionColor));
    //   TimeText.setColor(new util.Color(DecisionColor));
  } 
  
  
  if (t>= 5.0 && responses.keys.length === 0) {
      conditionalBlank.setAutoDraw(false);
      continueRoutine = false;
  }
    
  // *conditionalBlank* updates
  if (responses.keys.length > 0 && conditionalBlank.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    conditionalBlank.tStart = t;  // (not accounting for frame time here)
    conditionalBlank.frameNStart = frameN;  // exact frame index
    conditionalBlank.setAutoDraw(true);
  }


  if (conditionalBlank.status === PsychoJS.Status.STARTED && t >= (conditionalBlank.tStart + 2.0)) {
    conditionalBlank.setAutoDraw(false);
  }

//   show the response for 2 seconds, then move on to next trial
 if (conditionalBlank.status == PsychoJS.Status.FINISHED){
    LeftMoney.setAutoDraw(false);
    RightMoney.setAutoDraw(false);
    //TimeText.setAutoDraw(false);
//    NowText.setAutoDraw(false);
    continueRoutine = false;
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of ChoiceComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ChoiceRoutineEnd() {
  //------Ending Routine 'Choice'-------
  for (const thisComponent of ChoiceComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (responses.keys === undefined || responses.keys.length === 0) {    // No response was made
      responses.keys = undefined;
  }

  psychoJS.experiment.addData('responses.keys', responses.keys);
  if (typeof responses.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('responses.rt', responses.rt);
      }
  
  LeftMoney.setColor(new util.Color("white"));
  RightMoney.setColor(new util.Color("white"));
//  NowText.setColor(new util.Color("white"));
  //TimeText.setColor(new util.Color("white"));
  

  // the Routine "Choice" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();

  return Scheduler.Event.NEXT;
}

var ISIComponents;
function ISIRoutineBegin() {
  //------Prepare to start Routine 'ISI'-------
  t = 0;
  ISIClock.reset(); // clock
  frameN = -1;
  routineTimer.add(ITI);
  // update component parameters for each repeat
  // keep track of which components have finished
  ISIComponents = [];
  ISIComponents.push(ISI);
  
  for (const thisComponent of ISIComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function ISIRoutineEachFrame() {
  //------Loop for each frame of Routine 'ISI'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ISIClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *ISI* updates
  if (t >= 0.0 && ISI.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ISI.tStart = t;  // (not accounting for frame time here)
    ISI.frameNStart = frameN;  // exact frame index
    ISI.setAutoDraw(true);
  }

  frameRemains = 0.0 + ITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ISI.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ISI.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of ISIComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function ISIRoutineEnd() {
  //------Ending Routine 'ISI'-------
  for (const thisComponent of ISIComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var key_resp_2;
var Thank_YouComponents;
function Thank_YouRoutineBegin() {
  //------Prepare to start Routine 'Thank_You'-------
  t = 0;
  Thank_YouClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  ThankYou.setText('Thank you for participating!\n\nNow you will be answering a few questions about your experience during the task. \n\nFor each question, use your mouse to click on the scale to respond, then press ENTER to move on. \n\nPlease press the SPACEBAR to continue!');
  key_resp_2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Thank_YouComponents = [];
  Thank_YouComponents.push(ThankYou);
  Thank_YouComponents.push(key_resp_2);
  
  for (const thisComponent of Thank_YouComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Thank_YouRoutineEachFrame() {
  //------Loop for each frame of Routine 'Thank_You'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Thank_YouClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *ThankYou* updates
  if (t >= 0.0 && ThankYou.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ThankYou.tStart = t;  // (not accounting for frame time here)
    ThankYou.frameNStart = frameN;  // exact frame index
    ThankYou.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    key_resp_2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_2.rt = key_resp_2.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Thank_YouComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Thank_YouRoutineEnd() {
  //------Ending Routine 'Thank_You'-------
  for (const thisComponent of Thank_YouComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_2.keys === undefined || key_resp_2.keys.length === 0) {    // No response was made
      key_resp_2.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  // the Routine "Thank_You" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Q1Components;
function Q1RoutineBegin() {
  //------Prepare to start Routine 'Q1'-------
  t = 0;
  Q1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q1Components = [];
  Q1Components.push(Question1);
  Q1Components.push(slider1);
  Q1Components.push(slider1Clock);
  Q1Components.push(slideKeys);
  Q1Components.push(scale_msg1);
  Q1Components.push(scale_msg2);
//  Q1Components.push(scale_msg3);
  
  for (const thisComponent of Q1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Q1RoutineEachFrame() {
  //------Loop for each frame of Routine 'Q1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Question1* updates
  if (t >= 0.0 && Question1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Question1.tStart = t;  // (not accounting for frame time here)
    Question1.frameNStart = frameN;  // exact frame index
    Question1.setAutoDraw(true);
  }

  //   display the ratings scale
  if (t >= 0.0 && slider1.status === PsychoJS.Status.NOT_STARTED) {
    slider1.tStart = t;
    slider1.frameNStart = frameN;
    slider1.setAutoDraw(true);
  }

  
  // *scale_msg1* updates
  if (t >= 0.0 && scale_msg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale_msg1.tStart = t;  // (not accounting for frame time here)
    scale_msg1.frameNStart = frameN;  // exact frame index
    scale_msg1.setAutoDraw(true);
  }

  
  // *scale_msg2* updates
  if (t >= 0.0 && scale_msg2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale_msg2.tStart = t;  // (not accounting for frame time here)
    scale_msg2.frameNStart = frameN;  // exact frame index
    scale_msg2.setAutoDraw(true);
  }

/*  
  // *scale_msg3* updates
  if (t >= 0.0 && scale_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale_msg3.tStart = t;  // (not accounting for frame time here)
    scale_msg3.frameNStart = frameN;  // exact frame index
    scale_msg3.setAutoDraw(true);
  }
*/

// let them press enter to record the answer
  if (t >= 0.0 && slideKeys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slideKeys.tStart = t;  // (not accounting for frame time here)
    slideKeys.frameNStart = frameN;  // exact frame index
    slideKeys.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { slideKeys.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
 if (slideKeys.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      slideKeys.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      slideKeys.rt = slideKeys.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
  
    }
  }



  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Q1Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q1RoutineEnd() {
  //------Ending Routine 'Q1'-------
  for (const thisComponent of Q1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  psychoJS.experiment.addData('slider1.response', slider1.getRating());
  psychoJS.experiment.addData('slider1.rt', slider1.getRT());
  
  if (slideKeys.keys === undefined || slideKeys.keys.length === 0) {   
    slideKeys.keys = undefined;
  }

  if (typeof slideKeys.keys !== 'undefined') {  
    psychoJS.experiment.addData('slideKeys.rt', slideKeys.rt);
    routineTimer.reset();
  }

  // the Routine "Q1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

/* var Q2Components;
function Q2RoutineBegin() {
  //------Prepare to start Routine 'Q2'-------
  t = 0;
  Q2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q2Components = [];
  Q2Components.push(Question2);
  Q2Components.push(slider2);
  Q2Components.push(slideKeys2);
  Q2Components.push(scale2_msg1);
  Q2Components.push(scale2_msg2);
  Q2Components.push(scale2_msg3);
  
  for (const thisComponent of Q2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Q2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Q2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Question2* updates
  if (t >= 0.0 && Question2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Question2.tStart = t;  // (not accounting for frame time here)
    Question2.frameNStart = frameN;  // exact frame index
    Question2.setAutoDraw(true);
  }

  
  // *scale2_msg1* updates
  if (t >= 0.0 && scale2_msg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale2_msg1.tStart = t;  // (not accounting for frame time here)
    scale2_msg1.frameNStart = frameN;  // exact frame index
    scale2_msg1.setAutoDraw(true);
  }
  
  if (t >= 0.0 && scale2_msg2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale2_msg2.tStart = t;  // (not accounting for frame time here)
    scale2_msg2.frameNStart = frameN;  // exact frame index
    scale2_msg2.setAutoDraw(true);
  }

  
  // *slider2* updates
  if (t >= 0.0 && slider2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slider2.tStart = t;  // (not accounting for frame time here)
    slider2.frameNStart = frameN;  // exact frame index
    slider2.setAutoDraw(true);
  }

  
  // *scale2_msg3* updates
  if (t >= 0.0 && scale2_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale2_msg3.tStart = t;  // (not accounting for frame time here)
    scale2_msg3.frameNStart = frameN;  // exact frame index
    scale2_msg3.setAutoDraw(true);
  }

// let them press enter to record the answer
  if (t >= 0.0 && slideKeys2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slideKeys2.tStart = t;  // (not accounting for frame time here)
    slideKeys2.frameNStart = frameN;  // exact frame index
    slideKeys2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { slideKeys2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
 if (slideKeys2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      slideKeys2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      slideKeys2.rt = slideKeys2.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
  
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Q2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q2RoutineEnd() {
  //------Ending Routine 'Q2'-------
  for (const thisComponent of Q2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  psychoJS.experiment.addData('slider2.response', slider2.getRating());
  psychoJS.experiment.addData('slider2.rt', slider2.getRT());
  
  if (slideKeys2.keys === undefined || slideKeys2.keys.length === 0) {   
    slideKeys2.keys = undefined;
  }

  if (typeof slideKeys2.keys !== 'undefined') {  
    psychoJS.experiment.addData('slideKeys2.rt', slideKeys2.rt);
    routineTimer.reset();
  }
  // the Routine "Q2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Q3Components;
function Q3RoutineBegin() {
  //------Prepare to start Routine 'Q3'-------
  t = 0;
  Q3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q3Components = [];
  Q3Components.push(Question3);
  Q3Components.push(slider3);
  Q3Components.push(slider3Clock);
  Q3Components.push(slideKeys3);
  Q3Components.push(scale3_msg3);
  Q3Components.push(scale3_msg2);
  Q3Components.push(scale3_msg1);
  
  for (const thisComponent of Q3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Q3RoutineEachFrame() {
  //------Loop for each frame of Routine 'Q3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Question3* updates
  if (t >= 0.0 && Question3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Question3.tStart = t;  // (not accounting for frame time here)
    Question3.frameNStart = frameN;  // exact frame index
    Question3.setAutoDraw(true);
  }

  
  // *scale3_msg3* updates
  if (t >= 0.0 && scale3_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale3_msg3.tStart = t;  // (not accounting for frame time here)
    scale3_msg3.frameNStart = frameN;  // exact frame index
    scale3_msg3.setAutoDraw(true);
  }

  
  // *scale3_msg2* updates
  if (t >= 0.0 && scale3_msg2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale3_msg2.tStart = t;  // (not accounting for frame time here)
    scale3_msg2.frameNStart = frameN;  // exact frame index
    scale3_msg2.setAutoDraw(true);
  }

  
  // *scale3_msg1* updates
  if (t >= 0.0 && scale3_msg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale3_msg1.tStart = t;  // (not accounting for frame time here)
    scale3_msg1.frameNStart = frameN;  // exact frame index
    scale3_msg1.setAutoDraw(true);
  }

  // *slider3* updates
  if (t >= 0.0 && slider3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slider3.tStart = t;  // (not accounting for frame time here)
    slider3.frameNStart = frameN;  // exact frame index
    slider3.setAutoDraw(true);
  }
// let them press enter to record the answer
  if (t >= 0.0 && slideKeys3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slideKeys3.tStart = t;  // (not accounting for frame time here)
    slideKeys3.frameNStart = frameN;  // exact frame index
    slideKeys3.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { slideKeys3.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
 if (slideKeys3.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      slideKeys3.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      slideKeys3.rt = slideKeys3.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
  
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Q3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q3RoutineEnd() {
  //------Ending Routine 'Q3'-------
  for (const thisComponent of Q3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  psychoJS.experiment.addData('slider3.response', slider3.getRating());
  psychoJS.experiment.addData('slider3.rt', slider3.getRT());
  
  if (slideKeys3.keys === undefined || slideKeys3.keys.length === 0) {   
    slideKeys3.keys = undefined;
  }

  if (typeof slideKeys3.keys !== 'undefined') {  
    psychoJS.experiment.addData('slideKeys3.rt', slideKeys3.rt);
    routineTimer.reset();
  }
  // the Routine "Q3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Q4Components;
function Q4RoutineBegin() {
  //------Prepare to start Routine 'Q4'-------
  t = 0;
  Q4Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q4Components = [];
  Q4Components.push(Question4);
  Q4Components.push(scale4_msg1);
  Q4Components.push(scale4_msg2);
  Q4Components.push(scale4_msg3);
  Q4Components.push(slider4);
  Q4Components.push(slider4Clock);
  Q4Components.push(slideKeys4);
  
  for (const thisComponent of Q4Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Q4RoutineEachFrame() {
  //------Loop for each frame of Routine 'Q4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Question4* updates
  if (t >= 0.0 && Question4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Question4.tStart = t;  // (not accounting for frame time here)
    Question4.frameNStart = frameN;  // exact frame index
    Question4.setAutoDraw(true);
  }

  
  // *scale4_msg1* updates
  if (t >= 0.0 && scale4_msg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale4_msg1.tStart = t;  // (not accounting for frame time here)
    scale4_msg1.frameNStart = frameN;  // exact frame index
    scale4_msg1.setAutoDraw(true);
  }

  
  // *scale4_msg2* updates
  if (t >= 0.0 && scale4_msg2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale4_msg2.tStart = t;  // (not accounting for frame time here)
    scale4_msg2.frameNStart = frameN;  // exact frame index
    scale4_msg2.setAutoDraw(true);
  }

  
  // *scale4_msg3* updates
  if (t >= 0.0 && scale4_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale4_msg3.tStart = t;  // (not accounting for frame time here)
    scale4_msg3.frameNStart = frameN;  // exact frame index
    scale4_msg3.setAutoDraw(true);
  }

  // *slider4* updates
  if (t >= 0.0 && slider4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slider4.tStart = t;  // (not accounting for frame time here)
    slider4.frameNStart = frameN;  // exact frame index
    slider4.setAutoDraw(true);
  }
// let them press enter to record the answer
  if (t >= 0.0 && slideKeys4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slideKeys4.tStart = t;  // (not accounting for frame time here)
    slideKeys4.frameNStart = frameN;  // exact frame index
    slideKeys4.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { slideKeys2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
 if (slideKeys4.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      slideKeys4.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      slideKeys4.rt = slideKeys4.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
  
    }
  }


  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Q4Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q4RoutineEnd() {
  //------Ending Routine 'Q4'-------
  for (const thisComponent of Q4Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  psychoJS.experiment.addData('slider4.response', slider4.getRating());
  psychoJS.experiment.addData('slider4.rt', slider4.getRT());
  
  if (slideKeys4.keys === undefined || slideKeys4.keys.length === 0) {   
    slideKeys4.keys = undefined;
  }

  if (typeof slideKeys4.keys !== 'undefined') {  
    psychoJS.experiment.addData('slideKeys4.rt', slideKeys4.rt);
    routineTimer.reset();
  }
  // the Routine "Q4" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Q5Components;
function Q5RoutineBegin() {
  //------Prepare to start Routine 'Q5'-------
  t = 0;
  Q5Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q5Components = [];
  Q5Components.push(Question5);
  Q5Components.push(scale5_msg1);
  Q5Components.push(scale5_msg2);
  Q5Components.push(scale5_msg3);
  
  for (const thisComponent of Q5Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Q5RoutineEachFrame() {
  //------Loop for each frame of Routine 'Q5'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Q5Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Question5* updates
  if (t >= 0.0 && Question5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Question5.tStart = t;  // (not accounting for frame time here)
    Question5.frameNStart = frameN;  // exact frame index
    Question5.setAutoDraw(true);
  }

  
  // *scale5_msg1* updates
  if (t >= 0.0 && scale5_msg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale5_msg1.tStart = t;  // (not accounting for frame time here)
    scale5_msg1.frameNStart = frameN;  // exact frame index
    scale5_msg1.setAutoDraw(true);
  }

  
  // *scale5_msg2* updates
  if (t >= 0.0 && scale5_msg2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale5_msg2.tStart = t;  // (not accounting for frame time here)
    scale5_msg2.frameNStart = frameN;  // exact frame index
    scale5_msg2.setAutoDraw(true);
  }

  
  // *scale5_msg3* updates
  if (t >= 0.0 && scale5_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale5_msg3.tStart = t;  // (not accounting for frame time here)
    scale5_msg3.frameNStart = frameN;  // exact frame index
    scale5_msg3.setAutoDraw(true);
  }
  
    // *slider5* updates
  if (t >= 0.0 && slider5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slider5.tStart = t;  // (not accounting for frame time here)
    slider5.frameNStart = frameN;  // exact frame index
    slider5.setAutoDraw(true);
  }
// let them press enter to record the answer
  if (t >= 0.0 && slideKeys5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    slideKeys5.tStart = t;  // (not accounting for frame time here)
    slideKeys5.frameNStart = frameN;  // exact frame index
    slideKeys5.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { slideKeys5.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
 if (slideKeys5.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['return']});
    
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      slideKeys5.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      slideKeys5.rt = slideKeys5.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
  
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of Q5Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Q5RoutineEnd() {
  //------Ending Routine 'Q5'-------
  for (const thisComponent of Q5Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  psychoJS.experiment.addData('slider5.response', slider5.getRating());
  psychoJS.experiment.addData('slider5.rt', slider5.getRT());
  
  if (slideKeys5.keys === undefined || slideKeys5.keys.length === 0) {   
    slideKeys5.keys = undefined;
  }

  if (typeof slideKeys5.keys !== 'undefined') {  
    psychoJS.experiment.addData('slideKeys5.rt', slideKeys5.rt);
    routineTimer.reset();
  }
  
  // the Routine "Q5" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}
*/

function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
//   when they press space, redirect to choice task
//  window.location.replace("https://adelphiderner.co1.qualtrics.com/jfe/form/SV_40Z0dWo03o54Fhz");

  return Scheduler.Event.QUIT;
}
