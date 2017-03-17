import boto3
from boto3.session import Session
 
session = Session(aws_access_key_id='', aws_secret_access_key='')
machinelearning = session.client('machinelearning', region_name='us-east-1')
model_id = 'ml-ynN3hzs1Q0a'

index= raw_input('Enter index: ')
loan_amnt= raw_input('Enter loan_amnt: ')
funded_amnt= raw_input('Enter funded_amnt: ')
funded_amnt_inv= raw_input('Enter funded_amnt_inv: ')
term= raw_input('Enter term')
int_rate= raw_input('Enter int_rate:')
installment= raw_input('Enter installment:')
grade= raw_input('Enter grade:')
sub_grade= raw_input('Enter sub_grade:')
emp_title= raw_input('Enter emp_title:')
emp_length= raw_input('Enter emp_length:')
home_ownership= raw_input('Enter home_ownership:')
annual_inc= raw_input('Enter annual_inc:')
verification_status= raw_input('Enter verification_status:')
issue_d= raw_input('Enter issue_d:')
pymnt_plan= raw_input('Enter pymnt_plan:')
url= raw_input('Enter url:')
desc= raw_input('Enter desc: ')
purpose = raw_input('Enter purpose: ')
title= raw_input('Enter title: ')
zip_code= raw_input('Enter zip_code: ')
addr_state= raw_input('Enter addr_state: ')
dti = raw_input('Enter dti: ')
delinq_2yrs= raw_input('Enter delinq_2yrs: ')
earliest_cr_line= raw_input('Enter earliest_cr_line: ')
inq_last_6mths= raw_input('Enter inq_last_6mths: ')
mths_since_last_delinq= raw_input('Enter mths_since_last_delinq: ')
mths_since_last_record= raw_input('Enter mths_since_last_record: ')
open_acc= raw_input('Enter open_acc: ')
pub_rec= raw_input('Enter pub_rec: ')
revol_bal= raw_input('Enter revol_bal: ')
revol_util= raw_input('Enter revol_util: ')
total_acc= raw_input('Enter total_acc: ')
initial_list_status= raw_input('Enter initial_list_status: ')
out_prncp= raw_input('Enter out_prncp: ')
out_prncp_inv= raw_input('Enter out_prncp_inv: ')
total_pymnt= raw_input('Enter total_pymnt: ')
total_pymnt_inv= raw_input('Enter total_pymnt_inv: ')
total_rec_prncp= raw_input('Enter total_rec_prncp: ')
total_rec_int= raw_input('Enter total_rec_int: ')
total_rec_late_fee= raw_input('Enter total_rec_late_fee: ')
recoveries= raw_input('Enter recoveries: ')
collection_recovery_fee= raw_input('Enter collection_recovery_fee: ')
last_pymnt_d= raw_input('Enter last_pymnt_d: ')
last_pymnt_amnt = raw_input('Enter last_pymnt_amnt : ')
next_pymnt_d= raw_input('Enter next_pymnt_d: ')
last_credit_pull_d= raw_input('Enter last_credit_pull_d: ')
collections_12_mths_ex_med= raw_input('Enter collections_12_mths_ex_med: ')
mths_since_last_major_derog= raw_input('Enter mths_since_last_major_derog: ')
policy_code= raw_input('Enter policy_code: ')
application_type= raw_input('Enter application_type: ')
annual_inc_joint= raw_input('Enter annual_inc_joint: ')
dti_joint= raw_input('Enter dti_joint: ')
verification_status_joint= raw_input('Enter verification_status_joint: ')
acc_now_delinq= raw_input('Enter acc_now_delinq: ')
tot_coll_amt = raw_input('Enter tot_coll_amt: ')
tot_cur_bal= raw_input('Enter tot_cur_bal: ')
open_acc_6m= raw_input('Enter open_acc_6m: ')
open_il_6m= raw_input('Enter open_il_6m: ')
open_il_12m= raw_input('Enter open_il_12m: ')
open_il_24m= raw_input('Enter : open_il_24m')
mths_since_rcnt_il= raw_input('Enter mths_since_rcnt_il: ')
total_bal_il= raw_input('Enter total_bal_il: ')
il_util= raw_input('Enter il_util: ')
open_rv_12m= raw_input('Enter open_rv_12m: ')
open_rv_24m= raw_input('Enter open_rv_24m: ')
max_bal_bc= raw_input('Enter max_bal_bc: ')
all_util= raw_input('Enter all_util: ')
total_rev_hi_lim= raw_input('Enter : total_rev_hi_lim')
inq_fi= raw_input('Enter inq_fi: ')
total_cu_tl= raw_input('Enter total_cu_tl: ')
inq_last_12m= raw_input('Enter inq_last_12m: ')
acc_open_past_24mths= raw_input('Enter acc_open_past_24mths: ')
avg_cur_bal= raw_input('Enter avg_cur_bal: ')
bc_open_to_buy= raw_input('Enter bc_open_to_buy: ')
bc_util= raw_input('Enter bc_util: ')
chargeoff_within_12_mths= raw_input('Enter chargeoff_within_12_mths: ')
delinq_amnt= raw_input('Enter delinq_amnt: ')
mo_sin_old_il_acct= raw_input('Enter mo_sin_old_il_acct: ')
mo_sin_old_rev_tl_op= raw_input('Enter mo_sin_old_rev_tl_op: ')
mo_sin_rcnt_rev_tl_op= raw_input('Enter mo_sin_rcnt_rev_tl_op: ')
mo_sin_rcnt_tl= raw_input('Enter mo_sin_rcnt_tl: ')
mort_acc= raw_input('Enter mort_acc: ')
mths_since_recent_bc= raw_input('Enter mths_since_recent_bc: ')
mths_since_recent_bc_dlq= raw_input('Enter mths_since_recent_bc_dlq: ')
mths_since_recent_inq= raw_input('Enter mths_since_recent_inq: ')
mths_since_recent_revol_delinq= raw_input('Enter mths_since_recent_revol_delinq: ')
num_accts_ever_120_pd= raw_input('Enter num_accts_ever_120_pd: ')
num_actv_bc_tl= raw_input('Enter num_actv_bc_tl: ')
num_actv_rev_tl = raw_input('Enter : num_actv_rev_tl')
num_bc_sats= raw_input('Enter : num_bc_sats')
num_bc_tl= raw_input('Enter : num_bc_tl')
num_il_tl= raw_input('Enter num_il_tl: ')
num_op_rev_tl= raw_input('Enter num_op_rev_tl: ')
num_rev_accts= raw_input('Enter num_rev_accts: ')
num_rev_tl_bal_gt_0= raw_input('Enter num_rev_tl_bal_gt_0: ')
num_sats = raw_input('Enter num_sats: ')
num_tl_120dpd_2m= raw_input('Enter num_tl_120dpd_2m: ')
num_tl_30dpd= raw_input('Enter num_tl_30dpd: ')
num_tl_90g_dpd_24m= raw_input('Enter num_tl_90g_dpd_24m: ')
num_tl_op_past_12m = raw_input('Enter num_tl_op_past_12m: ')
pct_tl_nvr_dlq= raw_input('Enter pct_tl_nvr_dlq: ')
percent_bc_gt_75= raw_input('Enter percent_bc_gt_75: ')
pub_rec_bankruptcies= raw_input('Enter pub_rec_bankruptcies: ')
tax_liens= raw_input('Enter tax_liens: ')
tot_hi_cred_lim= raw_input('Enter tot_hi_cred_lim: ')
total_bal_ex_mort= raw_input('Enter total_bal_ex_mort: ')
total_bc_limit= raw_input('Enter total_bc_limit: ')
total_il_high_credit_limit= raw_input('Enter total_il_high_credit_limit: ')
#Y= raw_input('Enter Y: ')


labels = {"index": index, 
"loan_amnt": loan_amnt, 
"funded_amnt": funded_amnt, 
"funded_amnt_inv": funded_amnt_inv,
"term": term, 
"int_rate": int_rate, 
"installment": installment, 
"grade": grade, 
"sub_grade": sub_grade, 
"emp_title": emp_title,
"emp_length": emp_length, 
"home_ownership": home_ownership, 
"annual_inc": annual_inc, 
"verification_status": verification_status,
"issue_d": issue_d, 
"pymnt_plan": pymnt_plan, 
"url": url, 
"desc": desc, 
"purpose": purpose, 
"title": title,
"zip_code": zip_code, 
"addr_state": addr_state, 
"dti": dti, 
"delinq_2yrs": delinq_2yrs,
"earliest_cr_line": earliest_cr_line, 
"inq_last_6mths": inq_last_6mths, 
"mths_since_last_delinq": mths_since_last_delinq, 
"mths_since_last_record": mths_since_last_record, 
"open_acc": open_acc, 
"pub_rec": pub_rec,
"revol_bal": revol_bal, 
"revol_util": revol_util, 
"total_acc": total_acc, 
"initial_list_status": initial_list_status,
"out_prncp": out_prncp, 
"out_prncp_inv": out_prncp_inv, 
"total_pymnt": total_pymnt, 
"total_pymnt_inv": total_pymnt_inv, 
"total_rec_prncp": total_rec_prncp, 
"total_rec_int": total_rec_int,
"total_rec_late_fee": total_rec_late_fee, 
"recoveries": recoveries, 
"collection_recovery_fee": collection_recovery_fee, 
"last_pymnt_d": last_pymnt_d,
"last_pymnt_amnt": last_pymnt_amnt, 
"next_pymnt_d": next_pymnt_d, 
"last_credit_pull_d": last_credit_pull_d, 
"collections_12_mths_ex_med": collections_12_mths_ex_med, 
"mths_since_last_major_derog": mths_since_last_major_derog, 
"policy_code": policy_code,
"application_type": application_type, 
"annual_inc_joint": annual_inc_joint, 
"dti_joint": dti_joint, 
"verification_status_joint": verification_status_joint,
"acc_now_delinq": acc_now_delinq, 
"tot_coll_amt": tot_coll_amt, 
"tot_cur_bal": tot_cur_bal, 
"open_acc_6m": open_acc_6m, 
"open_il_6m": open_il_6m, 
"open_il_12m": open_il_12m,
"open_il_24m": open_il_24m, 
"mths_since_rcnt_il": mths_since_rcnt_il, 
"total_bal_il": total_bal_il, 
"il_util": il_util,
"open_rv_12m": open_rv_12m, 
"open_rv_24m": open_rv_24m, 
"max_bal_bc": max_bal_bc, 
"all_util": all_util, 
"total_rev_hi_lim": total_rev_hi_lim, 
"inq_fi": inq_fi,
"total_cu_tl": total_cu_tl, 
"inq_last_12m": inq_last_12m, 
"acc_open_past_24mths": acc_open_past_24mths, 
"avg_cur_bal": avg_cur_bal,
"bc_open_to_buy": bc_open_to_buy, 
"bc_util": bc_util, 
"chargeoff_within_12_mths": chargeoff_within_12_mths, 
"delinq_amnt": delinq_amnt, 
"mo_sin_old_il_acct": mo_sin_old_il_acct, 
"mo_sin_old_rev_tl_op": mo_sin_old_rev_tl_op,
"mo_sin_rcnt_rev_tl_op": mo_sin_rcnt_rev_tl_op, 
"mo_sin_rcnt_tl": mo_sin_rcnt_tl, 
"mort_acc": mort_acc, 
"mths_since_recent_bc": mths_since_recent_bc,
"mths_since_recent_bc_dlq": mths_since_recent_bc_dlq, 
"mths_since_recent_inq": mths_since_recent_inq, 
"mths_since_recent_revol_delinq": mths_since_recent_revol_delinq, 
"num_accts_ever_120_pd": num_accts_ever_120_pd, 
"num_actv_bc_tl": num_actv_bc_tl, 
"num_actv_rev_tl": num_actv_rev_tl,
"num_bc_sats": num_bc_sats, 
"num_bc_tl": num_bc_tl, 
"num_il_tl": num_il_tl, 
"num_op_rev_tl": num_op_rev_tl,
"num_rev_accts": num_rev_accts, 
"num_rev_tl_bal_gt_0": num_rev_tl_bal_gt_0, 
"num_sats": num_sats, 
"num_tl_120dpd_2m": num_tl_120dpd_2m, 
"num_tl_30dpd": num_tl_30dpd, 
"num_tl_90g_dpd_24m": num_tl_90g_dpd_24m,
"num_tl_op_past_12m": num_tl_op_past_12m, 
"pct_tl_nvr_dlq": pct_tl_nvr_dlq, 
"percent_bc_gt_75": percent_bc_gt_75, 
"pub_rec_bankruptcies": pub_rec_bankruptcies,
"tax_liens": tax_liens, 
"tot_hi_cred_lim": tot_hi_cred_lim, 
"total_bal_ex_mort": total_bal_ex_mort, 
"total_bc_limit": total_bc_limit, 
"total_il_high_credit_limit": total_il_high_credit_limit, 
"Y":""}
 
try:
 
    model = machinelearning.get_ml_model(MLModelId=model_id)
    prediction_endpoint = model.get('EndpointInfo').get('EndpointUrl')


    with open('DB6_LC_INDEX_MASTER_ABC.csv') as f:
        record_str = f.readline()
 
    record = {}
    for index,val in enumerate(record_str.split(',')):
        record['Var%03d' % (index+1)] = val
 
    response = machinelearning.predict(MLModelId=model_id, Record=record, PredictEndpoint=prediction_endpoint)
    print(response)
    label = response.get('Prediction').get('predictedLabel')
 

    print("You are currently %s." % labels[label])
 
except Exception as e:
    print(e)