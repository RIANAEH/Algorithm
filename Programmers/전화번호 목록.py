def solution(phone_book):
    phone_book.sort() # 와...
    
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
    return True
    
    # for i in range(len(phone_book)-1):
    #     for j in range(1, len(phone_book)):
    #         if len(phone_book[i]) < len(phone_book[j]):
    #             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
    #                 return False
    #         if len(phone_book[j]) < len(phone_book[i]):
    #             if phone_book[j] == phone_book[i][:len(phone_book[j])]:
    #                 return False
    # return True
    
    # for phone1 in phone_book:
    #     for phone2 in phone_book:
    #         if len(phone1) < len(phone2):
    #             if phone1 == phone2[:len(phone1)]:
    #                 return False
    # return True
