from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setup(self):
        meeting=Meeting(meetingtitle='Sams meeting',meetingdate='2022/02/04',meetingtime='2022/02/04 15:04:12-08', location='Seattle', agenda='A meeting')
        return meeting

    def test_meetingtable(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

    def test_titlestring(self):
        meeting=self.setup()
        self.assertEqual(str(meeting.meetingtitle), 'Sams meeting')
    
    def test_meetingdate(self):
        meeting=self.setup()
        self.assertEqual(str(meeting.meetingdate), '2022/02/04')

    def test_meetingtime(self):
        meeting=self.setup()
        self.assertEqual(str(meeting.meetingtime), '2022/02/04 15:04:12-08')

    def test_meetinglocation(self):
        meeting=self.setup()
        self.assertEqual(str(meeting.location), 'Seattle')

    def test_meetingagenda(self):
        meeting=self.setup()
        self.assertEqual(str(meeting.agenda), 'A meeting')

class MeetingMinutesTest(TestCase):
    def setup(self):
        meeting=Meeting(meetingtitle='Sams meeting',meetingdate='2022/02/04',meetingtime='2022/02/04 15:04:12-08', location='Seattle', agenda='A meeting')
        minutes=MeetingMinutes(meetingid=meeting, minutestext='test minutes text')
        return minutes

    def test_meetingminutestable(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

    def test_minutestext(self):
        minutes=self.setup()
        self.assertEqual(str(minutes.minutestext), 'test minutes text')

class ResourceTest(TestCase):
    def setup(self):
        resource=Resource(resourcename='name test', resourcetype='type test', url='www.testurl.com', dateentered='test date', description='test description')
        return resource
    
    def test_resourcetable(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

    def test_resourcename(self):
        resource=self.setup()
        self.assertEqual(str(resource.resourcename), 'name test')

    def test_resourcetype(self):
        resource=self.setup()
        self.assertEqual(str(resource.resourcetype), 'type test')

    def test_resourceurl(self):
        resource=self.setup()
        self.assertEqual(str(resource.url), 'www.testurl.com')

    def test_dateentered(self):
        resource=self.setup()
        self.assertEqual(str(resource.dateentered), 'test date')

    def test_resourcedescription(self):
        resource=self.setup()
        self.assertEqual(str(resource.description), 'test description')

class EventTest(TestCase):
    def setup(self):
        event=Event(eventtitle='test title', location='test location', eventdate='test date', eventtime='test time', description='test description')
        return event

    def test_eventtable(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

    def test_eventitle(self):
        event=self.setup()
        self.assertEqual(str(event.eventtitle), 'test title')

    def test_eventlocation(self):
        event=self.setup()
        self.assertEqual(str(event.location), 'test location')

    def test_eventdate(self):
        event=self.setup()
        self.assertEqual(str(event.eventdate), 'test date')

    def test_eventtime(self):
        event=self.setup()
        self.assertEqual(str(event.eventtime), 'test time')

    def test_eventdescription(self):
        event=self.setup()
        self.assertEqual(str(event.description), 'test description')
   

class New_Meeting_Authentification_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.meeting=Meeting.objects.create(meetingtitle='Sams meeting',meetingdate='2022/02/04',meetingtime='2022/02/04 15:04:12-08', location='Seattle', agenda='A meeting')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')