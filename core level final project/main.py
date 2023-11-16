import valid
import bookdata
import memberdata
import borrowingsystem
import reportingsystem
while True:
    print('1.Add a book\n2.Update a book \n3.Delete a book\n4.Search for a book\
            \n5.Add a member\n6.Update a member\n7.Delete a member\n8.Search for a member\
            \n9.Borrow a book\n10.Return a book\n11.Generate book availability report\
            \n12.Genenrate member borrowing history report\n13.Generate overdue book report\
            \n14.show all books\n15.Exit')
    ch=input('Enter your choice :')
    if ch=='1':
        reportingsystem.s1.add_book()
    elif ch=='2':
        reportingsystem.s1.update_book()
    elif ch=='3':
        reportingsystem.s1.delete_book()
    elif ch=='4':
        reportingsystem.s1.search_book()
    elif ch=='5':
        reportingsystem.s1.add_member()
    elif ch=='6':
        reportingsystem.s1.update_member()
    elif ch=='7':
        reportingsystem.s1.delete_member()
    elif ch=='8':
        reportingsystem.s1.search_member()
    elif ch=='9':
        reportingsystem.s1.borrow_book()
    elif ch=='10':
        reportingsystem.s1.return_book()
    elif ch=='11':
        reportingsystem.s1.book_availability()
    elif ch=='12':
        reportingsystem.s1.borrowing_history()
    elif ch=='13':
        reportingsystem.s1.overdue_report()
    elif ch=='14':
        reportingsystem.s1.show_all_available_books()
    elif ch=='15':
        break
    else:
        print('please enter the valid choice')
