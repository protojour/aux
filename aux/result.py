class Result(object):
    def is_success(self):
        return True

class ResultCollector(object):
    def get_results(self):
        return Result()
