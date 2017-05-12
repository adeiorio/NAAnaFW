#include <iostream>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TString.h"

using namespace std;
void macro_plot(TString channel, TString variabile, TString peso, int nbins, int xmin, int xmax, double sigma, double lumi, TString njmt, TString syst) {

  TH1F *h1_uncut= new TH1F;
  TFile *f1_uncut= TFile::Open("res/"+channel+"_muon.root");
  TFile *f1= TFile::Open("trees/trees_"+channel+"_muon.root");
  TString histoname = "h"+njmt+"_"+variabile;
  TH1F *h1= new TH1F(histoname, variabile+"_"+channel, nbins, xmin, xmax);
  TString treename = "events"+njmt;
  TString taglio, foutput;
  //cout << treename << endl;
  //cout << "nome file input " << "treesSmall/trees_" <<channel <<"_muon.root" <<endl;
  if(syst.EqualTo(""))
    {  
      taglio ="w_nominal*"+peso;
      foutput = "Plot/"+channel+"_muon.root";
    }
  else
    {
      taglio = syst+"*"+peso;
      foutput = "Plot/"+channel+"_muon_"+syst+".root"; 
    }
  //cout << taglio << endl;
  ((TTree*)f1->Get(treename))->Project(histoname,variabile,taglio);
  //cout << h1->Integral() << endl;
  TFile *fout = TFile::Open(foutput, "UPDATE"); 
  h1_uncut =(TH1F*)f1_uncut->Get("h_cutFlow");

  //h1->SetLineColor(kBlue);
  Double_t n_uncut = h1_uncut->GetBinContent(0);
  //cout << "canale " << channel << "  h_cutFlow->BinContent(0)" << n_uncut << endl;

  h1->Scale(lumi*sigma*1000/n_uncut);  //Normalizzo gli istogrammi alla luminosità misurata 
  //cout << h1->Integral() << endl;
 
  fout->cd();
    
  TLegend *leg= new TLegend(0.75,0.57,0.90,0.90);
  gStyle->SetOptStat(0);
  leg->AddEntry(h1,(variabile+channel),"l");
  h1->Draw();
  leg->Draw("SAME");
  h1->Write();
  fout->Close();
  
  f1->Close();
  f1_uncut->Close();
}
