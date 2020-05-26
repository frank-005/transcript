def main():
    def inputJob():
        jobId = input("Enter the Job Id: ")
        moneyEarned = input("How much did you earn on this job? ")
        return jobId, moneyEarned
        
    def money(moneyEarned):
        totalMoneyEarned = []
        moneyEarned.append(totalMoneyEarned)
        sumMoney = 0
        for i in totalMoneyEarned:
            sumMoney = sumMoney + i
        return sumMoney

    def inputRating():
        currentJobid = input("Job Id for job whose rating you want to give: ")
        ratingForJob = input("What is the rating? ")
        return currentJobid, ratingForJob
    
    def rating(jobId, currentJobid, ratingForJob):
        jobsDone = []
        jobId.append(jobsDone)
        if currentJobid in jobsDone:
            ratings = []
            sumRatings = 0
            for x in ratings:
                sumRatings = sumRatings + x
            return sumRatings
        else:
            print("The job Id is not in our records")
            inputRating()



if __name__ == '__main__':
    main()