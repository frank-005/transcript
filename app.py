def app():
    

    def inputJob():
        jobsDone = int(input("How many jobs have you done today?"))
        for x in range(int(jobsDone)):
            jobId = input("Enter the Job Id: ")
            moneyEarned = float(input("How much did you earn on this job? "))
        return jobId, moneyEarned, jobsDone

     

    def money(moneyEarned):
        totalMoneyEarned = []
        totalMoneyEarned.append(moneyEarned)   
        sumMoney = 0
        for i in totalMoneyEarned:
            sumMoney = sumMoney + i
        return sumMoney

    def inputRating():
        currentJobid = input("Job Id for job whose rating you want to give: ")
        ratingForJob = int(input("What is the rating? "))
        return currentJobid, ratingForJob
    
    def rating(jobId, currentJobid, ratingForJob):
        jobsDoneId = []
        jobsDoneId.append(jobId)
        if currentJobid in jobsDoneId:
            ratings = []
            ratings.append(ratingForJob)
            sumRatings = 0
            avgRatings = 0
            for x in ratings:
                sumRatings = sumRatings + x
                avgRatings = sumRatings / len(ratings)
                print(avgRatings)
            
        else:
            print("The job Id is not in our records")
            inputRating()
        return jobsDoneId, avgRatings

    def output(jobsDone, sumMoney, avgRatings):
        print("You have done "  + str(jobsDone) + " job during this period")
        print("And you have earned " + str(sumMoney))
        print("Your average rating for this period is: " + str(avgRatings))

    def main():
        jobId, moneyEarned, jobsDone = inputJob()
        sumMoney = money(moneyEarned)
        currentJobid, ratingForJob = inputRating()
        jobsDoneId, avgRatings = rating(jobId, currentJobid, ratingForJob)
        output(jobsDone, sumMoney, avgRatings)




    main()
app()