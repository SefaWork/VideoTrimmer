import sys
import subprocess

args = sys.argv
del args[0]

if len(args) == 0:
    sys.exit("No arguments were provided.")

try:
    result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
except FileNotFoundError:
    sys.exit("FFMPEG is not installed.")

i = 1
for filePath in args:
    split = filePath.split("\\")
    split[-1] = "trim_" + split[-1]
    saveName = "\\".join(split)

    print("Now processing file " + filePath + " | (File " + str(i) + ")")
    startTime = input("Start time? (HH:MM:SS): ")
    duration = input("Duration? (seconds): ")
    givenSaveName = input("Path for saved file? (" + saveName + "):")

    if givenSaveName != "":
        saveName = givenSaveName
    
    try:
        print("Processing file...")
        result = subprocess.run([
            "ffmpeg",
            "-ss", startTime,
            "-i", filePath,
            "-c", "copy",
            "-t", duration,
            saveName
        ], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        print("Done processing.")
    except subprocess.CalledProcessError as e:
        print("Failed to process file.")

    i = i + 1

print("Program finished.")