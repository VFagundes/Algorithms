def decorate(func):
    def run(p):
        return 'my data {}'.format(func(p))
    return run

@decorate
def voila(param):
    return 'woohoo my man {}'.format(param)