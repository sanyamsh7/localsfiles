##understanding some keyword argument charachterstics:
##    desired output:
##        ['a']
##        ['b']
##        ['c']
##
##attempt 1:
##here we define a foo() , keyword arg.--> (container) and positional arg.--> (element)
##here only the keyword container gets all the changes hence the default value of container is
##overwritten everytime we call foo() with previous value in place
##def foo(element, container = []):
##    container.append(element)
##    return print(container)
##
##foo('a')
##foo('b')
##foo('c')

##attemp2:
##    here for first call of foo() , (if) condition is false hence the keyword container is updated to 'a'
##    and retains this value for every call of the function . for every other call of foo() (if) condition is true
##    and hence the container is referenced to a new empty list of each call of foo().
##def foo(element, container = []):
##    if container:
##        container = []
##    container.append(element)
##    return print(container)
##
##foo('a')
##foo('b')
##foo('c')

##attempt3:
##    here, for every call of foo() , (if) condition is true and keyword (container) retains empty list
##    and later for everycall it is overwritten to an empty list hence the same ouput as previous attempt.
##def foo(element, container = []):
##    if not container:
##        container = []    
##    container.append(element)
##    return print(container)
##
##foo('a')
##foo('b')
##foo('c')

##attempt4:
##    solution to the problem
##def foo(element, container = []):
##    print('before changes', container)
##    container = []
##    print('AFTER OVERLAP', container)
##    container.append(element)
##    return print(container)
##
##foo('a')
##foo('b')
##foo('c')

##attempt5:
##    ANOTHER SOLUTION TO THE PROBLEM
##def foo(element, container = []):
##    container.append(element)
##    return print(container)
##
##foo('a',[])
##foo('b',[])
##foo('c',[])
