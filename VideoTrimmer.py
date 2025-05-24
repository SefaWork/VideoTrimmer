import sys
import subprocess

print(sys.argv)

args = sys.argv
del args[0]

if len(args) == 0:
    print("No arguments were provided.")
    return

try:
    result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
except FileNotFoundError:
    print("FFMPEG is not installed.")
    return

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

    print(saveName)
    
    try:
        result = subprocess.run([
            "ffmpeg",
            "-ss", startTime,
            "-i", filePath,
            "-c", "copy",
            "-t", duration,
            saveName
        ])
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failure.")

    i = i + 1

print("Program finished.")