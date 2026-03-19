import os

# Get and print the current working directory
p = os.getcwd()
print(p)

# Create 'TempDir' directory if it doesn't already exist
if not os.path.exists("TempDir"):
    os.mkdir('TempDir')

# Change the current working directory to D:/ and print it
os.chdir('D:/')
print(os.getcwd())
