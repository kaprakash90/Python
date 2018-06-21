def scope_test():
    def do_local():
        spam = "local spam"



    try:
        def do_global():
            global spam
            spam = "global spam"
        do_global()
        print(f"just After global assignment inside:{spam}")
    except:
        print('ERROR!!!!')
    print(f"just After global assignment:{spam}")

    #do_global()
    #print("Just After global assignment:", spam)
    #spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    #do_nonlocal()
    #print("After nonlocal assignment:", spam)
    #do_global()
    #print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


def scope_test1():

    def get_local():
        tst = 'test local'

    try:
        def get_global():
            global tst
            tst = 'testing this guy'
        get_global()
        print(f'what is tst now inside {tst}')
    except:
        print('oops error!!')
    print(f'local var {tst}')

scope_test1()
print(f'what is tst now {tst}')
#print(f'what is tst1 now {tst1}')
