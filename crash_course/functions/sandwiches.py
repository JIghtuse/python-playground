def make_sandwich(*items):
    print("\nSandwich with following ingredients ordered:")
    for item in items:
        print("- " + item)

make_sandwich()
make_sandwich('tuna')
make_sandwich('tuna', 'cheese', 'tomatoes')
