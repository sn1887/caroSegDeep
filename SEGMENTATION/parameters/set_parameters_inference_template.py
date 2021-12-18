from parameters.parameters_inference import Parameters
import os
from shutil import copyfile

# ****************************************************************
# *** HOWTO
# ****************************************************************

# 0) Do not modify this template file "setParameterstemplate.py"
# 1) Create a new copy of this file "setParametersTemplate.py" and rename it into "setParameters.py"
# 2) Indicate all the variables according to your local environment and experiment
# 3) Use your own "setParameters.py" file to run the code
# 4) Do not commit/push your own "setParameters.py" file to the collective repository, it is not relevant for other people
# 5) The untracked file "setParameters.py" is automatically copied to the tracked file "getParameters.py" for reproducibility
# ****************************************************************

def setParameters():

  p = Parameters(

                PATH_TO_SEQUENCES='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/DATA/IMAGES',                             # Path where the sequences/images are saved (.tiff, .DICOM, .MAT)
                PATH_TO_BORDERS='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/RESULTS/DATASET/BORDERS/BORDERS_UNION',     # Path where the borders are saved (.MAT)
                PATH_TO_CONTOURS='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/RESULTS/DATASET/CONTOURS',                            # Path where the contours are saved (.MAT, .txt)
                PATH_TO_CF='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/DATA/CF',
                PROCESS_FULL_SEQUENCE=False,        # Segment all the frame of the sequence or only the first one
                PATCH_HEIGHT=512,                   # The height of a patch
                PATCH_WIDTH=128,                    # The width of a patch
                OVERLAPPING=8,                      # Horizontal displacement of a patch
                DESIRED_SPATIAL_RESOLUTION=5,       # The desired spatial resolution in um
                PATH_WALL_SEGMENTATION_RES='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/RESULTS/INFERENCE',         # Path to save results
                PATH_TO_LOAD_TRAINED_MODEL_WALL='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/TRAINED_MODEL',        # Path where the trained model is saved
                MODEL_NAME_IMC='IMC_custom_dilated_unet',
                MODEL_NAME_FW='FW_custom_dilated_unet'
                USED_FAR_WALL_DETECTION_FOR_IMC=True,                                                                   # If true then the predicted far wall is used to segment the IMC
                PATH_TO_FOLDS='/home/laine/Documents/REPO/caroSegDeep/EXAMPLE/RESULTS/DATASET/DATASET/DISTRIBUTION',
      # In this directory .txt files contain the patient's name according to their belonging (train/val/test)
  )

  # --- Print all attributes in the console
  attrs = vars(p)
  print('\n'.join("%s: %s" % item for item in attrs.items()))
  print('----------------------------------------------------------------')

  # --- Save a backup of the parameters so it can be tracked on Git, without requiring to be adapted by from other contributors
  copyfile(os.path.join('parameters', os.path.basename(__file__)), os.path.join('parameters', 'get_parameters_inference.py'))

  # --- Modify the function name from "setParameters" to "getParameters"
  fid = open(os.path.join('parameters', 'get_parameters_inference.py'), 'rt')
  data = fid.read()
  data = data.replace('setParameters()', 'getParameters()')
  fid.close()
  fid = open(os.path.join('parameters', 'get_parameters.py'), 'wt')
  fid.write(data)
  fid.close()

  # --- Return populated object from Parameters class
  return p
