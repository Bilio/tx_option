import collections
import functools
__all__ = ['memoized', 'scan']

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        self.cache[args] = self.cache[args] if self.cache.get(args, False) else self.func(*args)
 
        return self.cache[args]
 
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

def value_scan(comb, s=6500, e=8500, o=10):
    for point in xrange(6500, 8500):
        print comb.gain(point)

