from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaFile
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaFile('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaFile('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
