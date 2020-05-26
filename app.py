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
        print(totalMoneyEarned)
        for i in totalMoneyEarned:
            sumMoney = sumMoney + i
        return sumMoney

    def inputRating(jobsDone):
        ratings = []
        for x in range(int(jobsDone)):
            currentJobid = input("Job Id for job whose rating you want to give: ")
            ratingForJob = int(input("What is the rating? "))
            ratings.append(ratingForJob)
            print(ratings)
        return currentJobid, ratings

    def rating(jobId, currentJobid, ratings, jobsDone, jobsDoneId):
        sumRatings = 0
        avgRatings = 0
        for rating in ratings:
            if currentJobid in jobsDoneId:
                sumRatings = sumRatings + rating
                print(sumRatings)
                avgRatings = sumRatings / len(ratings)
                print(avgRatings)
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
        currentJobid, ratings = inputRating(jobsDone)
        jobsDoneId, avgRatings = rating(jobId, currentJobid, ratings, jobsDone, jobsDoneId)
        output(jobsDone, sumMoney, avgRatings)

    main()
app()
