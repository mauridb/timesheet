from import_export import resources
from balance.models import Timesheet


class TimesheetResource(resources.ModelResource):
    class Meta:
        model = Timesheet
