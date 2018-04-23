def convert_from_string(context, string_value):
    if string_value == 'first':
        return 1

    elif string_value == 'second':
        return 2

    elif string_value == 'heading':
        return context.additional_data['head_block_number'] if context.additional_data['head_block_number'] else 1

    elif string_value == 'preheading':
        return context.additional_data['head_block_number'] - 1 if context.additional_data['head_block_number'] else 1

    elif string_value == 'future':
        return context.additional_data['head_block_number'] + 1 if context.additional_data['head_block_number'] else 1

    elif is_int(string_value):
        return int(string_value)

    elif string_value == 'None':
        return None

    else:
        return string_value


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False