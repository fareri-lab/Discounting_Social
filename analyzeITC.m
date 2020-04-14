% script to load in rej files and return discount parameters
% steps:  cd to subject directory, load file (dlmread), set variables, call
% ITC hyperbolic.m, write out file


% script to load in rej files and return discount parameters
% steps:  cd to subject directory, load file (dlmread), set variables, call
% ITC hyperbolic.m, write out file

clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'ITC_summary_testDF2020.csv');
fid_run = fopen(fname,'w');
fprintf(fid_run,'subnum,run,percentNow,percentDelayed,percentMissed,k,noise,LL,LL0,r2,percentPredicted\n');

sublist = [01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17];
%sublist = [01];
for s = 1:length(sublist)
    subj = sublist(s);
    runs = 2;
    tmp_data = zeros(runs,9);
    for r = 1:runs
        fname = fullfile(maindir,'logs','Rej',sprintf('%02d',subj),sprintf('sub-Rej_%02d_task-intertemporalchoice_run%d_raw.csv',subj,r-1));
        fid = fopen(fname,'r');
        C = textscan(fid,[repmat('%f',1,14) '%s' repmat('%f',1,9)],'Delimiter',',','HeaderLines',1,'EmptyValue', NaN);
        fclose(fid);
        
        choseDelayed = C{9};
        tmp = choseDelayed(:) == 1;
        choseDelayed(tmp) = 0;
        tmp = choseDelayed(:) == 2;
        choseDelayed(tmp) = 1;
        ImmedAmt = C{3};
        DelAmt = C{2};
        Delay = C{4};
        
        data = [choseDelayed ImmedAmt DelAmt Delay];
        [out] = ITChyperbolic(choseDelayed,ImmedAmt,DelAmt,Delay);
        
        tmp_data(r,:) = [out.percentNow,out.percentDelayed,out.percentMissed,out.k,out.noise,out.LL,out.LL0,out.r2,out.percentPredicted];
        fprintf(fid_run,'%d,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f\n',subj,r,tmp_data(r,:));
    end
end
%fclose(fid_subj);
fclose(fid_run);



%{
%import file
y = dlmread('sub-Rej_13_task-intertemporalchoice_run1_raw.csv',',',1,0)
y(:,9)
tmp = y(:,9)==1
y(tmp,9)=0
tmp = y(:,9)==2
y(tmp,9)=1
choseDelayed=y(:,9);
ImmedAmt=y(:,3)
DelAmt=y(:,2)
Delay = y(:,4)

y = dlmread('sub-Rej_13_task-intertemporalchoice_run1_raw.csv',',',1,0)
y(:,9)
tmp = y(:,9)==1
y(tmp,9)=0
tmp = y(:,9)==2
y(tmp,9)=1
choseDelayed=y(:,9);
ImmedAmt=y(:,3)
DelAmt=y(:,2)
Delay = y(:,4)
%}