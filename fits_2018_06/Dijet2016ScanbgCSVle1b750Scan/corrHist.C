void corrHist()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Jul 26 17:16:32 2018) by ROOT version6.02/05
   TCanvas *c = new TCanvas("c", "c",0,0,500,500);
   gStyle->SetOptStat(0);
   c->SetHighLightColor(2);
   c->Range(-0.5333333,-0.5,4.8,4.5);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetRightMargin(0.15);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   TH2D *correlation_matrix = new TH2D("correlation_matrix","correlation_matrix",4,0,4,4,0,4);
   correlation_matrix->SetBinContent(8,-0.9384509);
   correlation_matrix->SetBinContent(9,0.9974389);
   correlation_matrix->SetBinContent(10,1);
   correlation_matrix->SetBinContent(14,-0.9591183);
   correlation_matrix->SetBinContent(15,1);
   correlation_matrix->SetBinContent(16,0.9974389);
   correlation_matrix->SetBinContent(20,1);
   correlation_matrix->SetBinContent(21,-0.9591183);
   correlation_matrix->SetBinContent(22,-0.9384509);
   correlation_matrix->SetBinContent(25,1);
   correlation_matrix->SetBinError(8,0.9384509);
   correlation_matrix->SetBinError(9,0.9974389);
   correlation_matrix->SetBinError(10,1);
   correlation_matrix->SetBinError(14,0.9591183);
   correlation_matrix->SetBinError(15,1);
   correlation_matrix->SetBinError(16,0.9974389);
   correlation_matrix->SetBinError(20,1);
   correlation_matrix->SetBinError(21,0.9591183);
   correlation_matrix->SetBinError(22,0.9384509);
   correlation_matrix->SetBinError(25,1);
   correlation_matrix->SetMinimum(-1);
   correlation_matrix->SetMaximum(1);
   correlation_matrix->SetEntries(16);
   correlation_matrix->SetStats(0);
   correlation_matrix->SetContour(20);
   correlation_matrix->SetContourLevel(0,-1);
   correlation_matrix->SetContourLevel(1,-0.9);
   correlation_matrix->SetContourLevel(2,-0.8);
   correlation_matrix->SetContourLevel(3,-0.7);
   correlation_matrix->SetContourLevel(4,-0.6);
   correlation_matrix->SetContourLevel(5,-0.5);
   correlation_matrix->SetContourLevel(6,-0.4);
   correlation_matrix->SetContourLevel(7,-0.3);
   correlation_matrix->SetContourLevel(8,-0.2);
   correlation_matrix->SetContourLevel(9,-0.1);
   correlation_matrix->SetContourLevel(10,0);
   correlation_matrix->SetContourLevel(11,0.1);
   correlation_matrix->SetContourLevel(12,0.2);
   correlation_matrix->SetContourLevel(13,0.3);
   correlation_matrix->SetContourLevel(14,0.4);
   correlation_matrix->SetContourLevel(15,0.5);
   correlation_matrix->SetContourLevel(16,0.6);
   correlation_matrix->SetContourLevel(17,0.7);
   correlation_matrix->SetContourLevel(18,0.8);
   correlation_matrix->SetContourLevel(19,0.9);
   
   TPaletteAxis *palette = new TPaletteAxis(4.026667,0,4.266667,4,correlation_matrix);
palette->SetLabelColor(1);
palette->SetLabelFont(42);
palette->SetLabelOffset(0.005);
palette->SetLabelSize(0.035);
palette->SetTitleOffset(1);
palette->SetTitleSize(0.035);
   palette->SetFillColor(100);
   palette->SetFillStyle(1001);
   correlation_matrix->GetListOfFunctions()->Add(palette,"br");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   correlation_matrix->SetLineColor(ci);
   correlation_matrix->GetXaxis()->SetBinLabel(1,"Ntot_bkg_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetXaxis()->SetBinLabel(2,"p1_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetXaxis()->SetBinLabel(3,"p2_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetXaxis()->SetBinLabel(4,"p3_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetXaxis()->SetLabelFont(42);
   correlation_matrix->GetXaxis()->SetLabelSize(0.035);
   correlation_matrix->GetXaxis()->SetTitleSize(0.035);
   correlation_matrix->GetXaxis()->SetTitleFont(42);
   correlation_matrix->GetYaxis()->SetBinLabel(4,"Ntot_bkg_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetYaxis()->SetBinLabel(3,"p1_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetYaxis()->SetBinLabel(2,"p2_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetYaxis()->SetBinLabel(1,"p3_Dijet2016ScanbgCSVle1b750");
   correlation_matrix->GetYaxis()->SetLabelFont(42);
   correlation_matrix->GetYaxis()->SetLabelSize(0.035);
   correlation_matrix->GetYaxis()->SetTitleSize(0.035);
   correlation_matrix->GetYaxis()->SetTitleFont(42);
   correlation_matrix->GetZaxis()->SetLabelFont(42);
   correlation_matrix->GetZaxis()->SetLabelSize(0.035);
   correlation_matrix->GetZaxis()->SetTitleSize(0.035);
   correlation_matrix->GetZaxis()->SetTitleFont(42);
   correlation_matrix->Draw("colztext");
   
   TPaveText *pt = new TPaveText(0.2793145,0.9365254,0.7206855,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *AText = pt->AddText("correlation_matrix");
   pt->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
