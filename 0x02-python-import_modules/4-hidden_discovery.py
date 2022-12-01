#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    [print(x) for x in dir(hidden_4) if x[0:2] != "__"]
