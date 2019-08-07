/************************* 
 * Itc_Sdrd_Builder Test *
 *************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'ITC_SDRD_Builder';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
  
  return Scheduler.Event.NEXT;
}

var IntroductionClock;
var Instructions;
var ChoiceClock;
var leftbox;
var rightbox;
var money1;
var money2;
var blank;
var image;
var Immed_Resp;
var Delay_Resp;
var ISIClock;
var text_3;
var Thank_YouClock;
var ThankYou;
var Q1Clock;
var Question1;
var scale_msg1;
var scale_msg2;
var scale_msg3;
var Q2Clock;
var Question2;
var scale1;
var scale2;
var text;
var Q3Clock;
var Question3;
var scalemsg1;
var text_2;
var text_4;
var Q4Clock;
var Question4;
var scales1;
var scales2;
var scales3;
var Q5Clock;
var Question5;
var scale_1;
var text_5;
var text_6;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Introduction"
  IntroductionClock = new util.Clock();
  Instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instructions',
    text: 'In this task you will be choosing between an immediate reward or a delayed reward.\n\nIn the following slides: \nPress 1= choose immediate reward \nPress 2= choose delayed reward\n\nWhen you are ready, press the SPACEBAR to start',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Choice"
  ChoiceClock = new util.Clock();
  leftbox = new visual.TextStim({
    win: psychoJS.window,
    name: 'leftbox',
    text: 'default text',
    font: 'Times New Roman',
    pos: [(- 0.5), 0.0], height: 0.094,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  rightbox = new visual.TextStim({
    win: psychoJS.window,
    name: 'rightbox',
    text: 'default text',
    font: 'Times New Roman',
    pos: [0.5, 0.0], height: 0.094,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  money1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'money1',
    text: 'default text',
    font: 'Arial',
    pos: [0.5, (- 0.5)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  money2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'money2',
    text: 'default text',
    font: 'Arial',
    pos: [(- 0.5), (- 0.5)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
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
    ori : 0, pos : [0, 0.5], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  Immed_Resp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Immed_Resp',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  Delay_Resp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Delay_Resp',
    text: Delay,
    font: 'Arial',
    pos: [0.5, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -9.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
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
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Q1"
  Q1Clock = new util.Clock();
  Question1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question1',
    text: 'How likely were you to choose a social experience over a non-social experience?',
    font: 'Arial',
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  scale_msg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale_msg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg2',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scale_msg3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_msg3',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
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
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  scale1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scale2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
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
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  scalemsg1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scalemsg1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Q4"
  Q4Clock = new util.Clock();
  Question4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question4',
    text: 'How likely were you to choose experiences involving family over experiences involving a significant other',
    font: 'Arial',
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  scales1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scales1',
    text: 'Very Unlikely (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  scales2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scales2',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  scales3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scales3',
    text: 'Very Likely (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
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
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  scale_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'scale_1',
    text: 'Not at all (1)',
    font: 'Arial',
    pos: [(- 0.5), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Neutral',
    font: 'Arial',
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Very Much (7)',
    font: 'Arial',
    pos: [0.5, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
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

var Loop;
function LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Loop = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'IntertemporalChoice_17item_test.csv',
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
    thisScheduler.add(Q2RoutineBegin);
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
    thisScheduler.add(Q5RoutineEnd);
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
  leftbox.setText(Immed);
  rightbox.setText(Delay);
  responses = new core.BuilderKeyResponse(psychoJS);
  
  money1.setText(Time);
  money2.setText('Now');
  blank.setText('');
  Immed_Resp.setColor(new util.Color('red'));
  Immed_Resp.setPos([(- 0.5), 0]);
  Immed_Resp.setText(Immed);
  Immed_Resp.setFont('Arial');
  Immed_Resp.setHeight(0.1);
  // keep track of which components have finished
  ChoiceComponents = [];
  ChoiceComponents.push(leftbox);
  ChoiceComponents.push(rightbox);
  ChoiceComponents.push(responses);
  ChoiceComponents.push(money1);
  ChoiceComponents.push(money2);
  ChoiceComponents.push(blank);
  ChoiceComponents.push(image);
  ChoiceComponents.push(Immed_Resp);
  ChoiceComponents.push(Delay_Resp);
  
  for (const thisComponent of ChoiceComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function ChoiceRoutineEachFrame() {
  //------Loop for each frame of Routine 'Choice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ChoiceClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *leftbox* updates
  if (t >= 0.0 && leftbox.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    leftbox.tStart = t;  // (not accounting for frame time here)
    leftbox.frameNStart = frameN;  // exact frame index
    leftbox.setAutoDraw(true);
  }

  
  // *rightbox* updates
  if (t >= 0.0 && rightbox.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rightbox.tStart = t;  // (not accounting for frame time here)
    rightbox.frameNStart = frameN;  // exact frame index
    rightbox.setAutoDraw(true);
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

  if (responses.status === PsychoJS.Status.STARTED && bool((Immed_Resp.status == finished))) {
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
  
  
  // *money1* updates
  if (t >= 0.0 && money1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    money1.tStart = t;  // (not accounting for frame time here)
    money1.frameNStart = frameN;  // exact frame index
    money1.setAutoDraw(true);
  }

  
  // *money2* updates
  if (t >= 0.0 && money2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    money2.tStart = t;  // (not accounting for frame time here)
    money2.frameNStart = frameN;  // exact frame index
    money2.setAutoDraw(true);
  }

  
  // *blank* updates
  if (((border_right.autoDraw == False)) && blank.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    blank.tStart = t;  // (not accounting for frame time here)
    blank.frameNStart = frameN;  // exact frame index
    blank.setAutoDraw(true);
  }

  if (blank.status === PsychoJS.Status.STARTED && t >= (blank.tStart + 1.0)) {
    blank.setAutoDraw(false);
  }
  
  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  
  // *Immed_Resp* updates
  if (((responses.keys == '1')) && Immed_Resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Immed_Resp.tStart = t;  // (not accounting for frame time here)
    Immed_Resp.frameNStart = frameN;  // exact frame index
    Immed_Resp.setAutoDraw(true);
  }

  if (Immed_Resp.status === PsychoJS.Status.STARTED && t >= (Immed_Resp.tStart + 2)) {
    Immed_Resp.setAutoDraw(false);
  }
  
  // *Delay_Resp* updates
  if (((responses.keys == '2')) && Delay_Resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Delay_Resp.tStart = t;  // (not accounting for frame time here)
    Delay_Resp.frameNStart = frameN;  // exact frame index
    Delay_Resp.setAutoDraw(true);
  }

  if (Delay_Resp.status === PsychoJS.Status.STARTED && t >= (Delay_Resp.tStart + 2)) {
    Delay_Resp.setAutoDraw(false);
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
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  ISIComponents = [];
  ISIComponents.push(text_3);
  
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
  
  // *text_3* updates
  if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_3.setAutoDraw(false);
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
  ThankYou.setText('Thank you for participating!\n\nPlease notify the experimenter before moving on to the final \npart of the task');
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
  Q1Components.push(scale_msg1);
  Q1Components.push(scale_msg2);
  Q1Components.push(scale_msg3);
  
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

  
  // *scale_msg3* updates
  if (t >= 0.0 && scale_msg3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale_msg3.tStart = t;  // (not accounting for frame time here)
    scale_msg3.frameNStart = frameN;  // exact frame index
    scale_msg3.setAutoDraw(true);
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
  // the Routine "Q1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Q2Components;
function Q2RoutineBegin() {
  //------Prepare to start Routine 'Q2'-------
  t = 0;
  Q2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  Q2Components = [];
  Q2Components.push(Question2);
  Q2Components.push(scale1);
  Q2Components.push(scale2);
  Q2Components.push(text);
  
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

  
  // *scale1* updates
  if (t >= 0.0 && scale1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale1.tStart = t;  // (not accounting for frame time here)
    scale1.frameNStart = frameN;  // exact frame index
    scale1.setAutoDraw(true);
  }

  
  // *scale2* updates
  if (t >= 0.0 && scale2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale2.tStart = t;  // (not accounting for frame time here)
    scale2.frameNStart = frameN;  // exact frame index
    scale2.setAutoDraw(true);
  }

  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
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
  Q3Components.push(scalemsg1);
  Q3Components.push(text_2);
  Q3Components.push(text_4);
  
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

  
  // *scalemsg1* updates
  if (t >= 0.0 && scalemsg1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scalemsg1.tStart = t;  // (not accounting for frame time here)
    scalemsg1.frameNStart = frameN;  // exact frame index
    scalemsg1.setAutoDraw(true);
  }

  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // *text_4* updates
  if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
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
  Q4Components.push(scales1);
  Q4Components.push(scales2);
  Q4Components.push(scales3);
  
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

  
  // *scales1* updates
  if (t >= 0.0 && scales1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scales1.tStart = t;  // (not accounting for frame time here)
    scales1.frameNStart = frameN;  // exact frame index
    scales1.setAutoDraw(true);
  }

  
  // *scales2* updates
  if (t >= 0.0 && scales2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scales2.tStart = t;  // (not accounting for frame time here)
    scales2.frameNStart = frameN;  // exact frame index
    scales2.setAutoDraw(true);
  }

  
  // *scales3* updates
  if (t >= 0.0 && scales3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scales3.tStart = t;  // (not accounting for frame time here)
    scales3.frameNStart = frameN;  // exact frame index
    scales3.setAutoDraw(true);
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
  Q5Components.push(scale_1);
  Q5Components.push(text_5);
  Q5Components.push(text_6);
  
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

  
  // *scale_1* updates
  if (t >= 0.0 && scale_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scale_1.tStart = t;  // (not accounting for frame time here)
    scale_1.frameNStart = frameN;  // exact frame index
    scale_1.setAutoDraw(true);
  }

  
  // *text_5* updates
  if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_5.tStart = t;  // (not accounting for frame time here)
    text_5.frameNStart = frameN;  // exact frame index
    text_5.setAutoDraw(true);
  }

  
  // *text_6* updates
  if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_6.tStart = t;  // (not accounting for frame time here)
    text_6.frameNStart = frameN;  // exact frame index
    text_6.setAutoDraw(true);
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
  // the Routine "Q5" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


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
  psychoJS.quit({message, isCompleted});

  return Scheduler.Event.QUIT;
}
