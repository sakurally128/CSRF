from wtforms import Form, StringField, FloatField, PasswordField
from wtforms.validators import Email,Length,EqualTo,InputRequired,NumberRange
from models import User

class ResgistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3,10)])
    password = PasswordField(validators=[Length(6,20)])
    password_repeat = PasswordField(validators=[EqualTo("password")])
    deposit = FloatField(validators=[InputRequired()])

class LogintForm(Form):
    email = StringField(validators=[Email()])
    password = PasswordField(validators=[Length(6,20)])
    # def validate(self):
    #     result = super(LogintForm, self).validate()
    #     if not result:
    #         return False
    #     else:
    #         email = self.email.data
    #         password = self.password.data
    #         user = User.query.filter(User.email == email,User.password == password).first()
    #         if not user:
    #             self.email.errors.append("邮箱或密码错误！")
    #             return False
    #         return True
class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1,100000000)])