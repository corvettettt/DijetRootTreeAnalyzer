import sys, os
from argparse import ArgumentParser
from array import array
import numpy as np


# class storing input shape info
class ShapeStorage:
    def __init__(self, shapes, binxcenters):
        self.shapes = shapes
        self.binxcenters = binxcenters

        if len(self.shapes) < 2:
           print "** ERROR: ** Need at least 2 input shapes, %i provided. Aborting."%(len(self.shapes))
           sys.exit(1)
        nbins = []
        nbins.append(len(self.binxcenters))
        for key in self.shapes.keys():
            norm = sum(self.shapes[key])
            if abs(norm - 1.) > 0.01:
                print "** ERROR: ** Input shape for m =", key, "GeV not normalized. Make sure the input shapes are normalized to unity. Aborting."
                sys.exit(3)
            nbins.append(len(self.shapes[key]))
        if len(set(nbins)) > 1:
           print "** ERROR: ** Numbers of bins for different input shapes and the number of bin centers are not all identical. Aborting."
           sys.exit(2)


def LineShapePDF(shapes, mass, histo):
    # import ROOT
    from ROOT import Math

    x = shapes.binxcenters
    y = np.array([])
    if mass in shapes.shapes.keys():
        y = np.array(shapes.shapes[mass])
    else:
        input_masses = shapes.shapes.keys()
        min_mass = min(input_masses)
        max_mass = max(input_masses)
        ml = mass
        yl = np.array([])
        mh = mass
        yh = np.array([])
        if mass < min_mass:
            print "** WARNING: ** Attempting to extrapolate below the lowest input mass. The extrapolated shape(s) might not be reliable."
            m_temp = input_masses
            m_temp.sort()
            ml = m_temp[0]
            mh = m_temp[1]
        elif mass > max_mass:
            print "** WARNING: ** Attempting to extrapolate above the highest input mass. The extrapolated shape(s) might not be reliable."
            m_temp = input_masses
            m_temp.sort(reverse=True)
            ml = m_temp[1]
            mh = m_temp[0]
        else:
            ml = max([ m for m in input_masses if m<mass ])
            mh = min([ m for m in input_masses if m>mass ])

        yl = np.array(shapes.shapes[ml])
        yh = np.array(shapes.shapes[mh])

        y = ((yh - yl)/float(mh-ml))*float(mass - ml) + yl

    # define interpolator
    interpolator = Math.Interpolator(len(x))
    interpolator.SetData(len(x), array('d',x), array('d',y.tolist()))

    for i in range(1, histo.GetNbinsX()+1):
        xcenter = histo.GetBinCenter(i)/float(mass)
        if xcenter > shapes.binxcenters[0] and xcenter < shapes.binxcenters[-1]:

            xlow = histo.GetXaxis().GetBinLowEdge(i)/float(mass)
            if xlow < shapes.binxcenters[0]: xlow = shapes.binxcenters[0]
            xhigh = histo.GetXaxis().GetBinUpEdge(i)/float(mass)
            if xhigh > shapes.binxcenters[-1]: xhigh = shapes.binxcenters[-1]

            integral = interpolator.Integ(xlow, xhigh)
            histo.SetBinContent( i, (integral if integral >= 0. else 0.) )
        else:
            histo.SetBinContent(i, 0.)

    histo.Scale( 1./histo.Integral() )


def main():
    # usage description
    usage = "Example: ./getResonanceShapes.py -i inputs/input_shapes_qq_13TeV_PU20_Phys14.py -f qq --massrange 400 10000 100 -o ResonanceShapes_qq_13TeV_PU20_Phys14.root"

    # input parameters
    parser = ArgumentParser(description='Resonance shape interpolation code based on vertical template morphing',epilog=usage)

    parser.add_argument("-i", "--input_shapes", dest="input_shapes", required=True,
                        help="Input shapes",
                        metavar="INPUT_SHAPES")

    parser.add_argument("-o", "--output_file", dest="output_file", required=True,
                        help="Output ROOT file",
                        metavar="OUTPUT_FILE")

    parser.add_argument("-f", "--final_state", dest="final_state", required=True,
                        help="Final state (e.g. qq, qg, gg)",
                        metavar="FINAL_STATE")

    parser.add_argument("--fineBinning", dest="fineBinning", default=False, action="store_true", help="Use fine, 1-GeV binning")

    parser.add_argument("--storePDF", dest="storePDF", default=False, action="store_true", help="Also store a 1-GeV-binned PDF")

    parser.add_argument("--storeCDF", dest="storeCDF", default=False, action="store_true", help="Also store a 1-GeV-binned CDF")

    mass_group = parser.add_mutually_exclusive_group(required=True)
    mass_group.add_argument("--mass",
                            type=int,
                            nargs = '*',
                            default = 1000,
                            help="Mass can be specified as a single value or a whitespace separated list (default: %(default)s)"
                            )
    mass_group.add_argument("--massrange",
                            type=int,
                            nargs = 3,
                            help="Define a range of masses to be produced. Format: min max step",
                            metavar = ('MIN', 'MAX', 'STEP')
                            )
    mass_group.add_argument("--masslist",
                            help = "List containing mass information"
                            )

    args = parser.parse_args()

    # import ROOT
    from ROOT import TFile, TH1D

    # input shapes
    sys.path.insert(0, os.path.dirname(args.input_shapes))

    input_shapes = __import__(os.path.basename(args.input_shapes).replace(".py",""))

    # standard dijet mass binning
    binBoundaries = [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325,
        354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687,
        1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509,
        4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 
        10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000]

    # initialize shape storage
    shapes = ShapeStorage(input_shapes.shapes,input_shapes.binxcenters)

    # mass points for which resonance shapes will be produced
    masses = []

    if args.massrange != None:
        MIN, MAX, STEP = args.massrange
        masses = range(MIN, MAX+STEP, STEP)
    elif args.masslist != None:
        # A mass list was provided
        print  "Will create mass list according to", args.massdict
        masslist = __import__(args.masslist.replace(".py",""))
        masses = masslist.masses
    else:
        masses = args.mass

    # sort masses
    masses.sort()

    # output ROOT file
    output = TFile(args.output_file,"RECREATE")

    for mass in masses:

       print "Producing %s shape for m = %i GeV"%(args.final_state, int(mass))

       histname = "h_" + args.final_state + "_" + str(int(mass))

       h_shape = ( TH1D(histname, args.final_state + " Resonance Shape", 14000, 0, 14000) if args.fineBinning else TH1D(histname, args.final_state + " Resonance Shape", len(binBoundaries)-1, array('d',binBoundaries)) )
       h_shape.SetXTitle("Dijet Mass [GeV]")
       h_shape.SetYTitle("Probability")

       # interpolate resonance shape
       LineShapePDF(shapes, mass, h_shape);

       output.cd()
       h_shape.Write()

       if args.storePDF or args.storeCDF:

           h_pdf = TH1D(histname + "_pdf", args.final_state + " Resonance Shape PDF", 14000, 0, 14000)
           h_cdf = TH1D(histname + "_cdf", args.final_state + " Resonance Shape CDF", 14000, 0, 14000)

           for i in range(1,h_shape.GetNbinsX()+1):

               bin_min = h_pdf.GetXaxis().FindBin(h_shape.GetXaxis().GetBinLowEdge(i)+0.5)
               bin_max = h_pdf.GetXaxis().FindBin(h_shape.GetXaxis().GetBinUpEdge(i)-0.5)
               bin_content = h_shape.GetBinContent(i)/float(bin_max-bin_min+1)
               for b in range(bin_min,bin_max+1):
                  h_pdf.SetBinContent(b, bin_content);

           for i in range(1,h_cdf.GetNbinsX()+1):

               bin_min = h_pdf.GetXaxis().FindBin(h_cdf.GetXaxis().GetBinLowEdge(i)+0.5)
               bin_max = h_pdf.GetXaxis().FindBin(h_cdf.GetXaxis().GetBinUpEdge(i)-0.5)

               curr = 0.;
               for b in range(bin_min,bin_max+1):
                  curr = curr + h_pdf.GetBinContent(b)

               prev = h_cdf.GetBinContent(i-1)
               h_cdf.SetBinContent(i, prev+curr)

           output.cd()
           if args.storePDF: h_pdf.Write()
           if args.storeCDF: h_cdf.Write()

    output.Close()


if __name__ == '__main__':
    main()
