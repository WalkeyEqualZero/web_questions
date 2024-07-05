import flask
from flask import jsonify, make_response, request
from data.quest import Quest
from data import db_session
from ast import literal_eval


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/quests/<int:quests_id>', methods=['GET'])
def get_one_quest(quests_id):

    db_sess = db_session.create_session()
    quest = db_sess.query(Quest).get(quests_id)
    db_sess.close()
    if not quest:
        return jsonify({'error': 'Not found'})
    return jsonify(literal_eval(quest.json))


@blueprint.route('/api/add', methods=['POST'])
def create_quest():
    print(request.json)
    print(request.data)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    quest = Quest(json=str(request.json['data']))
    db_sess.add(quest)
    db_sess.commit()
    last = db_sess.query(Quest).all()[-1].id
    db_sess.close()
    return jsonify({'success': 'OK', 'last': last})
