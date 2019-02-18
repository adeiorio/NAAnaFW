#include <iostream>
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TString.h"

using namespace std;
void macro_plot(TString channel, TString variabile, TString title, TString peso, int nbins, float xmin, float xmax, TString njmt, TString syst, TString cut_tag, TString lep) {
  TFile *f1= TFile::Open("trees_lumi/"+lep+"/trees_"+channel+"_"+lep+".root");
  TString histoname;
  TString treename = "events_"+njmt;
  TString taglio, foutput;
  if(cut_tag.EqualTo(""))    histoname = "h_"+njmt+"_"+variabile;
  else    histoname = "h_"+njmt+"_"+variabile+"_"+cut_tag;
  TH1F *h1 = new TH1F(histoname, variabile+"_"+channel, nbins, xmin, xmax);
  h1->Sumw2();
  if(channel.EqualTo("Data")){
    taglio ="w_nominal*"+peso;
    foutput = "Plot/"+lep+"/"+channel+"_"+lep+".root";
  }
  else{
    if(njmt.EqualTo("2j1t")){
      if(syst.EqualTo("")){
	taglio = peso+"*w_nominal";
	foutput = "Plot/"+lep+"/"+channel+"_"+lep+".root"; 
      }else{
        if(syst.EqualTo("jesUp")||syst.EqualTo("jesDown")||syst.EqualTo("jerUp")||syst.EqualTo("jerDown")){
	  taglio = peso+"*w_nominal";
	  treename = "events_"+njmt+"_"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }else if(syst.Contains("cmva")){
	  taglio = peso+"*w_nominal";
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }else{
	  taglio = peso+"*"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
      }
    }
    if(njmt.EqualTo("3j1t")){
      if(syst.EqualTo("")){
	taglio = peso+"*(abs(leadingextrajetcsvweight))*w_nominal";
	foutput = "Plot/"+lep+"/"+channel+"_"+lep+".root"; 
      }else{
        if(syst.EqualTo("jesUp")||syst.EqualTo("jesDown")||syst.EqualTo("jerUp")||syst.EqualTo("jerDown")){
	  taglio = peso+"*abs(leadingextrajetcsvweight)*w_nominal";
	  treename = "events_"+njmt+"_"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
        else if(syst.Contains("cmva")){
	  taglio = peso+"*abs("+syst+")*abs(leadingextrajetcsvweight)";
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
        else{
	  taglio = peso+"*abs(leadingextrajetcsvweight)*"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
      }
    }
    if(njmt.EqualTo("3j2t")){
      if(syst.EqualTo("")){
	taglio = peso+"*w_nominal";
	foutput = "Plot/"+lep+"/"+channel+"_"+lep+".root"; 
      }
      else{
        if(syst.EqualTo("jesUp")||syst.EqualTo("jesDown")||syst.EqualTo("jerUp")||syst.EqualTo("jerDown")){
	  taglio = peso+"*w_nominal";
	  treename = "events_"+njmt+"_"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
        else if(syst.Contains("cmva")){
	  taglio = peso+"*w_nominal";
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
        else{
	  taglio = peso+"*"+syst;
	  foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"; 
        }
      }
    }
  } 
  ((TTree*)f1->Get(treename))->Project(histoname,variabile,taglio);
  h1->SetBinContent(1, h1->GetBinContent(0) + h1->GetBinContent(1));
  h1->SetBinError(1, sqrt(pow(h1->GetBinError(0),2) + pow(h1->GetBinError(1),2)));
  h1->SetBinContent(nbins, h1->GetBinContent(nbins) + h1->GetBinContent(nbins+1));
  h1->SetBinError(nbins, sqrt(pow(h1->GetBinError(nbins),2) + pow(h1->GetBinError(nbins+1),2)));
  for(int i=0; i<nbins+1; i++){
    Double_t content = h1->GetBinContent(i);
    if(content<0.) h1->SetBinContent(i, 0.);
  }
  //  cout << "integral " << channel << " is " << h1->Integral() <<endl;
  TFile *fout = TFile::Open(foutput, "UPDATE"); 
  
  fout->cd();
  h1->Write();
  fout->Close();
  f1->Close();
}
