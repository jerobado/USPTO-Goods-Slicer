"""
USPTO Goods Slicer is Python library that can remove bracketed goods and services of a USPTO trademark application.

Usage:
    >>> import uspto_goods_slicer
    >>> uspto_goods_slicer.remove_square_brackets('Literary agencies [management]')
    'Literary agencies'

Source: https://www.uspto.gov/trademark/guides-and-manuals/guidance-users##Brackets
"""


def remove_square_brackets(goods):
    """ Remove multiple pairs of square brackets. """

    for i in range(goods.count('[')):
        opening = goods.find('[')
        closing = goods.find(']') + 1
        goods = goods.replace(goods[opening:closing], '')
        return goods.replace('  ', ' ').strip()

