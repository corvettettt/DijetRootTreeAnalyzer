void fit_mjj_Full_Dijet2017ScanbgDeep1b850()
{
//=========Macro generated from canvas: c/c
//=========  (Thu Jul 26 18:12:30 2018) by ROOT version6.02/05
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
   
   TH1F *data_obs_density1 = new TH1F("data_obs_density1","pass_1DeepCSV0.85",44, xAxis1);
   data_obs_density1->SetEntries(4047013);
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
   
   TF1 *Dijet2017ScanbgDeep1b850_bkg_unbin1 = new TF1("*Dijet2017ScanbgDeep1b850_bkg_unbin",1246,7866,1);
    //The original function :  had originally been created by:
    //TF1 *Dijet2017ScanbgDeep1b850_bkg_unbin = new TF1("Dijet2017ScanbgDeep1b850_bkg_unbin",,1246,7866,1);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetRange(1246,7866);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetName("Dijet2017ScanbgDeep1b850_bkg_unbin");
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetTitle("");
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(0,0.0029904);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(1,0.003156216);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(2,0.002905739);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(3,0.002386036);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(4,0.001780217);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(5,0.001225687);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(6,0.0007889887);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(7,0.0004801259);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(8,0.0002788232);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(9,0.0001557756);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(10,8.431061e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(11,4.447154e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(12,2.298036e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(13,1.168612e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(14,5.871338e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(15,2.924547e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(16,1.448615e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(17,7.154532e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(18,3.531574e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(19,1.745907e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(20,8.660535e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(21,4.317719e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(22,2.166645e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(23,1.095757e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(24,5.591696e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(25,2.882254e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(26,1.502072e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(27,7.921161e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(28,4.23019e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(29,2.289313e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(30,1.256314e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(31,6.994985e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(32,3.953637e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(33,2.269522e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(34,1.323696e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(35,7.847497e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(36,4.730668e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(37,2.900744e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(38,1.809789e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(39,1.149224e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(40,7.429478e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(41,4.891016e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(42,3.27968e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(43,2.240547e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(44,1.559769e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(45,1.106725e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(46,8.005304e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(47,5.904147e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(48,4.440763e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(49,3.406882e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(50,2.666439e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(51,2.129394e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(52,1.735418e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(53,1.443608e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(54,1.225927e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(55,1.062974e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(56,9.41232e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(57,8.512574e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(58,7.864836e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(59,7.424354e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(60,7.162171e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(61,7.061974e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(62,7.118408e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(63,7.336634e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(64,7.733068e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(65,8.337464e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(66,9.196696e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(67,1.038094e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(68,1.199339e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(69,1.418551e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(70,1.718089e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(71,2.131312e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(72,2.708672e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(73,3.527637e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(74,4.709166e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(75,6.445477e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(76,9.047734e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(77,1.302943e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(78,1.925499e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(79,2.920991e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(80,4.550175e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(81,7.280875e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(82,1.197152e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(83,2.023409e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(84,3.516827e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(85,6.288135e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(86,1.157107e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(87,2.19225e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(88,4.278217e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(89,8.603806e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(90,1.783939e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(91,3.815451e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(92,8.421933e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(93,1.919597e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(94,4.520458e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(95,1.100476e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(96,2.771193e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(97,7.222932e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(98,1.949868e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(99,5.455538e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(100,1.583141e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(101,1246);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetSavedPoint(102,7866);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetFillColor(19);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetFillStyle(0);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetLineColor(2);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetLineWidth(2);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetXaxis()->SetLabelFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetXaxis()->SetLabelSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetXaxis()->SetTitleSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetXaxis()->SetTitleFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetYaxis()->SetLabelFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetYaxis()->SetLabelSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetYaxis()->SetTitleSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->GetYaxis()->SetTitleFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetParameter(0,7.287582e-122);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetParError(0,0);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->SetParLimits(0,0,0);
   Dijet2017ScanbgDeep1b850_bkg_unbin1->Draw("csame");
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
   entry=leg->AddEntry("Dijet2017ScanbgDeep1b850_bkg_unbin","Fit","l");
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
   AText = pt->AddText("#chi^{2} / ndf = 13139.0 / 10 = 1313.9");
   AText = pt->AddText("|#eta| < 2.5, |#Delta#eta| < 1.3");
   pt->Draw();
   
   TF1 *Dijet2017ScanbgDeep1b850_bkg_unbin2 = new TF1("*Dijet2017ScanbgDeep1b850_bkg_unbin",1246,7866,1);
    //The original function :  had originally been created by:
    //TF1 *Dijet2017ScanbgDeep1b850_bkg_unbin = new TF1("Dijet2017ScanbgDeep1b850_bkg_unbin",,1246,7866,1);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetRange(1246,7866);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetName("Dijet2017ScanbgDeep1b850_bkg_unbin");
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetTitle("");
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(0,0.0029904);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(1,0.003156216);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(2,0.002905739);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(3,0.002386036);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(4,0.001780217);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(5,0.001225687);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(6,0.0007889887);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(7,0.0004801259);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(8,0.0002788232);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(9,0.0001557756);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(10,8.431061e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(11,4.447154e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(12,2.298036e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(13,1.168612e-05);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(14,5.871338e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(15,2.924547e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(16,1.448615e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(17,7.154532e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(18,3.531574e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(19,1.745907e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(20,8.660535e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(21,4.317719e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(22,2.166645e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(23,1.095757e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(24,5.591696e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(25,2.882254e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(26,1.502072e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(27,7.921161e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(28,4.23019e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(29,2.289313e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(30,1.256314e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(31,6.994985e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(32,3.953637e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(33,2.269522e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(34,1.323696e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(35,7.847497e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(36,4.730668e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(37,2.900744e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(38,1.809789e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(39,1.149224e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(40,7.429478e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(41,4.891016e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(42,3.27968e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(43,2.240547e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(44,1.559769e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(45,1.106725e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(46,8.005304e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(47,5.904147e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(48,4.440763e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(49,3.406882e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(50,2.666439e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(51,2.129394e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(52,1.735418e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(53,1.443608e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(54,1.225927e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(55,1.062974e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(56,9.41232e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(57,8.512574e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(58,7.864836e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(59,7.424354e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(60,7.162171e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(61,7.061974e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(62,7.118408e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(63,7.336634e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(64,7.733068e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(65,8.337464e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(66,9.196696e-15);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(67,1.038094e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(68,1.199339e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(69,1.418551e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(70,1.718089e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(71,2.131312e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(72,2.708672e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(73,3.527637e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(74,4.709166e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(75,6.445477e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(76,9.047734e-14);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(77,1.302943e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(78,1.925499e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(79,2.920991e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(80,4.550175e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(81,7.280875e-13);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(82,1.197152e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(83,2.023409e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(84,3.516827e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(85,6.288135e-12);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(86,1.157107e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(87,2.19225e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(88,4.278217e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(89,8.603806e-11);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(90,1.783939e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(91,3.815451e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(92,8.421933e-10);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(93,1.919597e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(94,4.520458e-09);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(95,1.100476e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(96,2.771193e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(97,7.222932e-08);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(98,1.949868e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(99,5.455538e-07);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(100,1.583141e-06);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(101,1246);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetSavedPoint(102,7866);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetFillColor(19);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetFillStyle(0);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetLineColor(2);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetLineWidth(2);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetXaxis()->SetLabelFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetXaxis()->SetLabelSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetXaxis()->SetTitleSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetXaxis()->SetTitleFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetYaxis()->SetLabelFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetYaxis()->SetLabelSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetYaxis()->SetTitleSize(0.035);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->GetYaxis()->SetTitleFont(42);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetParameter(0,7.287582e-122);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetParError(0,0);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->SetParLimits(0,0,0);
   Dijet2017ScanbgDeep1b850_bkg_unbin2->Draw("csame");
   
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
   0.00878879,
   0,
   0.002983413,
   0,
   0.001063995,
   0,
   0.0003966841,
   0.0001631633,
   0,
   5.96827e-05,
   0,
   2.960822e-05,
   1.196172e-05,
   0,
   5.927933e-06,
   1.856129e-06,
   1.794258e-06,
   5.78793e-07,
   0,
   0,
   0,
   0,
   1.638592e-07,
   1.594896e-07,
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
   5.480674e-05,
   0,
   3.084889e-05,
   0,
   1.783716e-05,
   0,
   1.050373e-05,
   6.620911e-06,
   0,
   3.874154e-06,
   0,
   2.644748e-06,
   1.6379e-06,
   0,
   1.113565e-06,
   6.070597e-07,
   5.868244e-07,
   3.150036e-07,
   0,
   0,
   0,
   0,
   1.355529e-07,
   1.319382e-07,
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
   5.514958e-05,
   6.117274e-07,
   3.116953e-05,
   5.720048e-07,
   1.813872e-05,
   5.306551e-07,
   1.07856e-05,
   6.895183e-06,
   4.787432e-07,
   4.134179e-06,
   4.448926e-07,
   2.892235e-06,
   1.879139e-06,
   4.078183e-07,
   1.34534e-06,
   8.476915e-07,
   8.194351e-07,
   5.630194e-07,
   3.440967e-07,
   3.336695e-07,
   3.214918e-07,
   3.101716e-07,
   3.768057e-07,
   3.667575e-07,
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
   grae->SetTitle("pass_1DeepCSV0.85");
   grae->SetMarkerStyle(20);
   grae->SetMarkerSize(0);
   
   TH1F *Graph_g_data_clone3001 = new TH1F("Graph_g_data_clone3001","pass_1DeepCSV0.85",100,584,8528);
   Graph_g_data_clone3001->SetMinimum(9.728334e-06);
   Graph_g_data_clone3001->SetMaximum(0.009728334);
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
   0.00878879,
   99999,
   0.002983413,
   99999,
   0.001063995,
   99999,
   0.0003966841,
   0.0001631633,
   99999,
   5.96827e-05,
   99999,
   2.960822e-05,
   1.196172e-05,
   99999,
   5.927933e-06,
   1.856129e-06,
   1.794258e-06,
   5.78793e-07,
   99999,
   99999,
   99999,
   99999,
   1.638592e-07,
   1.594896e-07,
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
   5.480674e-05,
   0,
   3.084889e-05,
   0,
   1.783716e-05,
   0,
   1.050373e-05,
   6.620911e-06,
   0,
   3.874154e-06,
   0,
   2.644748e-06,
   1.6379e-06,
   0,
   1.113565e-06,
   6.070597e-07,
   5.868244e-07,
   3.150036e-07,
   0,
   0,
   0,
   0,
   1.355529e-07,
   1.319382e-07,
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
   5.514958e-05,
   6.117274e-07,
   3.116953e-05,
   5.720048e-07,
   1.813872e-05,
   5.306551e-07,
   1.07856e-05,
   6.895183e-06,
   4.787432e-07,
   4.134179e-06,
   4.448926e-07,
   2.892235e-06,
   1.879139e-06,
   4.078183e-07,
   1.34534e-06,
   8.476915e-07,
   8.194351e-07,
   5.630194e-07,
   3.440967e-07,
   3.336695e-07,
   3.214918e-07,
   3.101716e-07,
   3.768057e-07,
   3.667575e-07,
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
   grae->SetTitle("pass_1DeepCSV0.85");
   grae->SetMarkerStyle(20);
   grae->SetMarkerSize(0.9);
   
   TH1F *Graph_Graph_from_data_obs_rebin3002 = new TH1F("Graph_Graph_from_data_obs_rebin3002","pass_1DeepCSV0.85",100,584,8528);
   Graph_Graph_from_data_obs_rebin3002->SetMinimum(2.47963e-08);
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
   h_fit_residual_vs_mass2->SetBinContent(1,-4733.307);
   h_fit_residual_vs_mass2->SetBinContent(2,104.7334);
   h_fit_residual_vs_mass2->SetBinContent(3,-4249.147);
   h_fit_residual_vs_mass2->SetBinContent(4,33.54882);
   h_fit_residual_vs_mass2->SetBinContent(5,-2268.564);
   h_fit_residual_vs_mass2->SetBinContent(6,16.15946);
   h_fit_residual_vs_mass2->SetBinContent(7,-789.1872);
   h_fit_residual_vs_mass2->SetBinContent(8,18.16335);
   h_fit_residual_vs_mass2->SetBinContent(9,10.59679);
   h_fit_residual_vs_mass2->SetBinContent(10,-81.32098);
   h_fit_residual_vs_mass2->SetBinContent(11,11.47248);
   h_fit_residual_vs_mass2->SetBinContent(12,-12.58548);
   h_fit_residual_vs_mass2->SetBinContent(13,10.45642);
   h_fit_residual_vs_mass2->SetBinContent(14,6.904819);
   h_fit_residual_vs_mass2->SetBinContent(15,-0.5125536);
   h_fit_residual_vs_mass2->SetBinContent(16,5.264815);
   h_fit_residual_vs_mass2->SetBinContent(17,3.024981);
   h_fit_residual_vs_mass2->SetBinContent(18,3.047458);
   h_fit_residual_vs_mass2->SetBinContent(19,1.83181);
   h_fit_residual_vs_mass2->SetBinContent(20,-0.00152905);
   h_fit_residual_vs_mass2->SetBinContent(21,-0.0004746462);
   h_fit_residual_vs_mass2->SetBinContent(22,-0.00015077);
   h_fit_residual_vs_mass2->SetBinContent(23,-4.889395e-05);
   h_fit_residual_vs_mass2->SetBinContent(24,1.208785);
   h_fit_residual_vs_mass2->SetBinContent(25,1.208808);
   h_fit_residual_vs_mass2->SetBinContent(26,-2.158795e-06);
   h_fit_residual_vs_mass2->SetBinContent(27,-8.614209e-07);
   h_fit_residual_vs_mass2->SetBinContent(28,-3.730897e-07);
   h_fit_residual_vs_mass2->SetBinContent(29,-1.785867e-07);
   h_fit_residual_vs_mass2->SetBinContent(30,-9.479527e-08);
   h_fit_residual_vs_mass2->SetBinContent(31,-5.743283e-08);
   h_fit_residual_vs_mass2->SetBinContent(32,-4.015396e-08);
   h_fit_residual_vs_mass2->SetBinContent(33,-3.306937e-08);
   h_fit_residual_vs_mass2->SetBinContent(34,-3.297153e-08);
   h_fit_residual_vs_mass2->SetBinContent(35,-4.041706e-08);
   h_fit_residual_vs_mass2->SetBinContent(36,-6.28901e-08);
   h_fit_residual_vs_mass2->SetBinContent(37,-1.296142e-07);
   h_fit_residual_vs_mass2->SetBinContent(38,-3.624701e-07);
   h_fit_residual_vs_mass2->SetBinContent(39,-1.437733e-06);
   h_fit_residual_vs_mass2->SetBinContent(40,-8.548462e-06);
   h_fit_residual_vs_mass2->SetBinContent(41,-8.048931e-05);
   h_fit_residual_vs_mass2->SetBinContent(42,-0.001281785);
   h_fit_residual_vs_mass2->SetBinContent(43,-0.03778597);
   h_fit_residual_vs_mass2->SetBinContent(44,-2.231997);
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
