import pickle
import matplotlib.pyplot as plt
import matplotlib
mpl_version_intent = '3.10.1'

def check_mpl_version(warning=False):
    """
    Check if the current matplotlib version matches the intended version.
    """
    current_version = matplotlib.__version__
    if current_version != mpl_version_intent and warning:
        print(f'Warning: matplotlib version is not {mpl_version_intent} !!!')
        print('   Some features may not work as expected.')
        return False
    else:
        # print(f'matplotlib version is {current_version}, as expected.')
        return True

def openfig(filepaths_list):
    if not check_mpl_version(warning=True):
        ans = input('   Do you want to continue? (y/n): ')
        if ans != 'y': return 0
    
    if isinstance(filepaths_list, str):
        filepaths_list = [filepaths_list]
        
    fig = [None]*len(filepaths_list)
    for idx, filepath in enumerate(filepaths_list):
        if filepath.replace(" ", "") == "": continue
        with open(filepath, "rb") as f:
            fig[idx] = pickle.load(f)
    plt.show()
    plt.close('all')
# ### enddef openfig

def savefig(fig, filepath, png=False):
    """
    Save a figure to a file.
    """
    if not check_mpl_version(warning=True):
        ans = input('   Do you want to continue? (y/n): ')
        if ans != 'y': return 0
    
    if not filepath.endswith('.pkl'):
        print('   Warning: file extension is not .pkl, changing to .pkl')
        filepath = filepath + '.pkl'

    with open(filepath, "wb") as f:
        pickle.dump(fig, f, protocol=3)
    print(f'figure saved to {filepath}')

    if png:
        png_filepath = filepath.replace('.pkl', '.png')
        fig.savefig(png_filepath, dpi=300, bbox_inches='tight')
        # fig.savefig(png_filepath)
        print(f'figure saved to {png_filepath}')
    return 1
# ### enddef openfig

