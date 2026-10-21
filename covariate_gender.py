"""
@author: Tina Hsu
Experiment: Explore the association between gender and ITD.
"""
import numpy as np
from scipy import stats

# Tidy up the data for the gender
data_for_gender = patient_data_with_all_clinical_data.dropna(subset=["gender"])
data_for_gender.reset_index(drop=True, inplace=True)

def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))


def calculate_gender_percentage(data):
    print("Start to calculate!")
    itd_p_total = data[data["ITD"] == "ITD+"].shape[0]
    print(itd_p_total)
    itd_n_total = data[data["ITD"] == "ITD−"].shape[0]
    print(itd_n_total)

    male_itd_p = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    male_itd_n = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    female_itd_p = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    female_itd_n = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    Table = np.array([[male_itd_p, male_itd_n],
                  [female_itd_p, female_itd_n]])
    #print(Table)
    #print("Calculate p-value!")
    chi2, p, dof, ex = stats.chi2_contingency(Table, correction=False)
    Table = pd.DataFrame(Table, columns=["ITD+", "ITD−"], index=["Male", "Female"])
    return Table, p, itd_p_total, itd_n_total


def itd_gender_correlation(Table, p_value, p_total, n_total):
    # plot for gender-ITD percentages relation 
    # plt.figure(figsize=(7,5))
    plt.figure(figsize=(12,9))
    ind = np.arange(2)
    b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4')
    plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=25)
    plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=25)
    b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e")
    plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=25)
    plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=25)

    plt.text(0.5, 108, r"$P = {0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=30)
    
    plt.ylim([0,119])
    itd_p_label = "ITD+ (n=" + str(p_total) +")"
    itd_n_label = "ITD− (n=" + str(n_total) + ")"
    plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
    plt.yticks(fontsize=20)
    #plt.xlabel("ITD Positive/Negative", fontsize=30)
    #title = "Gender Percentages in ITD+/- groups (" + tumor +")"
    #plt.title(title,fontsize=36)
    plt.ylabel("Percentage (%)", fontsize=35)

    plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=20,bbox_to_anchor=(1., 1.0), loc='upper left')
		file_name = "F12_Correlation_between_ITD_and_Gender.tiff"
		plt.savefig(file_name, dpi=300, bbox_inches="tight")
    plt.show()


datas = data_for_gender
calculate_result, p_value, positive_total, negative_total= calculate_gender_percentage(datas)
print(calculate_result)
itd_gender_correlation(calculate_result, p_value, positive_total, negative_total)

#Plot
# for each cancer type
### Figure 13. Correlation of ITD and gender in each cancer type
# final: correlation of ITD and gender for each cancer type

# gender comparision function
import numpy as np
from scipy import stats

def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))


def calculate_gender_percentage(data):
    #print("Start to calculate!")
    itd_p_total = data[data["ITD"] == "ITD+"].shape[0]
    #print(itd_p_total)
    itd_n_total = data[data["ITD"] == "ITD−"].shape[0]
    #print(itd_n_total)

    male_itd_p = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    male_itd_n = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    female_itd_p = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    female_itd_n = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    Table = np.array([[male_itd_p, male_itd_n],
                  [female_itd_p, female_itd_n]])

    chi2, p, dof, ex = stats.chi2_contingency(Table, correction=False)
    Table = pd.DataFrame(Table, columns=["ITD+", "ITD−"], index=["Male", "Female"])
    return Table, p, itd_p_total, itd_n_total


def calculate_gender_percentage_without_statistics(data):
    #print("Start to calculate!")
    itd_p_total = data[data["ITD"] == "ITD+"].shape[0]
    #print(itd_p_total)
    itd_n_total = data[data["ITD"] == "ITD−"].shape[0]
    #print(itd_n_total)

    male_itd_p = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    male_itd_n = round(data[(data["gender"] == "male")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    female_itd_p = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD+")].shape[0]/itd_p_total*100, 1)
    female_itd_n = round(data[(data["gender"] == "female")&(data["ITD"] == "ITD−")].shape[0]/itd_n_total*100, 1)
    Table = np.array([[male_itd_p, male_itd_n],
                  [female_itd_p, female_itd_n]])
    Table = pd.DataFrame(Table, columns=["ITD+", "ITD−"], index=["Male", "Female"])
    return Table, itd_p_total, itd_n_total


# plot for gender-ITD percentages relation 
def itd_gender_correlation(tumor, Table, p_value, p_total, n_total):
    
    # only female in the cancer (not gender-cancers)
    if tumor in ["TCGA-ACC", "TCGA-SKCM", "TCGA-THYM"]:
        plt.figure(figsize=(12,9))
        ind = np.arange(2)
        ind = [0,0.5]
        b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4', width=0.35)
        #plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=30)
        b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e", width=0.35)
        plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=30)

        # plt.text(-0.023, 109, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        plt.text(0, 107.5, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        
        plt.ylim([0,119])
        itd_p_label = "ITD+ (n=" + str(p_total) +")"
        itd_n_label = "ITD− (n=" + str(n_total) + ")"
        plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
        plt.yticks(fontsize=20)
        plt.xlim([-0.25, 0.75])

        title = tumor  
        plt.title(title,fontsize=35, pad = 10)
        plt.ylabel("Percentage (%)", fontsize=30)
        plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=25, ncol=2, loc="upper right")

        file_name = "F13_Correlation_ITD_gender_"+ tumor +".tiff"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")
        plt.show()

    # only female gender-cancers
    elif (tumor in cancer_list_gender_cancer_7) & (tumor not in ["TCGA-BRCA", "TCGA-TGCT", "TCGA-PRAD"]):
        plt.figure(figsize=(12,9))
        ind = np.arange(2)
        ind = [0,0.5]
        b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4', width=0.35)
        #plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=30)
        #plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=30)
        b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e", width=0.35)
        plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=30)

        #plt.text(0, 107.5, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        
        plt.ylim([0,119])
        itd_p_label = "ITD+ (n=" + str(p_total) +")"
        itd_n_label = "ITD− (n=" + str(n_total) + ")"
        plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
        plt.yticks(fontsize=30)
        plt.xlim([-0.25, 0.75])

        title = tumor  
        plt.title(title,fontsize=35, pad = 10)
        plt.ylabel("Percentage (%)", fontsize=30)
        plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=25, ncol=2, loc="upper right")

        file_name = "F13_Correlation_ITD_gender_"+ tumor +".tiff"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")
        plt.show()

    # only male in the cancer
    elif (tumor in ["TCGA-DLBC", "TCGA-ESCA", "TCGA-KIRP"]):
        plt.figure(figsize=(12,9))
        ind = np.arange(2)
        ind = [0,0.5]
        b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4', width=0.35)
        plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=30)
        b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e", width=0.35)
        #plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=30)

        plt.text(0, 107.5, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        
        plt.ylim([0,119])
        itd_p_label = "ITD+ (n=" + str(p_total) +")"
        itd_n_label = "ITD− (n=" + str(n_total) + ")"
        plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
        plt.yticks(fontsize=30)
        plt.xlim([-0.25, 0.75])

        title = tumor  
        plt.title(title,fontsize=35, pad = 10)
        plt.ylabel("Percentage (%)", fontsize=30)
        plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=25, ncol=2, loc="upper right")

        file_name = "F13_Correlation_ITD_gender_"+ tumor +".tiff"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")
        plt.show()

    elif (tumor in ["TCGA-PRAD", "TCGA-TGCT"]):
        plt.figure(figsize=(12,9))
        ind = np.arange(2)
        ind = [0,0.5]
        b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4', width=0.35)
        plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=30)
        b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e", width=0.35)
        #plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=30)
        #plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=30)

        #plt.text(0, 107.5, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        
        plt.ylim([0,119])
        itd_p_label = "ITD+ (n=" + str(p_total) +")"
        itd_n_label = "ITD− (n=" + str(n_total) + ")"
        plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
        plt.yticks(fontsize=30)
        plt.xlim([-0.25, 0.75])

        title = tumor  
        plt.title(title,fontsize=35, pad = 10)
        plt.ylabel("Percentage (%)", fontsize=30)
        plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=25, ncol=2, loc="upper right")

        file_name = "F13_Correlation_ITD_gender_"+ tumor +".tiff"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")
        plt.show()


    else:
        plt.figure(figsize=(12,9))
        ind = np.arange(2)
        ind = [0,0.5]
        b1 = plt.bar(ind, list(Table.iloc[0,:]), color='#1f77b4', width=0.35)
        plt.text(ind[0],Table.iloc[0,0]/2,Table.iloc[0,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]/2,Table.iloc[0,1], horizontalalignment="center",weight="bold", fontsize=30)
        b2 = plt.bar(ind, list(Table.iloc[1,:]), bottom=list(Table.iloc[0,:]),color="#ff7f0e", width=0.35)
        plt.text(ind[0],Table.iloc[0,0]+Table.iloc[1,0]/2,Table.iloc[1,0], horizontalalignment="center", weight="bold", fontsize=30)
        plt.text(ind[1],Table.iloc[0,1]+Table.iloc[1,1]/2,Table.iloc[1,1], horizontalalignment="center", weight="bold", fontsize=30)

        plt.text(0, 107.5, r"$P={0:s}$".format(as_si(p_value, 2)), horizontalalignment="center", fontsize=25)
        
        plt.ylim([0,119])
        itd_p_label = "ITD+ (n=" + str(p_total) +")"
        itd_n_label = "ITD− (n=" + str(n_total) + ")"
        plt.xticks(ind, (itd_p_label, itd_n_label), fontsize=35)
        plt.yticks(fontsize=30)
        plt.xlim([-0.25, 0.75])

        title = tumor  
        plt.title(title,fontsize=35, pad = 10)
        plt.ylabel("Percentage (%)", fontsize=30)
        plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=25, ncol=2, loc="upper right")

        file_name = "F13_Correlation_ITD_gender_"+ tumor +".tiff"
        plt.savefig(file_name, dpi=300, bbox_inches="tight")
        plt.show()
    

for j in range(len(cancer_list_27)):
    project = "TCGA-" + str(cancer_list_27[j])
    datas = data_for_gender[data_for_gender["Project ID"] == project]
    datas.reset_index(inplace=True, drop=True)

    if (project in cancer_list_gender_cancer_7) & (project != "TCGA-BRCA"):
        calculate_result, positive_total, negative_total= calculate_gender_percentage_without_statistics(datas)
        itd_gender_correlation(project, calculate_result, p_value, positive_total, negative_total)
    else:
        calculate_result, p_value, positive_total, negative_total= calculate_gender_percentage(datas)
        itd_gender_correlation(project, calculate_result, p_value, positive_total, negative_total)


# Compare the proportions of gender (male and female) with ITD across all the cancer types
prop_df = data_for_gender.groupby(by=["Project ID", "gender"]).size().reset_index(name="Counts")

i=0
while (i < 66):
    tumor = prop_df.iloc[i,0]
    if tumor == prop_df.iloc[i+1, 0]:
        i += 2
    else:
        row = i+0.5
        genders = prop_df.iloc[i, 1]
        if genders == "female":
            prop_df.loc[row] = [tumor, "male", 0]
            prop_df = prop_df.sort_index().reset_index(drop=True)
            i += 2
        else:
            prop_df.loc[row] = [tumor, "female", 0]
            prop_df = prop_df.sort_index().reset_index(drop=True)
            i += 2

prop_df = prop_df.sort_values(by=["Project ID", "gender"])
prop_df["Percentage"] = 0
i = 0
while(i < 66):
    number_f = prop_df.iloc[i, 2]
    number_m = prop_df.iloc[i+1, 2]
    total_number = number_f + number_m
    per_f = round(number_f/total_number*100,1)
    per_m = round(number_m/total_number*100,1)
    prop_df.iloc[i,3] = per_f
    prop_df.iloc[i+1,3] = per_m
    i += 2

for i in range(prop_df.shape[0]):
    tumor = prop_df.iloc[i,0][5:]
    prop_df.iat[i,0] = tumor


###### plot
def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))

male_df = prop_df[prop_df["gender"] == "male"].reset_index(drop=True)
female_df = prop_df[prop_df["gender"] == "female"].reset_index(drop=True)

plt.figure(figsize=(12,9))
n=np.arange(33)
b1 = plt.bar(n, male_df.iloc[:,3], color='#1f77b4')
# for i in range(33):
#     plt.text(n[i], male_df.iloc[i,3]/2,male_df.iloc[i,3], horizontalalignment="center", weight="bold",fontsize = 25)
b2 = plt.bar(n, female_df.iloc[:,3], bottom=list(male_df.iloc[:,3]),color="#ff7f0e")
plt.yticks(fontsize=20)
plt.xticks(n, list(male_df.iloc[:,0]), rotation=90, fontsize=20)
plt.xlabel("Cancers", fontsize=30)
plt.ylim([0,105])
plt.ylabel("Percentage (%)", fontsize=30)
plt.xlim([-0.75, 32.75])
plt.legend((b2[0], b1[0]), ('Female', 'Male'), fontsize=20,bbox_to_anchor=(1., 1.0), loc='upper left')
file_name = "Proportion_of_genders_in_each_cancers.tiff"
plt.savefig(file_name, dpi=300, bbox_inches="tight")
plt.clf()


