#!/bin/bash


WD=/home/laine/cluster/REPOSITORIES/caroSegDeep/SEGMENTATION/
cd $WD
PYTHONPATH=$WD python run/run_IMC_segmentation.py -param set_parameters_inference_template.py
