from enum import Enyum

class EmployeeType(Enum):
    RESPONDENT  = 1
    MANAGER     = 2
    DIRECTOR    = 3

class CallStatus(Enum):
    NORMAL              = 1
    FIRST_ESCALATION    = 2
    SECOND_ESCALATION   = 3


class Employee:
    def __init__(self, EmployeeType: type): 
        super().__init__()
        self.type = type 

class Call():
    def __init__(self, customer):
        self.customer = ''
        self.status = CallStatus.NORMAL
        self.assigned_employee = None

    def assigned_employee(self, Employee: employee):
        self.assigned_employee = employee


class CallCenter:
    def __init__(self):
        self.employees = []
        self.available_respondents = [] # QUEUE
        self.available_manager = [] # QUEUE
        self.available_responders = [] # QUEUE
        self.active_calls = []
        self.pending_normal_calls = []
        self.pending_escalated1_calls = []
        self.pending_escalated2_calls = []

    
    def loadEmployess(self, list):
        self.employees = list

    def add_available_employee(self, Employee: emp):
        #add it to the queue or take pendingcalls based on 
        return
    
    def dispatchCall(self, Call: call):
        # add it to the queue or take it if and Emp is available
        if call.status == CallStatus.NORMAL:
            if len(self.available_responders) > 0:
                call.assigned_employee = self.available_responders.pop()
                self.active_calls.append(call)
            else:
                pass
        return

    def escalated_call(self, Call: call):
        return


        

    # how to scalate
    

