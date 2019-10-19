from string import ascii_lowercase
urls = list(ascii_lowercase*22)

distribution_number= 10
def _divide_process(urls, distribution_number):
    url_length = len(urls)
    if distribution_number > url_length:
        print urls
        return
    i = 0
    x= 0
    while i < url_length:
        print x
        maximum_index = int(url_length / distribution_number) + i
        urls_to_send = urls[i:maximum_index]
        print i, maximum_index,urls_to_send
        i = maximum_index
        x += 1

_divide_process(urls, distribution_number)