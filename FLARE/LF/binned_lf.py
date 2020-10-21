import numpy as np
import _pickle as pickle


class FLARES:

    def __init__(self):

        self.redshifts = np.array([5, 6, 7, 8, 9, 10])

        self.lf = {}
        self.lf['5'] = {'phi': [3.620468195471388e-08, 2.857120552379321e-07, 2.046608834527175e-06, 5.53929338228336e-06, 2.7401008809513548e-05, 6.272360452552339e-05, 0.00017756620792915514, 0.0004327706862701175, 0.0007126825098276741, 0.0010305879437519387, 0.001568502977675391, 0.0026112031222290206, 0.0045186457673592325, 0.007740658554210471, 0.011184527721477534], 'M': [-24.286142309855535, -23.786142309855535, -23.286142309855535, -22.786142309855535, -22.286142309855535, -21.786142309855535, -21.286142309855535, -20.786142309855535, -20.286142309855535, -19.786142309855535, -19.286142309855535, -18.786142309855535, -18.286142309855535, -17.786142309855535, -17.286142309855535], 'phi_err': [3.620468195471388e-08, 1.2346926197602796e-07, 1.5926026359505716e-06, 3.388524470156581e-06, 6.6900303454425076e-06, 1.1860962193596337e-05, 2.034970300298602e-05, 3.3127238192293414e-05, 4.3831447356132404e-05, 5.338919285545716e-05, 6.576826196035635e-05, 8.678837393827104e-05, 0.00011575718844842964, 0.00015225564493553394, 0.00018371957442209097]}
        self.lf['6'] = {'phi': [1.4729101132473125e-09, 4.0280903688079996e-07, 1.1833280146762812e-06, 9.026692848798519e-06, 3.889398828272041e-05, 9.691149617032777e-05, 0.00020189037216663356, 0.00034985696807461093, 0.0005488383575773444, 0.0010199965889171837, 0.0018102835679238937, 0.0036342954003872052, 0.006577820074276803, 0.009263650016115456, 0.0], 'M': [-23.761781090671015, -23.261781090671015, -22.761781090671015, -22.261781090671015, -21.761781090671015, -21.261781090671015, -20.761781090671015, -20.261781090671015, -19.761781090671015, -19.261781090671015, -18.761781090671015, -18.261781090671015, -17.761781090671015, -17.261781090671015, 0.0], 'phi_err': [1.4729101132473125e-09, 1.350677215402677e-07, 3.2370213324899135e-07, 2.528572254086125e-06, 8.608838843013251e-06, 1.5047008161368908e-05, 2.216821382924623e-05, 3.0210952540229724e-05, 3.766438446288881e-05, 5.379962510581388e-05, 7.205850471378194e-05, 0.0001028479836308859, 0.00014002692627275356, 0.00016650517736917082, 0.0]}
        self.lf['7'] = {'phi': [1.4729101132473125e-09, 1.29520180795474e-07, 9.022777062224307e-07, 4.673002356287154e-06, 2.3308003824389096e-05, 5.353720462640789e-05, 0.00011778541153838644, 0.00017096829006718243, 0.000367228262717374, 0.0006186072493266464, 0.0014181850898333955, 0.0034528785925367475, 0.005973471134963298, 0.0, 0.0], 'M': [-23.653975807394193, -23.153975807394193, -22.653975807394193, -22.153975807394193, -21.653975807394193, -21.153975807394193, -20.653975807394193, -20.153975807394193, -19.653975807394193, -19.153975807394193, -18.653975807394193, -18.153975807394193, -17.653975807394193, 0.0, 0.0], 'phi_err': [1.4729101132473125e-09, 8.008574774597257e-08, 3.0241522519707775e-07, 2.21593201532447e-06, 6.31989752071229e-06, 1.1574986974116211e-05, 1.660582688569287e-05, 2.039105122929629e-05, 3.162940562580706e-05, 4.019936940670222e-05, 6.252751314453621e-05, 0.0001001201736512684, 0.00013337464708746324, 0.0, 0.0]}
        self.lf['8'] = {'phi': [2.4069888598234e-08, 2.4293115728508355e-06, 1.7057424380004619e-06, 1.674789081912114e-05, 4.410573988725429e-05, 6.811205175613707e-05, 0.00011233102812873372, 0.00025984681924142637, 0.0006152088238863431, 0.001729010410562952, 0.0032976459326967676, 0.0, 0.0, 0.0, 0.0], 'M': [-22.887763794658635, -22.387763794658635, -21.887763794658635, -21.387763794658635, -20.887763794658635, -20.387763794658635, -19.887763794658635, -19.387763794658635, -18.887763794658635, -18.387763794658635, -17.887763794658635, 0.0, 0.0, 0.0, 0.0], 'phi_err': [2.4069888598234e-08, 1.5447030625324611e-06, 3.27839679311575e-07, 4.844808815724934e-06, 1.001761341055366e-05, 1.3425062446373348e-05, 1.724401840392697e-05, 2.6169132242482464e-05, 4.080320630107854e-05, 7.001566337071135e-05, 9.737906201740513e-05, 0.0, 0.0, 0.0, 0.0]}
        self.lf['9'] = {'phi': [1.5885828000048055e-07, 2.2788842571812913e-07, 2.8516515497422483e-06, 1.0976928558176787e-05, 2.9947990941272008e-05, 4.157428131292781e-05, 9.207229731909747e-05, 0.00020370034318117553, 0.0007095382816533016, 0.0018445478677445043, 0.003027669236875887, 0.0, 0.0, 0.0, 0.0], 'M': [-22.663648947363704, -22.163648947363704, -21.663648947363704, -21.163648947363704, -20.663648947363704, -20.163648947363704, -19.663648947363704, -19.163648947363704, -18.663648947363704, -18.163648947363704, -17.663648947363704, 0.0, 0.0, 0.0, 0.0], 'phi_err': [7.577938646893449e-08, 9.895695485122014e-08, 1.6238193128457156e-06, 4.143452438688053e-06, 8.79625466438686e-06, 9.92758849796868e-06, 1.5200635747156532e-05, 2.311637621284521e-05, 4.445044707848251e-05, 7.293108007501019e-05, 9.361992703283698e-05, 0.0, 0.0, 0.0, 0.0]}
        self.lf['10'] = {'phi': [2.4069888598234e-08, 4.502735471560751e-08, 2.074735921536794e-06, 8.170393718694847e-06, 9.697290227349253e-06, 1.250642371540935e-05, 5.988469659720102e-05, 0.0001795505983517714, 0.0005371495465119032, 0.0014657256844422192, 0.0, 0.0, 0.0, 0.0, 0.0], 'M': [-22.563036026095624, -22.063036026095624, -21.563036026095624, -21.063036026095624, -20.563036026095624, -20.063036026095624, -19.563036026095624, -19.063036026095624, -18.563036026095624, -18.063036026095624, 0.0, 0.0, 0.0, 0.0, 0.0], 'phi_err': [2.4069888598234e-08, 3.1915120604382086e-08, 1.538415631507385e-06, 4.224497470269563e-06, 3.6922780972283527e-06, 4.230924449756136e-06, 1.2370450443764489e-05, 2.1666117751306236e-05, 3.8477679849838193e-05, 6.39711242966861e-05, 0.0, 0.0, 0.0, 0.0, 0.0]}
