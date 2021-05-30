from view_transaction import controller

def view_transaction(user) :
    if user[0] == 'admin' or user[0] == 'warehouse' :
        relation = input('1. warehouse <-> admin\n2. shop<->warehouse\ninput : ')
   
    period_s = input('period start(format : yyyyMMdd)\ninput : ')
    period_e = input('period end(format : yyyyMMdd)\ninput : ')
    period = (period_s, period_e)

    ti = {"user" : user, "relation" : relation, "period" : period}
    controller.Controller(ti)
