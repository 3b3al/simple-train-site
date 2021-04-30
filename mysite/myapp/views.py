from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    return render(request,'index.html',{})

def homeView(request):
    stations=Station.objects.all()
    context={
        "stations" : stations,
        "st" : stations[0:4]
    }
    return render(request,'index.html',context)

'''def searchView(request):
    source = Station.objects.get(pk=request.POST['source'])
    dest = Station.objects.get(pk=request.POST['dest'])
    date = request.POST['journey_date']
    sourceTrains = []
    for s in source.station_schedule.all():
        sourceTrains.append(s.train)
    destTrains = []
    for s in dest.station_schedule.all():
        destTrains.append(s.train)
    allTrains=list(set(sourceTrains) & set(destTrains))


    trains=[]
    sourceSchedules=[]
    destSchedules=[]
    scheduleCharts=[]
    fares=[]
    for t in allTrains:
        departing_station = t.train_schedule.get(station=source)
        arriving_station = t.train_schedule.get(station=dest)
        if departing_station.pk < arriving_station.pk:
            scheduleCharts.append(Seat_Chart.objects.get(date=parser.parse(date),train=t))
            trains.append(t)
            sourceSchedules.append(departing_station)
            destSchedules.append(arriving_station)
            fare={}
            fare["1A"]=(arriving_station.pk - departing_station.pk)*20
            fare["2A"]=(arriving_station.pk - departing_station.pk)*15
            fare["3A"]=(arriving_station.pk - departing_station.pk)*10
            fare["SL"]=(arriving_station.pk - departing_station.pk)*5
            fares.append((fare))

    schedules=zip(trains,sourceSchedules,destSchedules,scheduleCharts,fares)
    data={
        "source": source,
        "dest": dest,
        "schedules":schedules,
        "date": date,
    }
    return render(request,'book/trainSearch.html',data)'''

'''def complexSearchView(request,source,dest,date):
    source = Station.objects.get(pk=source)
    dest = Station.objects.get(pk=dest)
    sourceTrains = []
    for s in source.station_schedule.all():
        sourceTrains.append(s.train)
    destTrains = []
    for s in dest.station_schedule.all():
        destTrains.append(s.train)
    # allTrains=list(set(sourceTrains) & set(destTrains))

    trains1 = []
    trains2 = []
    sourceSchedules = []
    commonSchedules1 = []
    commonSchedules2 = []
    destSchedules = []
    scheduleCharts1 = []
    scheduleCharts2 = []
    fares=[]


    for ts in sourceTrains:
        sourceSchedule=source.station_schedule.get(train=ts)
        source_stations = []
        for a in ts.train_schedule.filter(id__gte=sourceSchedule.id):
            source_stations.append(a.station)
        for td in destTrains:
            destSchedule = dest.station_schedule.get(train=td)
            dest_stations = []
            for a in td.train_schedule.filter(id__lte=destSchedule.id):
                dest_stations.append(a.station)
            common = list(set(source_stations) & set(dest_stations))
            for c in common:
                tempDestSchedule=c.station_schedule.get(train=ts)
                tempSourceSchedule=c.station_schedule.get(train=td)
                if(tempDestSchedule.arrival < tempSourceSchedule.departure):
                    trains1.append(ts)
                    trains2.append(td)
                    commonSchedules1.append(tempDestSchedule)
                    commonSchedules2.append(tempSourceSchedule)
                    sourceSchedules.append(sourceSchedule)
                    destSchedules.append(destSchedule)
                    c1=Seat_Chart.objects.get(date=parser.parse(date),train=ts)
                    c2=Seat_Chart.objects.get(date=parser.parse(date),train=td)
                    scheduleCharts1.append(c1)
                    scheduleCharts2.append(c2)
                    # fares.append(None)
                    fare = {}
                    fare["1A"] = (destSchedule.pk - tempSourceSchedule.pk + tempDestSchedule.pk - sourceSchedule.pk) * 20
                    fare["2A"] = (destSchedule.pk - tempSourceSchedule.pk + tempDestSchedule.pk - sourceSchedule.pk) * 15
                    fare["3A"] = (destSchedule.pk - tempSourceSchedule.pk + tempDestSchedule.pk - sourceSchedule.pk) * 10
                    fare["SL"] = (destSchedule.pk - tempSourceSchedule.pk + tempDestSchedule.pk - sourceSchedule.pk) * 5
                    fares.append((fare))
                    break

    schedules=zip(trains1,trains2,sourceSchedules,commonSchedules1,commonSchedules2,destSchedules,scheduleCharts1,scheduleCharts2,fares)
    data={
        "source": source,
        "dest": dest,
        "schedules":schedules,
        "date": date,
    }
    return render(request,'book/connectingTrainSearch.html',data)
'''


def bookView(request):
    chart = Seat_Chart.objects.get(pk=chart)
    train = chart.train
    sourceSchedule=Schedule.objects.get(pk=sourceSchedule)
    destSchedule=Schedule.objects.get(pk=destSchedule)
    source = sourceSchedule.station
    dest = destSchedule.station
    data = {
        "train": train,
        "chart": chart,
        "source": source,
        "destination": destination,
        "dest":dest,
        "type":type,
        "date":date,
    }
    return render(request,'book/booking.html',data)

'''
def complexBookView(request,chart1,chart2,sourceSchedule,commonSchedule1,commonSchedule2,destSchedule,type,date):
    chart1 = Seat_Chart.objects.get(pk=chart1)
    chart2 = Seat_Chart.objects.get(pk=chart2)
    train1 = chart1.train
    train2 = chart2.train
    sourceSchedule=Schedule.objects.get(pk=sourceSchedule)
    commonSchedule1=Schedule.objects.get(pk=commonSchedule1)
    commonSchedule2=Schedule.objects.get(pk=commonSchedule2)
    destSchedule=Schedule.objects.get(pk=destSchedule)
    source = sourceSchedule.station
    dest = destSchedule.station
    data = {
        "train1": train1,
        "train2": train2,
        "chart1": chart1,
        "chart2": chart2,
        "sourceSchedule": sourceSchedule,
        "commonSchedule1": commonSchedule1,
        "commonSchedule2": commonSchedule2,
        "destSchedule": destSchedule,
        "source":source,
        "dest":dest,
        "type":type,
        "date":date,
    }
    return render(request,'book/complexBooking.html',data)
'''

def confirmTicketView(request,chart,sourceSchedule,destSchedule,type,date):
    chart=Seat_Chart.objects.get(pk=chart)
    train=chart.train
    sourceSchedule=Schedule.objects.get(pk=sourceSchedule)
    destSchedule=Schedule.objects.get(pk=destSchedule)
    source = sourceSchedule.station
    dest = destSchedule.station
    
    seats=int(request.POST["seats"])
    for i in range(seats):
        name=request.POST.get("name"+str(i))
        b=Ticket()
        b.passenger=name
        b.train=train
        b.type=type
        b.chart=chart
      
        b.source=source
        b.dest=dest
        
        b.date = date
        
        b.save()


    data = {
        "train": train,
        "sourceSchedule": sourceSchedule,
        "destSchedule": destSchedule,
        "source":source,
        "dest":dest,
        "type":type
    }
    return render(request, 'book/home.html')

'''
def complexConfirmTicketView(request,chart1,chart2,sourceSchedule,commonSchedule1,commonSchedule2,destSchedule,type,date):
    chart1 = Seat_Chart.objects.get(pk=chart1)
    chart2 = Seat_Chart.objects.get(pk=chart2)
    train1 = chart1.train
    train2 = chart2.train
    sourceSchedule = Schedule.objects.get(pk=sourceSchedule)
    commonSchedule1 = Schedule.objects.get(pk=commonSchedule1)
    commonSchedule2 = Schedule.objects.get(pk=commonSchedule2)
    destSchedule = Schedule.objects.get(pk=destSchedule)
    source = sourceSchedule.station
    dest = destSchedule.station
    user= request.user
    seats=int(request.POST["seats"])
    for i in range(seats):
        name=request.POST.get("name"+str(i))
        b=Ticket()
        b.passenger=name
        b.train=train1
        b.type=type
        b.chart=chart1
        b.user=user
        b.source=source
        b.dest=dest
        b.source_schedule=sourceSchedule
        b.dest_schedule=commonSchedule1
        b.date = date
        b.calculateFare()
        b.save()

        b = Ticket()
        b.passenger = name
        b.train = train2
        b.type = type
        b.chart = chart2
        b.user = user
        b.source = source
        b.dest = dest
        b.source_schedule = commonSchedule2
        b.dest_schedule = destSchedule
        b.date = date
        b.calculateFare()
        b.save()


    data = {
        "train1": train1,
        "train2": train2,
        "chart1": chart1,
        "chart2": chart2,
        "sourceSchedule": sourceSchedule,
        "commonSchedule1": commonSchedule1,
        "commonSchedule2": commonSchedule2,
        "destSchedule": destSchedule,
        "source":source,
        "dest":dest,
        "type":type,
        "date":date,
    }
    return render(request, 'book/home.html')
'''

'''
class cancelTicket(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Ticket
    success_url = reverse_lazy('book:profile')
    
    def dispatch(self, request, *args, **kwargs):
        pk=kwargs['pk']
        if request.user != Ticket.objects.get(pk=pk).user:
            return redirect('book:home')
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
        '''