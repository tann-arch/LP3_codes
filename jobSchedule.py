class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):
    # Step 1: Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Create slot array and job sequence
    slots = [False] * max_deadline
    job_seq = ['-'] * max_deadline

    total_profit = 0

    # Step 4: Schedule jobs
    for job in jobs:
        # find a free slot for this job (starting from its deadline)
        for j in range(job.deadline - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                job_seq[j] = job.id
                total_profit += job.profit
                break

    # Step 5: Print result
    print("Job sequence:", " ".join([j for j in job_seq if j != '-']))
    print("Total profit:", total_profit)


# Example usage
if __name__ == "__main__":
    n = int(input("Enter number of jobs: "))
    jobs = []
    for i in range(n):
        job_id = input(f"Enter Job ID for job {i + 1}: ")
        deadline = int(input(f"Enter Deadline for job {i + 1}: "))
        profit = int(input(f"Enter Profit for job {i + 1}: "))
        jobs = jobs + [Job(job_id, deadline, profit)]
    # for i in range
    # jobs = [
    #     Job('A', 2, 100),
    #     Job('B', 1, 19),
    #     Job('C', 2, 27),
    #     Job('D', 1, 25),
    #     Job('E', 3, 15)
    # ]

    job_sequencing(jobs)
