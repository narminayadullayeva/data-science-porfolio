def sample_size(mean,std, delta, n_pop = None):
    """
    Calculates sample size for Type I error threshold (a) at 0.05, and 
    Type II error threshold (b) at 0.2.
    If n_pop other than None, finite population correction is applied.
    """
    
    s_s = (2*((1.96+0.8416)**2)*(std**2)) / ((mean*delta)**2)
    
    if n_pop !=None:
        s_s = (s_s*n_pop) / (s_s + n_pop - 1)
        
    return s_s