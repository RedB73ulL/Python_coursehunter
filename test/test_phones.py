import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.all_phones_from_contact_view_page == merge_phones_like_on_contact_view_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", # удаляем пусты строки, и склеиваем по "\n"
                            map(lambda x: clear(x), # во всех элементах удаляем лишние элементы, которые перечислены в функции clear
                                filter(lambda x: x is not None, # выкидываем все пустые значения
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

#def merge_phones_like_on_contact_view_page(contact):
#    return "\n".join(filter(lambda x: x != "", # удаляем пусты строки, и склеиваем по "\n"
#                            map(lambda x: clear(x), # во всех элементах удаляем лишние элементы, которые перечислены в функции clear
#                                filter(lambda x: x is not None, # выкидываем все пустые значения
#                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
