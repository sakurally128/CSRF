from flask import Flask,render_template,views,request,session
from forms import ResgistForm,LogintForm,TransferForm
from auth import login_request
from models import User
from exts import db
import config

app = Flask(__name__)
db.init_app(app)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template("index.html")

class RegistView(views.MethodView):
    def get(self):
        return render_template("regist.html")
    def post(self):
        form = ResgistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            # email = request.form.get("email")
            # username = request.form.get("username")
            # password = request.form.get("password")
            # deposit = request.form.get("deposit")
            user = User(email = email,username = username,password=password,deposit = deposit)
            db.session.add(user)
            db.session.commit()
            return u"注册成功"
        else:
            print(form.errors)
            return u"注册失败"

class LoginView(views.MethodView):
    def get(self):
        return render_template("login.html")
    def post(self):
        form = LogintForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter(User.email == email,User.password == password).first()
            if user:
                session["user_id"] = user.id
                return "登陆成功"
            else:
                return "邮箱或密码错误！"

class TransferView(views.MethodView):
    decorators = [login_request]
    def get(self):
        return render_template("transfer.html")
    def post(self):
        form = TransferForm(request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            user = User.query.filter_by(email=email).first()
            print(user)
            if user:
                user_id = session.get("user_id")
                myself = User.query.get(user_id)
                if myself.deposit >= money:
                    user.deposit += money
                    myself.deposit -= money
                    db.session.commit()
                    return u"转账成功！"
                else:
                    return u"余额不足！"
            else:
                return u"该用户不存在！"
        else:
            return u"数据填写不正确! "
#as_view:指定该url的名称
app.add_url_rule("/regist/",view_func = RegistView.as_view("regist"))
app.add_url_rule("/login/",view_func = LoginView.as_view("login"))
app.add_url_rule("/transfer/",view_func = TransferView.as_view("transfer"))


if __name__ == '__main__':
    app.run(debug=True)
