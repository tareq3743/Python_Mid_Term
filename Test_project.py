class Star_sinema():
        hall_list = []
        
        def entry_hall(self, hall):
            self.hall_list.append(hall)


class Hall(Star_sinema):
    def __init__(self, rows, columns, hall_no) -> None:
        
        self.__rows = rows 
        self.__columns = columns
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        Star_sinema().entry_hall(self)
        # temp = Star_sinema()
        # temp.entry_hall(self)

        for i in range(rows):
            row = [0 for j in range(columns)]
            self.__seats[i] = row


    def entry_show(self, id, movie_name, time):
        tp = (id,movie_name,time)
        self.__show_list.append(tp)
        pass

    def book_seats(self):
        id = int(input("Enter Movie id : "))
        check = any(item[0] == id for item in self.__show_list)
        if check == True:
            ticket = int(input("Number of Ticket : "))
            for i in range(ticket):
                row = int(input("Enter Row : "))
                column = int(input("Enter Column : "))
                if self.__rows<row and self.__columns<column:
                    print("You Entered out of Range ")
                    return
                elif self.__seats[row][column] != 1:
                    self.__seats[row][column] = 1
                    print(f'\nrow : {row} & column : {column}  \n\tBooked Successfully!!')
                else:
                    print(f'\nrow : {row} & column : {column} is Already Booked!! \n\tTry Another One')
        else:
            print(f'\n\tThere is no show According to {id} serial')
            

    def view_show_list(self):
        for key, value in enumerate(self.__show_list):
            print(f'{value}')

    def view_available_seat(self):
        for i in self.__seats.values():
            print(i)
        print()
            

hall = Hall(5,5,1001)
hall.entry_show(101,"Bilal: A New Breed of Hero (2015)", "7:00PM, 10 june, 2024")
hall.entry_show(102,"Muhammad: The Last Prophet (2002)", "7:00PM, 11 june, 2024")


while True:
    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    check = int(input("Enter Option: "))

    if check == 1:
        hall.view_show_list()
        print("\n\n")
    elif check == 2:
        hall.view_available_seat()
        print("\n\n")
    elif check == 3:
        hall.book_seats()
        print("\n\n")
    elif check == 4:
        print("\n\n")
        break
    else:
        print("Press Right Key")
        print("\n\n")
















# hall = Hall(5,5,101)
# cinema = Star_sinema()

# # hall.book_seats()
# hall.entry_show(101,"Love At First Site", "7:00PM, 10 june, 2024")
# hall.entry_show(102,"Love At Second Site", "7:00PM, 11 june, 2024")
# hall.view_show_list()
# hall.book_seats()

# # hall.view_available_seat()
# cinema.entry_hall(20,20,101)

