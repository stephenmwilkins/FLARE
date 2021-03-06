import numpy as np
import _pickle as pickle


class FLARES:

    def __init__(self):

        self.redshifts = np.array([5, 6, 7, 8, 9, 10])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'FLARES, Vijayan+2020'
        lf['ArXiv'] = 'https://arxiv.org/abs/2008.06057'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2020arXiv200806057V/abstract'
        lf['both_err'] = False
        lf['log_err'] = False
        lf['LF']['5'] = {'phi': [3.620468195471388e-08, 2.857120552379321e-07, 2.046608834527175e-06, 5.53929338228336e-06, 2.7401008809513548e-05, 6.272360452552339e-05, 0.00017756620792915514, 0.0004327706862701175, 0.0007126825098276741, 0.0010305879437519387, 0.001568502977675391, 0.0026112031222290206, 0.0045186457673592325, 0.007740658554210471, 0.011184527721477534], 'M': [-24.286142309855535, -23.786142309855535, -23.286142309855535, -22.786142309855535, -22.286142309855535, -21.786142309855535, -21.286142309855535, -20.786142309855535, -20.286142309855535, -19.786142309855535, -19.286142309855535, -18.786142309855535, -18.286142309855535, -17.786142309855535, -17.286142309855535], 'phi_err': [3.620468195471388e-08, 1.2346926197602796e-07, 1.5926026359505716e-06, 3.388524470156581e-06, 6.6900303454425076e-06, 1.1860962193596337e-05, 2.034970300298602e-05, 3.3127238192293414e-05, 4.3831447356132404e-05, 5.338919285545716e-05, 6.576826196035635e-05, 8.678837393827104e-05, 0.00011575718844842964, 0.00015225564493553394, 0.00018371957442209097], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['6'] = {'phi': [1.4729101132473125e-09, 4.0280903688079996e-07, 1.1833280146762812e-06, 9.026692848798519e-06, 3.889398828272041e-05, 9.691149617032777e-05, 0.00020189037216663356, 0.00034985696807461093, 0.0005488383575773444, 0.0010199965889171837, 0.0018102835679238937, 0.0036342954003872052, 0.006577820074276803, 0.009263650016115456, 0.0], 'M': [-23.761781090671015, -23.261781090671015, -22.761781090671015, -22.261781090671015, -21.761781090671015, -21.261781090671015, -20.761781090671015, -20.261781090671015, -19.761781090671015, -19.261781090671015, -18.761781090671015, -18.261781090671015, -17.761781090671015, -17.261781090671015, 0.0], 'phi_err': [1.4729101132473125e-09, 1.350677215402677e-07, 3.2370213324899135e-07, 2.528572254086125e-06, 8.608838843013251e-06, 1.5047008161368908e-05, 2.216821382924623e-05, 3.0210952540229724e-05, 3.766438446288881e-05, 5.379962510581388e-05, 7.205850471378194e-05, 0.0001028479836308859, 0.00014002692627275356, 0.00016650517736917082, 0.0], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['7'] = {'phi': [1.4729101132473125e-09, 1.29520180795474e-07, 9.022777062224307e-07, 4.673002356287154e-06, 2.3308003824389096e-05, 5.353720462640789e-05, 0.00011778541153838644, 0.00017096829006718243, 0.000367228262717374, 0.0006186072493266464, 0.0014181850898333955, 0.0034528785925367475, 0.005973471134963298, 0.0, 0.0], 'M': [-23.653975807394193, -23.153975807394193, -22.653975807394193, -22.153975807394193, -21.653975807394193, -21.153975807394193, -20.653975807394193, -20.153975807394193, -19.653975807394193, -19.153975807394193, -18.653975807394193, -18.153975807394193, -17.653975807394193, 0.0, 0.0], 'phi_err': [1.4729101132473125e-09, 8.008574774597257e-08, 3.0241522519707775e-07, 2.21593201532447e-06, 6.31989752071229e-06, 1.1574986974116211e-05, 1.660582688569287e-05, 2.039105122929629e-05, 3.162940562580706e-05, 4.019936940670222e-05, 6.252751314453621e-05, 0.0001001201736512684, 0.00013337464708746324, 0.0, 0.0], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['8'] = {'phi': [2.4069888598234e-08, 2.4293115728508355e-06, 1.7057424380004619e-06, 1.674789081912114e-05, 4.410573988725429e-05, 6.811205175613707e-05, 0.00011233102812873372, 0.00025984681924142637, 0.0006152088238863431, 0.001729010410562952, 0.0032976459326967676, 0.0, 0.0, 0.0, 0.0], 'M': [-22.887763794658635, -22.387763794658635, -21.887763794658635, -21.387763794658635, -20.887763794658635, -20.387763794658635, -19.887763794658635, -19.387763794658635, -18.887763794658635, -18.387763794658635, -17.887763794658635, 0.0, 0.0, 0.0, 0.0], 'phi_err': [2.4069888598234e-08, 1.5447030625324611e-06, 3.27839679311575e-07, 4.844808815724934e-06, 1.001761341055366e-05, 1.3425062446373348e-05, 1.724401840392697e-05, 2.6169132242482464e-05, 4.080320630107854e-05, 7.001566337071135e-05, 9.737906201740513e-05, 0.0, 0.0, 0.0, 0.0], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['9'] = {'phi': [1.5885828000048055e-07, 2.2788842571812913e-07, 2.8516515497422483e-06, 1.0976928558176787e-05, 2.9947990941272008e-05, 4.157428131292781e-05, 9.207229731909747e-05, 0.00020370034318117553, 0.0007095382816533016, 0.0018445478677445043, 0.003027669236875887, 0.0, 0.0, 0.0, 0.0], 'M': [-22.663648947363704, -22.163648947363704, -21.663648947363704, -21.163648947363704, -20.663648947363704, -20.163648947363704, -19.663648947363704, -19.163648947363704, -18.663648947363704, -18.163648947363704, -17.663648947363704, 0.0, 0.0, 0.0, 0.0], 'phi_err': [7.577938646893449e-08, 9.895695485122014e-08, 1.6238193128457156e-06, 4.143452438688053e-06, 8.79625466438686e-06, 9.92758849796868e-06, 1.5200635747156532e-05, 2.311637621284521e-05, 4.445044707848251e-05, 7.293108007501019e-05, 9.361992703283698e-05, 0.0, 0.0, 0.0, 0.0], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['10'] = {'phi': [2.4069888598234e-08, 4.502735471560751e-08, 2.074735921536794e-06, 8.170393718694847e-06, 9.697290227349253e-06, 1.250642371540935e-05, 5.988469659720102e-05, 0.0001795505983517714, 0.0005371495465119032, 0.0014657256844422192, 0.0, 0.0, 0.0, 0.0, 0.0], 'M': [-22.563036026095624, -22.063036026095624, -21.563036026095624, -21.063036026095624, -20.563036026095624, -20.063036026095624, -19.563036026095624, -19.063036026095624, -18.563036026095624, -18.063036026095624, 0.0, 0.0, 0.0, 0.0, 0.0], 'phi_err': [2.4069888598234e-08, 3.1915120604382086e-08, 1.538415631507385e-06, 4.224497470269563e-06, 3.6922780972283527e-06, 4.230924449756136e-06, 1.2370450443764489e-05, 2.1666117751306236e-05, 3.8477679849838193e-05, 6.39711242966861e-05, 0.0, 0.0, 0.0, 0.0, 0.0], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        self.lf = lf


class Finkelstein15:

    def __init__(self):

        self.redshifts = np.array([5, 6, 7, 8])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Finkelstein+2015'
        lf['ArXiv'] = 'https://arxiv.org/abs/1410.5439'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2015ApJ...810...71F/abstract'
        lf['both_err'] = True
        lf['log_err'] = False
        lf['LF']['5'] = {'phi': [0.0023e-03, 0.0082e-03, 0.0082e-03, 0.0758e-03, 0.2564e-03, 0.5181e-03, 0.9315e-03, 1.2086e-03, 2.0874e-03, 3.6886e-03, 4.7361e-03, 7.0842e-03], 'M': [-23.0, -22.5, -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5], 'phi_err': [[0.0020e-03, 0.0035e-03, 0.0036e-03, 0.0125e-03, 0.0240e-03, 0.0338e-03, 0.0482e-03, 0.0666e-03, 0.1147e-03, 0.3725e-03, 0.4413e-03, 1.1364e-03], [0.0000, 0.0050e-03, 0.0051e-03, 0.0137e-03, 0.0255e-03, 0.0365e-03, 0.0477e-03, 0.0488e-03, 0.1212e-03, 0.3864e-03, 0.4823e-03, 1.2829e-03]], 'uplim': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['6'] = {'phi': [0.0025e-03, 0.0025e-03, 0.0091e-03, 0.0338e-03, 0.0703e-03, 0.1910e-03, 0.3970e-03, 0.5858e-03, 0.8375e-03, 2.4450e-03, 3.6662e-03, 5.9126e-03], 'M': [-23.0, -22.5, -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0, -17.5], 'phi_err': [[0.0020e-03, 0.0020e-03, 0.0039e-03, 0.0085e-03, 0.0128e-03, 0.0229e-03, 0.0357e-03, 0.0437e-03, 0.0824e-03, 0.3515e-03, 0.8401e-03, 1.2338e-03], [0.0000, 0.0000, 0.0057e-03, 0.0105e-03, 0.0148e-03, 0.0249e-03, 0.0394e-03, 0.0527e-03, 0.0916e-03, 0.3887e-03, 1.0076e-03, 1.4481e-03]], 'uplim': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['7'] = {'phi': [0.0029e-03, 0.0029e-03, 0.0046e-03, 0.0187e-03, 0.0690e-03, 0.1301e-03, 0.2742e-03, 0.3848e-03, 0.5699e-03, 2.5650e-03, 3.0780e-03], 'M': [-23.0, -22.5, -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5, -18.0], 'phi_err': [[0.0020e-03, 0.0020e-03, 0.0028e-03, 0.0067e-03, 0.0144e-03, 0.0200e-03, 0.0329e-03, 0.0586e-03, 0.1817e-03, 0.7161e-03, 0.8845e-03], [0.0000, 0.0000, 0.0049e-03, 0.0085e-03, 0.0156e-03, 0.0239e-03, 0.0379e-03, 0.0633e-03, 0.2229e-03, 0.8735e-03, 1.0837e-03]], 'uplim': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['8'] = {'phi': [0.0035e-03, 0.0035e-03, 0.0035e-03, 0.0079e-03, 0.0150e-03, 0.0615e-03, 0.1097e-03, 0.2174e-03, 0.6073e-03, 1.5110e-03], 'M': [-23.0, -22.5, -22.0, -21.5, -21.0, -20.5, -20.0, -19.5, -19.0, -18.5], 'phi_err': [[0.0020e-03, 0.0020e-03, 0.0020e-03, 0.0046e-03, 0.0070e-03, 0.0165e-03, 0.0309e-03, 0.1250e-03, 0.2616e-03, 0.7718e-03], [0.0000, 0.0000, 0.0000, 0.0068e-03, 0.0094e-03, 0.0197e-03, 0.0356e-03, 0.1805e-03, 0.3501e-03, 1.0726e-03]], 'uplim': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]}

        self.lf = lf


class Atek18:

    def __init__(self):
        self.redshifts = np.array([6])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Atek+2018'
        lf['ArXiv'] = 'https://arxiv.org/abs/1412.1472v3'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2015MNRAS.450.3032M/abstract'
        lf['both_err'] = False
        lf['log_err'] = True
        lf['LF']['6'] = {'phi': [10**-4.58, 10**-4.57, 10**-4.03, 10**-3.64, 10**-3.32, 10**-3.05, 10**-2.69, 10**-2.42, 10**-2.22, 10**-1.98, 10**-1.81, 10**-1.71, 10**-1.54, 10**-1.36, 10**-1.39, 10**-1.38, 10**-1.47, 10**-1.56], 'M': [-21.86, -21.36, -20.86, -20.36, -19.86, -19.36, -18.61, -18.25, -17.75, -17.25, -16.75, -16.25, -15.75, -15.25, -14.75, -14.25, -13.75, -13.25], 'phi_err': [0.15, 0.19, 0.12, 0.09, 0.08, 0.08, 0.08, 0.09, 0.08, 0.08, 0.20, 0.15, 0.36, 0.37, 0.71, 0.53, 0.73, 1.40], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

        self.lf = lf


class Bouwens15:

    def __init__(self):
        self.redshifts = np.array([5, 6, 7, 8, 10])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Bouwens+2015'
        lf['ArXiv'] = 'https://arxiv.org/abs/1403.4295'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2015ApJ...803...34B/abstract'
        lf['both_err'] = False
        lf['log_err'] = False
        lf['LF']['5'] = {'phi': [0.000002, 0.000006, 0.000034, 0.000101, 0.000265, 0.000676, 0.001029, 0.001329, 0.002085, 0.004460, 0.008600, 0.024400], 'M': [-23.11, -22.61, -22.11, -21.61, -21.11, -20.61, -20.11, -19.61, -19.11, -18.36, -17.36, -16.36], 'phi_err': [0.000002, 0.000003, 0.000008, 0.000014, 0.000025, 0.000046, 0.000067, 0.000094, 0.000171, 0.000540, 0.001760, 0.007160], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['6'] = {'phi': [0.000002, 0.000015, 0.000053, 0.000176, 0.000320, 0.000698, 0.001246, 0.001900, 0.006680, 0.013640], 'M': [-22.52, -22.02, -21.52, -21.02, -20.52, -20.02, -19.52, -18.77, -17.77, -16.77], 'phi_err': [0.000002, 0.000006, 0.000012, 0.000025, 0.000041, 0.000083, 0.000137, 0.000320, 0.001380, 0.004200], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['7'] = {'phi': [0.000002, 0.000001, 0.000033, 0.000048, 0.000193, 0.000309, 0.000654, 0.000907, 0.001717, 0.005840, 0.008500], 'M': [-22.66, -22.16, -21.66, -21.16, -20.66, -20.16, -19.66, -19.16, -18.66, -17.91, -16.91], 'phi_err': [0.000002, 0.000006, 0.000009, 0.000015, 0.000034, 0.000061, 0.000100, 0.000177, 0.000478, 0.001460, 0.002940], 'uplim': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['8'] = {'phi': [0.000002, 0.000002, 0.000005, 0.000013, 0.000058, 0.000060, 0.000331, 0.000533, 0.001060, 0.002740], 'M': [-22.87, -22.37, -21.87, -21.37, -20.87, -20.37, -19.87, -19.37, -18.62, -17.62], 'phi_err': [0.000001, 0.000001, 0.000003, 0.000005, 0.000015, 0.000026, 0.000104, 0.000226, 0.000340, 0.001040], 'uplim': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]}
        lf['LF']['10'] = {'phi': [0.000001, 0.000001, 0.000010, 0.000049, 0.000266], 'M': [-22.23, -21.23, -20.23, -19.23, -18.23], 'phi_err': [0.0000001, 0.000001, 0.000005, 0.000005, 0.000171], 'uplim': [1, 0, 0, 1, 0]}

        self.lf = lf


class Bouwens16:

    def __init__(self):
        self.redshifts = np.array([9, 10])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Bouwens+2016'
        lf['ArXiv'] = 'https://arxiv.org/abs/1506.01035'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2016ApJ...830...67B/abstract'
        lf['both_err'] = True
        lf['log_err'] = False
        lf['LF']['9'] = {'phi': [0.0024e-03, 0.0044e-03, 0.0322e-03], 'M': [-21.94, -21.14, -20.34], 'phi_err': [[0.0010e-03, 0.0024e-03, 0.0138e-03], [0.0010e-03, 0.0042e-03, 0.0217e-03]], 'uplim': [1, 0, 0]}
        lf['LF']['10'] = {'phi': [0.0017e-03, 0.0009e-03, 0.0180e-03], 'M': [-22.05, -21.25, -20.45], 'phi_err': [[0.0010e-03, 0.0007e-03, 0.0098e-03], [0.0010e-03, 0.0021e-03, 0.0174e-03]], 'uplim': [1, 0, 0]}

        self.lf = lf


class Bouwens17:

    def __init__(self):
        self.redshifts = np.array([6])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Bouwens+2017'
        lf['ArXiv'] = 'https://arxiv.org/abs/1610.00283'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2017ApJ...843..129B/abstract'
        lf['both_err'] = True
        lf['log_err'] = False
        lf['LF']['6'] = {'phi': [0.0002, 0.0009, 0.0007, 0.0018, 0.0036, 0.0060, 0.0071, 0.0111, 0.0170], 'M': [-20.75, -20.25, -19.75, -19.25, -18.75, -18.25, -17.75, -17.25, -16.75], 'phi_err': [[0.0002, 0.0004, 0.0004, 0.0006, 0.0009, 0.0012, 0.0066, 0.0102, 0.0165], [0.0002, 0.0004, 0.0004, 0.0006, 0.0009, 0.0012, 0.0014, 0.0022, 0.0039]], 'uplim': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

        self.lf = lf


class Bowler20:

    def __init__(self):
        self.redshifts = np.array([8, 9])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Bowler+2020'
        lf['ArXiv'] = 'https://arxiv.org/abs/1911.12832'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2020MNRAS.493.2059B/abstract'
        lf['both_err'] = False          # Switch for marking where data has separate + and - errors
        lf['log_err'] = False           # Switch for marking an error on log10(phi)
        lf['LF']['8'] = {'phi': [2.95e-06, 0.58e-06, 0.14e-06], 'M': [-21.65, -22.15, -22.90], 'phi_err': [0.98e-06, 0.33e-06, 0.06e-06], 'uplim': [0, 0, 0]}
        lf['LF']['9'] = {'phi': [0.84e-06, 0.16e-06], 'M': [-21.90, -22.90], 'phi_err': [0.49e-06, 0.11e-06], 'uplim': [0, 0]}

        self.lf = lf


class McLeod15:

    def __init__(self):
        self.redshifts = np.array([9])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'McLeod+2015'
        lf['ArXiv'] = 'https://arxiv.org/abs/1412.1472'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2015MNRAS.450.3032M/abstract'
        lf['both_err'] = True           # Switch for marking where data has separate + and - errors
        lf['log_err'] = True           # Switch for marking an error on log10(phi)
        lf['LF']['9'] = {'phi': [10**-2.70, 10**-2.82, 10**-3.40, 10**-4.01], 'M': [-17.50, -18.00, -19.20, -20.20], 'phi_err': [[-2.70--2.89, -2.82--3.02, -3.40--3.66, -4.01--4.56], [-2.53--2.70, -2.65--2.82, -3.23--3.40, -3.72--4.01]], 'uplim': [0, 0, 0, 0]}

        self.lf = lf


class Oesch18:

    def __init__(self):
        self.redshifts = np.array([10])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Oesch+2018'
        lf['ArXiv'] = 'https://arxiv.org/abs/1710.11131'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2018ApJ...855..105O/abstract'
        lf['both_err'] = True           # Switch for marking where data has separate + and - errors
        lf['log_err'] = False           # Switch for marking an error on log10(phi)
        lf['LF']['10'] = {'phi': [0.0000017, 0.0000010, 0.000010, 0.0000340, 0.0001900, 0.0006300], 'M': [-22.25, -21.25, -20.25, -19.25, -18.25, -17.25], 'phi_err': [[0.0000005, 0.0000008, 0.000005, 0.0000220, 0.0001200, 0.0005200], [0.0000000, 0.0000022, 0.000010, 0.0000450, 0.0002500, 0.0014900]], 'uplim': [1, 0, 0, 0, 0, 0]}

        self.lf = lf


class Stefanon19:

    def __init__(self):
        self.redshifts = np.array([8, 9])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'Stefanon+2019'
        lf['ArXiv'] = 'https://arxiv.org/abs/1902.10713?'
        lf['ADS'] = 'https://ui.adsabs.harvard.edu/abs/2019ApJ...883...99S/abstract'
        lf['both_err'] = True           # Switch for marking where data has separate + and - errors
        lf['log_err'] = False           # Switch for marking an error on log10(phi)
        lf['LF']['8'] = {'phi': [0.76e-06, 1.38e-06, 4.87e-06], 'M': [-22.55, -22.05, -21.55], 'phi_err': [[0.41e-06, 0.66e-06, 1.41e-06], [0.74e-06, 1.09e-06, 2.01e-06]], 'uplim': [0, 0, 0]}
        lf['LF']['9'] = {'phi': [0.43e-06, 0.43e-06, 1.14e-06, 1.64e-06], 'M': [-22.35, -22.00, -21.60, -21.20], 'phi_err': [[0.36e-06, 0.36e-06, 0.73e-06, 1.06e-06], [0.99e-06, 0.98e-06, 1.50e-06, 2.16e-06]], 'uplim': [0, 0, 0, 0]}

        self.lf = lf


class template:

    def __init__(self):
        self.redshifts = np.array([5, 6, 7, 8])

        lf = {}
        lf['LF'] = {}
        lf['label'] = 'template'
        lf['ArXiv'] = ''
        lf['ADS'] = ''
        lf['both_err'] = False          # Switch for marking where data has separate + and - errors
        lf['log_err'] = False           # Switch for marking an error on log10(phi)
        lf['LF']['5'] = {'phi': [], 'M': [], 'phi_err': [], 'uplim': []}
        lf['LF']['6'] = {'phi': [], 'M': [], 'phi_err': [], 'uplim': []}
        lf['LF']['7'] = {'phi': [], 'M': [], 'phi_err': [], 'uplim': []}
        lf['LF']['8'] = {'phi': [], 'M': [], 'phi_err': [], 'uplim': []}

        self.lf = lf
