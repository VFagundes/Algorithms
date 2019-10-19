"""
// Given a job struct definition below write a function that takes 2 inputs:
// * ID of a job to run
// * a slice/array/list of known job descriptions
// and return a total execution time of job with ID=ID and all of its children
// recursively.
//
// We can assume that there are no cycles in dependency graph and job
// descriptions in the slice/array/list are unique i.e. there are no duplicates.
//
// Add a couple of tests to prove your solution.
// Use whatever language you feel most comfortable with.
//
// For the exemplar 'jobs' slice below:
// For the exemplar 'jobs' slice below:
// * given ID=4 the function should return 60 - just a single job's duration
//   without any dependencies
// * given ID=2 the function should return 30 - duration of jobs 2 and 3
// * given ID=1 the function should return 120 - duration of jobs 1, 2, 3 and 4

type Job struct {
    ID          int
    jobTime     int
    childJobIDs []int
}

var jobs = []Job{
    Job{1, 30, []int{2, 4}},
    Job{2, 10, []int{3}},
    Job{4, 60, []int{}},
    Job{3, 20, []int{}},
}
"""


class Job(object):

    def __init__(self, id: int, job_time: int, child_jobs: list):
        self.id = id
        self.job_time = job_time
        self.child_jobs = child_jobs


jobs = list()
jobs.append(Job(id=1, job_time=30, child_jobs=[2, 4]))
jobs.append(Job(id=2, job_time=10, child_jobs=[3]))
jobs.append(Job(id=4, job_time=60, child_jobs=[]))
jobs.append(Job(id=3, job_time=20, child_jobs=[]))


class Solution:
    duration = 0
    job_ids = []

    def calculate_job_duration(self, job_list, job_id):
        if job_id in self.job_ids:
            self.job_ids.remove(job_id)
        for job in job_list:
            if job.id == job_id:
                self.duration += job.job_time
                self.job_ids += job.child_jobs

        if len(self.job_ids) > 0:
            for job_id in self.job_ids:
                self.calculate_job_duration(job_list, job_id)


class TestJobDuration:

    @property
    def sample_data_1(self):
        jobs = list()
        jobs.append(Job(id=1, job_time=30, child_jobs=[2, 4]))
        jobs.append(Job(id=2, job_time=10, child_jobs=[3]))
        jobs.append(Job(id=4, job_time=60, child_jobs=[]))
        jobs.append(Job(id=3, job_time=20, child_jobs=[]))
        jobs.append(Job(id=5, job_time=0, child_jobs=[1]))
        return jobs

    def test_should_calculate_duration_of_a_job_without_child(self):
        expected_duration = 20
        solution = Solution()
        solution.calculate_job_duration(job_list=self.sample_data_1, job_id=3)
        assert solution.duration == expected_duration

    def test_should_calculate_duration_of_a_job_with_child(self):
        expected_duration = 120
        solution = Solution()
        solution.calculate_job_duration(job_list=self.sample_data_1, job_id=1)
        assert solution.duration == expected_duration

    def test_should_calculate_duration_of_a_job_with_child_but_without_base_duration(self):
        expected_duration = 120
        solution = Solution()
        solution.calculate_job_duration(job_list=self.sample_data_1, job_id=5)
        assert solution.duration == expected_duration


test = TestJobDuration()
test.test_should_calculate_duration_of_a_job_without_child()
test.test_should_calculate_duration_of_a_job_with_child()
test.test_should_calculate_duration_of_a_job_with_child_but_without_base_duration()
