# Full path and name to your csv file
csv_filepathname="/Users/eva/Documents/ada/capstone/capstone_project/CapProj/seed_data/RePORTER_PRJ_C_FY2018_013.csv"

import django
import os
import sys

PATH=os.path.abspath(os.path.dirname(__file__))

if os.name == 'posix': # Unix based systems
    bin_name = 'bin'
else:                  # Windows
    bin_name = 'Scripts'

# Relative path to the virtual environment
# (relative to the stand-alone script)
rel_path = '../venv/%s/activate_this.py' % bin_name
activate_this = os.path.join(PATH, rel_path)

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CapProj.settings")

django.setup()
from django.core.exceptions import ValidationError
from CapApp.models import Grant

import csv
# from django.db import models
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

def fake_date(fieldname, row_index):
    if row[row_index]=="":
        grant.fieldname = "1111/11/11"
    else:
        grant.fieldname = row[row_index]



index = 0
success = 0
for row in dataReader:
    index +=1
    if row[0] != 'APPLICATION_ID': # Ignore the headerrow,
        grant = Grant()
        print(row[0])
        grant.application_id = row[0]
        print(row[1])
        grant.activity = row [1]
        print(row[2])
        grant.administering_ic = row[2]
        print(row[3])
        grant.application_type = row[3]

        # grant.arra_funded = row[4]

        # if row[5]=="":
        #     grant.award_notice_date = "1111-11-11"
        # else:
        #     temp = row[5]
        #     temp = temp[6:10] + "-"+ temp[0:2] + "-" + temp[3:5]
        #     print(temp)
        #     grant.award_notice_date = temp

        print(row[6])
        if row[6]=="":
            grant.budget_start = "1111-11-11"
        else:
            temp = row[6]
            temp = temp[6:10] + "-"+ temp[0:2] + "-" + temp[3:5]
            grant.budget_start = temp

        print(row[7])
        if row[7]=="":
            grant.budget_end = "1111-11-11"
        else:
            temp = row[7]
            temp = temp[6:10] + "-"+ temp[0:2] + "-" + temp[3:5]
            grant.budget_end = temp

        # grant.cfda_code = row[8]
        print(row[9])
        grant.core_project_num = row[9]
        print(row[10])
        grant.ed_inst_type = row[10]

        # grant.foa_number = row[11]
        print(row[12])
        grant.full_project_num = row[12]
        print(row[13])
        grant.funding_ics = row[13]
        print(row[14])
        grant.funding_mechanism = row[14]

        print(row[15])
        grant.FY = row[15]

        print(row[16])
        grant.ic_name = row[16]

        # grant.nih_spending_cats = row[17]

        print(row[18])
        grant.org_city = row[18]

        print(row[19])
        grant.org_country = row[19]

        print(row[20])
        grant.org_dept = row[20]

        print(row[21])
        if row[21] == "":
            grant.org_district = None
        else:
            grant.org_district = row[21]

        # grant.org_duns = row[22]

        # grant.org_fips = row[23]

        # grant.org_ipf_code = row[24]
        print(row[25])
        grant.org_name = row[25]

        print(row[26])
        grant.org_state = row[26]

        print(row[27])
        grant.org_zipcode = row[27]

        # print(row[28])
        grant.phr = row[28]

        print(row[29])
        grant.pi_ids = row[29]

        print(row[30])
        grant.pi_name= row[30]

        # grant.program_officer_name = row[31]

        # grant.project_start = row[32]

        # grant.project_end = row[33]

        print(row[34])
        grant.project_terms = row[34]

        print(row[35])
        grant.project_title = row[35]

        # grant.serial_number = row[36]

        print(row[37])
        grant.study_section = row[37]

        print(row[38])
        grant.study_section_name = row[38]

        print(row[39])
        grant.subproject_id = row[39]

        # grant.suffix = row[40]

        print(row[41])
        if row[41] == "":
            grant.support_year = None
        else:
            grant.support_year = row[41]

        print(row[42])
        if row[42] == "":
            grant.direct_cost_amt = None
        else:
            grant.direct_cost_amt = row[42]

        print(row[43])
        if row[43] == "":
            grant.indirect_cost_amt = None
        else:
            grant.indirect_cost_amt = row[43]

        print(row[44])
        if row[44] == "":
            grant.total_cost = None;
        else:
            grant.total_cost = row[44]

        print(row[45])
        if row[45] == "":
            grant.total_cost_sub_project = None
        else:
            grant.total_cost_sub_project = row[45]

        try:
            Grant.clean_fields(grant)
        except ValidationError as e:
            print(e)


        try:
            grant.save()
            success +=1
            print(f"saved application_id {grant.application_id}")
            # print(f"saved date {grant.award_notice_date}")
            print(f"saved {success} out of {index}")
        except:

            print(f"there was a problem with row {index}")
            print(f"saved {success} out of {index}")
