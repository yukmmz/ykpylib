import matplotlib.pyplot as plt
import figio_recent


if __name__ == "__main__":
    while True:
        try:
            filepaths = input("Enter the pklfile paths(seperated by '.pkl', break='b'): ")
            ## remove quotes, 
            # separete by '.pkl', 
            # add '.pkl' back,
            # then strip
            filepaths = filepaths.replace('"', '').replace("'", "")
            if filepaths=='b':
                break
            filepaths_list = []
            for path in filepaths.split('.pkl'):
                if path.replace(" ", "") == "": continue
                path_tmp = path + '.pkl'
                filepaths_list.append(path_tmp.strip())
            # print(filepaths_list)

            figio_recent.openfig(filepaths_list)
        except:
            print("Invalid input")
            continue
    ### endwhile
    print('Exiting...')
    exit()
# ### endif