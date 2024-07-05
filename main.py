from flask import Flask, url_for, render_template, jsonify
from data import api
from data import db_session
from data.quest import Quest
from ast import literal_eval

app = Flask(__name__)


@app.route('/<quests_id>/<ids>')
def bootstrap(quests_id, ids):
    db_sess = db_session.create_session()
    quest = db_sess.query(Quest).get(quests_id)
    db_sess.close()
    if not quest:
        return render_template('oops.html')
    lst = literal_eval(quest.json)
    if ids not in lst:
        return render_template('oops.html')
    return render_template("someshit.html", quest=lst[ids])


if __name__ == '__main__':
    db_session.global_init("db/db.db")
    app.register_blueprint(api.blueprint)
    app.run(port=8080, host='127.0.0.1')
