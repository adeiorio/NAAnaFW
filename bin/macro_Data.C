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

void macro_Data(TString lep)
{
  Float_t e1, e2, e3;
  Float_t newe1, newe2, newe3;
  TFile * f1 = TFile::Open("trees_lumi/"+lep+"/trees_Data_"+lep+".root","UPDATE");

  TTree * t1 = (TTree*)f1->Get("events_2j1t");
  TTree * t2 = (TTree*)f1->Get("events_3j1t");
  TTree * t3 = (TTree*)f1->Get("events_3j2t");

  t1->SetBranchAddress("etajprime", &e1); 
  t2->SetBranchAddress("etajprime", &e2); 
  t3->SetBranchAddress("etajprime", &e3); 

  TBranch * b1 = t1->Branch("etajprime_bin", &newe1,"etajprime_bin/F"); 
  TBranch * b2 = t2->Branch("etajprime_bin", &newe2,"etajprime_bin/F"); 
  TBranch * b3 = t3->Branch("etajprime_bin", &newe3,"etajprime_bin/F"); 

  Int_t nentries1 = (Int_t) t1->GetEntries();
  for (Int_t i = 0; i<nentries1; i++)
    {
      t1->GetEntry(i);
      newe1 = etajprimebinner(e1);
      b1->Fill();
    }
  Int_t nentries2 = (Int_t) t2->GetEntries();
  for (Int_t i = 0; i<nentries2; i++)
    {
      t2->GetEntry(i);
      newe2 = etajprimebinner(e2);
      b2->Fill();
    }
  Int_t nentries3 = (Int_t) t3->GetEntries();
  for (Int_t i = 0; i<nentries3; i++)
    {
      t3->GetEntry(i);
      newe3 = etajprimebinner(e3);
      b3->Fill();
    }
  f1->Write();
}
