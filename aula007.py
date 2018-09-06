try:
    1/1
except(Exception, ZeroDivisionError) as e:
    print(e)
else:
    print('No exception')
finally:
    print('Finaly')