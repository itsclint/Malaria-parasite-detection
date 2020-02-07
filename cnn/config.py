import os 

#initiaize the path to the original input directory of the images
orig_input_dataset = "malaria/cell_images"

#initialize the base path to the new directory that will contanin
#our images after computing the training na d test split
base_path = "malaria"

# derive the training, vaidation, and testing dirctories
train_path = os.path.sep.join([base_path, "training"])
val_path = os.path.sep.join([base_path, "validation"])
test_path = os.path.sep.join([base_path, "testing"])
# define the ammount of data thd=st will beused for the trianing
train_split = 0.8

# the ammount of validation data will be a pacentage of the 
# # trainig data 
val_split = 0.1