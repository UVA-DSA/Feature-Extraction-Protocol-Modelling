from pymetamap import MetaMap
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
from pyDatalog import pyDatalog

# initialize
mm = MetaMap.get_instance('/Users/sileshu/Downloads/public_mm/bin/metamap16')
pyDatalog.create_terms('RH, PH, C, BR, P, BL, op, Y')

# clauses
(op[RH,PH,C,BR,P,BL] == 'Eliminate_Hazard') <= (True == RH)
(op[RH,PH,C,BR,P,BL] == 'Eliminate_Hazard') <= (False == RH) & (True == PH)
(op[RH,PH,C,BR,P,BL] == 'Secondary_Survey') <= (False == RH) & (False == PH) & \
                                            (True == C) & (False == BL)
(op[RH,PH,C,BR,P,BL] == 'Control_Bleeding') <= (False == RH) & (False == PH) & \
                                            (True == C) & (True == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Secondary_Survey') <= (False == RH) & \
                                            (False == PH) & (False == C) & (True == BR) & \
                                            (True == P) & (False == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Control_Bleeding') <= (False == RH) & \
                                            (False == PH) & (False == C) & (True == BR) & \
                                            (True == P) & (True == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_Artificial_Ventilation, Secondary_Survey') <= (False == RH) & \
                                            (False == PH) & (False == C) & (False == BR) & \
                                            (True == P) & (False == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_Artificial_Ventilation, Control_Bleeding') <= (False == RH) & \
                                            (False == PH) & (False == C) & (False == BR) & \
                                            (True == P) & (True == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_External_Cardiac_Compressions, Secondary_Survey') \
                                            <= (False == RH) & \
                                            (False == PH) & (False == C) & (True == BR) & \
                                            (False == P) & (False == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_External_Cardiac_Compressions, Control_Bleeding') \
                                            <= (False == RH) & \
                                            (False == PH) & (False == C) & (True == BR) & \
                                            (False == P) & (True == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_Artificial_Ventilation, Start_External_Cardiac_Compressions, Secondary_Survey') <= (False == RH) & \
                                            (False == PH) & (False == C) & (False == BR) & \
                                            (False == P) & (False == BL)
(op[RH,PH,C,BR,P,BL] == 'Open_the_Airway, Start_Artificial_Ventilation, Start_External_Cardiac_Compressions, Control_Bleeding') <= (False == RH) & \
                                            (False == PH) & (False == C) & (False == BR) & \
                                            (False == P) & (True == BL)

# Ground Truth
GT_1 = {'conscious':1,'breath':7,'pulse':1,'blood pressure':1,'asthma':1,'skin temperature':1,'skin moisture':1}
GT_5 = {'conscious':0,'breath':1,'pulse':1,'bleed':1,'blood pressure':1,'wound':4}
GT_7 = {'conscious':2,'breath':1,'pulse':1,'blood pressure':1}
GT_6 = {'conscious':2,'blood pressure':1,'heart diseases':1,'last visit':1}
eGT_1 = {'breath':1,'pulse':1,'asthma':1}
eGT_5 = {'pulse':1,'blood pressure':1}
eGT_7 = {'pulse':1,'blood pressure':1}
eGT_6 = {'blood pressure':1}
ex_GT1 = {'chest pain':1, 'exercising':1, 'inhaler':1, 'pulse oximetry':2, 'ecg':1, \
          'sinus':1, 'proventil':2, 'atrovent':1, 'oxygen':1}
ex_GT5 = {'sinus':1,'o2 stat':1}
ex_GT7 = {'motor vehicle accident':1, 'chest pain':1,'pain':1, 'lower back pain':1,\
          'neck pain':1, 'saline':1, 'sinus':1}
ex_GT6 = {'sinus':1,  'chest pain':3, 'chief complaint':1, \
          '12 lead':3, \
         'mi':1, 'gcs':1, 'vital':1, 'heart rate':1, 'sat':1, 'aspirin':1, 'iv':1,\
         'nitroglycerin':1}

# result calculation method
def cal(result,GT):
    TP, FP, TN, FN, precision, recall = 0, 0, 0, 0, 0., 0.
    cat = list(set(result))
    for item in cat:
        num = result.count(item)
        if item not in GT.keys():
            print item in GT.keys()
            FP += num
        else:
            if num > GT[item]:
                TP += GT[item]
                FP += (num - GT[item])
            else:
                TP += num
                FN += (GT[item] - num)
    for con in GT.keys():
        if con not in cat:
            FN += GT[con]
    if TP == 0:
        precision, recall = 0,0
    else:
        precision = TP / float(TP + FP)
        recall = TP / float(TP + FN)
   # cal_result = {'TP':TP, 'FP':FP, 'TN':TN, 'FN':FN, 'precision':precision, 'recall':recall}
    cal_result = [TP, FP, TN, FN, precision, recall]
    return cal_result

# load concept lists								
extra_concept_list = pd.read_csv("/Users/sileshu/Desktop/Concept_List_2.csv", header = None)
extra_concept_list = [item.lower() for item in extra_concept_list[0]]
extended_concept_list = pd.read_csv("/Users/sileshu/Desktop/Extended_Concept_List.csv")
exact_concept_list = [item.lower() for item in extended_concept_list['Required Concept'] if item > 0]
CUIs = [item for item in extended_concept_list['CUI']]
CUI2Concept = {}
for idx,item in enumerate(extended_concept_list['Required Concept']):
    if item > 0:
        temp = item
        CUI2Concept[CUIs[idx]] = temp.lower()
    else:
        CUI2Concept[CUIs[idx]] = temp.lower()

# load file lists	
route = "/Users/sileshu/Desktop/data/"
files = os.listdir(route)
files.sort()

# concept extraction
result = {}
raw_result = {}
exact_result = {}
extra_result = {}
PS_action = {}

for fi in files:
    fo = open(route + fi, 'r')
    sents = [item for line in fo for item in line.rstrip('\r\n').split(".")]
  #  if len(sents) > 1:
  #      print sents
    concepts,error = mm.extract_concepts(sents,word_sense_disambiguation=True,\
                                     ignore_stop_phrases=True)
    fo.close()
    PS = {'rescuer hazard':False, 'patient hazard':False, 'conscious':True, 'breath':True,\
          'bleed':False, 'pulse':True}
    ex_exact_cons = []
    ex_extra_cons = []
    ex_extend_cons = []
    raw_ex_cons = []
    for concept in concepts:
        normalized_trigger_name = concept[6].split('-')[3].strip('"').lower()
        # last part of "trigger" field, 1 means negation is detected
        negation = concept[6].split('-')[-1].rstrip(']') == '0' # negation = False if negation is detected
        CUI = concept[4]
        num = len(concept[8].split(',['))
		# deal with multiple concepts inside a single MMI field output
        for i in range(num):
            raw_ex_cons.append(concept)
            if normalized_trigger_name in exact_concept_list:
                ex_exact_cons.append(normalized_trigger_name)
            if CUI in CUIs:
                mapped_concept = CUI2Concept[CUI]
                ex_extend_cons.append(mapped_concept)
                if mapped_concept in PS:
                    PS[mapped_concept] = negation
            if normalized_trigger_name in extra_concept_list:
                ex_extra_cons.append(normalized_trigger_name)
    result[fi] = ex_extend_cons
    raw_result[fi] = raw_ex_cons
    exact_result[fi] = ex_exact_cons
    extra_result[fi] = ex_extra_cons
    PS_action[fi] = op[PS['rescuer hazard'],PS['patient hazard'],\
            PS['conscious'],PS['breath'],PS['pulse'],PS['bleed']] == Y

# vectorize actions
PS_action_encode = {}
encodes = []
for fi in files:
    actions = PS_action[fi][0][0].split(', ')
    PS_action_encode[fi] = [actions.count('Eliminate_Hazard'),\
                     actions.count('Open_the_Airway'),\
                     actions.count('Start_Artificial_Ventilation'),\
                     actions.count('Start_External_Cardiac_Compressions'),\
                     actions.count('Control_Bleeding'),\
                     actions.count('Secondary_Survey')]
    encodes.append(PS_action_encode[fi])

# calculate and log results based on extended list
extend_results = DataFrame(index = files)
TP = []
FP = []
TN = []
FN = []
precision = []
recall = []
for fi in files:
    if fi[0] == '1':
        TP.append(cal(result[fi],GT_1)[0])
        FP.append(cal(result[fi],GT_1)[1])
        TN.append(cal(result[fi],GT_1)[2])
        FN.append(cal(result[fi],GT_1)[3])
        precision.append(cal(result[fi],GT_1)[4])
        recall.append(cal(result[fi],GT_1)[5])
    if fi[0] == '5':
        TP.append(cal(result[fi],GT_5)[0])
        FP.append(cal(result[fi],GT_5)[1])
        TN.append(cal(result[fi],GT_5)[2])
        FN.append(cal(result[fi],GT_5)[3])
        precision.append(cal(result[fi],GT_5)[4])
        recall.append(cal(result[fi],GT_5)[5])
    if fi[0] == '6':
        TP.append(cal(result[fi],GT_6)[0])
        FP.append(cal(result[fi],GT_6)[1])
        TN.append(cal(result[fi],GT_6)[2])
        FN.append(cal(result[fi],GT_6)[3])
        precision.append(cal(result[fi],GT_6)[4])
        recall.append(cal(result[fi],GT_6)[5])
    if fi[0] == '7':
        TP.append(cal(result[fi],GT_7)[0])
        FP.append(cal(result[fi],GT_7)[1])
        TN.append(cal(result[fi],GT_7)[2])
        FN.append(cal(result[fi],GT_7)[3])
        precision.append(cal(result[fi],GT_7)[4])
        recall.append(cal(result[fi],GT_7)[5])
extend_results['TP'] = TP
extend_results['FP'] = FP
extend_results['FN'] = FN
extend_results['precision'] = precision
extend_results['recall'] = recall
extend_results['actions'] = encodes
extend_results.to_csv('MetaMap_Concept_Extraction_Results1.csv')

# calculate and log results based on exact list
exact_results = DataFrame(index = files)
TP = []
FP = []
TN = []
FN = []
precision = []
recall = []
for fi in files:
    if fi[0] == '1':
        TP.append(cal(exact_result[fi],eGT_1)[0])
        FP.append(cal(exact_result[fi],eGT_1)[1])
        TN.append(cal(exact_result[fi],eGT_1)[2])
        FN.append(cal(exact_result[fi],eGT_1)[3])
        precision.append(cal(exact_result[fi],eGT_1)[4])
        recall.append(cal(exact_result[fi],eGT_1)[5])
    if fi[0] == '5':
        TP.append(cal(exact_result[fi],eGT_5)[0])
        FP.append(cal(exact_result[fi],eGT_5)[1])
        TN.append(cal(exact_result[fi],eGT_5)[2])
        FN.append(cal(exact_result[fi],eGT_5)[3])
        precision.append(cal(exact_result[fi],eGT_5)[4])
        recall.append(cal(exact_result[fi],eGT_5)[5])
    if fi[0] == '6':
        TP.append(cal(exact_result[fi],eGT_6)[0])
        FP.append(cal(exact_result[fi],eGT_6)[1])
        TN.append(cal(exact_result[fi],eGT_6)[2])
        FN.append(cal(exact_result[fi],eGT_6)[3])
        precision.append(cal(exact_result[fi],eGT_6)[4])
        recall.append(cal(exact_result[fi],eGT_6)[5])
    if fi[0] == '7':
        TP.append(cal(exact_result[fi],eGT_7)[0])
        FP.append(cal(exact_result[fi],eGT_7)[1])
        TN.append(cal(exact_result[fi],eGT_7)[2])
        FN.append(cal(exact_result[fi],eGT_7)[3])
        precision.append(cal(exact_result[fi],eGT_7)[4])
        recall.append(cal(exact_result[fi],eGT_7)[5])
exact_results['TP'] = TP
exact_results['FP'] = FP
exact_results['FN'] = FN
exact_results['precision'] = precision
exact_results['recall'] = recall
exact_results.to_csv('MetaMap_Concept_Extraction_Results2.csv')

extra_results = DataFrame(index = files)
TP = []
FP = []
TN = []
FN = []
precision = []
recall = []
for fi in files:
    if fi[0] == '1':
        TP.append(cal(extra_result[fi],ex_GT1)[0])
        FP.append(cal(extra_result[fi],ex_GT1)[1])
        TN.append(cal(extra_result[fi],ex_GT1)[2])
        FN.append(cal(extra_result[fi],ex_GT1)[3])
        precision.append(cal(extra_result[fi],ex_GT1)[4])
        recall.append(cal(extra_result[fi],ex_GT1)[5])
    if fi[0] == '5':
        TP.append(cal(extra_result[fi],ex_GT5)[0])
        FP.append(cal(extra_result[fi],ex_GT5)[1])
        TN.append(cal(extra_result[fi],ex_GT5)[2])
        FN.append(cal(extra_result[fi],ex_GT5)[3])
        precision.append(cal(extra_result[fi],ex_GT5)[4])
        recall.append(cal(extra_result[fi],ex_GT5)[5])
    if fi[0] == '6':
        TP.append(cal(extra_result[fi],ex_GT6)[0])
        FP.append(cal(extra_result[fi],ex_GT6)[1])
        TN.append(cal(extra_result[fi],ex_GT6)[2])
        FN.append(cal(extra_result[fi],ex_GT6)[3])
        precision.append(cal(extra_result[fi],ex_GT6)[4])
        recall.append(cal(extra_result[fi],ex_GT6)[5])
    if fi[0] == '7':
        TP.append(cal(extra_result[fi],ex_GT7)[0])
        FP.append(cal(extra_result[fi],ex_GT7)[1])
        TN.append(cal(extra_result[fi],ex_GT7)[2])
        FN.append(cal(extra_result[fi],ex_GT7)[3])
        precision.append(cal(extra_result[fi],ex_GT7)[4])
        recall.append(cal(extra_result[fi],ex_GT7)[5])
extra_results['TP'] = TP
extra_results['FP'] = FP
extra_results['FN'] = FN
extra_results['precision'] = precision
extra_results['recall'] = recall

