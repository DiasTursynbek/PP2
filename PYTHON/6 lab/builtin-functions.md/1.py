import math
numbers = list(map(int,input("put the number: ").split()))
result = math.prod(numbers)
print(result)





# ✅ Абсолютный путь — удобен, если работаешь с файлом из разных мест и хочешь, чтобы путь всегда был однозначным.
# ✅ Относительный путь — удобен, если работаешь в проекте и не хочешь жёстко привязываться к конкретной системе.



# try block:
#     with open(filename) as f_obj:
#         contests=f_obj.read()
                                        # -----------------------> ABOUT TRY BLOCK AND EXCEPT BLOCK
# except block FileNotFoundError:
#     msg="Sorry , the file " + filename + " does not exist."
#     print(msg)



#                                         DIFFERENCE
# with open() --> сама открывает и закрывает  |  open() --> само открывает и нужно закрыть close()