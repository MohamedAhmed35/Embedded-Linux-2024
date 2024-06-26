import sys


print(f"This is the name/path of hte script {sys.argv[0]}")

print(f"Number of arguments: {len(sys.argv)}")
print("Argument list: ", end = '')
for i in sys.argv:
    print(i, end = ' ')
