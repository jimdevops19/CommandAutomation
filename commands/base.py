import sys


def main(**kwargs):
    '''
    Describe what this command does
    Args:
        Your Args description

    Usage:
        Your Usage description
    :return:
    '''
    pass


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [

    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)
