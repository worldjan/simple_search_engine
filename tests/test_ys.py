import pprint

__author__ = 'youngsun'


if __name__ == '__main__':
    ft_matrix = {5: {1, 2, 3}, 7: {4, 5}, 3: {6, 7, 8, 9}}
    df = {term: len(ft_matrix[term]) for term in ft_matrix.keys()}
    print df
