#include <iostream>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TString.h"

using namespace std;

void test(TString channel, TString lep){
  Int_t halfevents_2j1t = 0, halfevents_b_2j1t = 0;
  Int_t halfevents_3j1t = 0, halfevents_b_3j1t = 0;
  Int_t halfevents_3j2t = 0, halfevents_b_3j2t = 0;
  if(channel.EqualTo("TT")){
    halfevents_b_2j1t = 20000;
    halfevents_b_3j1t = 20000;
    halfevents_b_3j2t = 20000;
  }else if(channel.EqualTo("ST_tch")){
    halfevents_b_2j1t = 20000;
    halfevents_b_3j1t = 15000;
    halfevents_b_3j2t = 10000;
  }else if(channel.EqualTo("ST_tch_p_sd")){
    halfevents_b_2j1t = 15000;
    halfevents_b_3j1t = 2500;
    halfevents_b_3j2t = 0;
  }else if(channel.EqualTo("ST_tch_sd")){
    halfevents_b_2j1t = 3000;
    halfevents_b_3j1t = 2000;
    halfevents_b_3j2t = 0;
    /*  }else if(channel.EqualTo("WToLNu2J")){
    halfevents_b_2j1t = 10000;
    halfevents_b_3j1t = 4000;
    halfevents_b_3j2t = 0;*/
  }else{
    return;
  }

  Float_t w1, w2, w3;
  TFile *f1 = TFile::Open("trees_lumi/trees_"+channel+"_"+lep+".root");

  TTree *t1 = (TTree*)f1->Get("events_2j1t");
  TTree *t1_jesU = (TTree*)f1->Get("events_2j1t_jesUp");
  TTree *t1_jesD = (TTree*)f1->Get("events_2j1t_jesDown");
  TTree *t1_jerU = (TTree*)f1->Get("events_2j1t_jerUp");
  TTree *t1_jerD = (TTree*)f1->Get("events_2j1t_jerDown");
  TTree *t2 = (TTree*)f1->Get("events_3j1t");
  TTree *t2_jesU = (TTree*)f1->Get("events_3j1t_jesUp");
  TTree *t2_jesD = (TTree*)f1->Get("events_3j1t_jesDown");
  TTree *t2_jerU = (TTree*)f1->Get("events_3j1t_jerUp");
  TTree *t2_jerD = (TTree*)f1->Get("events_3j1t_jerDown");
  TTree *t3 = (TTree*)f1->Get("events_3j2t");
  TTree *t3_jesU = (TTree*)f1->Get("events_3j2t_jesUp");
  TTree *t3_jesD = (TTree*)f1->Get("events_3j2t_jesDown");
  TTree *t3_jerU = (TTree*)f1->Get("events_3j2t_jerUp");
  TTree *t3_jerD = (TTree*)f1->Get("events_3j2t_jerDown");

  t1->SetBranchAddress("w", &w1); 
  t2->SetBranchAddress("w", &w2); 
  t3->SetBranchAddress("w", &w3); 

  TFile *f1_new = TFile::Open("trees_lumi/"+lep+"/trees_"+channel+"_"+lep+".root","RECREATE");  
  TTree *t1_new = t1->CloneTree(0); 
  TTree *t1_jesU_new = t1_jesU->CloneTree(); 
  TTree *t1_jesD_new = t1_jesD->CloneTree(); 
  TTree *t1_jerU_new = t1_jerU->CloneTree(); 
  TTree *t1_jerD_new = t1_jerD->CloneTree(); 
  TTree *t2_new = t2->CloneTree(0); 
  TTree *t2_jesU_new = t2_jesU->CloneTree(); 
  TTree *t2_jesD_new = t2_jesD->CloneTree(); 
  TTree *t2_jerU_new = t2_jerU->CloneTree(); 
  TTree *t2_jerD_new = t2_jerD->CloneTree(); 
  TTree *t3_new = t3->CloneTree(0); 
  TTree *t3_jesU_new = t3_jesU->CloneTree(); 
  TTree *t3_jesD_new = t3_jesD->CloneTree(); 
  TTree *t3_jerU_new = t3_jerU->CloneTree(); 
  TTree *t3_jerD_new = t3_jerD->CloneTree(); 
  
  Int_t nentries1 = (Int_t) t1->GetEntries();
  Int_t nentries2 = (Int_t) t2->GetEntries();
  Int_t nentries3 = (Int_t) t3->GetEntries();
  
  halfevents_2j1t = halfevents_b_2j1t;
  if(2*halfevents_2j1t>nentries1){
    halfevents_2j1t=0;
  }
  for (Int_t i = halfevents_2j1t; i<(nentries1-halfevents_2j1t); i++)
    {
      t1->GetEntry(i);
      w1*=(float)nentries1/((float)nentries1-((float)2*halfevents_2j1t));
      t1_new->Fill();
    }
  //    cout <<    (float)nentries1/((float)nentries1-((float)2*halfevents_2j1t)) <<endl;
  halfevents_3j1t = halfevents_b_3j1t;
  if(2*halfevents_3j1t>nentries2){
    halfevents_3j1t=0;
  }
  for (Int_t i = halfevents_3j1t; i<(nentries2-halfevents_3j1t); i++)
    {
      t2->GetEntry(i);
      w2*=(float)nentries2/((float)nentries2-((float)2*halfevents_3j1t));
      t2_new->Fill();
    }
  
  halfevents_3j2t = halfevents_b_3j2t;
  if(2*halfevents_3j2t>nentries3){
    halfevents_3j2t=0;
    }
  for (Int_t i = halfevents_3j2t; i<(nentries3-halfevents_3j2t); i++)
    {
      t3->GetEntry(i);
      w3*=(float)nentries3/((float)nentries3-((float)2*halfevents_3j2t));
      t3_new->Fill();
    }
  f1_new->Write();
  f1_new->Close();
}

void train(TString channel, TString lep){
  Int_t halfevents_2j1t = 0, halfevents_b_2j1t = 0;
  Int_t halfevents_3j1t = 0, halfevents_b_3j1t = 0;
  Int_t halfevents_3j2t = 0, halfevents_b_3j2t = 0;
  if(channel.EqualTo("TT")){
    halfevents_b_2j1t = 20000;
    halfevents_b_3j1t = 20000;
    halfevents_b_3j2t = 20000;
  }else if(channel.EqualTo("ST_tch")){
    halfevents_b_2j1t = 20000;
    halfevents_b_3j1t = 15000;
    halfevents_b_3j2t = 10000;
  }else if(channel.EqualTo("ST_tch_p_sd")){
    halfevents_b_2j1t = 15000;
    halfevents_b_3j1t = 2500;
    halfevents_b_3j2t = 0;
  }else if(channel.EqualTo("ST_tch_sd")){
    halfevents_b_2j1t = 3000;
    halfevents_b_3j1t = 2000;
    halfevents_b_3j2t = 0;
    /*  }else if(channel.EqualTo("WToLNu2J")){
    halfevents_b_2j1t = 10000;
    halfevents_b_3j1t = 4000;
    halfevents_b_3j2t = 0;*/
  }else{
    return;
  }

  Float_t w1, w2, w3;
  TFile *f1 = TFile::Open("trees_lumi/trees_"+channel+"_"+lep+".root");

  TTree *t1 = (TTree*)f1->Get("events_2j1t");
  TTree *t1_jesU = (TTree*)f1->Get("events_2j1t_jesUp");
  TTree *t1_jesD = (TTree*)f1->Get("events_2j1t_jesDown");
  TTree *t1_jerU = (TTree*)f1->Get("events_2j1t_jerUp");
  TTree *t1_jerD = (TTree*)f1->Get("events_2j1t_jerDown");
  TTree *t2 = (TTree*)f1->Get("events_3j1t");
  TTree *t2_jesU = (TTree*)f1->Get("events_3j1t_jesUp");
  TTree *t2_jesD = (TTree*)f1->Get("events_3j1t_jesDown");
  TTree *t2_jerU = (TTree*)f1->Get("events_3j1t_jerUp");
  TTree *t2_jerD = (TTree*)f1->Get("events_3j1t_jerDown");
  TTree *t3 = (TTree*)f1->Get("events_3j2t");
  TTree *t3_jesU = (TTree*)f1->Get("events_3j2t_jesUp");
  TTree *t3_jesD = (TTree*)f1->Get("events_3j2t_jesDown");
  TTree *t3_jerU = (TTree*)f1->Get("events_3j2t_jerUp");
  TTree *t3_jerD = (TTree*)f1->Get("events_3j2t_jerDown");

  t1->SetBranchAddress("w", &w1); 
  t2->SetBranchAddress("w", &w2); 
  t3->SetBranchAddress("w", &w3); 

  TFile *f1_train = TFile::Open("trees_lumi/train/trees_"+channel+"_"+lep+"_train.root","RECREATE");  
  TTree *t1_train = t1->CloneTree(0); 
  TTree *t2_train = t2->CloneTree(0); 
  TTree *t3_train = t3->CloneTree(0); 
    
  Int_t nentries1 = (Int_t) t1->GetEntries();
  Int_t nentries2 = (Int_t) t2->GetEntries();
  Int_t nentries3 = (Int_t) t3->GetEntries();
  
  halfevents_2j1t = halfevents_b_2j1t;
  if(2*halfevents_2j1t>nentries1){
    halfevents=0;
  }
  for (Int_t i = 0; i<halfevents_2j1t; i++)
    {
      t1->GetEntry(i);
      w1*=(float)nentries1/((float)2*halfevents_2j1t);
      t1_train->Fill();
    }
  for (Int_t i = nentries1-halfevents_2j1t; i<nentries1; i++)
    {
      t1->GetEntry(i);
      w1*=(float)nentries1/((float)2*halfevents_2j1t);
      t1_train->Fill();
    }
  halfevents_3j1t = halfevents_b_3j1t;
  if(2*halfevents_3j1t>nentries2){
    halfevents=0;
  }
  for (Int_t i = 0; i<halfevents_3j1t; i++)
    {
      t2->GetEntry(i);
      w2*=(float)nentries2/((float)2*halfevents_3j1t);
      t2_train->Fill();
    }
  for (Int_t i = nentries2-halfevents_3j1t; i<nentries2; i++)
    {
      t2->GetEntry(i);
      w2*=(float)nentries2/((float)2*halfevents_3j1t);
      t2_train->Fill();
    }
  halfevents_3j2t = halfevents_b_3j2t;
  if(2*halfevents_3j2t>nentries3){
    halfevents_3j2t=0;
  }
  for (Int_t i = 0; i<halfevents_3j2t; i++)
    {
      t3->GetEntry(i);
      w3*=(float)nentries3/((float)2*halfevents_3j2t);
      t3_train->Fill();
    }
  for (Int_t i = nentries3-halfevents_3j2t; i<nentries3; i++)
    {
      t3->GetEntry(i);
      w3*=(float)nentries3/((float)2*halfevents_3j2t);
      t3_train->Fill();
    }
  f1_train->Write();
  f1_train->Close();
}


void trees_splitter(TString channel, TString lep, TString phase){
  if(phase =="test")    test(channel, lep);
  if(phase=="train")    train(channel, lep);
}
