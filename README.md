# ykpylib

usage
```python
import sys
sys.path.append('C:')
import ykpylib
```

for utility functions
```python
from ykpylib import ykfunc_util as ykutil

dirlist = ykutil.list_dir(parentfolder, fullpath=False)
filelist = ykutil.list_file(parentfolder, fullpath=False)
filelist_pkl = get_files_with_extension(directory, 'pkl', fullpath=True)
```

for fig_io
```python
import sys
sys.path.append('C:')
from ykpylib import figio_recent as ykfigio

# save fig
ykfigio.savefig(fig, filepath)

# if you want to add png file
ykfigio.savefig(fig, filepath, png=True)
```