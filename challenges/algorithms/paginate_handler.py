class PaginateHandler:
    @classmethod
    def distribute_array(cls, array: list, distribution_number: int):

        if distribution_number >= len(array):
            distribution_number = int(len(array)) + 1
        i = 0
        grouped_urls = []
        while i < len(array):
            maximum_index = int(len(array) / distribution_number) + i
            url_group = array[i:maximum_index]
            grouped_urls.append(url_group)
            i = maximum_index
        return grouped_urls
    

def run():
    arrTest1= [x for x in range(31)]
    arrTest2= [x for x in range(1001)]
    result1 = PaginateHandler.distribute_array(arrTest1,5)
    result2 = PaginateHandler.distribute_array(arrTest2,6)
    assert len(result1) == 6
    assert len(result2) == 7

run()