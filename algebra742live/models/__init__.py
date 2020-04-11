#from .. import db
from flask_sqlalchemy import SQLAlchemy
import random
import string
from datetime import datetime
import json
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

db = SQLAlchemy()

class RequestDenied(Exception):
    def __init__(self, message):
        self.message = message

def get(session, model, defaults=None, **kwargs):
    from sqlalchemy.sql.expression import ClauseElement
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        return None 

def get_or_create(session, model, defaults=None, **kwargs):
    from sqlalchemy.sql.expression import ClauseElement
    try:
        instance = session.query(model).filter_by(**kwargs).one()
        return instance
    except NoResultFound:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        session.commit()
        return instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return({ 'id': self.id,
                 'username': self.username,
                 'firstname': self.firstname,
                 'lastname': self.lastname,
                 'lti_user_id': self.lti_user_id })
    def submit(task, data):
        submission = Submission(user_id=self.id, task_id=task.id, data=json.dumps(data))
        db.session.add(submission)
        db.session.commit()
        return(submission)


def get_user_by_lti_user_id(session, lti_user_id):
    instance = db.session.query(User).filter_by(lti_user_id=lti_user_id).first() # TODO: ensure unique
    return instance

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

db.User = User
