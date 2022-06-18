input_file = open("/mnt/StudentFiles/2022/2022MBI_02/Projectbioinfo/AAugustus/HistoplasmaC_combi_Q10/augustusoutput_b9.gff", "r") #input file
read_file = input_file.read() #lees de file
predicted_genes = read_file.split("# start gene") #splitten van file in blokken per predicted gene
output_file = open("./onlyproteinseqcombiQ10Hc.fasta", "x") #output file, hier komt de fasta sequentie in te staan
identifier = ">gene"#is nodig om fasta file te maken
i = 1

for gene in predicted_genes[1:]: #in deze for loop wordt elke predicted gene gesplits zodat alleen de fasta sequentie eruit komt
    gene_seq = gene.replace("\n#", "") # replace elke nieuwe lijn dat begint met # naar  een leeg lijn
    gene_seq1 = gene_seq.replace("] end gene g*##\n", "") # replace elke end gene lijn en maakt ervaan een lege lijn
    gene_seq2 = gene_seq1.split("protein sequence = [") # splits protein sequence = [
    gene_fasta = gene_seq2[1].split("] end gene") # hierdoor krijgt je de sequence van eiwit los van protein = [ en ] end gene
    if gene == predicted_genes[1]: #voor de alles eerste gen boven in de gff file
        output_file.write(identifier + str(i) + "\n") # write > gene plus nummer gen en begin op een nieuwe lijn
        output_file.write(gene_fasta[0]) # en zet het in de output file als de eerste index
    else: #voor elk ander gen in .gff file
        output_file.write("\n" + identifier + str(i) + "\n") # \n zorgt ervoor dat elke gen  en informtaie op een nieuwe lijn begint
        output_file.write(gene_fasta[0])
    #print(gene_fasta[0])
    i += 1 # optellen ; opsomming van de nummer voor de genen

input_file.close()
output_file.close()

