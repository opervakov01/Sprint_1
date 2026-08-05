types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(ticket_lists):
    unique_tickets = {}
    for level, ticket_list in ticket_lists.items():
        unique_tickets[level] = list(set(ticket_list))
    return unique_tickets

def create_tickets_by_type(types_dict, tickets_dict):
    unique_tickets = remove_duplicates(tickets_dict)
    used_tickets = set()
    result = {}
    
    for level_num in range(1, 6):
        level_name = types_dict[level_num]
        current_tickets = unique_tickets[level_num]
        filtered_tickets = []
        for ticket in current_tickets:
            if ticket not in used_tickets:
                filtered_tickets.append(ticket)
                used_tickets.add(ticket)
        result[level_name] = filtered_tickets    
    return result

tickets_by_type = create_tickets_by_type(types, tickets)
print(tickets_by_type)