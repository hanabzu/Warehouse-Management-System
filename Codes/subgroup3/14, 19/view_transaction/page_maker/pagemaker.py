def make_page(td) :
    if len(td) == 0 :
        error_page()

    else :
        show_page(td)

def error_page() :
    print('N/A')

def show_page(td) :
    for data in td :
        print('%s(%s) <-> %s(%s) : '%(data[0], data[1], data[2], data[3]), end='')
        print('%-8s %-10s %-10s'%(data[4], data[5], data[6][:-1]))
