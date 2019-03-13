#include <iostream>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TString.h"

using namespace std;

float etajprimebinner(float etajprime){
  float newetajprime;
  if(etajprime>= 0.0 && etajprime<0.2)newetajprime=0.1;
  else if(etajprime>= 0.2 && etajprime<0.4)newetajprime=0.3;
  else if(etajprime>= 0.4 && etajprime<0.6)newetajprime=0.5;
  else if(etajprime>= 0.6 && etajprime<0.8)newetajprime=0.7;
  else if(etajprime>= 0.8 && etajprime<1.0)newetajprime=0.9;
  else if(etajprime>= 1.0 && etajprime<1.2)newetajprime=1.1;
  else if(etajprime>= 1.2 && etajprime<1.4)newetajprime=1.3;
  else if(etajprime>= 1.4 && etajprime<1.6)newetajprime=1.5;
  else if(etajprime>= 1.6 && etajprime<1.8)newetajprime=1.7;
  else if(etajprime>= 1.8 && etajprime<2.0)newetajprime=1.9;
  else if(etajprime>= 2.0 && etajprime<2.2)newetajprime=2.1;
  else if(etajprime>= 2.2 && etajprime<2.4)newetajprime=2.3;
  else if(etajprime>= 2.4 && etajprime<2.6)newetajprime=2.5;
  else if(etajprime>= 2.6 && etajprime<2.8)newetajprime=2.7;
  else if(etajprime>= 2.8 && etajprime<3.0)newetajprime=2.9;
  else if(etajprime>= 3.0 && etajprime<3.5)newetajprime=3.25;
  else if(etajprime>= 3.5 && etajprime<4.0)newetajprime=3.75;
  else if(etajprime>= 4.0 && etajprime<4.4)newetajprime=4.2;
  else if(etajprime>= 4.4 && etajprime<5.0)newetajprime=4.7;
  else if(etajprime>= 5.0 && etajprime<5.4)newetajprime=5.2;
  return newetajprime;
}

void macro_lumi(TString channel, double lumi, double sigma, TString lep)
{
  if((lep=="electron"||lep=="electronantiiso")&& channel=="QCDMuPt20toInf") return;
  if((lep=="muonantiiso"||lep=="electronantiiso")&& channel=="TT_sd") return;
  //  if((lep=="muonantiiso"||lep=="electronantiiso")&& (channel.Contains("hdamp")||channel.Contains("psq2"))) return;
  Float_t w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15;
  Float_t e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15;
  Float_t newe1, newe2, newe3, newe4, newe5, newe6, newe7, newe8, newe9, newe10, newe11, newe12, newe13, newe14, newe15;
  Float_t q2TUp1, q2TDown1, q2TbarUp1, q2TbarDown1, q2TUp6, q2TDown6, q2TbarUp6, q2TbarDown6, q2TUp11, q2TDown11, q2TbarUp11, q2TbarDown11;
  TFile * f1_uncut= TFile::Open("res/"+lep+"/"+channel+"_"+lep+".root");
  h1_uncut =(TH1F*)f1_uncut->Get("h_cutFlow");
  Float_t n_uncut = h1_uncut->GetBinContent(0);
  TFile * f1 = TFile::Open("trees/"+lep+"/trees_"+channel+"_"+lep+".root");
  //  h1_uncut =(TH1F*)f1->Get("h_cutFlow");
  //  Float_t n_uncut = h1_uncut->GetBinContent(0);

  TTree * t1 = (TTree*)f1->Get("events_2j1t");
  TTree * t2 = (TTree*)f1->Get("events_2j1t_jesUp");
  TTree * t3 = (TTree*)f1->Get("events_2j1t_jesDown");
  TTree * t4 = (TTree*)f1->Get("events_2j1t_jerUp");
  TTree * t5 = (TTree*)f1->Get("events_2j1t_jerDown");
  TTree * t6 = (TTree*)f1->Get("events_3j1t");
  TTree * t7 = (TTree*)f1->Get("events_3j1t_jesUp");
  TTree * t8 = (TTree*)f1->Get("events_3j1t_jesDown");
  TTree * t9 = (TTree*)f1->Get("events_3j1t_jerUp");
  TTree * t10 = (TTree*)f1->Get("events_3j1t_jerDown");
  TTree * t11 = (TTree*)f1->Get("events_3j2t");
  TTree * t12 = (TTree*)f1->Get("events_3j2t_jesUp");
  TTree * t13 = (TTree*)f1->Get("events_3j2t_jesDown");
  TTree * t14 = (TTree*)f1->Get("events_3j2t_jerUp");
  TTree * t15 = (TTree*)f1->Get("events_3j2t_jerDown");

  t1->SetBranchAddress("w", &w1); 
  t2->SetBranchAddress("w", &w2); 
  t3->SetBranchAddress("w", &w3); 
  t4->SetBranchAddress("w", &w4); 
  t5->SetBranchAddress("w", &w5); 
  t6->SetBranchAddress("w", &w6); 
  t7->SetBranchAddress("w", &w7); 
  t8->SetBranchAddress("w", &w8); 
  t9->SetBranchAddress("w", &w9); 
  t10->SetBranchAddress("w", &w10); 
  t11->SetBranchAddress("w", &w11); 
  t12->SetBranchAddress("w", &w12); 
  t13->SetBranchAddress("w", &w13); 
  t14->SetBranchAddress("w", &w14); 
  t15->SetBranchAddress("w", &w15); 

  t1->SetBranchAddress("etajprime", &e1); 
  t2->SetBranchAddress("etajprime", &e2); 
  t3->SetBranchAddress("etajprime", &e3); 
  t4->SetBranchAddress("etajprime", &e4); 
  t5->SetBranchAddress("etajprime", &e5); 
  t6->SetBranchAddress("etajprime", &e6); 
  t7->SetBranchAddress("etajprime", &e7); 
  t8->SetBranchAddress("etajprime", &e8); 
  t9->SetBranchAddress("etajprime", &e9); 
  t10->SetBranchAddress("etajprime", &e10); 
  t11->SetBranchAddress("etajprime", &e11); 
  t12->SetBranchAddress("etajprime", &e12); 
  t13->SetBranchAddress("etajprime", &e13); 
  t14->SetBranchAddress("etajprime", &e14); 
  t15->SetBranchAddress("etajprime", &e15); 

  t1->Branch("etajprime_bin", &newe1,"etajprime_bin/F"); 
  t2->Branch("etajprime_bin", &newe2,"etajprime_bin/F"); 
  t3->Branch("etajprime_bin", &newe3,"etajprime_bin/F"); 
  t4->Branch("etajprime_bin", &newe4,"etajprime_bin/F"); 
  t5->Branch("etajprime_bin", &newe5,"etajprime_bin/F"); 
  t6->Branch("etajprime_bin", &newe6,"etajprime_bin/F"); 
  t7->Branch("etajprime_bin", &newe7,"etajprime_bin/F"); 
  t8->Branch("etajprime_bin", &newe8,"etajprime_bin/F"); 
  t9->Branch("etajprime_bin", &newe9,"etajprime_bin/F"); 
  t10->Branch("etajprime_bin", &newe10,"etajprime_bin/F"); 
  t11->Branch("etajprime_bin", &newe11,"etajprime_bin/F"); 
  t12->Branch("etajprime_bin", &newe12,"etajprime_bin/F"); 
  t13->Branch("etajprime_bin", &newe13,"etajprime_bin/F"); 
  t14->Branch("etajprime_bin", &newe14,"etajprime_bin/F"); 
  t15->Branch("etajprime_bin", &newe15,"etajprime_bin/F"); 

  if(channel == "ST_T_tch"){
    t1->SetBranchAddress("q2Up", &q2TUp1); 
    t1->SetBranchAddress("q2Down", &q2TDown1); 
    t6->SetBranchAddress("q2Up", &q2TUp6); 
    t6->SetBranchAddress("q2Down", &q2TDown6); 
    t11->SetBranchAddress("q2Up", &q2TUp11); 
    t11->SetBranchAddress("q2Down", &q2TDown11); 
  }else if(channel == "ST_Tbar_tch"){
    t1->SetBranchAddress("q2Up", &q2TbarUp1); 
    t1->SetBranchAddress("q2Down", &q2TbarDown1); 
    t6->SetBranchAddress("q2Up", &q2TbarUp6); 
    t6->SetBranchAddress("q2Down", &q2TbarDown6); 
    t11->SetBranchAddress("q2Up", &q2TbarUp11); 
    t11->SetBranchAddress("q2Down", &q2TbarDown11); 
  }
  TFile *f1_new = TFile::Open("trees_lumi/"+lep+"/trees_"+channel+"_"+lep+".root","RECREATE");  

  TTree *t1_new = t1->CloneTree(0); 
  TTree *t2_new = t2->CloneTree(0); 
  TTree *t3_new = t3->CloneTree(0); 
  TTree *t4_new = t4->CloneTree(0); 
  TTree *t5_new = t5->CloneTree(0); 
  TTree *t6_new = t6->CloneTree(0); 
  TTree *t7_new = t7->CloneTree(0); 
  TTree *t8_new = t8->CloneTree(0); 
  TTree *t9_new = t9->CloneTree(0); 
  TTree *t10_new = t10->CloneTree(0); 
  TTree *t11_new = t11->CloneTree(0); 
  TTree *t12_new = t12->CloneTree(0); 
  TTree *t13_new = t13->CloneTree(0); 
  TTree *t14_new = t14->CloneTree(0); 
  TTree *t15_new = t15->CloneTree(0); 

  Int_t nentries1 = (Int_t) t1->GetEntries();
  for (Int_t i = 0; i<nentries1; i++)
    {
      t1->GetEntry(i);
      w1 *= (lumi*sigma*1000/n_uncut);
      newe1 = etajprimebinner(e1);
      if(channel == "ST_T_tch"){
	q2TUp1 *= 1.05324;
	q2TDown1 *= 0.933123;
      }else if(channel == "ST_Tbar_tch"){
	q2TbarUp1 *= 1.06297;
	q2TbarDown1 *= 0.936937;
      }
      t1_new->Fill();
    }
  Int_t nentries6 = (Int_t) t6->GetEntries();
  for (Int_t i = 0; i<nentries6; i++)
    {
      t6->GetEntry(i);
      w6*=(lumi*sigma*1000/n_uncut);
      newe6 = etajprimebinner(e6);
      if(channel == "ST_T_tch"){
	q2TUp6 *= 1.05324;
	q2TDown6 *= 0.933123;
      }else if(channel == "ST_Tbar_tch"){
	q2TbarUp6 *= 1.06297;
	q2TbarDown6 *= 0.936937;
      }
      t6_new->Fill();
    }
  Int_t nentries11 = (Int_t) t11->GetEntries();
  for (Int_t i = 0; i<nentries11; i++)
    {
      t11->GetEntry(i);
      w11*=(lumi*sigma*1000/n_uncut);
      newe11 = etajprimebinner(e11);
      if(channel == "ST_T_tch"){
	q2TUp11 *= 1.05324;
	q2TDown11 *= 0.933123;
      }else if(channel == "ST_Tbar_tch"){
	q2TbarUp11 *= 1.06297;
	q2TbarDown11 *= 0.936937;
      }    
      t11_new->Fill();
    }
  if(!(channel.Contains("hdamp")||channel.Contains("psq2"))){
    Int_t nentries2 = (Int_t) t2->GetEntries();
    for (Int_t i = 0; i<nentries2; i++)
      {
	t2->GetEntry(i);
	w2*=(lumi*sigma*1000/n_uncut);
	newe2 = etajprimebinner(e2);
	t2_new->Fill();
      }
    Int_t nentries3 = (Int_t) t3->GetEntries();
    for (Int_t i = 0; i<nentries3; i++)
      {
	t3->GetEntry(i);
	w3*=(lumi*sigma*1000/n_uncut);
	newe3 = etajprimebinner(e3);
	t3_new->Fill();
      }
    Int_t nentries4 = (Int_t) t4->GetEntries();
    for (Int_t i = 0; i<nentries4; i++)
      {
	t4->GetEntry(i);
	w4*=(lumi*sigma*1000/n_uncut);
	newe4 = etajprimebinner(e4);
	t4_new->Fill();
      }
    Int_t nentries5 = (Int_t) t5->GetEntries();
    for (Int_t i = 0; i<nentries5; i++)
      {
	t5->GetEntry(i);
	w5*=(lumi*sigma*1000/n_uncut);
	newe5 = etajprimebinner(e5);
	t5_new->Fill();
      }
    Int_t nentries7 = (Int_t) t7->GetEntries();
    for (Int_t i = 0; i<nentries7; i++)
      {
	t7->GetEntry(i);
	w7*=(lumi*sigma*1000/n_uncut);
	newe7 = etajprimebinner(e7);
	t7_new->Fill();
      }
    Int_t nentries8 = (Int_t) t8->GetEntries();
    for (Int_t i = 0; i<nentries8; i++)
      {
	t8->GetEntry(i);
	w8*=(lumi*sigma*1000/n_uncut);
	newe8 = etajprimebinner(e8);
	t8_new->Fill();
      }
    Int_t nentries9 = (Int_t) t9->GetEntries();
    for (Int_t i = 0; i<nentries9; i++)
      {
	t9->GetEntry(i);
	w9*=(lumi*sigma*1000/n_uncut);
	newe9 = etajprimebinner(e9);
	t9_new->Fill();
      }
    Int_t nentries10 = (Int_t) t10->GetEntries();
    for (Int_t i = 0; i<nentries10; i++)
      {
	t10->GetEntry(i);
	w10*=(lumi*sigma*1000/n_uncut);
	newe10 = etajprimebinner(e10);
	t10_new->Fill();
      }
    Int_t nentries12 = (Int_t) t12->GetEntries();
    for (Int_t i = 0; i<nentries12; i++)
      {
	t12->GetEntry(i);
	w12*=(lumi*sigma*1000/n_uncut);
	newe12 = etajprimebinner(e12);
	t12_new->Fill();
      }
    Int_t nentries13 = (Int_t) t13->GetEntries();
    for (Int_t i = 0; i<nentries13; i++)
      {
	t13->GetEntry(i);
	w13*=(lumi*sigma*1000/n_uncut);
	newe13 = etajprimebinner(e13);
	t13_new->Fill();
      }
    Int_t nentries14 = (Int_t) t14->GetEntries();
    for (Int_t i = 0; i<nentries14; i++)
      {
	t14->GetEntry(i);
	w14*=(lumi*sigma*1000/n_uncut);
	newe14 = etajprimebinner(e14);
	t14_new->Fill();
      }
    Int_t nentries15 = (Int_t) t15->GetEntries();
    for (Int_t i = 0; i<nentries15; i++)
      {
	t15->GetEntry(i);
	w15*=(lumi*sigma*1000/n_uncut);
	newe15 = etajprimebinner(e15);
	t15_new->Fill();
      }
  }
  f1_new->Write();
}
