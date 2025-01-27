
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            creed = get_credentials()
            service = build("calendar", "v3", credentials=creed)
            
            summary = form.cleaned_data['summary']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            start_datetime = form.cleaned_data['start_datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')
            end_datetime = form.cleaned_data['end_datetime'].strftime('%Y-%m-%dT%H:%M:%S%z')
            timezone = form.cleaned_data['timezone']
            attendee1_email = form.cleaned_data['attendee1_email']
            attendee2_email = form.cleaned_data['attendee2_email']
            
            event = {
                "summary": summary,
                "location": location,
                "description": description,
                "start": {"dateTime": start_datetime, "timeZone": timezone},
                "end": {"dateTime": end_datetime, "timeZone": timezone},
                "attendees": [{'email': attendee1_email}, {'email': attendee2_email}]
            }
            
            try:
                created_event = service.events().insert(calendarId="primary", body=event).execute()
                message = f"Event created: {created_event.get('htmlLink')}"
            except HttpError as error:
                message = f"An error occurred: {error}"
            
            return HttpResponse(message)
    else:
        form = EventForm()
    exam = models.Exam.objects.all()
    department = models.School.objects.all()
    context = {'department': department, 'exam': exam, 'form': form}
    return render(request,'create_event.html',context)
