from math import inf

def chk_dt_student(obj):
    v = check_id('student', obj['id'], '#', 6)
    if not v: return True
    obj['id'] = v
    a = check_if_empty('student', obj['name'])
    if not a: return True
    a = check_if_empty('student', obj['surname'])
    if not a: return True
    a = check_range('student', 'age', 16, inf, obj['age'])
    if not a: return True
    a = check_range('student', 'undergrduate year', 1, 4, obj['undergraduate_year'])
    if not a: return True
    clss = obj['classes']
    for i in range(len(clss)):
        s = check_id('class', clss[i], '$', 4)
        if not s: return True
        clss[i] = s
    return False

def chk_dt_teacher(obj):
    v = check_id('teacher', obj['id'], '@', 5)
    if not v: return True
    obj['id'] = v
    a = check_if_empty('teacher', obj['name'])
    if not a: return True
    a = check_if_empty('teacher', obj['surname'])
    if not a: return True
    a = check_range('teacher', 'age', 26, inf, obj['age'])
    if not a: return True
    clss = obj['classes']
    for i in range(len(clss)):
        s = check_id('class', clss[i], '$', 4)
        if not s: return True
        clss[i] = s
    return False

def chk_dt_grades(obj):
    v = check_id('grade', obj['id'], '%', 9)
    if not v: return True
    obj['id'] = v
    s = check_id('student', obj['student_id'], '#', 6)
    if not s: return True
    obj['student_id'] = s
    t = check_id('class', obj['class_id'], '$', 4)
    if not t: return True
    obj['class_id'] = t
    a = check_range('grade', 'midterm_1', -1, 100, obj['midterm_1'])
    if not a: return True
    a = check_range('grade', 'midterm_2', -2, 100, obj['midterm_2'])
    if not a: return True
    a = check_range('grade', 'final', -1, 100, obj['final'])
    if not a: return True
    return False

def chk_dt_classes(obj):
    v = check_id('class', obj['id'], '$', 4)
    if not v: return True
    obj['id'] = v
    a = check_if_empty('class', obj['name'])
    if not a: return True
    tecs = obj['teacher']
    for i in range(tecs):
        s = check_id('teacher', tecs[i], '@', 5)
        if not s: return True
        tecs[i] = s
    stds = obj['students']
    for i in range(len(stds)):
        t = check_id('student', stds[i], '#', 6)
        if not t: return True
        stds[i] = t
    return False

def check_for_error(obj, file):
    if file == 'students': return chk_dt_student(obj)
    if file == 'teachers': return chk_dt_teacher(obj)
    if file == 'grades': return chk_dt_grades(obj)
    if file == 'classes': return chk_dt_classes(obj)
    
def check_id(obj_name, id, s, l):
    if len(id) == 0 or id[0] != s:
        print(f'{obj_name} must start with {s}')
        return False
    if len(id) > l:
        print(f'{obj_name} id must be < {10 ** (l - 1)}')
        return False
    try:
        id = id[0] + str(int(id[1:]))
    except:
        print(f'{obj_name} id must be a number between 0 and {10 ** (l - 1) - 1}')
        return False
    return id

def check_if_empty(obj_name, label):
    if len(label) == 0:
        print(f'{obj_name} {label} must not be empty')
        return False
    return True

def check_range(obj_name, label, lower, upper, n):
    if n < lower:
        print(f'{obj_name} {label} must be >= {lower}')
        return False
    if n > upper:
        print(f'{obj_name} {label} must be <= {upper}')
        return False
    return True
