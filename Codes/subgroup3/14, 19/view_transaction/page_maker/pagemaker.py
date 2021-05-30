def make_page(td) :
    if len(td) == 0 :
        error_page()

    else :
        show_page(td)

def error_page() :
    print('N/A')

def show_page(td) :
    print('%9s <-> %-9s'%(data[0], data[2]))
    print('%-8s %-10s %-10s'%('날짜', '브랜드', '상품'))
    for data in td :
        print('%-8s %-10s %-10s'%(data[4], data[5], data[6]))
