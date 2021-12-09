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
    name = kwargs.get('name')
    age = kwargs.get('age')

    # NOTE: Could be replaced with switch case.
    # If your system interpreter uses Python3.10 or above
    print("Hello, thanks for using the CommandAutomation by JimShapedCoding!")
    if name:
        print(f"Your name is {name}")
    if age:
        print(f"Your age is {age}")


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        'name',
        'age'
    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)