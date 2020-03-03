import string
from random import choice
from flask import render_template, request,redirect,abort
from app import app, db
from url.forms import UrlForm
from url.models import Url



@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        old_code = request.form.get('old')
        print(old_code)
        exists = db.session.query(
                db.exists().where(Url.old == old_code)).scalar()
        if exists:
                existing_url = Url.query.filter_by(old=old_code).first()
                return render_template("exist_url.html", code=existing_url.new)


        def gen():
            chars = string.ascii_letters + string.digits
            length = 3
            code = ''.join(choice(chars) for x in range(length))
            exists = db.session.query(
                db.exists().where(Url.new == code)).scalar()
            if not exists:
                    print("Your new code is:", code)
                    return code
        code = gen()
        while code is None:
            code = gen()
            

    if request.method == 'POST' and code is not None:
        form = UrlForm(request.form)
        if form.validate_on_submit():
            url = form.save_url(Url(new=code))
            db.session.add(url)
            db.session.commit()
            return render_template("success.html", code=code)
        else:
            print("Validation failed")
    else:
        form = UrlForm()
    return render_template("index.html", form=form)


@app.route('/<new>')
def redirect_to_old(new):
    new = Url.query.filter_by(new=new).first()
    if new is None:
        abort(404)
    else:
        return redirect(new.old)
