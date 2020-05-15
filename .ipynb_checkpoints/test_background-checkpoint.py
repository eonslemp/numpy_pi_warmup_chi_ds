import glob
import pickle as pkl
import numpy as np

def pkl_dump(obj_name_list): 

    '''
    obj_name_list: 
    list of tuples as (obj, obj_name)
    
    '''
    
    for pair in obj_name_list:
        obj, file_name = pair
        
        files = glob.glob("test_objects/*.pkl")
    
        existing_files = [get_file_name(file) for file in files]

        if file_name in existing_files:
            return print(f'can"t dump, {file_name} already exists')

        with open(f'test_objects/{file_name}.pkl', 'wb') as f:
            pkl.dump(obj, f)
        
    return
        
    
def pkl_load(file_name):
    with open(f'test_objects/{file_name}.pkl', 'rb') as f:
        obj = pkl.load(f)
        
    return obj
    

def get_file_name(glob_listing):
    return (glob_listing
            .split('/')[1] #get the file name
            .split('.')[0] #remove .pkl
           )

def load_test_dict():
    files = glob.glob("test_objects/*.pkl")
        
    return {get_file_name(file)
            : pkl_load(
                get_file_name(file)
            ) 
            for file in files} 
    
    
test_dict = load_test_dict()


def run_test(obj, name):
    try:
        if type(obj)==np.ndarray:
            assert np.array_equal(obj, test_dict[name])
        
        else:
            assert obj==test_dict[name]
        return 'Hey, you did it.  Good job.'
    except AssertionError:
        return 'Try again'