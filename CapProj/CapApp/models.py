from django.db import models

#Explanation of field names here: https://exporter.nih.gov/about.aspx
class Grant(models.Model):
    PI_NAME = models.CharField(max_length=264, null=True) #Change this to lowercase
    # application_id = models.CharField(max_length=12)
    # abstract_text = models.Text(max_length=4000, null=True) ## need to get this from the abstract doc
    # activity = models.CharField(max_length=3, null=True) # A 3-character code ex. RO1 (https://grants.nih.gov/grants/funding/ac_search_results.htm)
    # administering_ic = models.CharField(max_length=2, null=True)# Administering Institute or Center
    # application_type = models.CharField(max_length=1, null=True)
    # arra_funded = models.CharField(max_length=1, null=True)
    # award_notice_date = models.DateField(null=True)
    # budget_start = models.DateField(null=True)
    # budget_end = models.DateField(null=True)
    # cfda_code = models.CharField(max_length=10, null=True)
    # core_proect_num = models.CharField(max_length=20, null=True)
    # ed_inst_type = models.CharField(max_length=50, null=True)
    # foa_number = models.CharField(max_length=50, null=True)
    # full_project_num = models.CharField(max_length=50, null=True)
    # funding_ics = models.CharField(max_length=100, null=True)
    # funding_mechanism = models.CharField(max_length=150, null=True)
    # FY = models.CharField(max_length=50, null=True)
    # fy = models.IntegerField(max_length=50, null=True)
    # ic_name = models.CharField(max_length=264, null=True)
    # nih_spending_cats = models.CharField(max_length=528, null=True)
    # org_city = models.CharField(max_length=64, null=True)
    # org_country = models.CharField(max_length=128, null=True)
    # org_dept = models.CharField(max_length=128, null=True)
    # org_district = models.IntegerField(max_length=10, null=True)
    # org_duns = models.IntegerField(max_length=64, null=True)
    # org_fips = models.IntegerField(max_length=10, null=True)
    # org_ipf_code = models.IntegerField(max_length=64, null=True)
    # org_name = models.CharField(max_length=100, null=True)
    # org_state = models.CharField(max_length=10, null=True)
    # org_zipcode = models.CharField(max_length=20, null=True)
    # phr = models.TextField(max_length=1000, null=True)
    # pi_ids = models.CharField(max_length=20, null=True)
    # program_officer_name = models.CharField(max_length=128, null=True)
    # project_start = models.CharField(max_length=128, null=True)
    # project_end = models.DateField(null=True)
    # project_terms = models.TextField(max_length=3000, null=True)
    # project_title = models.TextField(max_length=500, null=True)
    # serial_number = models.CharField(max_length=10, null=True)
    # study_section = models.CharField(max_length=10, null=True)
    # study_section_name = models.TextField(max_length=200, null=True)
    # subproject_id = models.CharField(max_length=16, null=True)
    # suffix = models.CharField(max_length=16, null=True)
    # support_year = models.IntegerField(max_length=8, null=True)
    # direct_cost_amt = models.IntegerField(max_length=16, null=True)
    # indirect_cost_amt = models.IntegerField(max_length=16, null=True)
    # total_cost = models.IntegerField(max_length=16, null=True)
    # total_cost_sub_project = models.IntegerField(max_length=16, null=True)

    def __str__(self):
        return self.PI_NAME # change this to something more sensible later

# class Grant_Publications(models.Model):
    # pmid = models.ForeignKey(Grant, on_delete=models.CASCADE)
    # project_number = models.ForeignKey(Grant, on_delete=models.CASCADE)
#not sure this is the right way to do it.

# class Publications(models.Model):
#     pmid = models.CharField(max_length=16)
#     Authors = models.TextField(max_length=5000, null=True)##(should this be one or many?)
#     Title = models.TextField(max_length=1000, null=True)
#     Journal = models.CharField(max_length=1000, null=True)
#     Abstract = models.TextField(max_length=1000, null=True)
#     Page numbers =
#     Date
#     DOI
#     Author information




# Create your models here.
