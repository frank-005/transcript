def app():


    def inputJob():
        jobsDone = int(input("How many jobs have you done today? "))
        jobsDoneId =  []
        totalMoneyEarned = []
        for x in range(int(jobsDone)):
            jobId = input("Enter the Job Id: ")
            jobsDoneId.append(jobId)
            moneyEarned = float(input("How much did you earn on this job? "))
            totalMoneyEarned.append(moneyEarned)
        return jobId, jobsDone, jobsDoneId, totalMoneyEarned
        
    def money(totalMoneyEarned):
        sumMoney = 0
        for i in totalMoneyEarned:
            sumMoney = sumMoney + i
        return sumMoney

    def inputRating(jobsDone):
        for x in range(int(jobsDone)):
            currentJobid = input("Job Id for job whose rating you want to give: ")
            ratingForJob = int(input("What is the rating? "))
            return currentJobid, ratingForJob

    def rating(jobId, currentJobid, ratingForJob, jobsDone, jobsDoneId):
        ratings = []

        sumRatings = 0
        avgRatings = 0
        for x in range(int(jobsDone)):
            if currentJobid in jobsDoneId:
                ratings.append(ratingForJob)

                for rating1 in ratings:
                    sumRatings = sumRatings + rating1
                    avgRatings = sumRatings / len(ratings)
            else:
                print("The job Id is not in our records")
                inputRating(jobsDone)
        return jobsDoneId, avgRatings

    def output(jobsDone, sumMoney, avgRatings):
        print("You have done "  + str(jobsDone) + " job during this period")
        print("And you have earned " + str(sumMoney))
        print("Your average rating for this period is: " + str(avgRatings))

    def main():
        jobId, jobsDone, jobsDoneId, totalMoneyEarned = inputJob()
        sumMoney = money(totalMoneyEarned)
        currentJobid, ratingForJob = inputRating(jobsDone)
        jobsDoneId, avgRatings = rating(jobId, currentJobid, ratingForJob, jobsDone, jobsDoneId)
        output(jobsDone, sumMoney, avgRatings)




    main()
app()
