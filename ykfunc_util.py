import numpy as np
import os


### get data of oscillation. 
### max,min,mean of amplitude, offset(osc. center)
### number of periods, durations of period, indices of peaks, peak values
def get_oscillation_data(x):
    dx = np.diff(x)
    # includes maxima and minima alternately
    ind_peak = np.where(dx[1:-1] * dx[0:-2] <= 0)[0] + 1 #cf.33-56
    
    
	### select one peak if peak indices exists in a row. cf.34-25
		# this does not includes...
		#	min-max, max-min in a row
    rmv_indinds = []
    d_ind_peak = np.diff(ind_peak) # check list. ind_peak(d_ind1s+1) are also peak.
    d_ind1s = np.where(d_ind_peak == 1)[0] # indices of ind_peak that will be removed.
    
    while len(d_ind1s) > 0:
        dind_1 = min(d_ind1s)
        inds_peak_inarow = [dind_1] # x(ind_peak(inds_peak_inarow)) have same peak value.
        peak_val = x[ind_peak[dind_1]]
        
        while dind_1 + 1 < len(ind_peak) and x[ind_peak[dind_1 + 1]] == peak_val:
            dind_1 += 1
            inds_peak_inarow.append(dind_1)

        ### remove peaks in a row except one of them.
		### if min-max in a row, length(inds_peak_inarow)==1, then, inds_tmp is empty.
        ind_1s_mean = round(np.mean(inds_peak_inarow))
        inds_tmp = list(set(inds_peak_inarow) - {ind_1s_mean})
        rmv_indinds.extend(inds_tmp)
        d_ind1s = list(set(d_ind1s) - set(inds_peak_inarow))
    # ### endwhile

    indinds_tmp = list(set(np.arange(len(ind_peak))) - set(rmv_indinds))
    ind_peak = np.sort(ind_peak[indinds_tmp]) # remove ind_peak in a row
    x_peak = x[ind_peak] # minima/maxima values
    n_period = len(ind_peak) // 2 # number of periods

    # calc durations of period    
    odd_indices = np.arange(1, len(ind_peak), 2)
    ind_split_period = ind_peak[odd_indices]
    dur_period = np.diff(ind_split_period)
    
    # list of oscilation amp, center
    amps = np.abs(np.diff(x_peak))
    ofss = (x_peak[:-1] + x_peak[1:]) / 2
    
    ampdata = {
        'amps': np.array(amps),
        'max': np.nanmax(amps),
        'min': np.nanmin(amps),
        'mean': np.nanmean(amps),
        'med': np.nanmedian(amps)
    }
    
    ofsdata = {
        'ofss': np.array(ofss),
        'max': np.nanmax(ofss),
        'min': np.nanmin(ofss),
        'mean': np.nanmean(ofss),
        'med': np.nanmedian(ofss)
    }
    
    oscdata = {
        'n_period': n_period,
        'dur_period': np.array(dur_period),
        'ind_peak': np.array(ind_peak),
        'x_peak': np.array(x_peak)
    }
    
    return ampdata, ofsdata, oscdata
# ### enddef get_oscillation_data

def make_dir_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created.")
        return 1
    else:
        print(f"Directory '{path}' already exists.")
        return 0
# ### enddef make_dir_if_not_exist


def list_dir(parentfolder, fullpath=False):
    """
    List all directories in the given parent folder.
    If fullpath is True, return full paths of the directories.
    """
    dirlist = []
    for folder in os.listdir(parentfolder):
        if os.path.isdir(os.path.join(parentfolder, folder)):
            if fullpath:
                dirlist.append(os.path.join(parentfolder, folder))
            else:
                dirlist.append(folder)
    return dirlist
    #     if fullpath:
    #         return [os.path.join(parentfolder, folder) for folder in os.listdir(parentfolder) if os.path.isdir(os.path.join(parentfolder, folder))]
    #     else:
    #         return [folder for folder in os.listdir(parentfolder) if os.path.isdir(os.path.join(parentfolder, folder))]
    # # ### enddef list_dir
# ### enddef list_dir


def list_file(parentfolder, fullpath=False):
    """
    List all files in the given parent folder.
    If fullpath is True, return full paths of the directories.
    """
    filelist = []
    for file in os.listdir(parentfolder):
        if os.path.isfile(os.path.join(parentfolder, file)):
            if fullpath:
                filelist.append(os.path.join(parentfolder, file))
            else:
                filelist.append(file)
    return filelist
# ### enddef list_file


def get_files_with_extension(directory, extension, fullpath=False):
    """
    Get a list of files with a specific extension in a directory.
    If fullpath is True, return full paths of the files.
    """
    extension = extension.lower()
    file_list = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and file.lower().endswith(extension):
            if fullpath:
                file_list.append(os.path.join(directory, file))
            else:
                file_list.append(file)
    return file_list
# ### enddef get_files_with_extension