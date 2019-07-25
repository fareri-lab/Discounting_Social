#clear workspace
rm(list=ls());

#set working directory
setwd('//Users/dfareri/Dropbox/Dominic/Adelphi_Teaching/EmergingScholars_2018_2019')

#WSLSdata<-read.table(file = 'Controls_allsubs_8_2017_formodeling_151_178excl.txt', header = TRUE, sep = '\t')

SLAGSRdata<-read.table(file = 'SLA_allsubs_GSR_updatedDF.csv', header = TRUE, sep = ',')

SLAGSRdata_DecisionOnly<-SLAGSRdata[SLAGSRdata$Phase==0]


subj = c("SLA001",
         "SLA002",
         "SLA003",
         "SLA004",
         "SLA005",
         "SLA006",
         "SLA007",
         "SLA008",
         "SLA009",
         "SLA010",
         "SLA011",
         "SLA012",
         "SLA013",
         "SLA014",
         "SLA015",
         "SLA016",
         "SLA017",
         "SLA019",
         "SLA020",
         "SLA021",
         "SLA022",
         "SLA023",
         "SLA024",
         "SLA025",
         "SLA026",
         "SLA027",
         "SLA028",
         "SLA029",
         "SLAFR001",
         "SLAFR002",
         "SLAFR003",
         "SLAFR004",
         "SLAFR005",
         "SLAFR006",
         "SLAFR007",
         "SLAFR008",
         "SLAFR009",
         "SLAFR010",
         "SLAFR011",
         "SLAFR012",
         "SLAFR013",
         "SLAFR014",
         "SLAFR016",
         "SLAFR018",
         "SLAFR019",
         "SLAFR020",
         "SLAFR021",
         "SLAFR022",
         "SLAFR023",
         "SLAFR024",
         "SLAFR025",
         "SLAFR026",
         );

nsubj=length(subj)
trial=(1:30)
ntrial=length(trial)
run=(0:8)
nrun=length(run)


#WSLSdata_wide<-data.frame(matrix(NA,nrow=55,ncol=16))
#names(WSLSdata_wide)<-c("Subject","Age","Sex","AgeGrp","SummaryWS_Overall","SummaryLS_Overall","SummaryWS_Approach","SummaryWS_Avoid","SummaryLS_Approach","SummaryLS_Avoid","WSLSDiff_Overall","WSLSDiff_Approach","WSLSDiff_Avoid","Acc_Approach","Acc_Avoid","Accuracy_Overall")
#WSLSdata_wide$Subject<-unique(WSLSdata$Subject)

ITCdiff=data.frame(matrix(NA,nrow=14,ncol=2))
names(ITCdiff)<-c("percentNow","k")

subj=c("1",
       "2",
       "3",
       "4",
       "5",
       "6",
       "7",
       "8",
       "9",
       "10",
       "11",
       "12",
       "13",
       "14");


nsubj=14

for(i in 1:nsubj){
  ITCdiff$percentNow[i]<-ITCdata$percentNow[ITCdata$subnum==subj[i] & ITCdata$run==2] - ITCdata$percentNow[ITCdata$subnum==subj[i] & ITCdata$run==1]
  ITCdiff$k[i]<-ITCdata$k[ITCdata$subnum==subj[i] & ITCdata$run==2] - ITCdata$k[ITCdata$subnum==subj[i] & ITCdata$run==1]
}



for(i in 1:nsubj){
  for (r in 1:nrun){
    for(t in 1:ntrial){
      #meanWS<-mean(WSLSdata$WS[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]],na.rm = TRUE) 
      #meanLS<-mean(WSLSdata$LS[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]],na.rm = TRUE)
      #WSLSdata$SummaryWS[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-meanWS
      #WSLSdata$SummaryLS[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-meanLS  
      #WSLSdata$WSLSDiff[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-(meanWS-meanLS)
      #meanAcc<-mean(WSLSdata$IsCorrectResp[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]],na.rm = TRUE)
      #WSLSdata$meanAcc[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-meanAcc
      #AmountPosFB<-sum(WSLSdata$Outcome_modelNAs[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]],na.rm = TRUE)
      #WSLSdata$AmountPosFB[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-AmountPosFB
      #AmountNegFB<-length(which(WSLSdata$Outcome_modelNAs[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]==0))
      #WSLSdata$AmountNegFB[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-AmountNegFB
      WSLSdata$PosNegDiff[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]]<-(WSLSdata$AmountPosFB[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]] - WSLSdata$AmountNegFB[WSLSdata$Subject==subj[i] & WSLSdata$Run==run[r]])
    }
  }
}






for(i in 1:nsubj){
  #ages<-unique(WSLSdata$Age[WSLSdata$Subject==subj[i]])
  #WSLSdata_wide$Age[WSLSdata_wide$Subject==subj[i]]<-ages
  
  #sex<-unique(WSLSdata$Sex[WSLSdata$Subject==subj[i]])
  #WSLSdata_wide$Sex[WSLSdata_wide$Subject==subj[i]]<-sex
  
  #ageGrp<-unique(WSLSdata$AgeGrp[WSLSdata$Subject==subj[i]])
  #WSLSdata_wide$AgeGrp[WSLSdata_wide$Subject==subj[i]]<-ageGrp
  
  #WSoverall<-mean(WSLSdata$WS[WSLSdata$Subject==subj[i]],na.rm=TRUE)
  #WSLSdata_wide$SummaryWS_Overall[WSLSdata_wide$Subject==subj[i]]<-WSoverall
  
  #LSoverall<-mean(WSLSdata$SummaryLS[WSLSdata$Subject==subj[i]])
  #WSLSdata_wide$SummaryLS_Overall[WSLSdata_wide$Subject==subj[i]]<-LSoverall
  
  #WSapp<-unique(WSLSdata$SummaryWS[WSLSdata$Subject==subj[i] & WSLSdata$Run==1])
  #WSLSdata_wide$SummaryWS_Approach[WSLSdata_wide$Subject==subj[i]]<-WSapp}
  
  
  write.table(WSLSdata_wide,file="WSLSdata_wide_forSPSS_updated_10.16.18",row.names=FALSE,col.names=TRUE)
  