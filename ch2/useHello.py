from hello_slam import print_hello  # 在 __init__.py 中直接暴露接口


def main(*args, **kwargs):
    print_hello()
    return 0


if __name__ == '__main__':
    main()
