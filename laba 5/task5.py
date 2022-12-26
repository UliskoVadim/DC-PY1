def get_random_password():
    from random import sample
    k=ord('A')
    a=''.join([chr(i) for i in range(k,k+28)])
    a1=a.lower()
    a2=''.join([str(i) for i in range(10)])
    final_=sample(a+a1+a2,8)
    return ''.join(final_)





print(get_random_password())
