void fit_mjj_Full_Dijet2016ScanbgDeep1b883()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Jul 26 18:20:33 2018) by ROOT version6.02/05
   TCanvas *c = new TCanvas("c", "c",0,0,600,700);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c->SetHighLightColor(2);
   c->Range(0,0,1,1);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetTopMargin(0.04761905);
   c->SetBottomMargin(0.05);
   c->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: c_1
   TPad *c_1 = new TPad("c_1", "c_1",0.01,0.37,0.99,0.98);
   c_1->Draw();
   c_1->cd();
   c_1->Range(2.91482,-2.30103,3.947382,1.465895);
   c_1->SetFillColor(0);
   c_1->SetBorderMode(0);
   c_1->SetBorderSize(2);
   c_1->SetLogx();
   c_1->SetLogy();
   c_1->SetLeftMargin(0.175);
   c_1->SetRightMargin(0.05);
   c_1->SetTopMargin(0.05);
   c_1->SetBottomMargin(0);
   c_1->SetFrameFillStyle(0);
   c_1->SetFrameBorderMode(0);
   c_1->SetFrameFillStyle(0);
   c_1->SetFrameBorderMode(0);
   Double_t xAxis1[45] = {1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866}; 
   
   TH1F *data_obs_density1 = new TH1F("data_obs_density1","pass_1DeepCSV0.8838",44, xAxis1);
   data_obs_density1->SetEntries(6928083);
   data_obs_density1->SetLineColor(0);
   data_obs_density1->SetLineWidth(0);
   data_obs_density1->SetMarkerColor(0);
   data_obs_density1->GetXaxis()->SetRange(1,44);
   data_obs_density1->GetXaxis()->SetLabelFont(42);
   data_obs_density1->GetXaxis()->SetLabelSize(0.035);
   data_obs_density1->GetXaxis()->SetTitleSize(0.035);
   data_obs_density1->GetXaxis()->SetTitleFont(42);
   data_obs_density1->GetYaxis()->SetTitle("d#sigma/dm_{jj} [pb/TeV]");
   data_obs_density1->GetYaxis()->SetLabelFont(42);
   data_obs_density1->GetYaxis()->SetLabelSize(0.05);
   data_obs_density1->GetYaxis()->SetTitleSize(0.07);
   data_obs_density1->GetYaxis()->SetTitleFont(42);
   data_obs_density1->GetZaxis()->SetLabelFont(42);
   data_obs_density1->GetZaxis()->SetLabelSize(0.035);
   data_obs_density1->GetZaxis()->SetTitleSize(0.035);
   data_obs_density1->GetZaxis()->SetTitleFont(42);
   data_obs_density1->Draw("axis");
   
   TF1 *Dijet2016ScanbgDeep1b883_bkg_unbin1 = new TF1("*Dijet2016ScanbgDeep1b883_bkg_unbin",1246,7866,1);
    //The original function :  had originally been created by:
    //TF1 *Dijet2016ScanbgDeep1b883_bkg_unbin = new TF1("Dijet2016ScanbgDeep1b883_bkg_unbin",,1246,7866,1);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetRange(1246,7866);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetName("Dijet2016ScanbgDeep1b883_bkg_unbin");
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetTitle("");
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(0,0.00216572);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(1,0.002239378);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(2,0.002064669);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(3,0.001729401);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(4,0.001336648);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(5,0.0009657549);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(6,0.0006594901);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(7,0.0004296124);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(8,0.0002690978);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(9,0.0001631743);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(10,9.634565e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(11,5.567197e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(12,3.161983e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(13,1.771939e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(14,9.829749e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(15,5.41377e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(16,2.967745e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(17,1.622917e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(18,8.870913e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(19,4.855157e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(20,2.664868e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(21,1.468877e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(22,8.140794e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(23,4.541473e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(24,2.552714e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(25,1.446991e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(26,8.278116e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(27,4.783089e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(28,2.793031e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(29,1.649248e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(30,9.852971e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(31,5.958367e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(32,3.64884e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(33,2.263717e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(34,1.423269e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(35,9.071803e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(36,5.863745e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(37,3.844626e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(38,2.557669e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(39,1.726838e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(40,1.183515e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(41,8.235764e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(42,5.820072e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(43,4.177624e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(44,3.046383e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(45,2.257192e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(46,1.699621e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(47,1.300781e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(48,1.012024e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(49,8.005292e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(50,6.439112e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(51,5.267437e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(52,4.382871e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(53,3.709921e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(54,3.195051e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(55,2.800004e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(56,2.497285e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(57,2.267081e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(58,2.095162e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(59,1.971435e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(60,1.888971e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(61,1.843363e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(62,1.832339e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(63,1.855573e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(64,1.914683e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(65,2.013417e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(66,2.158054e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(67,2.358078e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(68,2.627237e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(69,2.985148e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(70,3.459722e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(71,4.090826e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(72,4.935871e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(73,6.078433e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(74,7.641688e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(75,9.809689e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(76,1.286149e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(77,1.722675e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(78,2.357765e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(79,3.298348e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(80,4.71747e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(81,6.900183e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(82,1.032471e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(83,1.580855e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(84,2.477652e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(85,3.976166e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(86,6.535999e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(87,1.100869e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(88,1.90062e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(89,3.364773e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(90,6.110674e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(91,1.13887e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(92,2.179199e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(93,4.283025e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(94,8.650409e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(95,1.79624e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(96,3.83665e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(97,8.433868e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(98,1.909083e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(99,4.452388e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(100,1.070503e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(101,1246);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetSavedPoint(102,7866);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetFillColor(19);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetFillStyle(0);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetLineColor(2);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetLineWidth(2);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetXaxis()->SetLabelFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetXaxis()->SetLabelSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetXaxis()->SetTitleSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetXaxis()->SetTitleFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetYaxis()->SetLabelFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetYaxis()->SetLabelSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetYaxis()->SetTitleSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->GetYaxis()->SetTitleFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetParameter(0,4.27621e-103);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetParError(0,0);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->SetParLimits(0,0,0);
   Dijet2016ScanbgDeep1b883_bkg_unbin1->Draw("csame");
   TLatex *   tex = new TLatex(0.72,0.96,"41.8 fb^{-1} (13 TeV)");
tex->SetNDC();
   tex->SetTextFont(42);
   tex->SetTextSize(0.045);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.22,0.89,"CMS");
tex->SetNDC();
   tex->SetTextSize(0.065);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.32,0.89,"Preliminary");
tex->SetNDC();
   tex->SetTextFont(52);
   tex->SetTextSize(0.045);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TLegend *leg = new TLegend(0.6,0.58,0.89,0.94,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(0);
   leg->SetLineStyle(1);
   leg->SetLineWidth(0);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("Graph_from_data_obs_rebin","Data","pe");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(0.9);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Dijet2016ScanbgDeep1b883_bkg_unbin","Fit","l");
   entry->SetLineColor(2);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0.2,0.03,0.5,0.23,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextAlign(11);
   pt->SetTextFont(42);
   pt->SetTextSize(0.045);
   AText = pt->AddText("#chi^{2} / ndf = 9663.5 / 11 = 878.5");
   AText = pt->AddText("|#eta| < 2.5, |#Delta#eta| < 1.3");
   pt->Draw();
   
   TF1 *Dijet2016ScanbgDeep1b883_bkg_unbin2 = new TF1("*Dijet2016ScanbgDeep1b883_bkg_unbin",1246,7866,1);
    //The original function :  had originally been created by:
    //TF1 *Dijet2016ScanbgDeep1b883_bkg_unbin = new TF1("Dijet2016ScanbgDeep1b883_bkg_unbin",,1246,7866,1);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetRange(1246,7866);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetName("Dijet2016ScanbgDeep1b883_bkg_unbin");
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetTitle("");
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(0,0.00216572);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(1,0.002239378);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(2,0.002064669);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(3,0.001729401);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(4,0.001336648);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(5,0.0009657549);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(6,0.0006594901);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(7,0.0004296124);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(8,0.0002690978);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(9,0.0001631743);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(10,9.634565e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(11,5.567197e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(12,3.161983e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(13,1.771939e-05);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(14,9.829749e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(15,5.41377e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(16,2.967745e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(17,1.622917e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(18,8.870913e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(19,4.855157e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(20,2.664868e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(21,1.468877e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(22,8.140794e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(23,4.541473e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(24,2.552714e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(25,1.446991e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(26,8.278116e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(27,4.783089e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(28,2.793031e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(29,1.649248e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(30,9.852971e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(31,5.958367e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(32,3.64884e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(33,2.263717e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(34,1.423269e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(35,9.071803e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(36,5.863745e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(37,3.844626e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(38,2.557669e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(39,1.726838e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(40,1.183515e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(41,8.235764e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(42,5.820072e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(43,4.177624e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(44,3.046383e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(45,2.257192e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(46,1.699621e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(47,1.300781e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(48,1.012024e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(49,8.005292e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(50,6.439112e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(51,5.267437e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(52,4.382871e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(53,3.709921e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(54,3.195051e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(55,2.800004e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(56,2.497285e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(57,2.267081e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(58,2.095162e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(59,1.971435e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(60,1.888971e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(61,1.843363e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(62,1.832339e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(63,1.855573e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(64,1.914683e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(65,2.013417e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(66,2.158054e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(67,2.358078e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(68,2.627237e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(69,2.985148e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(70,3.459722e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(71,4.090826e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(72,4.935871e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(73,6.078433e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(74,7.641688e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(75,9.809689e-13);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(76,1.286149e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(77,1.722675e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(78,2.357765e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(79,3.298348e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(80,4.71747e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(81,6.900183e-12);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(82,1.032471e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(83,1.580855e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(84,2.477652e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(85,3.976166e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(86,6.535999e-11);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(87,1.100869e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(88,1.90062e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(89,3.364773e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(90,6.110674e-10);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(91,1.13887e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(92,2.179199e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(93,4.283025e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(94,8.650409e-09);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(95,1.79624e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(96,3.83665e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(97,8.433868e-08);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(98,1.909083e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(99,4.452388e-07);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(100,1.070503e-06);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(101,1246);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetSavedPoint(102,7866);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetFillColor(19);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetFillStyle(0);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetLineColor(2);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetLineWidth(2);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetXaxis()->SetLabelFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetXaxis()->SetLabelSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetXaxis()->SetTitleSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetXaxis()->SetTitleFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetYaxis()->SetLabelFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetYaxis()->SetLabelSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetYaxis()->SetTitleSize(0.035);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->GetYaxis()->SetTitleFont(42);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetParameter(0,4.27621e-103);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetParError(0,0);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->SetParLimits(0,0,0);
   Dijet2016ScanbgDeep1b883_bkg_unbin2->Draw("csame");
   
   Double_t g_data_clone_fx3001[44] = {
   1279.5,
   1348,
   1419,
   1492.5,
   1568.5,
   1647,
   1728.5,
   1813,
   1900.5,
   1991,
   2084.5,
   2181.5,
   2281.5,
   2385,
   2492,
   2602.5,
   2717,
   2835,
   2957,
   3083,
   3213,
   3347.5,
   3487,
   3631,
   3779,
   3932,
   4090.5,
   4254,
   4423,
   4597.5,
   4777.5,
   4963.5,
   5155.5,
   5354,
   5559,
   5770,
   5988,
   6213.5,
   6446,
   6686,
   6934,
   7190,
   7454.5,
   7727.5};
   Double_t g_data_clone_fy3001[44] = {
   0,
   0.006203349,
   0,
   0.002357576,
   0,
   0.0009043062,
   0,
   0.0003688661,
   0.0001497231,
   0,
   6.799295e-05,
   0,
   3.197688e-05,
   1.015618e-05,
   0,
   4.44595e-06,
   1.856129e-06,
   9.968102e-07,
   5.78793e-07,
   0,
   5.437147e-07,
   0,
   1.68475e-07,
   3.277184e-07,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t g_data_clone_felx3001[44] = {
   33.5,
   35,
   36,
   37.5,
   38.5,
   40,
   41.5,
   43,
   44.5,
   46,
   47.5,
   49.5,
   50.5,
   53,
   54,
   56.5,
   58,
   60,
   62,
   64,
   66,
   68.5,
   71,
   73,
   75,
   78,
   80.5,
   83,
   86,
   88.5,
   91.5,
   94.5,
   97.5,
   101,
   104,
   107,
   111,
   114.5,
   118,
   122,
   126,
   130,
   134.5,
   138.5};
   Double_t g_data_clone_fely3001[44] = {
   0,
   4.604488e-05,
   0,
   2.742291e-05,
   0,
   1.64441e-05,
   0,
   1.012865e-05,
   6.342205e-06,
   0,
   4.135444e-06,
   0,
   2.748777e-06,
   1.508376e-06,
   0,
   9.624193e-07,
   6.070597e-07,
   4.30567e-07,
   3.150036e-07,
   0,
   2.959125e-07,
   0,
   1.393713e-07,
   2.116782e-07,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t g_data_clone_fehx3001[44] = {
   33.5,
   35,
   36,
   37.5,
   38.5,
   40,
   41.5,
   43,
   44.5,
   46,
   47.5,
   49.5,
   50.5,
   53,
   54,
   56.5,
   58,
   60,
   62,
   64,
   66,
   68.5,
   71,
   73,
   75,
   78,
   80.5,
   83,
   86,
   88.5,
   91.5,
   94.5,
   97.5,
   101,
   104,
   107,
   111,
   114.5,
   118,
   122,
   126,
   130,
   134.5,
   138.5};
   Double_t g_data_clone_fehy3001[44] = {
   6.573787e-07,
   4.638792e-05,
   6.117274e-07,
   2.774376e-05,
   5.720048e-07,
   1.674587e-05,
   5.306551e-07,
   1.041066e-05,
   6.616716e-06,
   4.787432e-07,
   4.394951e-06,
   4.448926e-07,
   2.995862e-06,
   1.75094e-06,
   4.078183e-07,
   1.197294e-06,
   8.476915e-07,
   6.743499e-07,
   5.630194e-07,
   3.440967e-07,
   5.288971e-07,
   3.214918e-07,
   3.874199e-07,
   4.322459e-07,
   2.936291e-07,
   2.823357e-07,
   2.735675e-07,
   2.653275e-07,
   2.560719e-07,
   2.488383e-07,
   2.406796e-07,
   2.33039e-07,
   2.258686e-07,
   2.180414e-07,
   2.117518e-07,
   2.058148e-07,
   1.983981e-07,
   1.923335e-07,
   1.866287e-07,
   1.805097e-07,
   1.747793e-07,
   1.694014e-07,
   1.637337e-07,
   1.59005e-07};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(44,g_data_clone_fx3001,g_data_clone_fy3001,g_data_clone_felx3001,g_data_clone_fehx3001,g_data_clone_fely3001,g_data_clone_fehy3001);
   grae->SetName("g_data_clone");
   grae->SetTitle("pass_1DeepCSV0.8838");
   grae->SetMarkerStyle(20);
   grae->SetMarkerSize(0);
   
   TH1F *Graph_g_data_clone3001 = new TH1F("Graph_g_data_clone3001","pass_1DeepCSV0.8838",100,584,8528);
   Graph_g_data_clone3001->SetMinimum(6.874711e-06);
   Graph_g_data_clone3001->SetMaximum(0.006874711);
   Graph_g_data_clone3001->SetDirectory(0);
   Graph_g_data_clone3001->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_g_data_clone3001->SetLineColor(ci);
   Graph_g_data_clone3001->GetXaxis()->SetLabelFont(42);
   Graph_g_data_clone3001->GetXaxis()->SetLabelSize(0.035);
   Graph_g_data_clone3001->GetXaxis()->SetTitleSize(0.035);
   Graph_g_data_clone3001->GetXaxis()->SetTitleFont(42);
   Graph_g_data_clone3001->GetYaxis()->SetLabelFont(42);
   Graph_g_data_clone3001->GetYaxis()->SetLabelSize(0.035);
   Graph_g_data_clone3001->GetYaxis()->SetTitleSize(0.035);
   Graph_g_data_clone3001->GetYaxis()->SetTitleFont(42);
   Graph_g_data_clone3001->GetZaxis()->SetLabelFont(42);
   Graph_g_data_clone3001->GetZaxis()->SetLabelSize(0.035);
   Graph_g_data_clone3001->GetZaxis()->SetTitleSize(0.035);
   Graph_g_data_clone3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_g_data_clone3001);
   
   grae->Draw("zp");
   
   Double_t Graph_from_data_obs_rebin_fx3002[44] = {
   1279.5,
   1348,
   1419,
   1492.5,
   1568.5,
   1647,
   1728.5,
   1813,
   1900.5,
   1991,
   2084.5,
   2181.5,
   2281.5,
   2385,
   2492,
   2602.5,
   2717,
   2835,
   2957,
   3083,
   3213,
   3347.5,
   3487,
   3631,
   3779,
   3932,
   4090.5,
   4254,
   4423,
   4597.5,
   4777.5,
   4963.5,
   5155.5,
   5354,
   5559,
   5770,
   5988,
   6213.5,
   6446,
   6686,
   6934,
   7190,
   7454.5,
   7727.5};
   Double_t Graph_from_data_obs_rebin_fy3002[44] = {
   99999,
   0.006203349,
   99999,
   0.002357576,
   99999,
   0.0009043062,
   99999,
   0.0003688661,
   0.0001497231,
   99999,
   6.799295e-05,
   99999,
   3.197688e-05,
   1.015618e-05,
   99999,
   4.44595e-06,
   1.856129e-06,
   9.968102e-07,
   5.78793e-07,
   99999,
   5.437147e-07,
   99999,
   1.68475e-07,
   3.277184e-07,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999,
   99999};
   Double_t Graph_from_data_obs_rebin_felx3002[44] = {
   33.5,
   35,
   36,
   37.5,
   38.5,
   40,
   41.5,
   43,
   44.5,
   46,
   47.5,
   49.5,
   50.5,
   53,
   54,
   56.5,
   58,
   60,
   62,
   64,
   66,
   68.5,
   71,
   73,
   75,
   78,
   80.5,
   83,
   86,
   88.5,
   91.5,
   94.5,
   97.5,
   101,
   104,
   107,
   111,
   114.5,
   118,
   122,
   126,
   130,
   134.5,
   138.5};
   Double_t Graph_from_data_obs_rebin_fely3002[44] = {
   0,
   4.604488e-05,
   0,
   2.742291e-05,
   0,
   1.64441e-05,
   0,
   1.012865e-05,
   6.342205e-06,
   0,
   4.135444e-06,
   0,
   2.748777e-06,
   1.508376e-06,
   0,
   9.624193e-07,
   6.070597e-07,
   4.30567e-07,
   3.150036e-07,
   0,
   2.959125e-07,
   0,
   1.393713e-07,
   2.116782e-07,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   Double_t Graph_from_data_obs_rebin_fehx3002[44] = {
   33.5,
   35,
   36,
   37.5,
   38.5,
   40,
   41.5,
   43,
   44.5,
   46,
   47.5,
   49.5,
   50.5,
   53,
   54,
   56.5,
   58,
   60,
   62,
   64,
   66,
   68.5,
   71,
   73,
   75,
   78,
   80.5,
   83,
   86,
   88.5,
   91.5,
   94.5,
   97.5,
   101,
   104,
   107,
   111,
   114.5,
   118,
   122,
   126,
   130,
   134.5,
   138.5};
   Double_t Graph_from_data_obs_rebin_fehy3002[44] = {
   6.573787e-07,
   4.638792e-05,
   6.117274e-07,
   2.774376e-05,
   5.720048e-07,
   1.674587e-05,
   5.306551e-07,
   1.041066e-05,
   6.616716e-06,
   4.787432e-07,
   4.394951e-06,
   4.448926e-07,
   2.995862e-06,
   1.75094e-06,
   4.078183e-07,
   1.197294e-06,
   8.476915e-07,
   6.743499e-07,
   5.630194e-07,
   3.440967e-07,
   5.288971e-07,
   3.214918e-07,
   3.874199e-07,
   4.322459e-07,
   2.936291e-07,
   2.823357e-07,
   2.735675e-07,
   2.653275e-07,
   2.560719e-07,
   2.488383e-07,
   2.406796e-07,
   2.33039e-07,
   2.258686e-07,
   2.180414e-07,
   2.117518e-07,
   2.058148e-07,
   1.983981e-07,
   1.923335e-07,
   1.866287e-07,
   1.805097e-07,
   1.747793e-07,
   1.694014e-07,
   1.637337e-07,
   1.59005e-07};
   grae = new TGraphAsymmErrors(44,Graph_from_data_obs_rebin_fx3002,Graph_from_data_obs_rebin_fy3002,Graph_from_data_obs_rebin_felx3002,Graph_from_data_obs_rebin_fehx3002,Graph_from_data_obs_rebin_fely3002,Graph_from_data_obs_rebin_fehy3002);
   grae->SetName("Graph_from_data_obs_rebin");
   grae->SetTitle("pass_1DeepCSV0.8838");
   grae->SetMarkerStyle(20);
   grae->SetMarkerSize(0.9);
   
   TH1F *Graph_Graph_from_data_obs_rebin3002 = new TH1F("Graph_Graph_from_data_obs_rebin3002","pass_1DeepCSV0.8838",100,584,8528);
   Graph_Graph_from_data_obs_rebin3002->SetMinimum(2.619327e-08);
   Graph_Graph_from_data_obs_rebin3002->SetMaximum(109998.9);
   Graph_Graph_from_data_obs_rebin3002->SetDirectory(0);
   Graph_Graph_from_data_obs_rebin3002->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_from_data_obs_rebin3002->SetLineColor(ci);
   Graph_Graph_from_data_obs_rebin3002->GetXaxis()->SetLabelFont(42);
   Graph_Graph_from_data_obs_rebin3002->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetXaxis()->SetTitleFont(42);
   Graph_Graph_from_data_obs_rebin3002->GetYaxis()->SetLabelFont(42);
   Graph_Graph_from_data_obs_rebin3002->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetYaxis()->SetTitleFont(42);
   Graph_Graph_from_data_obs_rebin3002->GetZaxis()->SetLabelFont(42);
   Graph_Graph_from_data_obs_rebin3002->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph_from_data_obs_rebin3002->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph_from_data_obs_rebin3002);
   
   grae->Draw("zp");
   c_1->Modified();
   c->cd();
  
// ------------>Primitives in pad: c_2
   TPad *c_2 = new TPad("c_2", "c_2",0.01,0.02,0.99,0.37);
   c_2->Draw();
   c_2->cd();
   c_2->Range(2.91482,-7.269231,3.947382,3.5);
   c_2->SetFillColor(0);
   c_2->SetBorderMode(0);
   c_2->SetBorderSize(2);
   c_2->SetLogx();
   c_2->SetGridx();
   c_2->SetGridy();
   c_2->SetLeftMargin(0.175);
   c_2->SetRightMargin(0.05);
   c_2->SetTopMargin(0);
   c_2->SetBottomMargin(0.35);
   c_2->SetFrameBorderMode(0);
   c_2->SetFrameBorderMode(0);
   Double_t xAxis2[45] = {1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866}; 
   
   TH1D *h_fit_residual_vs_mass2 = new TH1D("h_fit_residual_vs_mass2","h_fit_residual_vs_mass",44, xAxis2);
   h_fit_residual_vs_mass2->SetBinContent(1,-3385.604);
   h_fit_residual_vs_mass2->SetBinContent(2,87.78329);
   h_fit_residual_vs_mass2->SetBinContent(3,-3051.357);
   h_fit_residual_vs_mass2->SetBinContent(4,33.23858);
   h_fit_residual_vs_mass2->SetBinContent(5,-1772.499);
   h_fit_residual_vs_mass2->SetBinContent(6,15.52876);
   h_fit_residual_vs_mass2->SetBinContent(7,-718.1202);
   h_fit_residual_vs_mass2->SetBinContent(8,16.00285);
   h_fit_residual_vs_mass2->SetBinContent(9,7.13952);
   h_fit_residual_vs_mass2->SetBinContent(10,-103.3296);
   h_fit_residual_vs_mass2->SetBinContent(11,11.08936);
   h_fit_residual_vs_mass2->SetBinContent(12,-21.10102);
   h_fit_residual_vs_mass2->SetBinContent(13,10.24662);
   h_fit_residual_vs_mass2->SetBinContent(14,5.745366);
   h_fit_residual_vs_mass2->SetBinContent(15,-1.379637);
   h_fit_residual_vs_mass2->SetBinContent(16,4.403851);
   h_fit_residual_vs_mass2->SetBinContent(17,2.934391);
   h_fit_residual_vs_mass2->SetBinContent(18,2.253165);
   h_fit_residual_vs_mass2->SetBinContent(19,1.807443);
   h_fit_residual_vs_mass2->SetBinContent(20,-0.009716595);
   h_fit_residual_vs_mass2->SetBinContent(21,1.833383);
   h_fit_residual_vs_mass2->SetBinContent(22,-0.001343077);
   h_fit_residual_vs_mass2->SetBinContent(23,1.20768);
   h_fit_residual_vs_mass2->SetBinContent(24,1.547907);
   h_fit_residual_vs_mass2->SetBinContent(25,-8.137526e-05);
   h_fit_residual_vs_mass2->SetBinContent(26,-3.514243e-05);
   h_fit_residual_vs_mass2->SetBinContent(27,-1.58944e-05);
   h_fit_residual_vs_mass2->SetBinContent(28,-7.691359e-06);
   h_fit_residual_vs_mass2->SetBinContent(29,-4.045964e-06);
   h_fit_residual_vs_mass2->SetBinContent(30,-2.315684e-06);
   h_fit_residual_vs_mass2->SetBinContent(31,-1.479913e-06);
   h_fit_residual_vs_mass2->SetBinContent(32,-1.064594e-06);
   h_fit_residual_vs_mass2->SetBinContent(33,-8.768894e-07);
   h_fit_residual_vs_mass2->SetBinContent(34,-8.466489e-07);
   h_fit_residual_vs_mass2->SetBinContent(35,-9.688523e-07);
   h_fit_residual_vs_mass2->SetBinContent(36,-1.350579e-06);
   h_fit_residual_vs_mass2->SetBinContent(37,-2.378564e-06);
   h_fit_residual_vs_mass2->SetBinContent(38,-5.385904e-06);
   h_fit_residual_vs_mass2->SetBinContent(39,-1.627878e-05);
   h_fit_residual_vs_mass2->SetBinContent(40,-6.87783e-05);
   h_fit_residual_vs_mass2->SetBinContent(41,-0.0004247625);
   h_fit_residual_vs_mass2->SetBinContent(42,-0.004049606);
   h_fit_residual_vs_mass2->SetBinContent(43,-0.06425549);
   h_fit_residual_vs_mass2->SetBinContent(44,-1.811863);
   h_fit_residual_vs_mass2->SetBinError(1,1);
   h_fit_residual_vs_mass2->SetBinError(2,1);
   h_fit_residual_vs_mass2->SetBinError(3,1);
   h_fit_residual_vs_mass2->SetBinError(4,1);
   h_fit_residual_vs_mass2->SetBinError(5,1);
   h_fit_residual_vs_mass2->SetBinError(6,1);
   h_fit_residual_vs_mass2->SetBinError(7,1);
   h_fit_residual_vs_mass2->SetBinError(8,1);
   h_fit_residual_vs_mass2->SetBinError(9,1);
   h_fit_residual_vs_mass2->SetBinError(10,1);
   h_fit_residual_vs_mass2->SetBinError(11,1);
   h_fit_residual_vs_mass2->SetBinError(12,1);
   h_fit_residual_vs_mass2->SetBinError(13,1);
   h_fit_residual_vs_mass2->SetBinError(14,1);
   h_fit_residual_vs_mass2->SetBinError(15,1);
   h_fit_residual_vs_mass2->SetBinError(16,1);
   h_fit_residual_vs_mass2->SetBinError(17,1);
   h_fit_residual_vs_mass2->SetBinError(18,1);
   h_fit_residual_vs_mass2->SetBinError(19,1);
   h_fit_residual_vs_mass2->SetBinError(20,1);
   h_fit_residual_vs_mass2->SetBinError(21,1);
   h_fit_residual_vs_mass2->SetBinError(22,1);
   h_fit_residual_vs_mass2->SetBinError(23,1);
   h_fit_residual_vs_mass2->SetBinError(24,1);
   h_fit_residual_vs_mass2->SetBinError(25,1);
   h_fit_residual_vs_mass2->SetBinError(26,1);
   h_fit_residual_vs_mass2->SetBinError(27,1);
   h_fit_residual_vs_mass2->SetBinError(28,1);
   h_fit_residual_vs_mass2->SetBinError(29,1);
   h_fit_residual_vs_mass2->SetBinError(30,1);
   h_fit_residual_vs_mass2->SetBinError(31,1);
   h_fit_residual_vs_mass2->SetBinError(32,1);
   h_fit_residual_vs_mass2->SetBinError(33,1);
   h_fit_residual_vs_mass2->SetBinError(34,1);
   h_fit_residual_vs_mass2->SetBinError(35,1);
   h_fit_residual_vs_mass2->SetBinError(36,1);
   h_fit_residual_vs_mass2->SetBinError(37,1);
   h_fit_residual_vs_mass2->SetBinError(38,1);
   h_fit_residual_vs_mass2->SetBinError(39,1);
   h_fit_residual_vs_mass2->SetBinError(40,1);
   h_fit_residual_vs_mass2->SetBinError(41,1);
   h_fit_residual_vs_mass2->SetBinError(42,1);
   h_fit_residual_vs_mass2->SetBinError(43,1);
   h_fit_residual_vs_mass2->SetBinError(44,1);
   h_fit_residual_vs_mass2->SetMinimum(-3.5);
   h_fit_residual_vs_mass2->SetMaximum(3.5);
   h_fit_residual_vs_mass2->SetEntries(44);
   h_fit_residual_vs_mass2->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   h_fit_residual_vs_mass2->SetFillColor(ci);
   h_fit_residual_vs_mass2->GetXaxis()->SetTitle("Dijet mass [TeV]");
   h_fit_residual_vs_mass2->GetXaxis()->SetRange(1,44);
   h_fit_residual_vs_mass2->GetXaxis()->SetMoreLogLabels();
   h_fit_residual_vs_mass2->GetXaxis()->SetNoExponent();
   h_fit_residual_vs_mass2->GetXaxis()->SetNdivisions(999);
   h_fit_residual_vs_mass2->GetXaxis()->SetLabelFont(42);
   h_fit_residual_vs_mass2->GetXaxis()->SetLabelOffset(1000);
   h_fit_residual_vs_mass2->GetXaxis()->SetLabelSize(0.1);
   h_fit_residual_vs_mass2->GetXaxis()->SetTitleSize(0.12);
   h_fit_residual_vs_mass2->GetXaxis()->SetTitleFont(42);
   h_fit_residual_vs_mass2->GetYaxis()->SetTitle("#frac{(Data-Fit)}{Uncertainty}");
   h_fit_residual_vs_mass2->GetYaxis()->SetNdivisions(210);
   h_fit_residual_vs_mass2->GetYaxis()->SetLabelFont(42);
   h_fit_residual_vs_mass2->GetYaxis()->SetLabelSize(0.1);
   h_fit_residual_vs_mass2->GetYaxis()->SetTitleSize(0.12);
   h_fit_residual_vs_mass2->GetYaxis()->SetTitleOffset(0.6);
   h_fit_residual_vs_mass2->GetYaxis()->SetTitleFont(42);
   h_fit_residual_vs_mass2->GetZaxis()->SetLabelFont(42);
   h_fit_residual_vs_mass2->GetZaxis()->SetLabelSize(0.035);
   h_fit_residual_vs_mass2->GetZaxis()->SetTitleSize(0.035);
   h_fit_residual_vs_mass2->GetZaxis()->SetTitleFont(42);
   h_fit_residual_vs_mass2->Draw("hist");
      tex = new TLatex(2000,-4,"2");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(3000,-4,"3");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(4000,-4,"4");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(5000,-4,"5");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(6000,-4,"6");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(7000,-4,"7");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(8000,-4,"8");
   tex->SetTextAlign(22);
   tex->SetTextFont(42);
   tex->SetTextSize(0.1);
   tex->SetLineWidth(2);
   tex->Draw();
   TGaxis *gaxis = new TGaxis(1246,-3.5,7866,-3.5,1246,7866,509,"BS");
   gaxis->SetLabelOffset(1000);
   gaxis->SetLabelSize(0.04);
   gaxis->SetTickSize(0.03);
   gaxis->SetGridLength(0);
   gaxis->SetTitleOffset(1);
   gaxis->SetTitleSize(0.04);
   gaxis->SetTitleColor(1);
   gaxis->SetTitleFont(62);
   gaxis->SetMoreLogLabels();
   gaxis->Draw();
   c_2->Modified();
   c->cd();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
