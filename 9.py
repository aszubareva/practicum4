print("Собака короткошерстной породы?")
answer = input().lower()

if answer == "да":
    print("Рост собаки менее 50 см?")
    answer = input().lower()
    
    if answer == "да":
        print("У собаки короткий хвост?")
        answer = input().lower()
        
        if answer == "да":
            print("английский бульдог")
        else:
            print("У собаки длинные уши?")
            answer = input().lower()
            
            if answer == "да":
                print("гончая")
            else:
                print("У собаки короткое тело?")
                answer = input().lower()
                
                if answer == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        print("Собака весит более 50 кг?")
        answer = input().lower()
        
        if answer == "да":
            print("датский дог")
        else:
            print("фоксхаунд")
else:
    print("Рост собаки менее 50 см?")
    answer = input().lower()
    
    if answer == "да":
        print("У собаки доброжелательный характер?")
        answer = input().lower()
        
        if answer == "да":
            print("кокер-спаниель")
        else:
            print("ирландский сеттер")
    else:
        print("У собаки рост менее 70 см?")
        answer = input().lower()
        
        if answer == "да":
            print("У собаки длинные уши?")
            answer = input().lower()
            
            if answer == "да":
                print("большой вандейский гриффон")
            else:
                print("колли")
        else:
            print("Окрас рыжий с белыми отметинами?")
            answer = input().lower()
            
            if answer == "да":
                print("сенбернар")
            else:
                print("У собаки белый окрас?")
                answer = input().lower()
                
                if answer == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")
