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
        fig.savefig(png_filepath, bbox_inches='tight')
        # fig.savefig(png_filepath)
        print(f'figure saved to {png_filepath}')
    return 1
# ### enddef openfig

def csavefig(fig, filepath_without_ext, ext='pkl', verbose=True):
    """
    customized savefig function
    Save a figure to a file with multiple formats.
    <input>
    fig: figure object to save
    filepath_without_ext: str, file path without extension
    ext: str or list of str of file extensions to save the figure as
    verbose: bool, if True, print the file paths of saved figures

    <output>
    filepathlist: list of str, file paths of saved figures
    """
    filepathlist = []
    if isinstance(ext, str):
        ext = [ext]
    else:
        ext = ext
    
    for ext_ in ext:
        if ext_.startswith('.'):
            ext_ = ext_[1:]
        filepath = filepath_without_ext + '.' + ext_

        if ext_ == 'pkl':
            if not check_mpl_version(warning=True):
                ans = input('   Do you want to continue? (y/n): ')
                if ans != 'y': return 0
            with open(filepath, "wb") as f:
                pickle.dump(fig, f, protocol=3)
            if verbose: print(f'figure saved to {filepath}')
            filepathlist.append(filepath)
        else:
            fig.savefig(filepath, format=ext_, bbox_inches='tight')
            if verbose: print(f'figure saved to {filepath}')
            filepathlist.append(filepath)
        
    return filepathlist
# ### enddef openfig
# fig.savefig("figure_output", format="svg")