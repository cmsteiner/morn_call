#!python3
# morn_call.py
import os, subprocess, sys, csv, pprint

scriptPath = 'C:\\Users\\Csteiner\\Documents\\morn_call'
scriptTF = 'open_incidents.cli'     # CLI script to get updates from TeamForge
tfFile = 'inc_track_out.csv'    # output file for the TF CLI script
outFile = 'daily_update.txt'    # output file from this script

# Check if current working directory is correct, and if not go to correct directory
if os.getcwd() != scriptPath:
    os.chdir(scriptPath)

# Check if the TF CLI output file already exists, and if so remove it    
# if os.path.exists(tfFile):
    # try:
        # os.remove(tfFile)
    # except OSError as e:
        # print("Error: %s - %s." % (e.filename,e.strerror))
        
# # Run the TF CLI script to generate the tfFile
# subprocess.run(['ctf', '--script', scriptTF, tfFile])

# Open tfFile and read into a list of lists
with open(tfFile, 'r') as f:
    reader = csv.reader(f)
    tabList = list(reader)

# Count the rows in the file from TF to determine number of open artifacts
count = len(tabList)

# Flatten the tabList
flatten = lambda l: [item for sublist in tabList for item in sublist]
newList = flatten(tabList)
addList = ['There are ' + str(count) + ' open incident artifacts in the tracker this morning.']
outList = [addList + newList]

# Write the opening line, including count of artifacts, then each row
with open(outFile, 'w') as f:
    # f.write('There are ' + str(count) + ' open incident artifacts in the tracker this morning.')
    for row in outList:
        f.write(str(row))
        # f.write('\n')
        
