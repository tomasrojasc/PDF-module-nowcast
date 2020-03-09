from modules.utils import UTDF_dict_from_df
import pickle

answer = input('do you have the file ./data/dicts_of_utdf.pickle? [y/n]: \n')
if answer == 'n':

    with open('data/UTdf.all_days', 'rb') as f:
        dicts_of_utdf = UTDF_dict_from_df(pickle.load(f))
    f.close()

    with open('data/dicts_of_utdf.pickle', 'wb') as f:
        pickle.dump(dicts_of_utdf, f)
    f.close()
import scripts.filtering
import scripts.making_dicts
import scripts.make_pdf
import scripts.merge4
print('done')