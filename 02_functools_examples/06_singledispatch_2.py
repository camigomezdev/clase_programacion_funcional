from functools import singledispatch
import itertools

@singledispatch
def yield_lines(iterable):
    r"""
    Yield valid lines of a string or iterable.

    >>> list(yield_lines(''))
    []
    >>> list(yield_lines(['foo', 'bar']))
    ['foo', 'bar']
    >>> list(yield_lines('foo\nbar'))
    ['foo', 'bar']
    >>> list(yield_lines('\nfoo\n#bar\nbaz #comment'))
    ['foo', 'baz #comment']
    >>> list(yield_lines(['foo\nbar', 'baz', 'bing\n\n\n']))
    ['foo', 'bar', 'baz', 'bing']
    """
    return itertools.chain.from_iterable(map(yield_lines, iterable))


@yield_lines.register(str)
def _(text):
    return filter(lambda x: x != "", map(str.strip, text.splitlines()))


print(list(yield_lines('')))
print(list(yield_lines('foo\nbar')))
print(list(yield_lines('\nfoo\n#bar\nbaz #comment')))
print(list(yield_lines(['foo\nbar', 'baz', 'bing\n\n\n'])))
