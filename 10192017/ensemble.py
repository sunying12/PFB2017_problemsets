#!/usr/bin/env Python3

cellp = open("alpaca_stemcellproliferation_genes.tsv", "r")
pigment = open("alpaca_pigmentation_genes.tsv", "r")
allgen = open("alpaca_all_genes.tsv","r")
TF = open("alpaca_transcriptionFactors.tsv", "r")



TF_read = TF.read()
cellpcontents = cellp.read ()
pigmentcontents = pigment.read()
allgencontents = allgen.read()

# convert into a list of strings
cellpsplit = cellpcontents.split()
pigmentsplit = pigmentcontents.split()
allgensplit = allgencontents.split()
TF_readsplit = TF_read.split()

TF_readsplit.remove("Gene")
TF_readsplit.remove("stable")
TF_readsplit.remove("ID")

cellpsplit.remove("Gene")
cellpsplit.remove("stable")
cellpsplit.remove("ID")

allgensplit.remove("Gene")
allgensplit.remove("stable")
allgensplit.remove("ID")

pigmentsplit.remove("Gene")
pigmentsplit.remove("stable")
pigmentsplit.remove("ID")


# having sets
set_cellpsplit = set(cellpsplit)
set_pigmentsplit = set(pigmentsplit)
set_allgensplit = set(allgensplit)
set_TF = set(TF_readsplit)

# not in cell proliferation genes
not_cellp = set_allgensplit - set_cellpsplit

# both stemcell proliferation genes and pigment genes
both_stemandpig = set_cellpsplit & set_pigmentsplit

# TFs for cell proliferation
TF_pro = set_TF & set_cellpsplit 

