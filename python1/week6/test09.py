def get_formatted_name(last, first, opt=''):
    ßfullname = ''
    if opt == 'eng':
        fullname = f"{first} {last}".title()
    else:
        fullname = f"{last}{first}"

    return fullname


print(get_formatted_name('handrix', 'jimi', 'eng'))
print(get_formatted_name('김', '석진'))
print(get_formatted_name('김', '석진', 'jp'))
