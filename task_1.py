time_values = ('1h 45m,360s,25m,30m 120s,2h 60s')
total_minutes = 0

time_parts = time_values.split(',')

for time_value in time_parts:
    time_value = time_value.replace(' ', '')
    
    hours = 0
    minutes = 0
    seconds = 0
    
    if 'h' in time_value:
        parts = time_value.split('h')
        hours = int(parts[0])
        time_value = parts[1]
    
    if 'm' in time_value:
        parts = time_value.split('m')
        minutes = int(parts[0])
        time_value = parts[1]
    
    if 's' in time_value:
        parts = time_value.split('s')
        seconds = int(parts[0])
    
    total_minutes += hours * 60 + minutes + seconds // 60

print(total_minutes)