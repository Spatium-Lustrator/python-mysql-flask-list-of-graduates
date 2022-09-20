from flask import Flask, render_template, request
from db_requests import Requester

requester = Requester()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sign_in_page.html')


@app.route('/check-admins/', methods=["GET"])
def check_admins():
    login = request.args.get('login')
    password = request.args.get('password')
    password_from_bd = requester.return_value_from_bd(column_to_return="password",
                                                      table="admins",
                                                      column_to_check="login",
                                                      value_to_check=login)

    return render_template('account_page.html') \
        if password_from_bd is not None and password == password_from_bd[0] else render_template('sign_in_page.html')

@app.route('/check-certificate-ids/', methods=["GET"])
def check_certificate_ids():
    certificate_id = request.args.get("certificate_id")
    result = requester.return_value_from_bd(column_to_return="certificate_id",
                                            table="certificate_ids",
                                            column_to_check="certificate_id",
                                            value_to_check=certificate_id)

    return render_template('sign_up_user_page.html') if result > 0 else render_template('sign_in_page.html')

@app.route('/sign-up-user/', methods=["GET"])
def sign_up_user():
    surname, first_name, patronymic, university, certificate_id, user_id = request.args.get("user_surname"),\
                                      request.args.get("user_first_name"),\
                                      request.args.get("user_patronymic"), \
                                      request.args.get("user_university"), \
                                      request.args.get("certificate_id"),\
                                      request.args.get("user_id")
    requester.insert_user(certificate_id=certificate_id, user_id=user_id, university_id=university, surname=surname,
                          first_name=first_name, patronymic=patronymic)
    return render_template('sign_in_page.html')

@app.route('/go-to-users-table/', methods=["GET"])
def go_to_users_table():
    list_of_users = requester.return_list_of_values_from_bd()
    return render_template("all_users_table.html", list_of_users=list_of_users)

@app.route('/add-certificate-id/', methods=["GET"])
def add_certificate_id():
    certificate_id = request.args.get("certificate_id")
    requester.insert_certificate_id(certificate_id)
    return render_template("account_page.html")

if __name__ == '__main__':
    app.run(debug=True)
