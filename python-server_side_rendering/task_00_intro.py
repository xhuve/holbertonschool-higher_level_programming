
def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template, str):
        print("template should be a string")
        return
    
    if not all([isinstance(value, dict) for value in attendees]):
        print("attendees should be a list of dict's")
        return
    
    for i, attendee in enumerate(attendees):
        personal_template = template
        for attr, value in attendee.items():
            if not value:
                value = "N/A"
            personal_template = personal_template.replace('{' + attr + '}', value)
        with open('output_' + str(i + 1) + ".txt", 'w', encoding="utf-8") as f:
            f.write(personal_template)

    


