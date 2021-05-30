def make_page(td) :
    if len(td) == 0 :
        error_page()

    else :
        show_page(td)

def error_page() :
    print('N/A')

def show_page(td) :
    print('%s <-> %s'%(td[0][0], td[0][2]))
    for data in td :
        print('%-8s %-10s %-10s'%(data[4], data[5], data[6][:-1]))
