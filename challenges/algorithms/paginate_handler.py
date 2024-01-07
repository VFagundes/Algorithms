class PaginateHandler:
    @classmethod
    def distribute_array(cls, array: list, distribution_number: int):
        distribution_number = max(1, min(distribution_number, len(array)))
        group_size = max(1, len(array) // distribution_number)
        grouped_urls = [array[i:i + group_size] for i in range(0, len(array), group_size)]
        return grouped_urls
    

def run():
    arrTest1= [x for x in range(31)]
    arrTest2= [x for x in range(1001)]
    arrTest3= [x for x in range(347)]
    result1 = PaginateHandler.distribute_array(arrTest1,5)
    result2 = PaginateHandler.distribute_array(arrTest2,6)
    result3 = PaginateHandler.distribute_array(arrTest3,12)
    assert len(result1) == 6
    assert len(result2) == 7
    assert len(result3) == 13

run()