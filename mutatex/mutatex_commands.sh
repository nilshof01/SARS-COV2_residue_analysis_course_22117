
#!/bin/bash

$cp /home/projects/22117_proteins/lecture4_exercise/group0/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .
$cp /home/projects/22117_proteins/lecture4_exercise/group0/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .
$cp /home/projects/22117_proteins/lecture4_exercise/group0/mutatex_templates/mutatex/templates/mutation_list.txt .


$/home/ctools/foldx-5.2023/foldx --command=RepairPDB --pdb=bx116_RBD_correct.pdb --ionStrength=0.05 --pH=7 -vdwDesign=2 --out-pdb=1 --pdbHydrogens=False


$mutatex bx116_RBD__Repair.pdb -p 10 -m mutation_list.txt -x /home/ctools/foldx-5.2023/foldx -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -c -L -l -v &

$/home/ctools/anaconda3_2021.11/bin/ddg2excel -p RBD_BX116__Repair.pdb  -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/final_averages/ -F csv

