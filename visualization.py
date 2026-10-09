"""
Visualization functions.
@author: Tina Hsu
"""
import matplotlib.patches as mpatches


def my_surc(durations, event, groups, label_p, label_n, plocx, plocy, time_name, name):
  
    # Identify two groups to compare
    groups = groups
    i1 = (groups == label_p)
    i2 = (groups == label_n) 
    #Log-Rank P
    LRP = llss.logrank_test(durations[i1], durations[i2], event[i1], event[i2]).p_value
    
    kmf1 = KaplanMeierFitter() 
    plt.figure(figsize = (12, 9))

    # First group
    kmf1.fit(durations[i1], event[i1], label=label_p+' (n='+str(len(durations[i1]))+')')
    a1 = kmf1.plot(ci_show=False, color='#FF7300', linewidth=4)
    # Second group
    kmf1.fit(durations[i2], event[i2], label=label_n+' (n='+str(len(durations[i2]))+')')
    kmf1.plot(ax=a1, ci_show=False,  color='#20B2AA', linewidth=4)
 
    plt.text(plocx, plocy, r"$LogRankP = {0:s}$".format(as_si(LRP, 2)), fontsize=25)
    plt.xticks([0, 100, 200, 300],fontsize=20)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0],fontsize=20)
    plt.xlabel('Time (Months)', fontsize=35)
    plt.ylabel(str(time_name) + ' (%)', fontsize=35)
    #plt.title(title, fontsize=25)
    plt.tight_layout()

    colors = ["#FF7300", "#20B2AA"]
    texts = [label_p+' (n='+str(len(durations[i1]))+')', label_n+' (n='+str(len(durations[i2]))+')']
    patches = [ mpatches.Patch(color=colors[i], label="{:s}".format(texts[i]) ) for i in range(len(texts)) ]
    # plt.legend(handles=patches, bbox_to_anchor=(0.5, 0.5), loc='center', ncol=2)
    plt.legend(handles=patches, loc='upper right', ncol=1, fontsize=20)

    plt.savefig(f"{name}_survival_plot.tiff", dpi=300, bbox_inches="tight")
    plt.show()



