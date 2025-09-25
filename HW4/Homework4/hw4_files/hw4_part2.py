from hw4_util import part2_get_week, print_abbreviations


#setting up the loop
week = 1
print("...")
while week >= 0:
    week = int(input("Please enter the index for a week: "))
    print(week)
    if week < 0:
        break
    elif week > 29 or week == 0:
        print("No data for that week")
    else:
        weeklist = part2_get_week(week)
        request = str(input("Request (daily, pct, quar, high): "))
        print(request)
        request = request.lower()
        
#daily
        
        if request == "daily":
            abbreviation = str(input("Enter the state: "))
            print(abbreviation)
            abbreviation = abbreviation.upper()
            statecheck = 0
            for i in weeklist:
                if i[0] == abbreviation:
                    data = i
                    statecheck += 1
            if statecheck == 0:
                print("State", abbreviation, "not found")
            else:
                pop = int(data[1])
                number = pop/100000
                positive = sum(data[2:9])
                per = (positive/7)/number
                per = per*1.0
                per = round(per, 1)
                print("Average daily positives per 100K population:", per)
                
#pct

        elif request == "pct":
            abbreviation = str(input("Enter the state: "))
            print(abbreviation)
            abbreviation = abbreviation.upper()
            statecheck = 0
            for i in weeklist:
                if i[0] == abbreviation:
                    data = i
                    statecheck += 1
            if statecheck == 0:
                print("State", abbreviation, "not found")
            else:
                positive = sum(data[2:9])
                negative = sum(data[9:16])
                percent = (positive/(positive+negative))*100.0
                percent = round(percent, 1)
                print("Average daily positive percent:", percent)
                
#quar

        elif request == "quar":
            states = []
            for i in weeklist:
                data = i
                state = data[0]
                pop = int(data[1])
                positive = sum(data[2:9])
                negative = sum(data[9:16])
                number = pop/100000
                per = (positive/7)/number
                per = per*1.0
                per = round(per,1)
                percent = (positive/(positive+negative))*100.0
                percent = round(percent, 1)
                if per > 10 or percent > 10:
                    states.append(state)
            print("Quarantine states:")
            print_abbreviations(states)
        
#high
        elif request == "high":
            highest = 0
            state = ""
            for i in weeklist:
                data = i
                pop = int(data[1])
                number = pop/100000
                positive = sum(data[2:9])
                per = (positive/7)/number
                per = per*1.0
                per = round(per, 1)
                if per > highest:
                    highest = per
                    state = str(data[0])
            print("State with highest infection rate is", state)
            print("Rate is", highest, "per 100,000 people")


#request-invalid       
        else:
            print("Unrecognized request")



#final dots
    print("...")      