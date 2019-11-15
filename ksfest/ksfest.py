# Any results you write to the current directory are saved as output.

# -*- coding: utf-8 -*-

import numpy as np # linear algebra
import pandas as pd 
import itertools
from scipy.stats import ks_2samp
from tqdm import tqdm 
#import pickle


class ks_fest(object):
    def __init__(self):
        
        self.dict_ks = dict()
        self.dict_cdfs= dict()
        self.plot_scale = plot_scale
   
    def fit_curves(self, df,resolution=500,sample=0.05,var_dim):

        '''
        Fit and store all CDF curves by a variable
        df :  Pandas dataframe
        var_dim : string 
        sample: samplin portion from datafram

        '''

        #Sampling

        data=df.sample(frac=sample)
        #valores Missing
        

        if df.shape[0]<resolution:  
            resolution=df.shape[0]
        
        

        for dim in np.unique(df[var_dim]):
            dict_cdfs={}
            for col in df.columns:    
                sorted_col=np.sort(df.loc[df[var_dim]==dim, col].fillna(-1))
                n=len(sorted_col)
                bins_vector=np.linspace(start=min(sorted_col),stop=max(sorted_col),num=resolution)
                cdf= np.searchsorted(bins_vector, sorted_col)/n
                dict_cdfs[col]=cdf
            self.dict_cdfs_var_dim[dim]=dict_cdfs

        else:

            for col in df.columns:    
                    sorted_col=np.sort(df.loc[df[var_dim]==dim, col].fillna(-1))
                    n=len(sorted_col)
                    bins_vector=np.linspace(start=min(sorted_col),stop=max(sorted_col),num=resolution)
                    cdf= np.searchsorted(bins_vector, sorted_col)/n
                    self.dict_cdfs[col]=cdf



    def fit_ks(self, df,var_dim,columns, sample):
        for comb in tqdm(itertools.combinations(np.unique(df[var_dim]),2)):
            ks_list=[]
            
            if columns==None:
                columns=df.columns

            for col in [col for col in columns if col!=var_dim]:
                ks_list.append(ks_2samp(df.loc[df[var_dim]==comb[0], col].sample(frac=0.1).fillna(-1), df.loc[df[var_dim]==comb[1], col].sample(frac=0.1).fillna(-1))[0])
            self.dict_ks[str(comb[0])+'_'+str(comb[1])] = ks_list
            

            pandas_ks_=pd.DataFrame().from_dict(self.dict_ks)
            self.pandas_ks= pandas_ks_.T
            self.pandas_ks.columns=[col for col in df.columns if col!=var_dim]
            self.pandas_ks['safra']=pandas_ks.index
            self.pandas_ks.index=range(len(pandas_ks))

    #def save_cdfs(fname, self.disct_cdfs):
    #    pickle.dump(fname,'wd')
        
    #def load_cdfs(fname):
    #    with open(fname,'rd'):
    #        self.disct_cdfs=pickle.load() 
        
            
    #def check_ks(df_new,self.disct_cdfs, self.dict_ks):
        #check columns

        #Calculate new