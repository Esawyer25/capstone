from CapApp.models import Grant

class Stats:
    def find_total_cost(list):
        total = 0
        # if list.count() > 0:
        for item in list:
            if item.total_cost:
                total += item.total_cost
        return total
        
    def find_direct_cost(list):
        total = 0
        # if list.count() > 0:
        for item in list:
            if item.direct_cost_amt:
                total += item.direct_cost_amt
        return total

    def find_indirect_cost(list):
        total = 0
        # if list.count() > 0:
        for item in list:
            if item.indirect_cost_amt:
                total += item.indirect_cost_amt
        return total

    def return_stats_dict(grant_list, query):
        grant_count = len(grant_list)
        grant_total_cost = Stats.find_total_cost(grant_list)
        grant_indirect_cost = Stats.find_indirect_cost(grant_list)
        grant_direct_cost = Stats.find_direct_cost(grant_list)
        #Individual Predoctoral NRSA for M.D./Ph.D. Fellowships
        grant_f30 = Grant.objects.filter(abstract_text__search=query).filter(activity="F30")
        f30_total_cost = Stats.find_total_cost(grant_f30)
        f30_count = grant_f30.count()


        #Predoctoral Individual National Research Service Award
        grant_f31 = Grant.objects.filter(abstract_text__search=query).filter(activity="F31")
        f31_total_cost = Stats.find_total_cost(grant_f31)
        f31_count = grant_f31.count()

        #Postdoctoral Individual National Research Service Award
        grant_f32 = Grant.objects.filter(abstract_text__search=query).filter(activity="F32")
        f32_total_cost = Stats.find_total_cost(grant_f32)
        f32_count = grant_f32.count()

        #Career Transition Award
        grant_k99 = Grant.objects.filter(abstract_text__search=query).filter(activity="K99")
        k99_total_cost = Stats.find_total_cost(grant_k99)
        k99_count = grant_k99.count()

        #Research Transition Award
        grant_r00 = Grant.objects.filter(abstract_text__search=query).filter(activity="R00")
        r00_total_cost = Stats.find_total_cost(grant_r00)
        r00_count = grant_r00.count()

        #Research Project
        grant_r01 = Grant.objects.filter(abstract_text__search=query).filter(activity="R01")
        r01_total_cost = Stats.find_total_cost(grant_r01)
        r01_count = grant_r01.count

        #Outstanding Investigator Award
        grant_r35 = Grant.objects.filter(abstract_text__search=query).filter(activity="R35")
        r35_total_cost = Stats.find_total_cost(grant_r35)
        r35_count = grant_r35.count

        #NIH Director’s Pioneer Award (NDPA)
        grant_dp1 =Grant.objects.filter(abstract_text__search=query).filter(activity="DP1")
        dp1_total_cost = Stats.find_total_cost(grant_dp1)
        dp1_count = grant_dp1.count

        #NIH Director’s New Innovator Award
        grant_dp2 =Grant.objects.filter(abstract_text__search=query).filter(activity="DP2")
        dp2_total_cost = Stats.find_total_cost(grant_dp1)
        dp2_count = grant_dp1.count

        grant_stats_dict={'query': query,'grant_count': grant_count, 'grant_total_cost': grant_total_cost,'grant_direct_cost':grant_direct_cost,'grant_indirect_cost':grant_indirect_cost,'f30_count':f30_count,'f30_total_cost':f30_total_cost,'f31_count':f31_count,'f31_total_cost':f31_total_cost,'f32_count':f32_count,'f32_total_cost':f32_total_cost,'k99_count':k99_count,'k99_total_cost':k99_total_cost,'r00_count':r00_count,'r00_total_cost':r00_total_cost,'r01_count': r01_count,'r01_total_cost':r01_total_cost,'r35_count':r35_count,'r35_total_cost':r35_total_cost,'dp1_count':dp1_count,'dp1_total_cost':dp1_total_cost,'dp2_count':dp2_count,'dp2_total_cost':dp2_total_cost}

        return grant_stats_dict
