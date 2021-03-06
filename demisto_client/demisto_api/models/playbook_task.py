# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.advance_arg import AdvanceArg  # noqa: F401,E501
from demisto_client.demisto_api.models.data_collection_form import DataCollectionForm  # noqa: F401,E501
from demisto_client.demisto_api.models.evidence_data import EvidenceData  # noqa: F401,E501
from demisto_client.demisto_api.models.field_mapping import FieldMapping  # noqa: F401,E501
from demisto_client.demisto_api.models.form_display import FormDisplay  # noqa: F401,E501
from demisto_client.demisto_api.models.notifiable_item import NotifiableItem  # noqa: F401,E501
from demisto_client.demisto_api.models.quiet_mode import QuietMode  # noqa: F401,E501
from demisto_client.demisto_api.models.reputation_calc_alg import ReputationCalcAlg  # noqa: F401,E501
from demisto_client.demisto_api.models.sla import SLA  # noqa: F401,E501
from demisto_client.demisto_api.models.task import Task  # noqa: F401,E501
from demisto_client.demisto_api.models.task_condition import TaskCondition  # noqa: F401,E501
from demisto_client.demisto_api.models.task_loop import TaskLoop  # noqa: F401,E501
from demisto_client.demisto_api.models.task_type import TaskType  # noqa: F401,E501
from demisto_client.demisto_api.models.task_view import TaskView  # noqa: F401,E501
from demisto_client.demisto_api.models.timer_trigger import TimerTrigger  # noqa: F401,E501


class PlaybookTask(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'conditions': 'list[TaskCondition]',
        'continue_on_error': 'bool',
        'default_assignee': 'str',
        'default_assignee_complex': 'AdvanceArg',
        'default_reminder': 'int',
        'evidence_data': 'EvidenceData',
        'field_mapping': 'list[FieldMapping]',
        'form': 'DataCollectionForm',
        'form_display': 'FormDisplay',
        'id': 'str',
        'ignore_worker': 'bool',
        'loop': 'TaskLoop',
        'message': 'NotifiableItem',
        'next_tasks': 'dict(str, list[str])',
        'note': 'bool',
        'quiet_mode': 'QuietMode',
        'reputation_calc': 'ReputationCalcAlg',
        'restricted_completion': 'bool',
        'script_arguments': 'dict(str, AdvanceArg)',
        'separate_context': 'bool',
        'skip_unavailable': 'bool',
        'sla': 'SLA',
        'sla_reminder': 'SLA',
        'task': 'Task',
        'task_id': 'str',
        'timer_triggers': 'list[TimerTrigger]',
        'type': 'TaskType',
        'view': 'TaskView'
    }

    attribute_map = {
        'conditions': 'conditions',
        'continue_on_error': 'continueOnError',
        'default_assignee': 'defaultAssignee',
        'default_assignee_complex': 'defaultAssigneeComplex',
        'default_reminder': 'defaultReminder',
        'evidence_data': 'evidenceData',
        'field_mapping': 'fieldMapping',
        'form': 'form',
        'form_display': 'formDisplay',
        'id': 'id',
        'ignore_worker': 'ignoreWorker',
        'loop': 'loop',
        'message': 'message',
        'next_tasks': 'nextTasks',
        'note': 'note',
        'quiet_mode': 'quietMode',
        'reputation_calc': 'reputationCalc',
        'restricted_completion': 'restrictedCompletion',
        'script_arguments': 'scriptArguments',
        'separate_context': 'separateContext',
        'skip_unavailable': 'skipUnavailable',
        'sla': 'sla',
        'sla_reminder': 'slaReminder',
        'task': 'task',
        'task_id': 'taskId',
        'timer_triggers': 'timerTriggers',
        'type': 'type',
        'view': 'view'
    }

    def __init__(self, conditions=None, continue_on_error=None, default_assignee=None, default_assignee_complex=None, default_reminder=None, evidence_data=None, field_mapping=None, form=None, form_display=None, id=None, ignore_worker=None, loop=None, message=None, next_tasks=None, note=None, quiet_mode=None, reputation_calc=None, restricted_completion=None, script_arguments=None, separate_context=None, skip_unavailable=None, sla=None, sla_reminder=None, task=None, task_id=None, timer_triggers=None, type=None, view=None):  # noqa: E501
        """PlaybookTask - a model defined in Swagger"""  # noqa: E501

        self._conditions = None
        self._continue_on_error = None
        self._default_assignee = None
        self._default_assignee_complex = None
        self._default_reminder = None
        self._evidence_data = None
        self._field_mapping = None
        self._form = None
        self._form_display = None
        self._id = None
        self._ignore_worker = None
        self._loop = None
        self._message = None
        self._next_tasks = None
        self._note = None
        self._quiet_mode = None
        self._reputation_calc = None
        self._restricted_completion = None
        self._script_arguments = None
        self._separate_context = None
        self._skip_unavailable = None
        self._sla = None
        self._sla_reminder = None
        self._task = None
        self._task_id = None
        self._timer_triggers = None
        self._type = None
        self._view = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if continue_on_error is not None:
            self.continue_on_error = continue_on_error
        if default_assignee is not None:
            self.default_assignee = default_assignee
        if default_assignee_complex is not None:
            self.default_assignee_complex = default_assignee_complex
        if default_reminder is not None:
            self.default_reminder = default_reminder
        if evidence_data is not None:
            self.evidence_data = evidence_data
        if field_mapping is not None:
            self.field_mapping = field_mapping
        if form is not None:
            self.form = form
        if form_display is not None:
            self.form_display = form_display
        if id is not None:
            self.id = id
        if ignore_worker is not None:
            self.ignore_worker = ignore_worker
        if loop is not None:
            self.loop = loop
        if message is not None:
            self.message = message
        if next_tasks is not None:
            self.next_tasks = next_tasks
        if note is not None:
            self.note = note
        if quiet_mode is not None:
            self.quiet_mode = quiet_mode
        if reputation_calc is not None:
            self.reputation_calc = reputation_calc
        if restricted_completion is not None:
            self.restricted_completion = restricted_completion
        if script_arguments is not None:
            self.script_arguments = script_arguments
        if separate_context is not None:
            self.separate_context = separate_context
        if skip_unavailable is not None:
            self.skip_unavailable = skip_unavailable
        if sla is not None:
            self.sla = sla
        if sla_reminder is not None:
            self.sla_reminder = sla_reminder
        if task is not None:
            self.task = task
        if task_id is not None:
            self.task_id = task_id
        if timer_triggers is not None:
            self.timer_triggers = timer_triggers
        if type is not None:
            self.type = type
        if view is not None:
            self.view = view

    @property
    def conditions(self):
        """Gets the conditions of this PlaybookTask.  # noqa: E501

        Conditions - optional list of conditions to run when task is conditional. we check conditions by their order (e.i. - considering the first one that satisfied)  # noqa: E501

        :return: The conditions of this PlaybookTask.  # noqa: E501
        :rtype: list[TaskCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PlaybookTask.

        Conditions - optional list of conditions to run when task is conditional. we check conditions by their order (e.i. - considering the first one that satisfied)  # noqa: E501

        :param conditions: The conditions of this PlaybookTask.  # noqa: E501
        :type: list[TaskCondition]
        """

        self._conditions = conditions

    @property
    def continue_on_error(self):
        """Gets the continue_on_error of this PlaybookTask.  # noqa: E501


        :return: The continue_on_error of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._continue_on_error

    @continue_on_error.setter
    def continue_on_error(self, continue_on_error):
        """Sets the continue_on_error of this PlaybookTask.


        :param continue_on_error: The continue_on_error of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._continue_on_error = continue_on_error

    @property
    def default_assignee(self):
        """Gets the default_assignee of this PlaybookTask.  # noqa: E501


        :return: The default_assignee of this PlaybookTask.  # noqa: E501
        :rtype: str
        """
        return self._default_assignee

    @default_assignee.setter
    def default_assignee(self, default_assignee):
        """Sets the default_assignee of this PlaybookTask.


        :param default_assignee: The default_assignee of this PlaybookTask.  # noqa: E501
        :type: str
        """

        self._default_assignee = default_assignee

    @property
    def default_assignee_complex(self):
        """Gets the default_assignee_complex of this PlaybookTask.  # noqa: E501


        :return: The default_assignee_complex of this PlaybookTask.  # noqa: E501
        :rtype: AdvanceArg
        """
        return self._default_assignee_complex

    @default_assignee_complex.setter
    def default_assignee_complex(self, default_assignee_complex):
        """Sets the default_assignee_complex of this PlaybookTask.


        :param default_assignee_complex: The default_assignee_complex of this PlaybookTask.  # noqa: E501
        :type: AdvanceArg
        """

        self._default_assignee_complex = default_assignee_complex

    @property
    def default_reminder(self):
        """Gets the default_reminder of this PlaybookTask.  # noqa: E501


        :return: The default_reminder of this PlaybookTask.  # noqa: E501
        :rtype: int
        """
        return self._default_reminder

    @default_reminder.setter
    def default_reminder(self, default_reminder):
        """Sets the default_reminder of this PlaybookTask.


        :param default_reminder: The default_reminder of this PlaybookTask.  # noqa: E501
        :type: int
        """

        self._default_reminder = default_reminder

    @property
    def evidence_data(self):
        """Gets the evidence_data of this PlaybookTask.  # noqa: E501


        :return: The evidence_data of this PlaybookTask.  # noqa: E501
        :rtype: EvidenceData
        """
        return self._evidence_data

    @evidence_data.setter
    def evidence_data(self, evidence_data):
        """Sets the evidence_data of this PlaybookTask.


        :param evidence_data: The evidence_data of this PlaybookTask.  # noqa: E501
        :type: EvidenceData
        """

        self._evidence_data = evidence_data

    @property
    def field_mapping(self):
        """Gets the field_mapping of this PlaybookTask.  # noqa: E501


        :return: The field_mapping of this PlaybookTask.  # noqa: E501
        :rtype: list[FieldMapping]
        """
        return self._field_mapping

    @field_mapping.setter
    def field_mapping(self, field_mapping):
        """Sets the field_mapping of this PlaybookTask.


        :param field_mapping: The field_mapping of this PlaybookTask.  # noqa: E501
        :type: list[FieldMapping]
        """

        self._field_mapping = field_mapping

    @property
    def form(self):
        """Gets the form of this PlaybookTask.  # noqa: E501


        :return: The form of this PlaybookTask.  # noqa: E501
        :rtype: DataCollectionForm
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this PlaybookTask.


        :param form: The form of this PlaybookTask.  # noqa: E501
        :type: DataCollectionForm
        """

        self._form = form

    @property
    def form_display(self):
        """Gets the form_display of this PlaybookTask.  # noqa: E501


        :return: The form_display of this PlaybookTask.  # noqa: E501
        :rtype: FormDisplay
        """
        return self._form_display

    @form_display.setter
    def form_display(self, form_display):
        """Sets the form_display of this PlaybookTask.


        :param form_display: The form_display of this PlaybookTask.  # noqa: E501
        :type: FormDisplay
        """

        self._form_display = form_display

    @property
    def id(self):
        """Gets the id of this PlaybookTask.  # noqa: E501


        :return: The id of this PlaybookTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybookTask.


        :param id: The id of this PlaybookTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ignore_worker(self):
        """Gets the ignore_worker of this PlaybookTask.  # noqa: E501

        Do not run this task in a worker  # noqa: E501

        :return: The ignore_worker of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_worker

    @ignore_worker.setter
    def ignore_worker(self, ignore_worker):
        """Sets the ignore_worker of this PlaybookTask.

        Do not run this task in a worker  # noqa: E501

        :param ignore_worker: The ignore_worker of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._ignore_worker = ignore_worker

    @property
    def loop(self):
        """Gets the loop of this PlaybookTask.  # noqa: E501


        :return: The loop of this PlaybookTask.  # noqa: E501
        :rtype: TaskLoop
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this PlaybookTask.


        :param loop: The loop of this PlaybookTask.  # noqa: E501
        :type: TaskLoop
        """

        self._loop = loop

    @property
    def message(self):
        """Gets the message of this PlaybookTask.  # noqa: E501


        :return: The message of this PlaybookTask.  # noqa: E501
        :rtype: NotifiableItem
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PlaybookTask.


        :param message: The message of this PlaybookTask.  # noqa: E501
        :type: NotifiableItem
        """

        self._message = message

    @property
    def next_tasks(self):
        """Gets the next_tasks of this PlaybookTask.  # noqa: E501


        :return: The next_tasks of this PlaybookTask.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._next_tasks

    @next_tasks.setter
    def next_tasks(self, next_tasks):
        """Sets the next_tasks of this PlaybookTask.


        :param next_tasks: The next_tasks of this PlaybookTask.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._next_tasks = next_tasks

    @property
    def note(self):
        """Gets the note of this PlaybookTask.  # noqa: E501


        :return: The note of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PlaybookTask.


        :param note: The note of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._note = note

    @property
    def quiet_mode(self):
        """Gets the quiet_mode of this PlaybookTask.  # noqa: E501


        :return: The quiet_mode of this PlaybookTask.  # noqa: E501
        :rtype: QuietMode
        """
        return self._quiet_mode

    @quiet_mode.setter
    def quiet_mode(self, quiet_mode):
        """Sets the quiet_mode of this PlaybookTask.


        :param quiet_mode: The quiet_mode of this PlaybookTask.  # noqa: E501
        :type: QuietMode
        """

        self._quiet_mode = quiet_mode

    @property
    def reputation_calc(self):
        """Gets the reputation_calc of this PlaybookTask.  # noqa: E501


        :return: The reputation_calc of this PlaybookTask.  # noqa: E501
        :rtype: ReputationCalcAlg
        """
        return self._reputation_calc

    @reputation_calc.setter
    def reputation_calc(self, reputation_calc):
        """Sets the reputation_calc of this PlaybookTask.


        :param reputation_calc: The reputation_calc of this PlaybookTask.  # noqa: E501
        :type: ReputationCalcAlg
        """

        self._reputation_calc = reputation_calc

    @property
    def restricted_completion(self):
        """Gets the restricted_completion of this PlaybookTask.  # noqa: E501


        :return: The restricted_completion of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_completion

    @restricted_completion.setter
    def restricted_completion(self, restricted_completion):
        """Sets the restricted_completion of this PlaybookTask.


        :param restricted_completion: The restricted_completion of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._restricted_completion = restricted_completion

    @property
    def script_arguments(self):
        """Gets the script_arguments of this PlaybookTask.  # noqa: E501


        :return: The script_arguments of this PlaybookTask.  # noqa: E501
        :rtype: dict(str, AdvanceArg)
        """
        return self._script_arguments

    @script_arguments.setter
    def script_arguments(self, script_arguments):
        """Sets the script_arguments of this PlaybookTask.


        :param script_arguments: The script_arguments of this PlaybookTask.  # noqa: E501
        :type: dict(str, AdvanceArg)
        """

        self._script_arguments = script_arguments

    @property
    def separate_context(self):
        """Gets the separate_context of this PlaybookTask.  # noqa: E501


        :return: The separate_context of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._separate_context

    @separate_context.setter
    def separate_context(self, separate_context):
        """Sets the separate_context of this PlaybookTask.


        :param separate_context: The separate_context of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._separate_context = separate_context

    @property
    def skip_unavailable(self):
        """Gets the skip_unavailable of this PlaybookTask.  # noqa: E501

        SkipUnavailable if true then will check if automation exists, integration of that command is installed and active or sub playbook exists in Demisto  # noqa: E501

        :return: The skip_unavailable of this PlaybookTask.  # noqa: E501
        :rtype: bool
        """
        return self._skip_unavailable

    @skip_unavailable.setter
    def skip_unavailable(self, skip_unavailable):
        """Sets the skip_unavailable of this PlaybookTask.

        SkipUnavailable if true then will check if automation exists, integration of that command is installed and active or sub playbook exists in Demisto  # noqa: E501

        :param skip_unavailable: The skip_unavailable of this PlaybookTask.  # noqa: E501
        :type: bool
        """

        self._skip_unavailable = skip_unavailable

    @property
    def sla(self):
        """Gets the sla of this PlaybookTask.  # noqa: E501


        :return: The sla of this PlaybookTask.  # noqa: E501
        :rtype: SLA
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this PlaybookTask.


        :param sla: The sla of this PlaybookTask.  # noqa: E501
        :type: SLA
        """

        self._sla = sla

    @property
    def sla_reminder(self):
        """Gets the sla_reminder of this PlaybookTask.  # noqa: E501


        :return: The sla_reminder of this PlaybookTask.  # noqa: E501
        :rtype: SLA
        """
        return self._sla_reminder

    @sla_reminder.setter
    def sla_reminder(self, sla_reminder):
        """Sets the sla_reminder of this PlaybookTask.


        :param sla_reminder: The sla_reminder of this PlaybookTask.  # noqa: E501
        :type: SLA
        """

        self._sla_reminder = sla_reminder

    @property
    def task(self):
        """Gets the task of this PlaybookTask.  # noqa: E501


        :return: The task of this PlaybookTask.  # noqa: E501
        :rtype: Task
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this PlaybookTask.


        :param task: The task of this PlaybookTask.  # noqa: E501
        :type: Task
        """

        self._task = task

    @property
    def task_id(self):
        """Gets the task_id of this PlaybookTask.  # noqa: E501


        :return: The task_id of this PlaybookTask.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this PlaybookTask.


        :param task_id: The task_id of this PlaybookTask.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def timer_triggers(self):
        """Gets the timer_triggers of this PlaybookTask.  # noqa: E501

        SLA fields  # noqa: E501

        :return: The timer_triggers of this PlaybookTask.  # noqa: E501
        :rtype: list[TimerTrigger]
        """
        return self._timer_triggers

    @timer_triggers.setter
    def timer_triggers(self, timer_triggers):
        """Sets the timer_triggers of this PlaybookTask.

        SLA fields  # noqa: E501

        :param timer_triggers: The timer_triggers of this PlaybookTask.  # noqa: E501
        :type: list[TimerTrigger]
        """

        self._timer_triggers = timer_triggers

    @property
    def type(self):
        """Gets the type of this PlaybookTask.  # noqa: E501


        :return: The type of this PlaybookTask.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlaybookTask.


        :param type: The type of this PlaybookTask.  # noqa: E501
        :type: TaskType
        """

        self._type = type

    @property
    def view(self):
        """Gets the view of this PlaybookTask.  # noqa: E501


        :return: The view of this PlaybookTask.  # noqa: E501
        :rtype: TaskView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this PlaybookTask.


        :param view: The view of this PlaybookTask.  # noqa: E501
        :type: TaskView
        """

        self._view = view

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlaybookTask, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlaybookTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
