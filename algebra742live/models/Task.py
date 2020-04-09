from flask import current_app as app
from datetime import datetime
from .. import db
import json
import re # for matching source patterns to task collections and tasks
import os # for reading task collection files
from sqlalchemy.orm import relationship

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text)
    parameters = db.Column(db.Text)
    submitted = db.Column(db.Boolean, default=False)

    submissions = relationship("Submission", back_populates="task")

    def params(self):
        return(json.loads(self.parameters))

    def to_json(self):
        return({
            'id': self.id,
            'source': self.source,
            'data': self.data(),
            'parameters': self.params(),
            'submitted': list(self.submitted),
            })

    def data(self):
        repo, tags = self.source.split(":",1)
        if repo == 'snow-qm':
            collection, task = tags.split(":")
            with open(os.path.join(app.config["SNOW_QM_COLLECTIONS_DIR"],collection+'.json')) as f:
                collection_data = json.load(f)
            task_data = data[task]
            return(task_data)

def get_task_by_id(task_id):
    task = db.session.query(Task).get(task_id)
    return(task)

def get_task_from_source(source):
    repo, tags = source.split(":",1)
    if repo == 'snow-qm':
        collection, task = tags.split(":")
        collection = collection
        with open(os.path.join(app.config["SNOW_QM_COLLECTIONS_DIR"],collection+'.json')) as f:
            collection_data = json.load(f)
        if task in collection_data:
            task = get_or_create(db.session, Task, source=source)
            task.parameters = json.dumps(collection_data[task])
            return(task)

def get_task_data_by_source_pattern(source_pattern):
    repo, tags = source_pattern.split(":",1)
    if repo == 'snow-qm':
        collection_pattern, task_pattern = tags.split(":")
        collection = collection_pattern
        with open(os.path.join(app.config["SNOW_QM_COLLECTIONS_DIR"],collection+'.json')) as f:
            collection_data = json.load(f)
        for task in filter(re.compile(task_pattern).match,collection_data.keys()):
            yield {'source': '{:s}:{:s}:{:s}'.format(repo,collection,task), 'data': collection_data[task]}
