function [parameters] = setupdiscanalysis(xlsfilename, numbersubs)
%3.15.18 Karolina Lempert
%Function that takes an Excel file with choice data from multiple subjects,
%and returns hyperbolic discount rate parameters for each subject (the specific parameters returned
%are described below). 
%Numbersubs is a scalar indicating how many subjects are in the Excel file.
%Excel file should take this form:
%first row is headers; sheet is named "Sheet1" (though this can be altered
%n the code below.)
%Column 1: Subject number
%Column 2: Amount14.RESP (either 'f' or 'j', indicates choice for that
%EPrime object)
%Column 3: Amount6.RESP	(either 'f' or 'j', indicates choice for that
%EPrime object)
%Column 4: AmtL immediate reward amount
%Column 5: AmtR delayed reward amount
%Column 6: DelR	delayed reward delay (# of days); Note for now this script
%only works when the smaller/sooner delay is 0 days.
%Column 7: LeftRight, variable with a 1 or 0, indicating whether Amount14
%or Amount6 was seen on that trial.

%read in numbers and strings separately from the Excel sheet
[subject,strings] = xlsread([xlsfilename],'Sheet1');
%delete first row of "strings" so as to align it with the numbers matrix.
strings(1,:) = [];
%this goes through and converts the "f"'s and "j"s to 1s and 0s, so that we
%can have all variables in the same matrix, "subject." Note (4/16/18): if you already
%have data in 1 and 0 form, you can edit out this part.
for j = 1:length(strings)
    if strings{j,2} == 'f', 
        subject(j,2) = 1;
    elseif strings{j,2} == 'j'
        subject(j,2) = 0;
    end
    if strings{j,3} == 'f', 
        subject(j,3) = 1;
    elseif strings{j,3} == 'j'
        subject(j,3) = 0;
    end
end
%this next loop makes a new column in "Subject" that indicates the choice
%on that trial (0 = chose immediate; 1 = chose delayed), based on the
%LeftRight variable and the choice of left or right on that trial.
for i = 1:length(subject)
   if subject(i,7) == 1 && subject(i,3) == 1
       subject(i,8) = 0;
   elseif subject(i,7) == 1 && subject(i,3) == 0
       subject(i,8) = 1;
   end

   if subject(i,7) == 0 && subject(i,2) == 1
       subject(i,8) = 1;
   elseif subject(i,7) == 0 && subject(i,2) == 0
       subject(i,8) = 0;
   end
end
%indicates number of choices, which is 51 for this task. Careful if you
%delete any choices, since the next part depends on each subject having the same number of
%choices.
numberchoices = 51;

%gets parameters for the first subject by running the ITCHyperbolic script.

for j = 1:1
choseDelayed = subject(1:numberchoices,8);
ImmedAmt = subject(1:numberchoices,4);
DelAmt = subject(1:numberchoices,5);
Delay = subject(1:numberchoices,6);
[out] = ITChyperbolic(choseDelayed,ImmedAmt,DelAmt,Delay);

parameters(j,1) = subject(1,1);
%subject number in first column
parameters(j,2) = out.k;
%discount rate k in second column
parameters(j,3) = out.percentDelayed;
%percent of choices that were for delayed reward in 3rd column
parameters(j,4) = out.noise;
%noise parameter in 4th column. Not often used but it is another fit
%parameter of the model and tells you about how consistent subjects were
parameters(j,5) = out.LL;
%log-likelihood of model fit (in case you want to compare to other models)
end

%gets parameters for remaining subjects by running the ITCHyperbolic
%script. (There is probably a more elegant way to do this...)
for j = 2:numbersubs
choseDelayed = subject((((j-1)*numberchoices)+1):(((j-1)*numberchoices)+numberchoices),8);
ImmedAmt = subject((((j-1)*numberchoices)+1):(((j-1)*numberchoices)+numberchoices),4);
DelAmt = subject((((j-1)*numberchoices)+1):(((j-1)*numberchoices)+numberchoices),5);
Delay = subject((((j-1)*numberchoices)+1):(((j-1)*numberchoices)+numberchoices),6);
[out] = ITChyperbolic(choseDelayed,ImmedAmt,DelAmt,Delay);
parameters(j,1) = subject(((j-1)*numberchoices+1),1);
parameters(j,2) = out.k;
parameters(j,3) = out.percentDelayed;
parameters(j,4) = out.noise;
parameters(j,5) = out.LL;
end
end