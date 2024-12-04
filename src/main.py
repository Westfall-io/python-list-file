import time
start_time = time.time()

from functions.filesystem import get_config

def main(debug=False):
    config = get_config()

if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
