
import itertools
from scipy.stats import ks_2samp
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from .utils import read_sample

class ks_fest(object):


    """

    Values
    ----------
    
    data : pandas.DataFrame

    """

    def __init__(self):

        self.dict_cdfs_var_dim=dict()
        self.cols=None
        self.dict_ks=dict()
    
    
    def get_ks(self,df,var_dim,columns, sample, na_number=-1, **kwargs):

        """

        Fit and save cdf to check data quality.

        Parameters
        ----------
        df: pandas dataframe or csv file
        var_dim: string 
        sample: samplin portion from datafram
        
        Attributes
        ----------
        
        
        """

        if not isinstance(df, pd.DataFrame):
            df=read_sample(df, sample_size=sample, **kwargs)


        if columns==None:
                columns=[col for col in df.columns if col!=var_dim]
        
        
        

        for comb in tqdm(itertools.combinations(np.unique(df[var_dim]),2)):
            ks_list=[]
            pvalue_list=[]

            for col in columns:
                ks_result=ks_2samp(df.loc[df[var_dim]==comb[0], col].sample(frac=sample).fillna(na_number), df.loc[df[var_dim]==comb[1], col].sample(frac=sample).fillna(na_number))[0]
                ks_list.append(ks_result[0])
                pvalue_list.append(ks_result[1])
            self.dict_ks[str(comb[0])+'_'+str(comb[1])] = ks_list
            

        pandas_ks_=pd.DataFrame().from_dict(self.dict_ks)
        self.pandas_ks= pandas_ks_.T
        self.pandas_ks.columns=columns
        self.pandas_ks[var_dim]=self.pandas_ks.index
        self.pandas_ks.index=range(len(self.pandas_ks))
        return self.pandas_ks
    
    #def save_cdfs(fname, self.disct_cdfs):
    #    pickle.dump(fname,'wd')
        
    #def load_cdfs(fname):
    #    with open(fname,'rd'):
    #        self.disct_cdfs=pickle.load() 
        
            
    #def check_ks(df_new,self.disct_cdfs, self.dict_ks):
        #check columns

        #Calculate new