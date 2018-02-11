"""
    Python wrapper for HSE RUZ API

    Usage
    -----
    import ruz
    assert ruz.person_lessons("mymail@edu.hse.ru")
"""

from ruz.main import (auditoriums, buildings, chairs, faculties,
                      get_formated_date, groups, is_hse_email, is_student,
                      is_valid_hse_email, kind_of_works, lecturers,
                      person_lessons, schedules, staff_of_group,
                      staff_of_streams, streams, sub_groups,
                      type_of_auditoriums)


__author__ = "Dmitriy Pchelkin | hell03end"
__version__ = (2, 0, 0)
