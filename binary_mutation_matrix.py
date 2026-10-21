"""
@author: Tina Hsu
Experiment: Gene frequency of ITD.
"""
def get_gene(values):
    first = values.split(";")
    element = []
    for i in range(len(first)):
        to_add = first[i].split("(")[0]
        element.append(to_add)
        print(f"Distinct gene: {i}")
    
    return list(set(element))[0]


if __name__ == '__main__':

  for i in range(itd_data_to_analysis.shape[0]):
      ref_gene = itd_data_to_analysis.loc[i, "RefSeq_gene_Exon"]
      gene_name = get_gene(ref_gene)
      itd_data_to_analysis.loc[i, "Gene Name"] = gene_name

  # Abstract the lists of the genes and the patients (Gene Name & Case ID)
  genes_721 = list(set(itd_data_to_analysis["Gene Name"]))
  case_10526 = list(set(patient_data_with_all_clinical_data["Case ID"]))
  
  binary_mutation_matrix = pd.DataFrame(0, index=genes_721, columns=case_10526)
  mutation_matrix = pd.DataFrame(0, index=genes_721, columns=case_10526)
  binary_mutation_matrix.to_csv("Binary_Mutation_Matrix.csv", index=True)
  mutation_matrix.to_csv("Mutation_Matrix.csv", index=True)

  # Calculate gene frequency and percentage
  check_genes_in_cancers = {}
  total_patient = patient_data_with_all_clinical_data.shape[0]
  for i in range(len(genes_721)):
      gene = genes_721[i]
      counts = sum(binary_mutation_matrix.loc[gene,:])
      per = round(counts/total_patient*100,2)
      check_genes_in_cancers[gene] = per
  check_genes_in_cancers = sorted(check_genes_in_cancers.items(), key=lambda x:x[1], reverse=True)
  check_genes_in_cancers = dict(check_genes_in_cancers)
  
  # Draw Top 25 genes
  test = {}
  i = 0
  for key, value in check_genes_in_cancers.items():
      if i < 25:
          test[key] = value
          i += 1

  # Visualization
  plt.figure(figsize=(20,5))
  plt.bar(*zip(*test.items()), width=0.8, color='#1f77b4')
  plt.xlabel("Genes" ,fontsize=36)
  plt.ylabel("Frequency (%)" ,fontsize=36)
  plt.ylim([0,1.75])
  plt.xlim([-0.75,24.75])
  plt.xticks(rotation=90,fontsize=15)
  plt.yticks(fontsize=15)
  #plt.title("Frequency of genes in Pan-Cancer (Top 25)",fontsize=40)
  for key, value in test.items():
      plt.text(key, value+0.02, value, horizontalalignment="center",fontsize=14)
  plt.text("FAT1", 1.2, "n=10526", fontsize=30)
  plt.savefig("F10_frequency_of_top_25.tiff", dpi=300, bbox_inches="tight")
  plt.show()

