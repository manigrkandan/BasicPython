class multipleFunctions():
    def SubFields():
        subfields = [
            'Machine Learning',
            'Neural Networks',
            'Vision',
            'Robotics',
            'Speech Processing',
            'Natural Language Processing'
        ]
        print('Sub-fields in AI are:')
        for field in subfields:
            print(field)

    def OddEven():
        number = int(input('Enter a number:'))
        if(number%2 == 0):
            print(f"{number} is even number.")
        else:
            print(f"{number} is odd number.")

    def percentage10():
        marklist = [89,93,95,85,97]
        total = 0
        num_subjects = len(marklist)
        for i, mark in enumerate(marklist):
            print(f"Subject {i+1} = {mark}")
            total += mark
        max_marks = num_subjects * 100
        percentage = (total/max_marks) * 100
        print(f"Total marks: {total}")
        print(f"Percentage: {percentage}")

    def marriageEligibility():
        inputAge = int(input('Enter your age '))
        inputGender = input('Enter your gender ')
        print(f"Your Age: {inputAge}")
        print(f"Your Gender: {inputAge}")
        if inputAge > 21:
            print('You are eligible for marriage')
        else:
            print('You are not eligible for marriage')

    def triangle():
        height = 10
        height1 = 11
        height2 = 22
        breadth = 20
        area = height * breadth * 0.5
        print(f"Height: {height}")
        print(f"Breadth: {breadth}")
        print("Area Formula: (Height*Breadth)/2")
        print('Area of triangle is ', area)
        print(f"Height1: {height1}")
        print(f"Height2: {height2}")
        print(f"Breadth: {breadth}")
        perimeter = height1 + height2 + breadth
        print('Perimeter of triangle is ', perimeter)
        



