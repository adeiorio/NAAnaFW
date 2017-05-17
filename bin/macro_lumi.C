#include <iostream>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TString.h"

using namespace std;
void macro_lumi(TString channel, double lumi, double sigma)
{

  Float_t w_nominal1, w_nominal2, w_nominal3;
  TFile *f1_uncut= TFile::Open("res/"+channel+"_muon.root");
  TFile *f1 = TFile::Open("trees/trees_"+channel+"_muon.root");
  TTree *t1 =(TTree*)f1->Get("events_2j1t");
  t1->SetBranchAddress("w_nominal", &w_nominal1); 
  TFile *f1_new = TFile::Open("trees_lumi/trees_"+channel+"_muon.root","RECREATE");  
  h1_uncut =(TH1F*)f1_uncut->Get("h_cutFlow");
  Double_t n_uncut = h1_uncut->GetBinContent(0);
  TTree *t1_new =t1->CloneTree(0); 
  Int_t nentries1 = (Int_t) t1->GetEntries();
  for (Int_t i = 0; i<=nentries1; i++)
    {
      t1->GetEntry(i);
      w_nominal1*=(lumi*sigma*1000/n_uncut);
      t1_new->Fill();
    }

  TTree *t2 =(TTree*)f1->Get("events_3j2t");
  t2->SetBranchAddress("w_nominal", &w_nominal2); 
  TTree *t2_new = t2->CloneTree(0); 
  Int_t nentries2 = (Int_t) t2->GetEntries();
  for (Int_t i = 0; i<=nentries2; i++)
    {
      t2->GetEntry(i);
      w_nominal2*=(lumi*sigma*1000/n_uncut);
      t2_new->Fill();
    }

  TTree *t3 =(TTree*)f1->Get("events_3j1t");
  t3->SetBranchAddress("w_nominal", &w_nominal3); 
  TTree *t3_new = t3->CloneTree(0); 
  Int_t nentries3 = (Int_t) t2->GetEntries();
  for (Int_t i = 0; i<=nentries3; i++)
    {
      t3->GetEntry(i);
      w_nominal3*=(lumi*sigma*1000/n_uncut);
      t3_new->Fill();
    }
  f1_new->Write();
}
