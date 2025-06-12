import numpy as np

'''
由于是python的实现，所以本程序演示使用numpy代替Eigen库的基本使用
'''

MATRIX_SIZE = 50

def main(*args, **kwargs):
    # numpy中的矩阵使用 np.array 定义，并且建议批量传入数据，这样效率更高

    # 声明一个2x3的float矩阵
    matrix_23 = np.array([[1., 2., 3.],
                                [4., 5., 6.]], dtype=np.float32)

    # 初始化为零
    matrix_33 = np.zeros((3,3))

    # 访问矩阵中的元素
    print("print matrix 2x3:")
    for i in range(2):
        for j in range(3):
            print(matrix_23[i][j], end='\t')
    print('\n')

    # 矩阵和向量相乘
    v_3d = np.array((3, 2, 1), dtype=np.float32)
    vd_3d = np.array((4, 5, 6), dtype=np.float32)

    result = matrix_23.dot(v_3d)
    print(f'[[1,2,3],[4,5,6]]*[3,2,1]={result.transpose()}')

    return 0


if __name__ == "__main__":
    main()
