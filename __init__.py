#Соберите из созданных на уроке и в рамках домашнего задания 
# функций пакет для работы с файлами.




from .seminar_1 import number_to_file
from .seminar_2 import write_names_to_file
from .seminar_3 import combining_func
from .seminar_4_6 import func_new_files
from .seminar_7 import sorted_func
from .Task1HW7 import group_rename


__all__ = ['number_to_file', 'write_names_to_file', 
'combining_func', 
'func_new_files', 'sorted_func', 'group_rename']