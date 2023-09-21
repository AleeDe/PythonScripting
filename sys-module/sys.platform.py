import sys

if (sys.platform == "linux"):
    print("Running on linux system")
elif (sys.platform == "win32"):
    print("Running on Window system")
elif (sys.platform == "darwin"):
    print("Running on macOS system")
else:
    print("Running unknown platform")
