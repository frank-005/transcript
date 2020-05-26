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
        return jobsDone, jobsDoneId, totalMoneyEarned

    def money(totalMoneyEarned):
        sumMoney = 0
        for i in totalMoneyEarned:
            sumMoney = sumMoney + i
        return sumMoney

    def inputRating(jobsDone, jobsDoneId):
        ratings = []
        for x in range(int(jobsDone)):
            currentJobid = input("Job Id for job whose rating you want to give: ")
            if currentJobid in jobsDoneId:
                ratingForJob = int(input("What is the rating? "))
                ratings.append(ratingForJob)
            else:
                print("The job Id is not in our records")
                inputRating(jobsDone, jobsDoneId)

        return ratings

    def rating(ratings):
        sumRatings = 0
        avgRatings = 0
        for rating in ratings:
            sumRatings = sumRatings + rating
            avgRatings = sumRatings / len(ratings)
        return avgRatings

    def convert(sumMoney):
        kenyan = sumMoney * 103
        return kenyan

    def output(jobsDone, sumMoney, avgRatings, kenyan):
        print("You have done "  + str(jobsDone) + " job during this period")
        print("And you have earned $" + str(round(sumMoney, 2)) + " dollars")
        print("Which translates to " + str(int(kenyan)) + " Kenyan Shillings")
        print("Your average rating for this period is: " + str(round(avgRatings, 1)))

    def main():
        jobsDone, jobsDoneId, totalMoneyEarned = inputJob()
        sumMoney = money(totalMoneyEarned)
        ratings = inputRating(jobsDone, jobsDoneId)
        avgRatings = rating(ratings)
        kenyan = convert(sumMoney)
        output(jobsDone, sumMoney, avgRatings, kenyan)

    main()
if __name__ == "__main__":
    app()
