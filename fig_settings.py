
import matplotlib.pyplot as plt
import matplotlib as mpl

###########################
### Figure pre-settings
FS = 9
mpl.rcParams.update({
    'xtick.direction': 'in',       # 
    'ytick.direction': 'in',       # 
    'font.family': 'Times New Roman',  # Use Times New Roman font
    'font.size': FS,             #
    'axes.titlesize': FS,        # title of each axes
    'axes.labelsize': FS,        #
    'xtick.labelsize': FS,       #
    'ytick.labelsize': FS,       #
    'legend.fontsize': FS,       #
    'figure.titlesize': FS,       # title of whole figure
    'figure.dpi': 72,          # if dpi = 72, fontsize will be standard as LaTeX
})
def figsize_from_pt(width_pt, height_pt, dpi=72):
    return (width_pt / dpi, height_pt / dpi)




###########################
### Figure settings inside the script
fig = plt.figure(figsize=figsize_from_pt(200, 300))
plt.subplots_adjust(wspace=0.5, hspace=0.5) # wspace(hspace) = ratio to axis width(height)
ax = [None] * 4
for i in range(4):
    ax[i] = fig.add_subplot(2, 2, i + 1)
    ax[i].set_xlabel('Time [s]')
    ax[i].set_ylabel('Force [N]')
    ax[i].set_title(f'Plot {i + 1}')

    # *** 
    ax[i].set_xlim(0, 10)
    ax[i].set_xticks(range(0, 11, 2))
    ax[i].set_xticklabels([])
    ax[i].set_ylim(-10, 10)
    ax[i].set_yticks(range(-10, 11, 5))
    ax[i].set_yticklabels([])
    ax[i].set_box_aspect(3 / 4)
    # ***

    ax[i].grid(False)  # add grid to each subplot
plt.show()


# ###########################
# ### for example, check this out:
# axdHVM = {}
# fig = plt.figure(figsize=figsize_from_pt(200, 300))
# # fig.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)
# axdHVM['QSM_u'] = fig.add_subplot(2, 2, 1)
# axdHVM['CFD_u'] = fig.add_subplot(2, 2, 2)
# axdHVM['QSM_d'] = fig.add_subplot(2, 2, 3)
# axdHVM['CFD_d'] = fig.add_subplot(2, 2, 4)
# axdHVM['QSM_d'].set_title('QSM_d')
# axdHVM['CFD_d'].set_title('CFD_d')
# axdHVM['QSM_d'].set_xlabel('Time [s]')
# axdHVM['CFD_d'].set_xlabel('Time [s]')
# axdHVM['QSM_d'].set_ylabel('Force [N]')
# axdHVM['CFD_d'].set_ylabel('Force [N]')
# axdHVM['QSM_u'].set_title('QSM_u')
# axdHVM['CFD_u'].set_title('CFD_u')
# axdHVM['QSM_u'].set_xlabel('Time [s]')
# axdHVM['CFD_u'].set_xlabel('Time [s]')
# axdHVM['QSM_u'].set_ylabel('Force [N]')
# axdHVM['CFD_u'].set_ylabel('Force [N]')

# axdHVM['QSM_u'].set_box_aspect(3 / 4)
# axdHVM['CFD_u'].set_box_aspect(3 / 4)
# axdHVM['QSM_d'].set_box_aspect(3 / 4)
# axdHVM['CFD_d'].set_box_aspect(3 / 4)
# plt.subplots_adjust(wspace=0.5, hspace=0.5)
# plt.show()
