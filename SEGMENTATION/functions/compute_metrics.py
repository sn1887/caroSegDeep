import numpy as np
from functions.evaluation import load_annotation, get_border_expert, get_narrow_borders, compute_metric_wall_MAE

def borders_pred(res):

    IFC4 = res[..., 1]
    dim = IFC4.shape[0]

    for k in range(dim):
        if IFC4[k]!=0:
            left_border = k
            break

    for k in range(IFC4.shape[0]-1,0,-1):
        if IFC4[k]!=0:
            right_border = k
            break

    return {'left_border': left_border, 'right_border': right_border}
# ----------------------------------------------------------------------------------------------------------------------

def compute_metrics(pGT, patient, expert, res, p):

    IFC3, IFC4 = load_annotation(pGT, patient.split('.')[0], expert)
    borders_expert = get_border_expert(IFC3, IFC4)
    borders_prediction = borders_pred(res)
    borders_ROI = get_narrow_borders(borders_prediction, borders_expert)
    prediction = {'IFC3': res[...,0],
                  'IFC4': res[...,1]}
    expert = {'IFC3': IFC3,
              'IFC4': IFC4}
    MAE_LI, MAE_MA, MAE_IMT = compute_metric_wall_MAE(patient.split('.')[0], prediction, expert, borders_ROI, set='', p=p)

    return MAE_IMT, MAE_LI, MAE_MA
# ----------------------------------------------------------------------------------------------------------------------