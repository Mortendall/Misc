import os
import shutil
os.chdir(r"C:\Users\tvb217\Documents\R\tmp\NAFLD_patient_investigation\Data")
dst = r"C:\Users\tvb217\Documents\R\tmp\NAFLD_patient_investigation\Collected_data"

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".gz"):
            print(os.path.join(root, file))
            shutil.move(os.path.join(root,file),dst)